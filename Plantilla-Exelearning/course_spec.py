# -*- coding: utf-8 -*-
"""
Plantilla para la especificación de un curso SCORM 1.2 compatible con eXeLearning.

Estructura:
  1. gen_common.COURSE: Título del curso.
  2. gen_common.PAGES: Lista de páginas del curso (índice, contenidos, cuestionario).
  3. BODIES: Diccionario {slug: html_body} con el contenido de cada página.
     - Usa gen_common.box(titulo, icono, html, prefix=...) para secciones de contenido.
     - Finaliza cada página con gen_common.nav_block(slug).
     - En portada (index) usa prefix="".
     - En el resto de páginas (html/) usa prefix="../".
  4. Cuestionario interactivo:
     - Configuración RANDOMIZE_OPTIONS = true para barajar opciones automáticamente en el alumno.
     - Incluye PREGUNTAS (array de objetos {q, opts, correct, fb}).
     - IMPORTANTE: La respuesta correcta (correct) DEBE distribuirse aleatoriamente entre 0, 1, 2 y 3 (A, B, C, D).
     - Evita fijar sistemáticamente la primera opción (correct: 0) o patrones repetitivos.
     - PASS: porcentaje mínimo para aprobar (por defecto 50).
     - Integra automáticamente el motor quiz_engine.html.
"""
import os
import gen_common
from gen_common import box, nav_block

# ---------------------------------------------------------------------------
# 1. TÍTULO DEL CURSO Y ESTRUCTURA DE PÁGINAS
# ---------------------------------------------------------------------------
gen_common.COURSE = "Nombre del Curso / Módulo"

gen_common.PAGES = [
    dict(slug="index",              pid="page-00", title="Portada",                  nav="Portada",       icon="objectives"),
    dict(slug="unidad-1-conceptos", pid="page-01", title="1. Conceptos Fundamentales", nav="1. Conceptos",  icon="book"),
    dict(slug="cuestionario",       pid="page-02", title="Cuestionario de Evaluación", nav="Cuestionario", icon="activity"),
]

# ---------------------------------------------------------------------------
# 2. CONTENIDO DE CADA PÁGINA (BODIES)
# ---------------------------------------------------------------------------
BODIES = {}

# --- Portada ---
BODIES["index"] = r"""
<div class="curso-banner"><img src="content/img/logo.png" alt="Logotipo o Cabecera"></div>
<div class="curso-hero">
  <p class="kicker">CICLO FORMATIVO / CURSO</p>
  <h2>Nombre del Curso / Módulo</h2>
  <p>Descripción general de los objetivos, competencias y contenidos que se abordarán en este curso.</p>
  <div class="tags"><span>Unidad 1</span><span>SCORM 1.2</span><span>Digital Interactivo</span></div>
</div>
""" + box("Objetivos del Curso", "objectives", r"""
<ul class="ra-list">
  <li>Identificar los principios y conceptos fundamentales de la materia.</li>
  <li>Aplicar los procedimientos y buenas prácticas requeridas en el ámbito profesional.</li>
  <li>Superar la evaluación final interactiva demostrando la asimilación de contenidos.</li>
</ul>
""", prefix="") + nav_block("index")

# --- Unidad 1 ---
BODIES["unidad-1-conceptos"] = box("1. Introducción y Fundamentos", "book", r"""
<p>Este es un apartado de contenido de ejemplo. Aquí puedes redactar explicaciones teóricas, incluir fórmulas matemáticas con MathJax como \( E = m \cdot c^2 \) o listas detalladas.</p>

<div class="callout nota">
  <span class="cap">Nota Importante</span>
  <p>Puedes utilizar llamadas de atención (callouts) para destacar aspectos normativos, advertencias de seguridad o consejos prácticos.</p>
</div>

<p>Para incluir imágenes, guárdalas en la subcarpeta <code>media/</code> (o <code>media/img/</code>) y referéncialas con la ruta <code>../content/img/nombre_imagen.ext</code>.</p>
""", prefix="../") + box("2. Procedimiento y Casos Prácticos", "case", r"""
<p>Descripción de un caso práctico o protocolo de trabajo paso a paso:</p>
<ol>
  <li><strong>Paso 1:</strong> Análisis preliminar y verificación documental.</li>
  <li><strong>Paso 2:</strong> Inspección física o técnica de las instalaciones/equipos.</li>
  <li><strong>Paso 3:</strong> Registro de resultados y emisión del informe preceptivo.</li>
</ol>
""", prefix="../") + nav_block("unidad-1-conceptos")

# --- Cuestionario de Evaluación Final ---
spec_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(spec_dir, "quiz_engine.html"), encoding="utf-8") as _f:
    _QUIZ_ENGINE = _f.read()

_PREGUNTAS_JS = r"""
// Configuración del cuestionario:
// NUM_PREGUNTAS: número de preguntas mostradas de 1 en 1 por intento (ej. 20 de un banco de 50).
var NUM_PREGUNTAS = 20;

// RANDOMIZE_OPTIONS: activa el barajado aleatorio de opciones con guardián anti-patrones.
// Garantiza que la opción correcta no sea predecible (evita rachas A, A, A o ciclos A, B, C, D).
var RANDOMIZE_OPTIONS = true;

// PASS: porcentaje mínimo para superar la evaluación (registrado en LMS mediante SCORM 1.2).
var PASS = 50;

// BANCO DE PREGUNTAS (ej. 50 preguntas):
var PREGUNTAS = [
  {
    q: "¿Cuál es el objetivo principal de este procedimiento?",
    opts: [
      "Reducir costes operativos omitiendo las especificaciones de seguridad",
      "Garantizar la conformidad técnica y normativa correspondiente",
      "Acelerar los tiempos de entrega sin realizar verificaciones previas",
      "Transferir la responsabilidad a terceros sin soporte documental"
    ],
    correct: 1, // Opción B
    fb: "Correcto. El objetivo es garantizar el estricto cumplimiento de la normativa técnica aplicable."
  },
  {
    q: "¿Qué documento o registro es preceptivo conservar antes de iniciar la actividad?",
    opts: [
      "La memoria descriptiva o declaración responsable suscrita",
      "Cualquier borrador interno provisional no firmado",
      "Un justificante verbal sin respaldo documental",
      "Ninguno de los anteriores"
    ],
    correct: 0, // Opción A
    fb: "Efectivamente, se requiere la documentación técnica o declaración responsable preceptiva."
  },
  {
    q: "Durante la inspección técnica, ¿qué actuación es prioritaria ante la detección de una anomalía crítica?",
    opts: [
      "Continuar con la operación rutinaria y registrar la incidencia al terminar la jornada",
      "Ignorar la anomalía si la maquinaria sigue en funcionamiento aparente",
      "Interrumpir de inmediato la operación y activar el protocolo de seguridad preceptivo",
      "Reiniciar los equipos sucesivamente hasta que se apague el indicador de aviso"
    ],
    correct: 2, // Opción C
    fb: "Exacto. Ante una anomalía crítica debe detenerse la actividad y seguirse el protocolo de seguridad."
  },
  {
    q: "¿Cuál es el criterio normativo general para el archivo y custodia de los registros de control?",
    opts: [
      "Destruir los registros una vez concluido el turno de trabajo",
      "Conservarlos únicamente en formato digital no verificable",
      "Mantenerlos en archivo por un plazo no superior a 15 días",
      "Custodiarlos durante el plazo legalmente establecido según la reglamentación sectorial"
    ],
    correct: 3, // Opción D
    fb: "Correcto. Los registros deben conservarse durante el periodo estipulado en la reglamentación sectorial."
  }
];
var PASS = 50; // Porcentaje mínimo para superar la evaluación
"""

BODIES["cuestionario"] = box("Cuestionario de Evaluación", "activity", r"""
<div class="quiz-intro">
  <p>Responde a las siguientes preguntas para comprobar tu nivel de asimilación de los contenidos. Al terminar, pulsa en <strong>Corregir</strong> para obtener tu puntuación y registrar tu progreso en el aula virtual.</p>
</div>
""", prefix="../") + _QUIZ_ENGINE.replace("/*__PREGUNTAS__*/", _PREGUNTAS_JS) + nav_block("cuestionario")

# ---------------------------------------------------------------------------
# 3. DESTINO GOOGLE DRIVE / NUBE (SINCRONIZACIÓN Y ENTREGA)
# ---------------------------------------------------------------------------
# URL o ID de la carpeta de Google Drive donde se depositará el paquete SCORM final:
# Ejemplos admitidos:
#   - "https://drive.google.com/drive/folders/1ZDaXiUeZ61kx-gTUsmo-gavCCB2T_sqR"
#   - "https://drive.google.com/drive/u/0/folders/1ZDaXiUeZ61kx-gTUsmo-gavCCB2T_sqR"
#   - "1ZDaXiUeZ61kx-gTUsmo-gavCCB2T_sqR"
GDRIVE_FOLDER_URL = ""
GDRIVE_FOLDER_ID = ""   # Opcional (si se deja vacío, se extrae automáticamente de GDRIVE_FOLDER_URL)

# Ruta local de sincronización (opcional, para entornos con Google Drive for Desktop):
# None = detección automática de unidades virtuales montadas (G:\, H:\, etc. o /mnt/g/)
GDRIVE_LOCAL_PATH = None

# Activar exportación/sincronización automática al ejecutar build.py
GDRIVE_AUTO_EXPORT = True
