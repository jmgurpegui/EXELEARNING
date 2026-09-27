# -*- coding: utf-8 -*-
"""
gdrive_export.py — Módulo de exportación y sincronización de entregables SCORM con Google Drive.

Estrategias implementadas:
1. Google Drive for Desktop: detección de unidades montadas (G:, H:, etc. o /mnt/g/) y copia a 'Mi unidad'.
2. Google Drive API v3: subida directa a la nube si existen credenciales OAuth/Service Account.
3. Repositorio local de cursos y zona de descarga: copia de seguridad en H:/0-TRAINING/Scorm y Downloads.
"""

import os
import sys
import re
import shutil
import sqlite3
from urllib.parse import urlparse

def parse_gdrive_target(folder_url_or_id):
    """
    Extrae el ID limpio de Google Drive y la URL canónica.
    Acepta URLs completas (drive.google.com/drive/.../folders/<ID>) o directamente el ID.
    """
    if not folder_url_or_id:
        return None, None
    
    text = str(folder_url_or_id).strip()
    
    # 1. Buscar patrón /folders/<ID>
    m_folders = re.search(r'folders/([a-zA-Z0-9_-]{15,})', text)
    if m_folders:
        folder_id = m_folders.group(1)
        return folder_id, f"https://drive.google.com/drive/folders/{folder_id}"
    
    # 2. Buscar patrón id=<ID>
    m_id = re.search(r'[?&]id=([a-zA-Z0-9_-]{15,})', text)
    if m_id:
        folder_id = m_id.group(1)
        return folder_id, f"https://drive.google.com/drive/folders/{folder_id}"
        
    # 3. Asumir que es el ID directo si tiene longitud suficiente y caracteres válidos
    if re.match(r'^[a-zA-Z0-9_-]{15,}$', text):
        return text, f"https://drive.google.com/drive/folders/{text}"
        
    return None, text

def get_drivefs_mount_letter():
    """
    Intenta averiguar la letra de unidad asignada a Google Drive en Windows leyendo root_preference_sqlite.db.
    """
    candidates = [
        r"C:\Users\jmgur\AppData\Local\Google\DriveFS\root_preference_sqlite.db",
        "/mnt/c/Users/jmgur/AppData/Local/Google/DriveFS/root_preference_sqlite.db",
    ]
    localapp = os.environ.get("LOCALAPPDATA")
    if localapp:
        candidates.insert(0, os.path.join(localapp, "Google", "DriveFS", "root_preference_sqlite.db"))
        
    for p in candidates:
        if os.path.isfile(p):
            try:
                conn = sqlite3.connect(p)
                cur = conn.cursor()
                for row in cur.execute("SELECT mount_point FROM media WHERE mount_point LIKE '%:%'"):
                    mp = row[0]
                    m = re.match(r'^([a-zA-Z]):', mp)
                    if m:
                        return m.group(1).upper()
            except Exception:
                pass
    return "G"

def find_gdrive_desktop_paths(custom_path=None):
    """
    Localiza las rutas locales genuinas de Google Drive for Desktop en Windows o WSL.
    Solo acepta carpetas que contengan 'Mi unidad', 'My Drive' o la ruta configurada explícitamente.
    """
    paths = []
    
    # Si el usuario definió una ruta fija personalizada
    if custom_path:
        cp = os.path.expanduser(custom_path)
        if os.path.exists(cp):
            paths.append(cp)
        # Adaptar si estamos en WSL y la ruta es Windows tipo G:\...
        if cp.startswith(("G:", "g:", "H:", "h:", "D:", "d:", "C:", "c:")):
            wsl_conv = f"/mnt/{cp[0].lower()}/{cp[3:].replace(os.sep, '/')}"
            if os.path.exists(wsl_conv):
                paths.append(wsl_conv)
                
    preferred_letter = get_drivefs_mount_letter()
    
    # Comprobar letras de unidad candidatas pero exigiendo que exista 'Mi unidad' o 'My Drive'
    check_letters = [preferred_letter, "G", "I"]
    for l in check_letters:
        # Windows
        for sub in ["Mi unidad", "My Drive", "Unidades compartidas", "Shared drives"]:
            w_path = os.path.join(f"{l}:\\", sub)
            if os.path.isdir(w_path):
                paths.append(w_path)
            # WSL
            wsl_path = f"/mnt/{l.lower()}/{sub}"
            if os.path.isdir(wsl_path):
                paths.append(wsl_path)
                
    # Deduplicar manteniendo orden
    seen = set()
    uniq = []
    for p in paths:
        norm = os.path.normpath(p)
        if norm not in seen:
            seen.add(norm)
            uniq.append(p)
    return uniq

def find_local_training_repos():
    """
    Rutas locales de respaldo en el equipo de desarrollo (SCORM Training y Descargas).
    """
    candidates = [
        ("/mnt/h/0-TRAINING/Scorm", "Repositorio central SCORM (H:\\0-TRAINING\\Scorm)"),
        (r"H:\0-TRAINING\Scorm", "Repositorio central SCORM (H:\\0-TRAINING\\Scorm)"),
        ("/mnt/c/Users/jmgur/Downloads", "Carpeta de Descargas de Windows"),
        (r"C:\Users\jmgur\Downloads", "Carpeta de Descargas de Windows"),
        (os.path.expanduser("~/Downloads"), "Carpeta de Descargas de usuario"),
    ]
    repos = []
    seen = set()
    for path, label in candidates:
        if os.path.isdir(path):
            norm = os.path.normpath(path)
            if norm not in seen:
                seen.add(norm)
                repos.append((path, label))
    return repos

def upload_via_gdrive_api(zip_path, folder_id, course_dir=None):
    """
    Intenta subir el archivo a Google Drive mediante Google Drive API v3
    si existen credenciales de servicio o cliente OAuth (credentials.json, token.json).
    """
    cred_candidates = [
        os.path.join(course_dir, "credentials.json") if course_dir else None,
        os.path.join(course_dir, "token.json") if course_dir else None,
        os.path.join(course_dir, "service_account.json") if course_dir else None,
        os.path.expanduser("~/.gdrive/credentials.json"),
        os.path.expanduser("~/.gdrive/token.json"),
        os.path.expanduser("~/.config/gdrive/credentials.json"),
        r"C:\Users\jmgur\.gdrive\credentials.json",
        r"C:\Users\jmgur\.gdrive\token.json",
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
        os.environ.get("GDRIVE_CREDENTIALS"),
    ]
    cred_file = next((c for c in cred_candidates if c and os.path.isfile(c)), None)
    
    if not cred_file:
        return {"attempted": False, "reason": "No se encontraron archivos de credenciales API"}
        
    try:
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        from google.oauth2 import service_account
        from google.oauth2.credentials import Credentials
        
        creds = None
        if "service_account" in cred_file or cred_file.endswith("_sa.json"):
            creds = service_account.Credentials.from_service_account_file(
                cred_file, scopes=['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
            )
        else:
            creds = Credentials.from_authorized_user_file(
                cred_file, scopes=['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
            )
            
        service = build('drive', 'v3', credentials=creds)
        file_name = os.path.basename(zip_path)
        
        # Comprobar si el archivo ya existe en la carpeta para actualizar o crear
        query = f"'{folder_id}' in parents and name='{file_name}' and trashed=false"
        results = service.files().list(q=query, fields="files(id, name, webViewLink)").execute()
        items = results.get('files', [])
        
        media = MediaFileUpload(zip_path, mimetype='application/zip', resumable=True)
        if items:
            existing_id = items[0]['id']
            updated = service.files().update(fileId=existing_id, media_body=media, fields='id, name, webViewLink').execute()
            return {"attempted": True, "success": True, "file_id": updated.get('id'), "link": updated.get('webViewLink'), "action": "actualizado"}
        else:
            meta = {'name': file_name, 'parents': [folder_id]}
            created = service.files().create(body=meta, media_body=media, fields='id, name, webViewLink').execute()
            return {"attempted": True, "success": True, "file_id": created.get('id'), "link": created.get('webViewLink'), "action": "creado"}
            
    except Exception as e:
        return {"attempted": True, "success": False, "error": str(e)}

def export_course_to_gdrive(zip_path, course_spec, course_dir):
    """
    Función principal de exportación invocada por build.py.
    """
    auto_export = getattr(course_spec, "GDRIVE_AUTO_EXPORT", True)
    if not auto_export:
        return {"status": "skipped", "message": "Exportación a Google Drive deshabilitada (GDRIVE_AUTO_EXPORT=False)"}

    target_url = getattr(course_spec, "GDRIVE_FOLDER_URL", None)
    target_id = getattr(course_spec, "GDRIVE_FOLDER_ID", None)
    custom_local = getattr(course_spec, "GDRIVE_LOCAL_PATH", None)
    
    # Resolver ID y URL canónica
    folder_id, canonical_url = parse_gdrive_target(target_id or target_url)
    
    print("\n" + "=" * 65)
    print(" ☁️  EXPORTACIÓN Y SINCRONIZACIÓN CON GOOGLE DRIVE")
    print("=" * 65)
    
    if folder_id:
        print(f"📁 Carpeta de destino : {canonical_url}")
        print(f"🆔 ID en Google Drive : {folder_id}")
    else:
        print("⚠️  No se ha especificado URL o ID de Google Drive en course_spec.py")

    results = {
        "folder_id": folder_id,
        "canonical_url": canonical_url,
        "api_upload": None,
        "desktop_copies": [],
        "local_copies": [],
    }

    # 1. Intento de subida directa por API de Google Drive
    if folder_id:
        api_res = upload_via_gdrive_api(zip_path, folder_id, course_dir)
        results["api_upload"] = api_res
        if api_res.get("success"):
            print(f"  ✓ Subida directa exitosa vía Google Drive API ({api_res.get('action')})")
            print(f"    Enlace directo: {api_res.get('link')}")
        elif api_res.get("attempted"):
            print(f"  ⚠️  Fallo en la API de Google Drive: {api_res.get('error')}")

    # 2. Búsqueda y sincronización con Google Drive for Desktop
    desktop_roots = find_gdrive_desktop_paths(custom_local)
    zip_filename = os.path.basename(zip_path)
    
    copied_to_desktop = False
    if desktop_roots:
        for root in desktop_roots:
            try:
                dest_path = os.path.join(root, zip_filename)
                shutil.copy2(zip_path, dest_path)
                results["desktop_copies"].append(dest_path)
                copied_to_desktop = True
                print(f"  ✓ Sincronizado en Google Drive Desktop: {dest_path}")
            except Exception:
                pass
                
    if not copied_to_desktop and not (results["api_upload"] and results["api_upload"].get("success")):
        preferred_letter = get_drivefs_mount_letter()
        print(f"  ℹ️  Google Drive for Desktop no está montado activamente en {preferred_letter}:\\")

    # 3. Copia de cortesía y seguridad en el repositorio local de cursos y Descargas
    local_repos = find_local_training_repos()
    for repo_path, label in local_repos:
        try:
            dest = os.path.join(repo_path, zip_filename)
            shutil.copy2(zip_path, dest)
            results["local_copies"].append(dest)
            print(f"  ✓ {label}:")
            print(f"    -> {dest}")
        except Exception:
            pass

    # 4. Resumen e instrucciones
    print("-" * 65)
    if results["api_upload"] and results["api_upload"].get("success"):
        print("🎉 El curso se encuentra publicado y actualizado en tu Google Drive.")
    elif results["desktop_copies"]:
        print("🎉 El paquete SCORM se sincronizará automáticamente con tu Google Drive.")
    else:
        print("📌 Para depositar el curso en la carpeta de Google Drive:")
        if canonical_url:
            print(f"   1. Abre la carpeta web:")
            print(f"      🔗 {canonical_url}")
            print(f"   2. Arrastra directamente el archivo desde:")
            print(f"      📦 {zip_path}")
        print("\n💡 Nota de productividad:")
        print("   Inicia Google Drive for Desktop en Windows para que todas tus")
        print("   compilaciones se sincronicen directamente en la nube sin pasos manuales.")
    print("=" * 65 + "\n")

    return results
