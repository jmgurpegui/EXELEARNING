# Plantilla eXeLearning 2026 (SCORM 1.2 / REA)

Plantilla oficial optimizada para generar paquetes de formación interactiva en formato **SCORM 1.2**, compatibles al 100% con **eXeLearning v4.0.1 (versión 2026)** y aceptados directamente por el **Aula Virtual de EducaMadrid y plataformas Moodle**, incorporando todas las firmas de autenticidad exigidas (`content.xml`, `content.dtd`, `imslrm.xml`, `imsmanifest.xml`).

---

## 🚀 Novedades y Mejoras eXeLearning 2026

La plantilla ha sido completamente actualizada con el motor y componentes de **eXeLearning 2026 (v4.0.1)**:
- **Nuevo Tema Visual "Zen"**: Sustituye al tema clásico por el diseño oficial más moderno, limpio y equilibrado.
- **Tipografía "Inter" Integrada**: Tipografía nativa offline (`theme/fonts/`) de gran legibilidad técnica en pantallas y dispositivos móviles.
- **50 Iconos Vectoriales SVG**: Gráficos nítidos a cualquier resolución y densidad de pantalla (`theme/icons/*.svg`), eliminando el pixelado de los antiguos PNG.
- **Barra de Accesibilidad REA (`exe_atools`)**: Soporte nativo para ajuste de contraste, tamaño de texto y tipografías para dislexia (*OpenDyslexic*).
- **Suite Ampliada de iDevices**: Incluye *text*, *form*, *download-source-file*, *slide*, *trueorfalse*, *quick-questions*, *guess*, *az-quiz-game* y *adaptative-quiz*.
- **Cierre Seguro SCORM y Prevención de Pérdida de Notas**: Botón de confirmación y guardado oficial en el LMS (`LMSCommit` + `LMSFinish`), blindado contra cierres involuntarios de pestaña.
- **Corrección de Bug Histórico de Estado ("No intentado")**: Eliminado el valor incompatible `"unknown"` en SCORM 1.2 que provocaba que alumnos figuraran como *"no intentado"* tras cursar el módulo.

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

El compilador realiza automáticamente:
1. Monta el runtime eXe 2026 y recursos multimedia en `pkg/`.
2. Genera los archivos HTML y las firmas de autenticidad (`content.xml`, `imslrm.xml`, `imsmanifest.xml`).
3. Valida la sintaxis XML, la conformidad estricta contra `content.dtd` y la consistencia disco <-> manifiesto (0 errores).
4. Genera el entregable comprimido **`<Nombre_del_Curso>_SCORM.zip`** listo para subir a Moodle / EducaMadrid.
5. Deposita y sincroniza automáticamente el paquete en la carpeta correspondiente de **Google Drive** y en el repositorio local de cursos.

---

## 📁 Estructura de la Carpeta

```
Plantilla-Exelearning/
├── README.md                      # Esta guía técnica completa y documentación de soporte
├── course_spec.py                 # Especificación del curso (título, páginas, HTML, test y Google Drive)
├── quiz_engine.html               # Motor JavaScript de autoevaluación con reporte SCORM y guardado seguro
├── Ficha_de_encargo_del_curso.docx # Ficha editable para toma de requerimientos
├── media/                         # Recursos propios aportados por el autor
│   ├── img/                       # Imágenes (PNG, JPG, SVG, WebP)
│   ├── files/                     # Documentos adjuntos (PDF, DOCX, ZIP)
│   ├── video/                     # Vídeos (MP4, WebM)
│   └── audio/                     # Audios (MP3, OGG)
├── build.py                       # Compilador, validador y empaquetador automático
├── core/                          # Motor interno de generación
│   ├── gen_common.py              # Funciones de maquetación HTML, cabeceras 2026 y navegación
│   ├── gen_content_xml.py         # Generador de firmas eXeLearning v4.0.1 y metadatos LOM-ES
│   └── gdrive_export.py           # Conector de sincronización con Google Drive (Desktop y API)
└── runtime/                       # Runtime validado de eXeLearning 2026 (Zen, librerías, MathJax, DTD)
```

---

## 🛠️ Maquetación y Componentes (`course_spec.py`)

### Bloques de Contenido (`box`)
Para añadir cajas de contenido atractivas con iconos vectoriales SVG de eXeLearning 2026:
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

### Iconos Vectoriales Disponibles (`theme/icons/` - formato SVG)
`activity`, `agreement`, `alert`, `arts`, `ask`, `book`, `calculate`, `case`, `chrono`, `collaborative`, `competencies`, `diary`, `diary_alt`, `discuss`, `download`, `draw`, `english`, `experiment`, `explore`, `file`, `gallery`, `geography`, `guide`, `history`, `info`, `interactive`, `letters`, `listen`, `math`, `music`, `nature`, `objectives`, `observe`, `passport`, `perform`, `piece`, `pieces`, `play`, `present`, `reflection`, `roadmap`, `share`, `sport`, `start`, `stop`, `suitcase`, `technology`, `think`, `think_alt`, `video`.

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

---

## 🔍 Problema: "No intentado" y "El puntaje de dominio anula el estado"

### ¿Qué significa "El puntaje de dominio anula el estado" en Moodle?
En Moodle / EducaMadrid, cada actividad SCORM cuenta con un ajuste interno denominado **"El puntaje de dominio anula el estado"** (`Mastery score overrides status`), el cual viene activado por defecto (`Sí`).
- **Comportamiento**: Si el paquete SCORM define un puntaje de dominio (*mastery score*) o si Moodle evalúa la calificación del paquete:
  1. Cuando finaliza la sesión (`LMSFinish`), Moodle comprueba la nota enviada en `cmi.core.score.raw`.
  2. Si la nota es **igual o superior** al puntaje de dominio, Moodle fija el estado como **`Aprobado` (passed)**.
  3. Si la nota es **inferior** al puntaje de dominio, Moodle **anula** cualquier estado previo (incluso si era "completado") y lo fuerza a **`Reprobado` (failed)**.
  4. Si **no se registró ninguna puntuación** (el alumno navegó pero no envió nota de cuestionario), Moodle no puede certificar la superación.

### ¿Por qué a algunos alumnos que finalizan el curso les figura "No intentado" (*not attempted*)?
Existen **4 causas técnicas combinadas** que provocan este error:

1. **Bug en el ciclo de vida de `SCOFunctions.js` (SCORM 1.2)**:
   - Al cargar la página, el script original ejecutaba `scorm.SetCompletionStatus("unknown")`.
   - En SCORM 1.2 **no existe el estado "unknown"** (solo en SCORM 2004). El conector de SCORM 1.2 traducía `"unknown"` a `"not attempted"`.
   - Como resultado, ¡cada vez que el alumno abría una página, su estado se reiniciaba forzosamente a *"No intentado"*!
   - **Solución aplicada en la plantilla 2026**: Se sustituyó por `"incomplete"`. En cuanto el alumno entra, Moodle registra que la actividad está *En curso / Incompleta*, garantizando que nunca quede como *No intentado*.

2. **Cierre abrupto de la pestaña o ventana del navegador**:
   - Cuando el alumno finaliza la lectura o el test y cierra directamente la ventana pulsando la **'X'** del navegador:
   - Los navegadores modernos (Chrome, Edge, Firefox) **bloquean o cancelan peticiones de red síncronas en el evento `unload`**.
   - Al cancelarse la llamada `LMSFinish()` / `LMSCommit()`, la sesión queda huérfana en el servidor y Moodle conserva el estado previo con el que abrió la página.
   - **Solución aplicada en la plantilla 2026**:
     - Se añadió un botón destacado: **`💾 Confirmar y Guardar Calificación Oficial`**.
     - Al corregir el examen, el botón ejecuta inmediatamente `s.save()` (`LMSCommit`), confirma el envío con el servidor y llama de forma limpia a `s.quit()` (`LMSFinish`) antes de cerrar la ventana.

3. **Incompatibilidad entre Criterios de Finalización de Moodle**:
   - Si en los ajustes de Moodle (*Finalización de actividad*) se configura:
     - *"El estudiante debe recibir una calificación para finalizar"* y *"Requerir calificación aprobatoria"*.
   - Y el alumno obtiene una nota por debajo del corte (por ejemplo 45% cuando el corte es 50%):
     - La opción *"El puntaje de dominio anula el estado"* anula la finalización y marca el intento como *reprobado*.
     - Para Moodle la actividad no cuenta como superada y en el Libro de Calificaciones no se computa como finalizada.

4. **Multi-SCO: Páginas teóricas vs Página de evaluación**:
   - En un paquete multi-página, las páginas de teoría no reportan nota (`cmi.core.score.raw`), solo el cuestionario lo hace.
   - Si el método de calificación de Moodle está en *"Calificación más alta"* pero el alumno no completó el test, no existe nota que asignar en el Libro de Calificaciones.

---

## ⚙️ Configuración Recomendada en EducaMadrid / Moodle

Para asegurar que el 100% de los alumnos registren su nota y estado correctamente:

### 1. En los Ajustes del Paquete SCORM en el Aula Virtual:
- **Calificación**:
  - **Método de calificación**: `Calificación más alta` (si tiene cuestionario) o `Objetos de aprendizaje` (si es solo lectura).
  - **Calificación máxima**: `10` o `100` (coincidente con la escala del curso).
- **Ajustes de compatibilidad**:
  - **El puntaje de dominio anula el estado**:
    - Si deseas que los alumnos que no alcancen el corte aprueben por el mero hecho de ver el contenido: marcar **`No`**.
    - Si deseas exigir que aprueben el test con la nota mínima para considerar la actividad superada: dejar en **`Sí`** (asegurando que la nota de corte en Moodle coincida con `PASS` en `course_spec.py`).
- **Finalización de actividad**:
  - Elegir: *"Mostrar la actividad como completada cuando se cumplan las condiciones"*.
  - Marcar: **`Requerir estado: Pasado`** y **`Requerir estado: Completado`** (marcar ambas casillas para admitir tanto si el LMS evalúa superación como si evalúa completitud).

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
1. **Google Drive for Desktop (Sincronización en segundo plano)**: Detecta la unidad virtual (`G:\Mi unidad` o `/mnt/g/`) y deposita el `.zip` automáticamente.
2. **Google Drive API v3 (Subida directa a la nube)**: Mediante `credentials.json` o `token.json` sube directamente vía API.
3. **Repositorio local y enlace de entrega**: Guarda copia de respaldo en `H:\0-TRAINING\Scorm` y `Descargas`.
