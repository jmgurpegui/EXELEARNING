# -*- coding: utf-8 -*-
"""Generate eXeLearning signature files: content.xml (ODE model) + imslrm.xml (LOM-ES).
Parses the already-generated HTML pages in pkg/ to build faithful htmlView blocks."""
import os, re, json, html as _html, datetime, random, string
from bs4 import BeautifulSoup
import gen_common

AUTHOR = "IES San Blas (Madrid)"
DESCRIPTION = ("Recurso educativo sobre fundamentos de electricidad y cambios de unidades "
               "aplicados al automóvil, para el módulo Circuitos eléctricos auxiliares del vehículo "
               "(CFGM Electromecánica de Vehículos Automóviles).")
LICENSE = "creative commons: attribution - share alike 4.0"
LICENSE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"

def _cdata(text):
    # Safe CDATA: neutralize any ]]> sequence
    text = text.replace("]]>", "]]]]><![CDATA[>")
    return "<![CDATA[" + text + "]]>"

def _page_path(pkg, slug):
    return os.path.join(pkg, "index.html") if slug == "index" else os.path.join(pkg, "html", slug + ".html")

def _extract_blocks(pkg, slug):
    """Return list of dicts: {blockName, iconName, inner_html} for each article.box on the page."""
    with open(_page_path(pkg, slug), encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    blocks = []
    for art in soup.select("article.box"):
        title_el = art.select_one("h1.box-title")
        block_name = title_el.get_text(strip=True) if title_el else ""
        icon = ""
        img = art.select_one(".box-icon img")
        if img and img.get("src"):
            icon = os.path.splitext(os.path.basename(img["src"]))[0]
        content = art.select_one(".box-content .exe-static-content")
        if content is None:
            content = art.select_one(".box-content")
        inner = "".join(str(c) for c in content.contents).strip() if content else ""
        blocks.append(dict(blockName=block_name, iconName=icon, inner=inner))
    return blocks

def _gen_id():
    ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    suf = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return ts + suf

def build_signatures(pkg):
    ode_id = _gen_id()
    ode_ver = _gen_id()
    modified_ms = str(int(datetime.datetime.now().timestamp() * 1000))

    # ---------------- content.xml ----------------
    out = []
    out.append('<?xml version="1.0" encoding="UTF-8"?>')
    out.append('<!DOCTYPE ode SYSTEM "content.dtd">')
    out.append('<ode xmlns="http://www.intef.es/xsd/ode" version="2.0">')
    out.append('<userPreferences>')
    out.append('  <userPreference><key>theme</key><value>zen</value></userPreference>')
    out.append('</userPreferences>')
    out.append('<odeResources>')
    out.append(f'  <odeResource><key>odeId</key><value>{ode_id}</value></odeResource>')
    out.append(f'  <odeResource><key>odeVersionId</key><value>{ode_ver}</value></odeResource>')
    out.append('  <odeResource><key>exe_version</key><value>4.0.1</value></odeResource>')
    out.append('</odeResources>')

    author = getattr(gen_common, "AUTHOR", AUTHOR)
    desc = getattr(gen_common, "DESCRIPTION", f"Recurso educativo interactivo: {gen_common.COURSE}")
    license_str = getattr(gen_common, "LICENSE", LICENSE)
    license_url = getattr(gen_common, "LICENSE_URL", LICENSE_URL)

    props = [
        ("pp_title", gen_common.COURSE),
        ("pp_author", author),
        ("pp_description", desc),
        ("pp_lang", "es"),
        ("pp_license", license_str),
        ("pp_licenseUrl", license_url),
        ("pp_theme", "zen"),
        ("pp_exelearning_version", "v4.0.1"),
        ("pp_modified", modified_ms),
        ("pp_addExeLink", "true"),
        ("pp_addPagination", "true"),
        ("pp_addSearchBox", "false"),
        ("pp_addAccessibilityToolbar", "true"),
        ("pp_addMathJax", "false"),
        ("exportSource", "true"),
        ("pp_globalFont", "default"),
    ]
    out.append('<odeProperties>')
    for k, v in props:
        out.append(f'  <odeProperty><key>{k}</key><value>{_html.escape(v)}</value></odeProperty>')
    out.append('</odeProperties>')

    out.append('<odeNavStructures>')
    for order, pg in enumerate(gen_common.PAGES):
        pid = pg["pid"]
        title = pg["title"]
        blocks = _extract_blocks(pkg, pg["slug"])
        if not blocks:
            blocks = [dict(blockName="", iconName="", inner="<p></p>")]
        out.append('  <odeNavStructure>')
        out.append(f'    <odePageId>{pid}</odePageId>')
        out.append('    <odeParentPageId/>')
        out.append(f'    <pageName>{_html.escape(title)}</pageName>')
        out.append(f'    <odeNavStructureOrder>{order}</odeNavStructureOrder>')
        out.append('    <odeNavStructureProperties>')
        out.append(f'      <odeNavStructureProperty><key>titlePage</key><value>{_html.escape(title)}</value></odeNavStructureProperty>')
        out.append('    </odeNavStructureProperties>')
        out.append('    <odePagStructures>')
        for bi, blk in enumerate(blocks):
            bid = f'block-{pid}-{bi:02d}'
            iid = f'idevice-{pid}-{bi:02d}'
            bname = _html.escape(blk["blockName"]) if blk["blockName"] else ""
            icon = _html.escape(blk["iconName"]) if blk["iconName"] else ""
            inner = blk["inner"] if blk["inner"] else "<p></p>"
            json_props = json.dumps({
                "textInfoParticipantsTextInput": "",
                "textInfoDurationTextInput": "",
                "textTextarea": inner,
                "textFeedbackInput": "",
                "textFeedbackTextarea": ""
            }, ensure_ascii=False)
            out.append('      <odePagStructure>')
            out.append(f'        <odePageId>{pid}</odePageId>')
            out.append(f'        <odeBlockId>{bid}</odeBlockId>')
            out.append(f'        <blockName>{bname}</blockName>' if bname else '        <blockName/>')
            out.append(f'        <iconName>{icon}</iconName>' if icon else '        <iconName/>')
            out.append(f'        <odePagStructureOrder>{bi}</odePagStructureOrder>')
            out.append('        <odePagStructureProperties></odePagStructureProperties>')
            out.append('        <odeComponents>')
            out.append('          <odeComponent>')
            out.append(f'            <odePageId>{pid}</odePageId>')
            out.append(f'            <odeBlockId>{bid}</odeBlockId>')
            out.append(f'            <odeIdeviceId>{iid}</odeIdeviceId>')
            out.append('            <odeIdeviceTypeName>text</odeIdeviceTypeName>')
            out.append('            <htmlView>' + _cdata(inner) + '</htmlView>')
            out.append('            <jsonProperties>' + _cdata(json_props) + '</jsonProperties>')
            out.append('            <odeComponentsOrder>0</odeComponentsOrder>')
            out.append('            <odeComponentsProperties></odeComponentsProperties>')
            out.append('          </odeComponent>')
            out.append('        </odeComponents>')
            out.append('      </odePagStructure>')
        out.append('    </odePagStructures>')
        out.append('  </odeNavStructure>')
    out.append('</odeNavStructures>')
    out.append('</ode>')

    with open(os.path.join(pkg, "content.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    # ---------------- imslrm.xml ----------------
    now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.00+02:00")
    vcard = f"BEGIN:VCARD VERSION:3.0 FN:{author} EMAIL;TYPE=INTERNET: ORG: END:VCARD"
    lrm = f"""<?xml version="1.0" encoding="UTF-8"?>
<lom xmlns="http://www.imsglobal.org/xsd/imsmd_rootv1p2p1">
  <general uniqueElementName="general">
    <identifier>
      <catalog uniqueElementName="catalog">none</catalog>
      <entry uniqueElementName="entry">ODE-{ode_id}</entry>
    </identifier>
    <title>
      <string language="es">{_html.escape(gen_common.COURSE)}</string>
    </title>
    <language>es</language>
    <description>
      <string language="es">{_html.escape(desc)}</string>
    </description>
    <aggregationLevel uniqueElementName="aggregationLevel">
      <source uniqueElementName="source">LOM-ESv1.0</source>
      <value uniqueElementName="value">2</value>
    </aggregationLevel>
  </general>
  <lifeCycle>
    <contribute>
      <role uniqueElementName="role">
        <source uniqueElementName="source">LOM-ESv1.0</source>
        <value uniqueElementName="value">author</value>
      </role>
      <entity>{vcard}</entity>
      <date>
        <dateTime uniqueElementName="dateTime">{now_iso}</dateTime>
        <description>
          <string language="es">Fecha de creación de los metadatos</string>
        </description>
      </date>
    </contribute>
  </lifeCycle>
  <metaMetadata uniqueElementName="metaMetadata">
    <contribute>
      <role uniqueElementName="role">
        <source uniqueElementName="source">LOM-ESv1.0</source>
        <value uniqueElementName="value">creator</value>
      </role>
      <entity>{vcard}</entity>
      <date>
        <dateTime uniqueElementName="dateTime">{now_iso}</dateTime>
        <description>
          <string language="es">Fecha de creación de los metadatos</string>
        </description>
      </date>
    </contribute>
    <metadataSchema>LOM-ESv1.0</metadataSchema>
    <language>es</language>
  </metaMetadata>
  <technical uniqueElementName="technical">
    <otherPlatformRequirements>
      <string language="es">editor: eXe Learning</string>
    </otherPlatformRequirements>
  </technical>
  <educational>
    <language>es</language>
  </educational>
  <rights uniqueElementName="rights">
    <copyrightAndOtherRestrictions uniqueElementName="copyrightAndOtherRestrictions">
      <source uniqueElementName="source">LOM-ESv1.0</source>
      <value uniqueElementName="value">{license_str}</value>
    </copyrightAndOtherRestrictions>
    <access uniqueElementName="access">
      <accessType uniqueElementName="accessType">
        <source uniqueElementName="source">LOM-ESv1.0</source>
        <value uniqueElementName="value">universal</value>
      </accessType>
      <description>
        <string language="en">Default</string>
      </description>
    </access>
  </rights>
</lom>
"""
    with open(os.path.join(pkg, "imslrm.xml"), "w", encoding="utf-8") as f:
        f.write(lrm)

    return ode_id, ode_ver
