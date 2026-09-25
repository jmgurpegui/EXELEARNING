# Sistema de Generación de Cursos SCORM eXeLearning

Kit optimizado para crear cursos interactivos en formato **SCORM 1.2** compatibles con **eXeLearning** y aceptados por el **Aula Virtual de EducaMadrid y Moodle**, con validación automática y firmas de autenticidad integradas.

---

## 📂 Contenido del Repositorio

El repositorio incluye la plantilla de trabajo autónoma y el plugin oficial para **Google Antigravity**:

1. 👉 **[`Plantilla-Exelearning/`](Plantilla-Exelearning/)**: Plantilla lista para usar y crear cursos directamente desde la terminal.
2. 👉 **[`antigravity-exelearning-plugin/`](antigravity-exelearning-plugin/)**: Plugin para Antigravity con reglas automáticas de maquetación y el skill `exelearning-builder`.

```
EXELEARNING/
├── Plantilla-Exelearning/             # Plantilla completa y autónoma para crear cursos
│   ├── course_spec.py                # Especificación de páginas, contenidos y test (patrón aleatorio)
│   ├── quiz_engine.html              # Motor de cuestionario interactivo SCORM (barajado dinámico)
│   ├── Ficha_de_encargo_del_curso.docx # Ficha para toma de requerimientos
│   ├── media/                        # Recursos propios (imágenes, PDFs, vídeos, audios)
│   ├── build.py                      # Compilador, validador y empaquetador ZIP en 1 comando
│   ├── core/                         # Módulos de generación de HTML y firmas XML
│   ├── runtime/                      # Motor eXe validado (librerías, tema, MathJax, DTD)
│   └── README.md                     # Guía detallada y componentes de maquetación
├── antigravity-exelearning-plugin/    # Plugin para Antigravity (skills + reglas de autoría)
└── README.md                         # Esta guía general
```

---

## 🎲 Cuestionarios con Respuestas Aleatorias (Anti-Patrón)

La plantilla incorpora un sistema para evitar que las respuestas correctas sigan un patrón fijo (por ejemplo, que la primera opción sea siempre la correcta):
- **Motor interactivo dinámico (`quiz_engine.html`)**: Por defecto baraja aleatoriamente el orden de las alternativas en cada intento del alumno (`RANDOMIZE_OPTIONS = true`), manteniendo el seguimiento de la opción correcta y recalculando la letra mostrada (A, B, C, D) y la retroalimentación.
- **Directrices de redacción pedagógica**: En las especificaciones (`course_spec.py`, `rules/AGENTS.md`, `SKILL.md`), las respuestas correctas se distribuyen de forma equilibrada y heterogénea entre las opciones `0`, `1`, `2` y `3` para evitar sesgos en el material de origen.
- **Control por pregunta**: Si alguna pregunta requiere mantener el orden de sus opciones (ej. *"Todas las anteriores"* o *"A y B son correctas"*), se puede indicar `shuffle: false` en dicha pregunta.

---

## 🚀 Uso Rápido

Para iniciar un nuevo curso manualmente:

```bash
# 1. Copiar la plantilla
cp -r Plantilla-Exelearning MiCurso
cd MiCurso

# 2. Personalizar course_spec.py y colocar recursos en media/

# 3. Compilar y empaquetar en un solo paso
python3 build.py
```

El script genera automáticamente el paquete final **`<Nombre_Curso>_SCORM.zip`** validado y listo para subir directamente a Moodle / EducaMadrid.

Para más detalles, consulta la documentación completa en **[`Plantilla-Exelearning/README.md`](Plantilla-Exelearning/README.md)**.
