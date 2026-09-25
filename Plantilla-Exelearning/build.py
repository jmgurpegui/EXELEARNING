#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Compilador, validador y empaquetador automático de cursos SCORM 1.2 eXeLearning.

Uso:
    python3 build.py                    # Compila el curso en el directorio actual
    python3 build.py <carpeta_del_curso> # Compila el curso especificado
    python3 build.py <course_spec.py>   # Compila a partir del archivo spec

Genera:
    1. Carpeta pkg/ con todo el contenido compilado, runtime eXe y firmas de autenticidad.
    2. Validación completa (sintaxis XML, content.dtd e integridad manifiesto <-> disco).
    3. Archivo ZIP final listo para subir al Aula Virtual / EducaMadrid / Moodle.
"""

import sys
import os
import shutil
import re
import importlib.util
import html as _html
import subprocess
import zipfile
import unicodedata

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text).strip()
    return re.sub(r'[-\s]+', '_', text)

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def find_locations(target_arg):
    here = os.path.dirname(os.path.abspath(__file__))

    # 1. Determinar course_dir y spec_path
    if not target_arg:
        if os.path.isfile("course_spec.py"):
            course_dir = os.path.abspath(".")
            spec_path = os.path.join(course_dir, "course_spec.py")
        elif os.path.isfile(os.path.join(here, "course_spec.py")):
            course_dir = here
            spec_path = os.path.join(here, "course_spec.py")
        else:
            print("❌ Error: No se encontró 'course_spec.py' en el directorio actual ni en la plantilla.")
            sys.exit(1)
    else:
        target = os.path.abspath(target_arg)
        if os.path.isfile(target):
            spec_path = target
            course_dir = os.path.dirname(target)
        elif os.path.isdir(target):
            course_dir = target
            spec_path = os.path.join(course_dir, "course_spec.py")
            if not os.path.isfile(spec_path):
                print(f"❌ Error: No se encontró 'course_spec.py' dentro de '{target}'.")
                sys.exit(1)
        else:
            print(f"❌ Error: La ruta '{target_arg}' no existe.")
            sys.exit(1)

    # 2. Localizar core/ (gen_common, gen_content_xml)
    core_candidates = [
        os.path.join(course_dir, "core"),
        os.path.join(here, "core"),
        os.path.join(os.path.dirname(here), "Plantilla-Exelearning", "core"),
    ]
    core_dir = next((c for c in core_candidates if os.path.isdir(c) and os.path.isfile(os.path.join(c, "gen_common.py"))), None)
    if not core_dir:
        print("❌ Error: No se encontró la carpeta 'core/' con los módulos de generación.")
        sys.exit(1)

    # 3. Localizar runtime/
    runtime_candidates = [
        os.path.join(course_dir, "runtime"),
        os.path.join(here, "runtime"),
        os.path.join(os.path.dirname(here), "Plantilla-Exelearning", "runtime"),
    ]
    runtime_dir = next((r for r in runtime_candidates if os.path.isdir(r) and os.path.isfile(os.path.join(r, "content.dtd"))), None)
    if not runtime_dir:
        print("❌ Error: No se encontró la carpeta 'runtime/' con los recursos validados de eXeLearning.")
        sys.exit(1)

    pkg_dir = os.path.join(course_dir, "pkg")
    return course_dir, spec_path, core_dir, runtime_dir, pkg_dir

def copy_runtime(runtime_dir, pkg_dir):
    for item in ["libs", "theme", "idevices"]:
        src = os.path.join(runtime_dir, item)
        dst = os.path.join(pkg_dir, item)
        if os.path.isdir(src):
            if os.path.isdir(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)

    for item in ["content.dtd"]:
        src = os.path.join(runtime_dir, item)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(pkg_dir, item))

    os.makedirs(os.path.join(pkg_dir, "content", "css"), exist_ok=True)
    os.makedirs(os.path.join(pkg_dir, "content", "img"), exist_ok=True)
    os.makedirs(os.path.join(pkg_dir, "content", "media", "video"), exist_ok=True)
    os.makedirs(os.path.join(pkg_dir, "content", "media", "audio"), exist_ok=True)
    os.makedirs(os.path.join(pkg_dir, "content", "files"), exist_ok=True)

    for css in ["base.css", "curso.css"]:
        src = os.path.join(runtime_dir, "content", "css", css)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(pkg_dir, "content", "css", css))

    res_src = os.path.join(runtime_dir, "content", "resources")
    res_dst = os.path.join(pkg_dir, "content", "resources")
    if os.path.isdir(res_src):
        if os.path.isdir(res_dst):
            shutil.rmtree(res_dst)
        shutil.copytree(res_src, res_dst)

def copy_user_media(course_dir, pkg_dir):
    media_dir = os.path.join(course_dir, "media")
    copied = 0
    if os.path.isdir(media_dir):
        for root, _, files in os.walk(media_dir):
            for fn in files:
                if fn in [".gitkeep", ".DS_Store", "Thumbs.db"]:
                    continue
                src_f = os.path.join(root, fn)
                rel = os.path.relpath(src_f, media_dir)
                parts = rel.split(os.sep)
                if parts[0] in ["img", "files", "media"]:
                    dst_f = os.path.join(pkg_dir, "content", rel)
                else:
                    ext = os.path.splitext(fn)[1].lower()
                    if ext in [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"]:
                        dst_f = os.path.join(pkg_dir, "content", "img", fn)
                    elif ext in [".mp4", ".webm", ".ogv"]:
                        dst_f = os.path.join(pkg_dir, "content", "media", "video", fn)
                    elif ext in [".mp3", ".wav", ".ogg"]:
                        dst_f = os.path.join(pkg_dir, "content", "media", "audio", fn)
                    else:
                        dst_f = os.path.join(pkg_dir, "content", "files", fn)
                os.makedirs(os.path.dirname(dst_f), exist_ok=True)
                shutil.copy2(src_f, dst_f)
                copied += 1
    return copied

def generate_pages(gen_common, course_spec, pkg_dir):
    os.makedirs(os.path.join(pkg_dir, "html"), exist_ok=True)
    PAGES = gen_common.PAGES
    BODIES = course_spec.BODIES
    for pg in PAGES:
        slug = pg["slug"]
        is_sc = (slug == "cuestionario" or len(PAGES) == 1 or pg.get("is_scorm", False))
        onunload = 'unloadPage(true)' if is_sc else 'unloadPage()'
        out = gen_common.page(slug, pg["title"], BODIES[slug], onunload=onunload)
        path = os.path.join(pkg_dir, "index.html") if slug == "index" else os.path.join(pkg_dir, "html", f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)

def generate_manifest(gen_common, ode_id, pkg_dir):
    PAGES = gen_common.PAGES
    COURSE = gen_common.COURSE

    asset_files = []
    for root, _, files in os.walk(pkg_dir):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), pkg_dir).replace(os.sep, "/")
            asset_files.append(rel)

    page_href = {pg["slug"]: ("index.html" if pg["slug"] == "index" else f"html/{pg['slug']}.html") for pg in PAGES}
    page_hrefs = set(page_href.values())
    assets = sorted(f for f in asset_files if f not in page_hrefs)

    org_items = "\n".join(
        f'      <item identifier="ITEM-{pg["pid"]}" identifierref="RES-{pg["pid"]}" isvisible="true">\n'
        f'        <title>{_html.escape(pg["title"])}</title>\n      </item>' for pg in PAGES)

    res_blocks = []
    for pg in PAGES:
        href = page_href[pg["slug"]]
        res_blocks.append(
            f'    <resource identifier="RES-{pg["pid"]}" type="webcontent" adlcp:scormtype="sco" href="{href}">\n'
            f'      <file href="{href}"/>\n      <dependency identifierref="COMMON_FILES"/>\n    </resource>')

    common = "\n".join(f'      <file href="{_html.escape(a)}"/>' for a in assets)
    res_blocks.append('    <resource identifier="COMMON_FILES" type="webcontent" adlcp:scormtype="asset">\n' + common + "\n    </resource>")

    manifest = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="eXe-MANIFEST-{ode_id}"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_v1p2">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
    <adlcp:location>imslrm.xml</adlcp:location>
  </metadata>
  <organizations default="eXe-{ode_id}">
    <organization identifier="eXe-{ode_id}" structure="hierarchical">
      <title>{_html.escape(COURSE)}</title>
{org_items}
    </organization>
  </organizations>
  <resources>
{chr(10).join(res_blocks)}
  </resources>
</manifest>
"""
    with open(os.path.join(pkg_dir, "imsmanifest.xml"), "w", encoding="utf-8") as f:
        f.write(manifest)
    return len(assets)

def validate_package(pkg_dir):
    print("\n🔍 Validando paquete eXeLearning y SCORM 1.2...")
    required_files = ["imsmanifest.xml", "index.html", "content.xml", "content.dtd", "imslrm.xml"]
    for f in required_files:
        fpath = os.path.join(pkg_dir, f)
        if not os.path.isfile(fpath):
            raise AssertionError(f"Falta archivo crítico de firma eXe: {f}")
    print("  ✓ Firmas eXeLearning presentes en la raíz")

    # Validación XML
    has_xmllint = shutil.which("xmllint") is not None
    if has_xmllint:
        r1 = subprocess.run(["xmllint", "--noout", "imsmanifest.xml", "imslrm.xml"], cwd=pkg_dir, capture_output=True, text=True)
        if r1.returncode != 0:
            raise AssertionError(f"Error en sintaxis XML (imsmanifest/imslrm):\n{r1.stderr}")

        r2 = subprocess.run(["xmllint", "--noout", "--valid", "content.xml"], cwd=pkg_dir, capture_output=True, text=True)
        if r2.returncode != 0:
            raise AssertionError(f"content.xml no cumple con content.dtd:\n{r2.stderr}")
        print("  ✓ content.xml validado estrictamente contra content.dtd (xmllint)")
    else:
        import xml.etree.ElementTree as ET
        for xf in ["imsmanifest.xml", "imslrm.xml", "content.xml"]:
            ET.parse(os.path.join(pkg_dir, xf))
        print("  ✓ Sintaxis XML verificada (python xml parser)")

    # Consistencia manifiesto <-> disco
    with open(os.path.join(pkg_dir, "imsmanifest.xml"), encoding="utf-8") as mf:
        man_text = mf.read()
    declared = set(_html.unescape(f) for f in re.findall(r'<file href="([^"]+)"/>', man_text))
    scos = set(re.findall(r'adlcp:scormtype="sco" href="([^"]+)"', man_text))
    all_declared = declared | scos

    disk = set()
    for root, _, files in os.walk(pkg_dir):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), pkg_dir).replace(os.sep, "/")
            disk.add(rel)

    missing = sorted(f for f in all_declared if not os.path.isfile(os.path.join(pkg_dir, f)))
    undeclared = sorted(disk - declared - {'imsmanifest.xml'})

    if missing:
        raise AssertionError(f"Archivos declarados en manifiesto ausentes en disco: {missing[:5]}")
    if undeclared:
        raise AssertionError(f"Archivos en disco sin declarar en manifiesto: {undeclared[:5]}")

    print(f"  ✓ Consistencia total: {len(all_declared)} recursos declarados y comprobados en disco (0 faltantes, 0 sin declarar)")
    print("  ✓ Paquete validado con éxito: 100% compatible con eXeLearning y EducaMadrid/Moodle.")

def create_scorm_zip(course_dir, pkg_dir, course_title):
    base_name = slugify(course_title) if course_title else os.path.basename(course_dir)
    zip_filename = f"{base_name}_SCORM.zip"
    zip_path = os.path.join(course_dir, zip_filename)

    print(f"\n📦 Empaquetando SCORM 1.2 en: {zip_filename}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(pkg_dir):
            for file in sorted(files):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, pkg_dir)
                zf.write(full_path, rel_path)

    size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    print(f"  ✓ Archivo creado: {zip_path} ({size_mb:.2f} MB)")
    print(f"  ✓ Estructura de raíz correcta (imsmanifest.xml e index.html en raíz del zip)")
    return zip_path

def main():
    target_arg = sys.argv[1] if len(sys.argv) > 1 else None
    course_dir, spec_path, core_dir, runtime_dir, pkg_dir = find_locations(target_arg)

    print("=" * 65)
    print("       GENERADOR DE CURSOS SCORM 1.2 EXELEARNING")
    print("=" * 65)
    print(f"📍 Carpeta del curso: {course_dir}")
    print(f"📄 Archivo spec     : {spec_path}")
    print(f"⚙️  Módulos core     : {core_dir}")
    print(f"🎨 Runtime eXe      : {runtime_dir}")
    print(f"📁 Salida pkg       : {pkg_dir}")

    # Asegurar que core_dir esté en sys.path
    if core_dir not in sys.path:
        sys.path.insert(0, core_dir)

    # Cargar gen_common y registrarlo en sys.modules
    gen_common = load_module(os.path.join(core_dir, "gen_common.py"), "gen_common")
    sys.modules["gen_common"] = gen_common
    gen_content_xml = load_module(os.path.join(core_dir, "gen_content_xml.py"), "gen_content_xml")

    # Cargar especificación del curso
    course_spec = load_module(spec_path, "course_spec")

    # Limpiar o crear pkg_dir
    os.makedirs(pkg_dir, exist_ok=True)

    print("\n1. Copiando motor y runtime eXeLearning...")
    copy_runtime(runtime_dir, pkg_dir)

    print("2. Copiando recursos multimedia propios (media/)...")
    media_count = copy_user_media(course_dir, pkg_dir)
    print(f"   ✓ {media_count} archivos multimedia integrados.")

    print("3. Generando páginas HTML interactivas...")
    generate_pages(gen_common, course_spec, pkg_dir)
    print(f"   ✓ {len(gen_common.PAGES)} páginas generadas.")

    print("4. Generando firmas de autenticidad eXeLearning (content.xml + imslrm.xml)...")
    ode_id, _ = gen_content_xml.build_signatures(pkg_dir)
    print(f"   ✓ Firmas generadas (odeId: {ode_id})")

    print("5. Generando imsmanifest.xml (SCORM 1.2)...")
    assets_count = generate_manifest(gen_common, ode_id, pkg_dir)
    print(f"   ✓ Manifiesto generado ({assets_count} recursos comunes declarados).")

    # Validación
    validate_package(pkg_dir)

    # Empaquetado ZIP
    zip_path = create_scorm_zip(course_dir, pkg_dir, gen_common.COURSE)

    print("\n" + "=" * 65)
    print(" 🎉 PROCESO COMPLETADO CON ÉXITO")
    print("=" * 65)
    print(f"Entregable listo para EducaMadrid / Moodle:")
    print(f"➡️  {zip_path}")
    print("Súbelo directamente mediante 'Añadir actividad o recurso -> Paquete SCORM'.\n")

if __name__ == "__main__":
    main()
