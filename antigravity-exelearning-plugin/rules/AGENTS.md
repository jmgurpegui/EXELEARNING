# Directrices para Generación de Cursos eXeLearning SCORM 1.2

Estas reglas aseguran que cualquier curso generado o modificado sea 100% compatible con eXeLearning, pase la validación estricta de `content.dtd` y sea aceptado sin errores por EducaMadrid y plataformas Moodle.

## 1. Estructura de `course_spec.py`

- **`COURSE`**: Diccionario con metadatos obligatorios (`title`, `description`, `author`, `lang`, `license`).
- **`PAGES`**: Lista ordenada de tuplas `(slug, titulo)`. La primera página DEBE ser `("index", "...")`.
- **`BODIES`**: Diccionario que asocia cada `slug` con su bloque HTML maquetado.
- **Navegación**: Termina cada contenido con `nav_block(slug)` o utiliza la composición estándar.

## 2. Maquetación con Bloques `box` y Prefijos de Ruta

- Para añadir cajas con iconos oficiales de eXeLearning, usa:
  ```python
  from gen_common import box, nav_block

  # En la portada (index): prefix=""
  BODIES["index"] = box("Bienvenida al Curso", "start", r"""...""", prefix="") + nav_block("index")

  # En páginas interiores (html/tema.html): prefix="../" (¡OBLIGATORIO!)
  BODIES["tema-1"] = box("1. Conceptos Clave", "book", r"""...""", prefix="../") + nav_block("tema-1")
  ```
- **Rutas multimedia relativas**:
  - Desde `index`: `<img src="content/img/ejemplo.png" alt="...">`
  - Desde páginas interiores: `<img src="../content/img/ejemplo.png" alt="...">`
- **Iconos válidos**: `activity`, `agreement`, `alert`, `arts`, `ask`, `book`, `calculate`, `case`, `chrono`, `collaborative`, `competencies`, `diary`, `discuss`, `download`, `explore`, `file`, `guide`, `history`, `info`, `interactive`, `math`, `objectives`, `observe`, `play`, `present`, `reflection`, `roadmap`, `share`, `start`, `stop`, `technology`, `think`, `video`.

## 3. Fórmulas Matemáticas (MathJax Offline)

- El runtime incluye MathJax local sin dependencias externas.
- Usa notación TeX estándar con escapes adecuados en strings de Python (o raw strings `r"""..."""`):
  - En línea: `\( E = mc^2 \)`
  - En bloque: `\[ \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi} \]`

## 4. Evaluación y Cuestionario SCORM

- El motor `quiz_engine.html` se comunica con el API SCORM (`cmi.core.score.raw` y `cmi.core.lesson_status`).
- **Aleatorización obligatoria de respuestas correctas**:
  - **PROHIBIDO** situar por defecto o sistemáticamente la respuesta correcta en la primera opción (`correct: 0`), ni seguir patrones predecibles o secuencias fijas.
  - Las respuestas correctas (`correct`) DEBEN alternar aleatoria y equitativamente entre las diferentes opciones (0, 1, 2, 3 -> A, B, C, D).
  - El motor `quiz_engine.html` incluye por defecto `var RANDOMIZE_OPTIONS = true;`, barajando automáticamente las alternativas en cada intento del alumno y calculando la letra correcta mostrada en pantalla.
  - Si una pregunta concreta requiere mantener un orden fijo (por ejemplo, opciones como *"Todas las anteriores"* o *"A y B son correctas"*), añade la propiedad `shuffle: false` a esa pregunta.
- Configura las preguntas en `PREGUNTAS` con este esquema:
  ```javascript
  var RANDOMIZE_OPTIONS = true; // Barajado automático de alternativas por intento
  var PREGUNTAS = [
    {
      q: "¿Primera pregunta de ejemplo?",
      opts: ["Opción de distracción A", "Opción CORRECTA B", "Opción de distracción C", "Opción de distracción D"],
      correct: 1, // Base 0 (opción B)
      fb: "Retroalimentación explicativa tanto si acierta como si falla."
    },
    {
      q: "¿Segunda pregunta de ejemplo?",
      opts: ["Opción CORRECTA A", "Opción de distracción B", "Opción de distracción C", "Opción de distracción D"],
      correct: 0, // Base 0 (opción A)
      fb: "Retroalimentación formativa justificando la solución correcta."
    },
    {
      q: "¿Tercera pregunta de ejemplo?",
      opts: ["Opción de distracción A", "Opción de distracción B", "Opción CORRECTA C", "Opción de distracción D"],
      correct: 2, // Base 0 (opción C)
      fb: "Fundamento normativo o técnico de la respuesta."
    },
    {
      q: "¿Cuarta pregunta de ejemplo?",
      opts: ["Opción de distracción A", "Opción de distracción B", "Opción de distracción C", "Opción CORRECTA D"],
      correct: 3, // Base 0 (opción D)
      fb: "Aclaración técnica reforzando el concepto clave."
    }
  ];
  var PASS = 50; // Calificación mínima porcentual para superar el curso (0-100)
  ```

## 5. Validación y Compilación Obligatoria

- Toda generación o modificación debe compilarse ejecutando:
  ```bash
  python3 build.py
  ```
- El validador incorporado en `build.py` revisa:
  1. Integridad de archivos contra `imsmanifest.xml`.
  2. Cumplimiento contra `content.dtd` de eXeLearning.
  3. Formato LOM-ES en `imslrm.xml`.
- Si el compilador arroja algún error o advertencia, corrige inmediatamente el HTML o los metadatos hasta obtener **0 errores**.
