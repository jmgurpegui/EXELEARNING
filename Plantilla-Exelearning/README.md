# Plantilla eXeLearning 2026 (SCORM 1.2 / REA)

Plantilla oficial optimizada para generar paquetes de formación interactiva en formato **SCORM 1.2**, compatibles al 100% con **eXeLearning v4.0.1 (versión 2026)** y aceptados directamente por el **Aula Virtual de EducaMadrid y plataformas Moodle**, incorporando todas las firmas de autenticidad exigidas (`content.xml`, `content.dtd`, `imslrm.xml`, `imsmanifest.xml`).

---

## 📐 Metodología y Prompt de Diseño Instruccional (EducaMadrid / FP)

Para garantizar la compatibilidad pedagógica y técnica con el estándar **SCORM 1.2** y asegurar el **registro automático de calificaciones al 100% en Moodle**, la plantilla implementa la siguiente metodología oficial de diseño instruccional para Formación Profesional:

### 🎯 Prompt Maestro para Generación de Contenidos Técnicos con IA
*(Disponible también como archivo independiente en [`PROMPT_DISENO_INSTRUCCIONAL.md`](PROMPT_DISENO_INSTRUCCIONAL.md))*

```markdown
Actúa como un diseñador instruccional y experto técnico en eXeLearning y plataformas Moodle (Aula Virtual de EducaMadrid).

Tu objetivo es estructurar el contenido de una unidad didáctica técnica para Formación Profesional garantizando compatibilidad total con el estándar SCORM 1.2 y el registro automático de calificaciones.

---

### Datos de entrada:
- Materia/Módulo: [Insertar módulo, ej.: Circuitos Eléctricos Auxiliares del Vehículo]
- Unidad/Tema: [Insertar título del tema]
- Nivel formativo: FP Grado Medio / Superior
- Contenidos clave a desarrollar: [Listar temas o epígrafes]

---

### Requisitos de diseño y estructura:
1. **Árbol de contenidos:**
   - Estructura modular dividida en epígrafes claros y jerárquicos.
   - Lenguaje técnico, riguroso y redactado siempre en segunda persona (aprenderás, debes comprobar, utiliza).
   - Inclusión de ejemplos prácticos de taller y diagnóstico.

2. **Propuesta de iDevices para eXeLearning:**
   - Para contenidos explicativos y procedimentales: especificar el uso de iDevice Texto.
   - Para actividades de autoevaluación formativa intermedia (sin calificación en Moodle): sugerir iDevice Pregunta de Selección Múltiple o Actividad desplegable, indicando explícitamente que son de práctica.

3. **Evaluación final SCORM obligatoria:**
   - Debe reservarse una página final específica denominada "Evaluación Final".
   - Debe diseñarse explícitamente para el iDevice Cuestionario SCORM (el único que envía variables cmi.core.score.raw al libro de calificaciones de Moodle).
   - Genera 10 preguntas tipo test de 4 opciones (1 correcta, 3 distractores técnicos plausibles).
   - Proporciona para cada pregunta:
     - Enunciado claro y contextualizado técnicamente.
     - Opciones A, B, C y D identificando la correcta.
     - Retroalimentación pedagógica técnica que justifique la respuesta correcta y descarte los errores comunes.

4. **Instrucciones de exportación y configuración:**
   - Recordatorio del estándar de empaquetado (SCORM 1.2).
   - Ajustes recomendados para la actividad en Moodle (Método de calificación: Calificación más alta, escala sobre 10 y visualización en la página actual).
```

---

## 🚀 Novedades y Mejoras eXeLearning 2026

La plantilla integra la arquitectura y componentes oficiales de **eXeLearning 2026 (v4.0.1)**:
- **Página 'Evaluación Final' Normalizada**: Diseñada exclusivamente para el iDevice **Cuestionario SCORM**, enviando `cmi.core.score.raw` al libro de calificaciones de Moodle.
- **Escala Decimal Oficial (0 a 10)**: Mapeo automático de notas sobre 10 (`cmi.core.score.max = 10`), evitando discordancias con las ponderaciones oficiales de FP en EducaMadrid.
- **Declaración de Mastery Score en el Manifiesto**: El archivo `imsmanifest.xml` incluye `<adlcp:masteryscore>5</adlcp:masteryscore>` en el ítem de evaluación para sincronizar con la regla de dominio de Moodle.
- **Nuevo Tema Visual "Zen"**: Diseño moderno, equilibrado y adaptable a cualquier dispositivo móvil.
- **Tipografía "Inter" Integrada**: Tipografía nativa offline (`theme/fonts/`) de gran legibilidad técnica.
- **50 Iconos Vectoriales SVG**: Gráficos nítidos a cualquier resolución (`theme/icons/*.svg`).
- **Barra de Accesibilidad REA (`exe_atools`)**: Contraste, tamaño de texto y tipografías para dislexia (*OpenDyslexic*).
- **Suite Ampliada de iDevices**: Incluye *text*, *form*, *download-source-file*, *slide*, *trueorfalse*, *quick-questions*, *guess*, *az-quiz-game* y *adaptative-quiz*.
- **Cierre Seguro SCORM**: Botón `💾 Confirmar y Guardar Calificación Oficial` que ejecuta `LMSCommit` y `LMSFinish` de forma explícita.
- **Corrección de Bug Histórico de Estado ("No intentado")**: Eliminado el valor `"unknown"` en SCORM 1.2 que reseteaba a los alumnos a *"no intentado"*.

---

## ⚡ Guía Rápida (3 Pasos)

### 1. Copia la plantilla para tu nuevo curso
Crea una carpeta propia para el curso que vas a desarrollar:
```bash
cp -r Plantilla-Exelearning MiNuevoCurso
cd MiNuevoCurso
```

### 2. Edita los contenidos
- **`course_spec.py`**: Define el título (`COURSE`), la lista de páginas (`PAGES`), el contenido de cada tema en `BODIES`, y las 10 preguntas de la evaluación final en `PREGUNTAS`.
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
├── PROMPT_DISENO_INSTRUCCIONAL.md # Prompt maestro de diseño instruccional para FP
├── course_spec.py                 # Especificación del curso (título, páginas, HTML, test y Google Drive)
├── quiz_engine.html               # Motor JavaScript de autoevaluación con reporte SCORM sobre 10
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
BODIES["unidad-1-conceptos"] = box("1. Fundamentos Técnicos", "book", r"""
<p>Explicación técnica con texto y elementos visuales redactada en segunda persona.</p>

<div class="callout nota">
  <span class="cap">Regla de Oro en Taller</span>
  <p>Detalle importante o advertencia de seguridad.</p>
</div>
""", prefix="../") + nav_block("unidad-1-conceptos")

# En la portada (index): usar prefix=""
```

### Iconos Vectoriales Disponibles (`theme/icons/` - formato SVG)
`activity`, `agreement`, `alert`, `arts`, `ask`, `book`, `calculate`, `case`, `chrono`, `collaborative`, `competencies`, `diary`, `diary_alt`, `discuss`, `download`, `draw`, `english`, `experiment`, `explore`, `file`, `gallery`, `geography`, `guide`, `history`, `info`, `interactive`, `letters`, `listen`, `math`, `music`, `nature`, `objectives`, `observe`, `passport`, `perform`, `piece`, `pieces`, `play`, `present`, `reflection`, `roadmap`, `share`, `sport`, `start`, `stop`, `suitcase`, `technology`, `think`, `think_alt`, `video`.

---

## 📝 Configuración de la Evaluación Final SCORM

El motor interactivo (`quiz_engine.html`) incluye presentación **1 a 1**, escala sobre 10, muestreo aleatorio y guardián anti-patrones:

```javascript
// Escala de calificación oficial en Moodle (10 para escala sobre 10 de FP, o 100)
var SCORE_SCALE = 10;

// Número de preguntas mostradas por intento (ej. 10)
var NUM_PREGUNTAS = 10;

// Activa el barajado aleatorio de alternativas con guardián anti-patrones (por defecto true)
var RANDOMIZE_OPTIONS = true;

// Porcentaje mínimo para aprobar (50% = 5.0 sobre 10)
var PASS = 50;

// Banco completo de preguntas:
var PREGUNTAS = [
  {
    q: "¿Cuál es la caída de tensión máxima admisible en una línea de potencia en automoción?",
    opts: ["1,5 V", "0,2 V a 0,3 V", "3,0 V", "0,00 V"],
    correct: 1, // Opción B
    fb: "Correcto. En conductores principales de potencia, la caída no debe exceder de 0,2 V a 0,3 V."
  },
  // ... resto de preguntas del banco ...
];
```

---

## 🔍 Diagnóstico: "¿Por qué no se registraban las calificaciones?"

1. **Colisión de estados en SCORM 1.2**:
   - En SCORM 1.2 solo existe una variable para estado: `cmi.core.lesson_status`.
   - Si se llamaba a `SetCompletionScormActivity("passed")` y después a `SetCompletionStatus("completed")`, la segunda llamada **sobrescribía `"passed"` convirtiéndolo en `"completed"`**.
   - En Moodle, si la finalización de la actividad exige *"Requerir estado: Aprobado (Passed)"*, o si actúa *"El puntaje de dominio anula el estado"*, Moodle no certificaba la superación del test.
   - **Solución implementada**: El motor ahora preserva de manera estricta `"passed"` (o `"failed"`) sin sobrescribirlo.

2. **Falta de correspondencia de escala (100 vs 10)**:
   - Los docentes en España configuran la calificación de la actividad en Moodle con una escala sobre **10**.
   - Si el paquete enviaba un `cmi.core.score.raw` de 80 (sobre 100), Moodle truncaba la nota o la marcaba fuera de rango.
   - **Solución implementada**: `SCORE_SCALE = 10` normaliza la nota oficial a escala decimal (ej. 8,5 sobre 10) y declara `<adlcp:masteryscore>5</adlcp:masteryscore>`.

3. **Cierre sin LMSFinish / LMSCommit**:
   - Al cerrar la pestaña pulsando la 'X', los navegadores cancelan las peticiones de guardado síncronas.
   - **Solución implementada**: El botón `💾 Confirmar y Guardar Calificación Oficial` fuerza el guardado antes de permitir el cierre de la ventana.

---

## ⚙️ Ajustes Recomendados en EducaMadrid / Moodle

Al subir el paquete SCORM al Aula Virtual:
1. **Apariencia**:
   * **Visualización del paquete**: `En la página actual` (evita bloqueos de ventanas emergentes en navegadores).
2. **Calificación**:
   * **Método de calificación**: `Calificación más alta`.
   * **Calificación máxima**: `10` (coincidente con la escala de Formación Profesional).
3. **Ajustes de compatibilidad**:
   * **El puntaje de dominio anula el estado**: Dejar en `Sí` (coincide con el mastery score de 5 sobre 10) o `No` si se desea evaluar por lectura.
4. **Finalización de actividad**:
   * Seleccionar: *Mostrar la actividad como completada cuando se cumplan las condiciones*.
   * Marcar: **`Requerir estado: Pasado`** y **`Requerir estado: Completado`**.

---

## ☁️ Integración y Sincronización con Google Drive

Configuración en `course_spec.py`:
```python
GDRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/TU_CARPETA_AQUI"
GDRIVE_AUTO_EXPORT = True
```
1. **Google Drive for Desktop**: Detecta automáticamente unidades montadas (`G:\Mi unidad` o `/mnt/g/`) y deposita el `.zip`.
2. **Google Drive API v3**: Si existe `credentials.json` o `token.json`, sube directamente a la nube.
3. **Repositorio local**: Copia de respaldo en `H:\0-TRAINING\Scorm` y `Descargas`.
