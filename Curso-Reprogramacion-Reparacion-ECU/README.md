# Plantilla eXeLearning (SCORM 1.2)

Plantilla optimizada para generar paquetes de formación interactiva en formato **SCORM 1.2**, compatibles al 100% con **eXeLearning** y aceptados directamente por el **Aula Virtual de EducaMadrid y plataformas Moodle**, incorporando todas las firmas de autenticidad exigidas (`content.xml`, `content.dtd`, `imslrm.xml`, `imsmanifest.xml`).

---

## ⚡ Guía Rápida (3 Pasos)

### 1. Copia la plantilla para tu nuevo curso
Crea una carpeta propia para el curso que vas a desarrollar:
```bash
cp -r Plantilla-Exelearning MiNuevoCurso
cd MiNuevoCurso
```

### 2. Edita los contenidos
- **`course_spec.py`**: Define el título (`COURSE`), la lista de páginas (`PAGES`), el contenido de cada tema en `BODIES`, y las preguntas del cuestionario final en `PREGUNTAS`.
- **`media/`**: Guarda imágenes (`media/img/`), documentos descargables (`media/files/`), vídeos (`media/video/`) o audios (`media/audio/`).

### 3. Compila y empaqueta en un solo comando
Ejecuta:
```bash
python3 build.py
```
*(También puedes compilar desde fuera pasando la ruta: `python3 Plantilla-Exelearning/build.py MiNuevoCurso`)*

    1. Monta el runtime eXe y recursos multimedia en `pkg/`.
    2. Genera los archivos HTML y las firmas de autenticidad (`content.xml`, `imslrm.xml`, `imsmanifest.xml`).
    3. Valida la sintaxis XML, la conformidad estricta contra `content.dtd` y la consistencia disco <-> manifiesto (0 errores).
    4. Genera el entregable comprimido **`<Nombre_del_Curso>_SCORM.zip`** listo para subir a Moodle / EducaMadrid.
    5. Deposita y sincroniza automáticamente el paquete en la carpeta correspondiente de **Google Drive** y en el repositorio local de cursos.

---

## 📁 Estructura de la Carpeta

```
Plantilla-Exelearning/
├── README.md                      # Esta guía simplificada y optimizada
├── course_spec.py                 # Especificación del curso (título, páginas, HTML, test y Google Drive)
├── quiz_engine.html               # Motor JavaScript de autoevaluación con reporte SCORM
├── Ficha_de_encargo_del_curso.docx # Ficha editable para toma de requerimientos
├── media/                         # Recursos propios aportados por el autor
│   ├── img/                       # Imágenes (PNG, JPG, SVG, WebP)
│   ├── files/                     # Documentos adjuntos (PDF, DOCX, ZIP)
│   ├── video/                     # Vídeos (MP4, WebM)
│   └── audio/                     # Audios (MP3, OGG)
├── build.py                       # Compilador, validador y empaquetador automático
├── core/                          # Motor interno de generación
│   ├── gen_common.py              # Funciones auxiliares de maquetación HTML y navegación
│   ├── gen_content_xml.py         # Generador de firmas eXeLearning y metadatos LOM-ES
│   └── gdrive_export.py           # Conector de sincronización con Google Drive (Desktop y API)
└── runtime/                       # Runtime validado de eXeLearning (librerías, tema, MathJax, DTD)
```

---

## 🛠️ Maquetación y Componentes (`course_spec.py`)

### Bloques de Contenido (`box`)
Para añadir cajas de contenido atractivas con iconos de eXeLearning:
```python
from gen_common import box, nav_block

# En páginas interiores (html/): usar prefix="../"
BODIES["mi-tema"] = box("1. Fundamentos Técnicos", "book", r"""
<p>Explicación técnica con texto y elementos visuales.</p>

<div class="callout nota">
  <span class="cap">Nota Técnica</span>
  <p>Detalle importante o advertencia de seguridad.</p>
</div>
""", prefix="../") + nav_block("mi-tema")

# En la portada (index): usar prefix=""
```

### Referencia de Rutas a Imágenes
- En la portada (`index.html`): `<img src="content/img/mi_imagen.png" alt="...">`
- En páginas interiores (`html/tema.html`): `<img src="../content/img/mi_imagen.png" alt="...">`

### Fórmulas Matemáticas (MathJax local)
Funciona 100% offline sin dependencias externas:
- En línea: `\( V = I \cdot R \)`
- En bloque: `\[ P = \frac{V^2}{R} \]`

### Iconos Disponibles (`theme/icons/`)
`activity`, `agreement`, `alert`, `arts`, `ask`, `book`, `calculate`, `case`, `chrono`, `collaborative`, `competencies`, `diary`, `discuss`, `download`, `explore`, `file`, `guide`, `history`, `info`, `interactive`, `math`, `objectives`, `observe`, `play`, `present`, `reflection`, `roadmap`, `share`, `start`, `stop`, `technology`, `think`, `video`.

---

## 📝 Configuración del Cuestionario SCORM

El motor interactivo (`quiz_engine.html`) incluye presentación **pregunta a pregunta (1 en 1)**, muestreo aleatorio de banco de preguntas y guardián anti-patrones:

```javascript
// Número de preguntas mostradas por intento (ej. 20 extraídas de un banco de 50)
var NUM_PREGUNTAS = 20;

// Activa el barajado aleatorio de alternativas con guardián anti-patrones (por defecto true)
var RANDOMIZE_OPTIONS = true;

// Porcentaje mínimo para aprobar
var PASS = 50;

// Banco completo de preguntas (ej. 50 preguntas):
var PREGUNTAS = [
  {
    q: "¿Cuál es la unidad de medida de la resistencia eléctrica en el SI?",
    opts: ["Voltio", "Ohmio", "Amperio", "Vatio"],
    correct: 1, // Opción B
    fb: "Correcto. El Ohmio (Ω) es la unidad de resistencia eléctrica."
  },
  // ... resto de preguntas del banco ...
];
```

### Características del Motor de Evaluación:
- **Navegación Pregunta a Pregunta (1 en 1)**: El alumno visualiza una única pregunta por pantalla, pudiendo avanzar con `Siguiente`, retroceder con `Anterior` o saltar directamente mediante la barra de píldoras numeradas (`1..20`).
- **Muestreo Aleatorio (ej. 20 de 50)**: En cada intento del alumno, el motor selecciona aleatoriamente 20 preguntas sin repetición del banco total.
- **Sin Patrones Predecibles (Guardián Anti-Patrón)**: Las alternativas se barajan dinámicamente y el algoritmo previene rachas consecutivas (evita secuencias como A, A, A o ciclos A, B, C, D), logrando una distribución equilibrada y auténticamente aleatoria.
- **Revisión y SCORM 1.2**: Tras corregir, las píldoras se tiñen de verde (acierto) o rojo (fallo), se muestra el porcentaje obtenido, se envía la nota al Libro de Calificaciones de Moodle/EducaMadrid (`cmi.core.score.raw`), y se permite revisar todas las explicaciones o reintentar con un nuevo test aleatorio.

---

## 📤 Entrega en EducaMadrid / Moodle

1. En tu curso del Aula Virtual, activa la edición.
2. Selecciona **"Añadir una actividad o recurso"** ➡️ **"Paquete SCORM"**.
3. Sube el archivo **`.zip`** generado por `build.py` (sin descomprimir).
4. Configura intentos y calificación según prefieras y guarda los cambios.

---

## ☁️ Integración y Sincronización con Google Drive

La plantilla permite depositar automáticamente el entregable final en la carpeta de Google Drive que hayas utilizado como fuente de información o almacén de entrega:

### Configuración en `course_spec.py`:
```python
# URL completa o ID de la carpeta de Google Drive:
GDRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/1ZDaXiUeZ61kx-gTUsmo-gavCCB2T_sqR"
GDRIVE_FOLDER_ID = ""   # Opcional (se extrae automáticamente si se omite)
GDRIVE_LOCAL_PATH = None # Opcional: ruta local personalizada
GDRIVE_AUTO_EXPORT = True # Activa la exportación al compilar
```

### Métodos de Entrega Soportados:
1. **Google Drive for Desktop (Sincronización en segundo plano)**:
   - Al ejecutar `build.py`, si la aplicación Google Drive for Desktop está iniciada, detecta la unidad virtual (`G:\Mi unidad` o `/mnt/g/`) y deposita el `.zip` directamente para que se sincronice en la nube.
2. **Google Drive API v3 (Subida directa a la nube)**:
   - Si se coloca un archivo `credentials.json` o `token.json` (OAuth2 o cuenta de servicio), el script sube y actualiza el archivo en Google Drive automáticamente mediante la API.
3. **Repositorio local y enlace de entrega**:
   - Guarda una copia de seguridad en tu carpeta de entregas (`H:\0-TRAINING\Scorm` y `Descargas`) y muestra en la consola el enlace web directo a la carpeta de Google Drive para subir con un solo clic.

