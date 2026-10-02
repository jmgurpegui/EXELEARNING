# -*- coding: utf-8 -*-
"""
Plantilla para la especificación de un curso SCORM 1.2 compatible con eXeLearning.
Estructurada según la metodología oficial de diseño instruccional para Formación Profesional (EducaMadrid).

Estructura:
  1. gen_common.COURSE: Título de la materia/módulo o unidad temática.
  2. gen_common.PAGES: Lista jerárquica de páginas (Portada, Contenidos teóricos/procedimentales, Evaluación Final).
  3. BODIES: Diccionario {slug: html_body} con el contenido de cada página.
     - Contenidos explicativos y procedimentales: iDevice Texto (gen_common.box).
     - Redacción técnica rigurosa en 2ª persona singular (aprenderás, debes comprobar, utiliza).
     - Actividades intermedias de autoevaluación: De carácter formativo (sin reporte a Moodle).
     - Finaliza cada página con gen_common.nav_block(slug).
  4. Evaluación Final SCORM obligatoria:
     - Reservada exclusivamente en la página 'evaluacion-final'.
     - iDevice Cuestionario SCORM (el único que envía cmi.core.score.raw al libro de calificaciones de Moodle).
     - Calificación oficial en escala sobre 10 (con mastery score 5.0).
     - 10 preguntas tipo test de 4 alternativas contextualizadas técnicamente con retroalimentación completa.
"""
import os
import gen_common
from gen_common import box, nav_block

# ---------------------------------------------------------------------------
# 1. TÍTULO DEL CURSO Y ESTRUCTURA DE PÁGINAS
# ---------------------------------------------------------------------------
gen_common.COURSE = "Circuitos Eléctricos Auxiliares del Vehículo"

gen_common.PAGES = [
    dict(slug="index",              pid="page-00",    title="Portada",                  nav="Portada",          icon="objectives"),
    dict(slug="unidad-1-conceptos", pid="page-01",    title="1. Conceptos Fundamentales", nav="1. Conceptos",     icon="book"),
    dict(slug="evaluacion-final",   pid="page-final", title="Evaluación Final",         nav="Evaluación Final", icon="activity"),
]

# ---------------------------------------------------------------------------
# 2. CONTENIDO DE CADA PÁGINA (BODIES)
# ---------------------------------------------------------------------------
BODIES = {}

# --- Portada ---
BODIES["index"] = r"""
<div class="curso-banner"><img src="content/img/logo.png" alt="Logotipo o Cabecera"></div>
<div class="curso-hero">
  <p class="kicker">FORMACIÓN PROFESIONAL · GRADO MEDIO / SUPERIOR</p>
  <h2>Circuitos Eléctricos Auxiliares del Vehículo</h2>
  <p>En esta unidad didáctica aprenderás a identificar, verificar y diagnosticar los componentes esenciales de los circuitos auxiliares del automóvil con criterios de seguridad y rigor técnico.</p>
  <div class="tags"><span>Electromecánica</span><span>SCORM 1.2</span><span>EducaMadrid</span></div>
</div>
""" + box("Objetivos de Aprendizaje y Competencias", "objectives", r"""
<p>Al finalizar esta unidad de trabajo serás capaz de:</p>
<ul class="ra-list">
  <li>Identificar los principios de funcionamiento de los circuitos auxiliares y la simbología normalizada en esquemas técnicos.</li>
  <li>Comprobar caídas de tensión, consumos parásitos y continuidad empleando el multímetro y osciloscopio en el taller.</li>
  <li>Aplicar protocolos de diagnosis guiada para la localización de averías por circuito abierto o cortocircuito.</li>
  <li>Superar la <strong>Evaluación Final SCORM</strong> obligatoria para el registro de tu calificación en el Aula Virtual.</li>
</ul>
""", prefix="") + nav_block("index")

# --- Unidad 1: Contenidos Teóricos y Casos de Taller ---
BODIES["unidad-1-conceptos"] = box("1. Fundamentos Técnicos y Medición", "book", r"""
<p>Cuando trabajes sobre la instalación eléctrica de un vehículo moderno, debes considerar que las caídas de tensión no admisibles representan más del 70% de las averías en consumidores auxiliares (alumbrado, elevalunas, climatización y limpiaparabrisas).</p>

<p>Para comprobar la integridad del circuito de alimentación y masa:</p>
<ul>
  <li><strong>Medición bajo carga:</strong> Realiza siempre la medición con el consumidor en funcionamiento para registrar la resistencia de contacto real según la ley de Ohm: \( V = I \cdot R \).</li>
  <li><strong>Caída de tensión máxima admisible:</strong> En líneas principales de potencia no debe exceder de \( 0{,}2\,\text{V} \); en líneas de masa de control electrónico debe ser inferior a \( 0{,}05\,\text{V} \).</li>
</ul>

<div class="callout nota">
  <span class="cap">Regla de Oro en Taller</span>
  <p>Nunca midas resistencia (ohmios) en un circuito bajo tensión. Aísla siempre la batería o el ramal correspondiente para evitar dañar los fusibles internos del multímetro o las unidades de control.</p>
</div>
""", prefix="../") + box("2. Procedimiento de Diagnosis de Consumo Parásito", "case", r"""
<p>Si el vehículo presenta descarga prematura de la batería tras estacionamientos prolongados, debes ejecutar el siguiente protocolo sistemático:</p>
<ol>
  <li><strong>Preparación del vehículo:</strong> Conecta un mantenedor de memoria, apaga todos los consumidores y bloquea las cerraduras manteniendo el capó abierto con el interruptor de contacto puenteado.</li>
  <li><strong>Periodo de latencia (Sleep Mode):</strong> Espera entre 15 y 30 minutos a que todas las centralitas electrónicas (ECU, BSI, BCM) pasen al estado de reposo absoluto.</li>
  <li><strong>Medición de corriente:</strong> Conecta una pinza amperimétrica de corriente continua (rango de mA) en el cable negativo de la batería. El consumo residual en reposo debe ser inferior a \( 40\,\text{mA} \) (\( 0{,}04\,\text{A} \)).</li>
  <li><strong>Aislamiento por fusible:</strong> Si el consumo excede el umbral, mide la caída de tensión en milivoltios a través de los terminales de cada fusible sin extraerlo para localizar el circuito activo.</li>
</ol>
""", prefix="../") + box("3. Autoevaluación Formativa Intermedia (Práctica)", "think", r"""
<div class="callout aviso">
  <span class="cap">Actividad Formativa de Práctica</span>
  <p>Esta actividad intermedia es de autoevaluación formativa y <strong>no computa calificación</strong> en el Libro de Calificaciones de Moodle. Su finalidad es consolidar conceptos antes de la prueba final.</p>
</div>
<p><em>Pregunta de reflexión técnica:</em> Si al medir la caída de tensión entre el borne positivo de la batería y la entrada del motor de arranque durante el accionamiento obtienes \( 0{,}85\,\text{V} \), ¿qué defecto evidencia?</p>
<details class="exe-details" style="margin-top:.8em;background:#fff;padding:.8em;border-radius:6px;border:1px solid #d2dbe0;">
  <summary style="cursor:pointer;font-weight:600;color:#078e8e;">▶ Ver justificación técnica</summary>
  <p style="margin-top:.6em;">Existe una resistencia anómala de contacto en el borne, borne sulfatado o cable de alimentación deteriorado. La caída máxima admisible en la línea principal de arranque no debe superar los \( 0{,}5\,\text{V} \).</p>
</details>
""", prefix="../") + nav_block("unidad-1-conceptos")

# --- Evaluación Final SCORM Obligatoria ---
spec_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(spec_dir, "quiz_engine.html"), encoding="utf-8") as _f:
    _QUIZ_ENGINE = _f.read()

_PREGUNTAS_JS = r"""
// Configuración de la Evaluación Final SCORM:
// SCORE_SCALE: Escala de calificación en Moodle (10 para FP y EducaMadrid sobre 10).
var SCORE_SCALE = 10;

// NUM_PREGUNTAS: Número de preguntas activas por intento (10 preguntas).
var NUM_PREGUNTAS = 10;

// PASS: Porcentaje mínimo de acierto para superar la actividad (50% = 5.0 / 10).
var PASS = 50;

// RANDOMIZE_OPTIONS: Barajado aleatorio con guardián anti-patrones (evita rachas o secuencias).
var RANDOMIZE_OPTIONS = true;

// BANCO DE 10 PREGUNTAS TÉCNICAS RIGUROSAS:
var PREGUNTAS = [
  {
    q: "¿Cuál es la caída de tensión máxima admisible en una línea de alimentación principal bajo carga hacia un consumidor de potencia?",
    opts: [
      "1,5 V",
      "0,2 V a 0,3 V",
      "3,0 V",
      "0,00 V (imposible de medir)"
    ],
    correct: 1, // B
    fb: "Correcto. En conductores principales de potencia, la caída de tensión en carga no debe sobrepasar 0,2 V a 0,3 V; caídas mayores indican cables infradimensionados o bornes con resistencia parásita."
  },
  {
    q: "Al diagnosticar un consumo parásito de batería en reposo, ¿qué valor máximo se considera admisible en un turismo moderno tras el periodo de latencia (sleep mode)?",
    opts: [
      "Inferior a 40-50 mA (0,04 - 0,05 A)",
      "Aproximadamente 500 mA (0,5 A)",
      "Entre 1 A y 2 A según el equipamiento",
      "Cero absoluto (0,00 mA)"
    ],
    correct: 0, // A
    fb: "Correcto. El consumo en reposo absoluto de las centralitas electrónicas debe situarse por debajo de 40-50 mA. Cualquier valor sostenido superior descargará la batería en pocos días."
  },
  {
    q: "Para verificar la continuidad y resistencia de una electroválvula actuadora con el multímetro en escala de ohmios, ¿qué condición previa es obligatoria?",
    opts: [
      "Mantener el contacto puesto y motor al ralentí",
      "Desconectar el conector eléctrico del componente para aislarlo del circuito y no medir bajo tensión",
      "Conectar las puntas del polímetro en paralelo con el circuito alimentado a 12 V",
      "Sustituir el fusible de protección por un puente directo"
    ],
    correct: 1, // B
    fb: "Correcto. Nunca debe medirse resistencia en presencia de tensión externa, ya que distorsiona la lectura y puede dañar el multímetro o la etapa de potencia de la centralita."
  },
  {
    q: "Si en un circuito de alumbrado mides 12,6 V en bornes de batería pero solo llegan 9,8 V a la lámpara halógena encendida, ¿qué avería presenta el sistema?",
    opts: [
      "Un cortocircuito directo a masa en el filamento",
      "Una resistencia parásita excesiva en la línea de alimentación o en el relé de mando",
      "La batería tiene un exceso de carga química",
      "El alternador está averiado por diodo cortocircuitado"
    ],
    correct: 1, // B
    fb: "Correcto. La diferencia de 2,8 V representa una caída de tensión excesiva en serie provocada por terminales sulfatados, contactos de relé carbonizados o falso contacto."
  },
  {
    q: "¿Por qué razón técnica se utiliza un osciloscopio en lugar de un multímetro digital para comprobar una señal de mando modulada por ancho de pulsos (PWM)?",
    opts: [
      "Porque el multímetro digital no soporta voltajes superiores a 5 V",
      "Porque el multímetro solo muestra el valor medio eficaz (RMS) y no permite analizar la frecuencia, amplitud real ni deformaciones de onda",
      "Porque el osciloscopio consume menos amperaje que el polímetro",
      "Porque las señales PWM solo pueden medirse con corriente alterna trifásica"
    ],
    correct: 1, // B
    fb: "Correcto. El multímetro promedia la señal y puede ocultar transitorios, picos inductivos, pérdidas de masa o distorsiones que solo el osciloscopio en el dominio del tiempo revela con precisión."
  },
  {
    q: "En un esquema eléctrico de automoción normalizado según norma DIN 72552, ¿qué designación corresponde al borne de alimentación permanente directo de batería?",
    opts: [
      "Borne 15",
      "Borne 31",
      "Borne 30",
      "Borne 50"
    ],
    correct: 2, // C
    fb: "Correcto. El borne 30 indica positivo directo de batería; el 15 es positivo tras contacto de llave; el 31 es masa y el 50 es señal de accionamiento de motor de arranque."
  },
  {
    q: "¿Qué función cumple el diodo supresor de picos conectado en paralelo inverso con la bobina de un relé electromagnético automotriz?",
    opts: [
      "Aumentar la velocidad de cierre de los contactos de potencia",
      "Cortocircuitar la tensión inducida inversa (fuerza contraelectromotriz) al desconectar la bobina para proteger la centralita",
      "Permitir el paso de corriente alterna hacia el consumidor",
      "Disminuir la resistencia óhmica del bobinado"
    ],
    correct: 1, // B
    fb: "Correcto. La autoinducción de la bobina al abrir el circuito genera picos de varios cientos de voltios (L·di/dt) que el diodo en polarización inversa deriva de forma segura."
  },
  {
    q: "Al comprobar con osciloscopio el bus de datos CAN High en estado recesivo y dominante en una red de alta velocidad (ISO 11898-2), ¿qué niveles de tensión debes registrar aproximadamente?",
    opts: [
      "0 V en recesivo y 12 V en dominante",
      "2,5 V en recesivo y sube a 3,5 V en dominante",
      "5,0 V constante sin oscilación",
      "1,5 V en recesivo y desciende a 0,5 V en dominante"
    ],
    correct: 1, // B
    fb: "Correcto. En CAN High la tensión en recesivo es de 2,5 V y en dominante asciende a 3,5 V (mientras que CAN Low baja de 2,5 V a 1,5 V, logrando 2 V diferenciales)."
  },
  {
    q: "¿Qué efecto produce una mala conexión de masa (borne 31 oxidado) en un piloto trasero multifunción cuando se activan los intermitentes y el freno simultáneamente?",
    opts: [
      "Se funden de inmediato todos los fusibles del vano motor",
      "Retorno de corriente parásita a través de otros filamentos provocando parpadeo atenuado cruzado ('árbol de navidad')",
      "Aumenta la luminosidad de todas las bombillas por sobretensión",
      "El alternador detiene su generación de corriente de carga"
    ],
    correct: 1, // B
    fb: "Correcto. Al no encontrar salida franca a masa, la corriente busca el camino de menor resistencia a través de los filamentos contiguos compartidos en el portalámparas."
  },
  {
    q: "Para localizar un fusible por el que se produce un consumo anómalo sin extraerlo (técnica de caída de tensión en microvoltios), ¿qué instrumento y procedimiento se emplea?",
    opts: [
      "Una lámpara de pruebas convencional conectada a la carrocería",
      "Un voltímetro en escala de mV DC apoyando las puntas en los dos puntos de prueba metálicos expuestos sobre la cabeza del fusible",
      "Un termómetro de infrarrojos exclusivamente",
      "Un puente con cable de prueba directo a masa"
    ],
    correct: 1, // B
    fb: "Correcto. Apoyando las puntas en las dos muescas metálicas del fusible en escala de mV se mide la minúscula caída producida por la corriente circulando por la resistencia del fusible."
  }
];
"""

BODIES["evaluacion-final"] = box("Evaluación Final SCORM", "activity", r"""
<div class="quiz-intro">
  <p>Esta es la prueba oficial de <strong>Evaluación Final SCORM</strong> de la unidad formativa. Consta de <strong>10 preguntas tipo test</strong> de selección única con 4 alternativas técnicas.</p>
  <p>Para superar la prueba y registrar tu calificación aprobatoria en el Libro de Calificaciones de EducaMadrid / Moodle debes obtener una nota mínima de <strong>5,0 sobre 10 (50%)</strong>.</p>
  <p>Al terminar, pulsa en <strong>Finalizar y Corregir</strong> y a continuación en <strong>Confirmar y Guardar Calificación Oficial</strong> para registrar tu nota oficial en la plataforma.</p>
</div>
""", prefix="../") + _QUIZ_ENGINE.replace("/*__PREGUNTAS__*/", _PREGUNTAS_JS) + nav_block("evaluacion-final")

# ---------------------------------------------------------------------------
# 3. DESTINO GOOGLE DRIVE / NUBE (SINCRONIZACIÓN Y ENTREGA)
# ---------------------------------------------------------------------------
GDRIVE_FOLDER_URL = ""
GDRIVE_FOLDER_ID = ""   # Opcional (si se deja vacío, se extrae automáticamente de GDRIVE_FOLDER_URL)
GDRIVE_LOCAL_PATH = None
GDRIVE_AUTO_EXPORT = True
