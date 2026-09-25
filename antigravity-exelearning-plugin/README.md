# Antigravity eXeLearning Plugin

Plugin de automatización para **Google Antigravity** que permite generar, maquetar, validar y empaquetar cursos interactivos en formato **SCORM 1.2** compatibles al 100% con **eXeLearning**, **EducaMadrid** y **Moodle**.

---

## 🚀 Instalación en Cualquier Equipo

Para disponer de este plugin en cualquier máquina donde utilices Antigravity, sólo tienes que clonarlo en tu directorio global de configuración de Gemini/Antigravity:

### En Linux / macOS / WSL:
```bash
git clone https://github.com/jmgurpegui/EXELEARNING.git ~/EXELEARNING
cp -r ~/EXELEARNING/antigravity-exelearning-plugin ~/.gemini/config/plugins/antigravity-exelearning-plugin
```

### En Windows (PowerShell):
```powershell
git clone https://github.com/jmgurpegui/EXELEARNING.git "$HOME\EXELEARNING"
Copy-Item -Recurse "$HOME\EXELEARNING\antigravity-exelearning-plugin" "$HOME\.gemini\config\plugins\antigravity-exelearning-plugin"
```

> **¡Listo!** Antigravity detectará el plugin automáticamente en cualquier terminal o proyecto que abras en esa máquina. No necesitas reiniciar ningún servicio ni añadir configuraciones adicionales.

---

## 💡 Cómo Usarlo

Una vez instalado, el agente de Antigravity reconocerá automáticamente las tareas relacionadas con eXeLearning. Puedes pedirle directamente en el chat:

- *"Crea un curso eXeLearning sobre Energías Renovables con 3 temas y un examen final."*
- *"Convierte los apuntes del archivo tema1.pdf en un curso SCORM."*
- *"Añade un cuestionario interactivo de 5 preguntas sobre prevención de riesgos a mi curso actual."*
- *"Compila y valida el curso de la carpeta actual para subirlo a EducaMadrid."*

El agente activará el skill `exelearning-builder`, utilizará la plantilla incorporada, redactará los contenidos maquetados con iconos oficiales de eXeLearning y compilará el archivo `.zip` final con 0 errores de validación DTD y firmas XML válidas.

---

## 📦 Estructura del Plugin

```text
antigravity-exelearning-plugin/
├── plugin.json                                # Manifiesto del plugin
├── README.md                                  # Esta guía de instalación y uso
├── rules/
│   └── AGENTS.md                              # Reglas de maquetación, DTD y buenas prácticas
└── skills/
    └── exelearning-builder/
        ├── SKILL.md                           # Instrucciones operativas del agente
        └── resources/
            └── Plantilla-Exelearning/         # Plantilla autónoma completa (runtime, build.py, core)
```

---

## ☁️ Recomendación de Flujo: GitHub + Google Drive

Para conseguir la **máxima velocidad y seguridad**:

1. **Herramienta y Plantilla (Este Plugin) en GitHub**:
   - Git garantiza control de versiones, actualización instantánea (`git pull`) y carga sin latencia en Antigravity.
2. **Desarrollo y Compilación en Local**:
   - Generar y compilar los cursos en el disco local (`python3 build.py`) es ultrarrápido y evita problemas de concurrencia o bloqueos de red al generar cientos de archivos XML y recursos web.
3. **Almacenamiento y Entrega de Cursos en Google Drive**:
   - Una vez compilado el paquete **`<Nombre_Curso>_SCORM.zip`**, guárdalo en tu carpeta de Google Drive. Desde allí tendrás copia de seguridad garantizada y podrás compartir el enlace directo con administradores de Moodle o compañeros docentes.

---

## 🔄 Actualización

Si realizas mejoras en la plantilla o en las reglas:
```bash
cd ~/.gemini/config/plugins/antigravity-exelearning-plugin
git pull
```
Todos tus equipos estarán actualizados al instante.
