# -*- coding: utf-8 -*-
"""
course_spec.py — Especificación técnica y pedagógica:
Curso Profesional: "Reprogramación y Reparación de Centralitas ECU"
Formación Profesional de Automoción (CFGS Automoción / CFGM Electromecánica de Vehículos)
Compatible al 100% con eXeLearning y validado para EducaMadrid (Moodle) y SCORM 1.2.
"""
import os
import json
import gen_common
from gen_common import box, nav_block

# ---------------------------------------------------------------------------
# 1. METADATOS INSTITUCIONALES Y LISTA DE PÁGINAS
# ---------------------------------------------------------------------------
gen_common.COURSE = "Reprogramación y Reparación de Centralitas ECU"
gen_common.AUTHOR = "Departamento de Automoción — Formación Profesional"
gen_common.DESCRIPTION = "Curso técnico profesional sobre arquitectura de hardware de la ECU, métodos de lectura y flasheo (OBD-II, Bench Mode, Bootloader, BDM/JTAG), modificación de mapas en memoria Flash, corrección de Checksum, diagnóstico y sustitución de componentes SMD en placa, estándar Pass-Thru (SAE J2534) y casos prácticos de taller."
gen_common.FOOTER_TEXT = "Material Didáctico Profesional · FP Automoción · CFGS Automoción / CFGM Electromecánica de Vehículos"

gen_common.PAGES = [
    dict(slug="index",                                pid="page-00", title="Portada y Guía Didáctica",                            nav="Portada",                 icon="objectives"),
    dict(slug="01-arquitectura-hardware-ecu",         pid="page-01", title="1. Arquitectura Interna del Hardware de la ECU",      nav="1. Hardware de la ECU",   icon="technology"),
    dict(slug="02-metodos-lectura-escritura",         pid="page-02", title="2. Protocolos y Métodos de Lectura y Flasheo",        nav="2. Métodos de Flasheo",   icon="calculate"),
    dict(slug="03-modificacion-mapas-checksum",       pid="page-03", title="3. Reprogramación de Mapas y Checksum",              nav="3. Mapas y Checksum",     icon="roadmap"),
    dict(slug="04-diagnostico-reparacion-hardware",   pid="page-04", title="4. Diagnóstico Físico y Reparación en Banco",        nav="4. Reparación en Banco",  icon="experiment"),
    dict(slug="05-normativa-pass-thru-j2534",         pid="page-05", title="5. Estándar Pass-Thru (SAE J2534) y Portales OEM",    nav="5. Pass-Thru J2534",      icon="competencies"),
    dict(slug="06-casos-practicos-taller",            pid="page-06", title="6. Casos Prácticos de Taller Paso a Paso",            nav="6. Casos Prácticos",      icon="case"),
    dict(slug="07-mediateca-tecnica",                 pid="page-07", title="7. Mediateca Técnica: Recursos Audiovisuales",        nav="7. Mediateca Audiovisual", icon="video"),
    dict(slug="cuestionario",                         pid="page-08", title="Evaluación Final (Test Aleatorio 20/50)",             nav="Evaluación Final",        icon="activity"),
]

def figura(img_file, caption, fig_num=None, prefix="../"):
    num_str = f'<span class="fig-num">Figura {fig_num}: </span>' if fig_num else ""
    return f"""<div class="figura-taller" style="text-align:center;margin:1.4em 0;">
  <img src="{prefix}content/img/{img_file}" alt="{caption}" style="max-width:100%;height:auto;border-radius:8px;border:1px solid #cbd5e1;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <div class="fig-cap" style="font-size:0.88rem;color:#64748b;margin-top:0.5em;font-weight:500;">{num_str}{caption}</div>
</div>"""

def video_embed(video_id, title, desc, badge="Vídeo Técnico", badge_class=""):
    b_cls = f" {badge_class}" if badge_class else ""
    return f"""<div class="video-card" style="border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;margin:1.3em 0;background:#ffffff;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
  <div class="video-card-header" style="background:#0f172a;color:#ffffff;padding:0.6em 1em;display:flex;justify-content:space-between;align-items:center;">
    <h4 style="margin:0;color:#ffffff;font-size:0.98rem;">{title}</h4>
    <span class="video-badge{b_cls}" style="background:#3b82f6;color:#ffffff;padding:0.2em 0.6em;border-radius:4px;font-size:0.75rem;font-weight:600;">{badge}</span>
  </div>
  <div class="video-container" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;background:#000;">
    <iframe src="https://www.youtube-nocookie.com/embed/{video_id}" title="{title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"></iframe>
  </div>
  <div style="padding:0.9em 1em;">
    <p class="video-desc" style="margin:0 0 0.6em;font-size:0.92rem;color:#334155;">{desc}</p>
    <a class="video-link-ext" href="https://www.youtube.com/watch?v={video_id}" target="_blank" rel="noopener" style="font-size:0.85rem;font-weight:600;color:#0284c7;text-decoration:none;">🔗 Abrir vídeo en YouTube</a>
  </div>
</div>"""

BODIES = {}

# ===============================================================
# PORTADA (index)
# ===============================================================
BODIES["index"] = r"""
<div class="curso-banner">
  <img src="content/img/logo.png" alt="Logo FP Automoción" style="max-height:85px;width:auto;">
</div>

<div class="curso-hero">
  <p class="kicker">MÓDULO: SISTEMAS ELÉCTRICOS, DE SEGURIDAD Y CONFORTABILIDAD · FP AUTOMOCIÓN</p>
  <h2>Reprogramación y Reparación de Centralitas ECU</h2>
  <p>Curso técnico integral para electromecánicos de automoción: diagnóstico de hardware, métodos de lectura y flasheo (OBD-II, Bench Mode con pines GPT, Bootloader y BDM/JTAG), modificación y calibración de mapas motor en memoria Flash, corrección de Checksum, reparación física de componentes SMD en banco, y protocolo oficial Pass-Thru (SAE J2534) con estabilizadores de tensión.</p>
  <div class="tags">
    <span>Hardware ECU &amp; PMIC</span>
    <span>Microcontroladores TriCore &amp; MPC</span>
    <span>OBD-II · Bench Mode · Boot · BDM</span>
    <span>Calibración Flash &amp; WinOLS</span>
    <span>Checksum &amp; Checksum Recalc</span>
    <span>Soldadura SMD &amp; Rework</span>
    <span>Pass-Thru SAE J2534</span>
    <span>SCORM 1.2</span>
  </div>
</div>
""" + box("Ficha Técnica y Competencias Profesionales", "objectives", r"""
<p>Bienvenido al curso técnico especializado en <strong>Reprogramación y Reparación de Unidades de Control Electrónico (UCE / ECU)</strong>, diseñado específicamente para técnicos electromecánicos de automoción de Grado Medio (CFGM) y Grado Superior (CFGS).</p>

<p>En el parque automovilístico actual, la gestión del motor de combustión, los sistemas de hibridación, el frenado electrónico y el confort dependen por completo de redes de microprocesadores. Este curso capacita al profesional para abordar tanto el <strong>software</strong> (telecargas, calibraciones, clonaciones de memoria) como el <strong>hardware</strong> (detección de componentes quemados, sustitución de drivers de potencia y reguladores de tensión en laboratorio).</p>

<div class="callout nota">
  <span class="cap">Enfoque de taller profesional</span>
  <p>Cada tema está orientado a situaciones reales de diagnosis: medición de señales con osciloscopio, localización de componentes en placas multicapa, conexión en banco sin abrir carcasas (Bench Mode) y precauciones críticas para evitar el bloqueo irreversible (<em>brick</em>) de centralitas.</p>
</div>

<h4>Resultados de Aprendizaje Oficiales (Currículo FP Automoción)</h4>
<ul class="ra-list">
  <li><strong>RA 1: Caracteriza la arquitectura interna del hardware de la ECU</strong>, identificando microcontroladores, memorias Flash/EEPROM, transceptores de bus y etapas de potencia.</li>
  <li><strong>RA 2: Selecciona y ejecuta el método de lectura y escritura idóneo</strong> (OBD, Bench, Boot o BDM) según la marca y nivel de protección antituning del procesador.</li>
  <li><strong>RA 3: Interpreta y modifica mapas de inyección, sobrealimentación y limitadores de par</strong>, recalculando matemáticamente el Checksum de integridad del archivo.</li>
  <li><strong>RA 4: Diagnostica averías físicas de placa</strong> mediante multímetro, cámara térmica y osciloscopio, aplicando técnicas seguras de desoldadura y soldadura SMD.</li>
  <li><strong>RA 5: Domina el estándar Pass-Thru (SAE J2534)</strong> para telecargas oficiales con herramientas de fabricante (ODIS, ISTA, Xentry), garantizando la estabilidad de tensión.</li>
</ul>
""", prefix="") + box("Decálogo de Seguridad Laboral y Normas ESD en el Laboratorio", "alert", r"""
<p>El trabajo directo sobre circuitos integrados y memorias exige protocolos estrictos de protección física y electrostática:</p>

<table class="tabla-curso">
  <thead>
    <tr>
      <th style="width:25%;">Factor de Riesgo</th>
      <th style="width:40%;">Consecuencia Técnica</th>
      <th style="width:35%;">Medida Preventiva Obligatoria</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Descarga Electrostática (ESD)</strong></td>
      <td>Destrucción por perforación del dieléctrico en puertas MOSFET y microcontroladores (latente o inmediata).</td>
      <td>Uso de <strong>pulsera antiestática</strong> conectada a tierra, tapete disipativo ESD y bata de algodón 100%.</td>
    </tr>
    <tr>
      <td><strong>Caída de Tensión en Flasheo</strong></td>
      <td>Microcontrolador bloqueado (<em>bricked</em>) al interrumpirse el borrado del sector de arranque (Bootloader).</td>
      <td>Uso obligado de <strong>estabilizador de taller de 70 A a 100 A</strong> (13,8 V - 14,4 V sin oscilaciones). Prohibido cargadores estándar.</td>
    </tr>
    <tr>
      <td><strong>Inversión de Polaridad en Banco</strong></td>
      <td>Destrucción instantánea del diodo de protección, condensadores electrolíticos y regulador de 5V.</td>
      <td>Verificación doble de esquemas de pinout (VCC, KL15 y GND) antes de activar la fuente de laboratorio.</td>
    </tr>
    <tr>
      <td><strong>Sobrecalentamiento de Pistas</strong></td>
      <td>Desprendimiento de pistas de cobre (pads) en la placa PCB y rotura de vías internas en multicapa.</td>
      <td>Soldadura controlada (máximo 350 °C - 380 °C en aire caliente), empleo de flux de alta calidad y precalentador de placa.</td>
    </tr>
    <tr>
      <td><strong>Inhalación de Humos</strong></td>
      <td>Toxicidad por resinas de colofonia, decapantes y aleaciones de soldadura sin plomo (SAC305).</td>
      <td>Uso de <strong>extractor de humos de banco</strong> con filtro de carbono activo y partículas HEPA.</td>
    </tr>
  </tbody>
</table>
""", prefix="") + nav_block("index")


# ===============================================================
# TEMA 1: ARQUITECTURA INTERNA DEL HARDWARE DE LA ECU
# ===============================================================
BODIES["01-arquitectura-hardware-ecu"] = box("1. Anatomía y Componentes de la Placa PCB", "technology", r"""
<p>Una Unidad de Control Electrónico (UCE / ECU) del motor es un ordenador de grado automotriz diseñado para operar en condiciones extremas de vibración (hasta 30G), humedad y temperatura (-40 °C a +125 °C en vano motor). Su hardware interno se monta sobre una <strong>placa de circuito impreso multicapa (PCB de 4 a 8 capas)</strong> donde las pistas intermedias actúan como planos de masa (<em>ground planes</em>) y apantallamiento contra interferencias electromagnéticas (EMI).</p>

""" + figura("diagrama_arquitectura_ecu.svg", "Arquitectura interna funcional de una centralita electrónica de motor", 1, prefix="../") + r"""

<div class="mag-grid">
  <div class="mag-card">
    <h4>Microcontrolador (MCU)</h4>
    <div class="sym">CPU</div>
    <div class="ud">Núcleo de 32 bits (TriCore / MPC)</div>
    <p>Ejecuta el sistema operativo en tiempo real (RTOS), gestiona interrupciones de cigüeñal e inyección, y procesa los algoritmos de control.</p>
  </div>
  <div class="mag-card">
    <h4>Memoria Flash</h4>
    <div class="sym">ROM</div>
    <div class="ud">512 KB a 8 MB (Interna / Externa)</div>
    <p>Almacena el código de firmware (programa principal) y todas las tablas y mapas de calibración del motor. Es la zona modificada en reprogramación.</p>
  </div>
  <div class="mag-card">
    <h4>Memoria EEPROM</h4>
    <div class="sym">SPI</div>
    <div class="ud">2 KB a 64 KB (Serie 95xxx / 24Cxx)</div>
    <p>Memoria no volátil reescribible que custodia los datos de inmovilizador (IMMO PIN), número de bastidor (VIN), odómetro y codificación de inyectores.</p>
  </div>
  <div class="mag-card">
    <h4>Regulador / PMIC</h4>
    <div class="sym">5.0V</div>
    <div class="ud">LDO / Step-Down conmutado</div>
    <p>Convierte los 12V de batería en tensiones limpias y ultraestables: 5,00 V para sensores externos, 3,3 V para lógica y 1,2 V - 1,5 V para el núcleo del MCU.</p>
  </div>
</div>

<h4>Familias de Microcontroladores en Automoción</h4>
<table class="tabla-curso">
  <thead>
    <tr>
      <th>Familia MCU</th>
      <th>Fabricante</th>
      <th>Centralitas Típicas</th>
      <th>Características de Programación</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>TriCore (TC17xx, AURIX TC2xx/3xx)</strong></td>
      <td>Infineon</td>
      <td>Bosch EDC17, MED17, MD1, MG1, Continental SID</td>
      <td>Arquitectura RISC 32 bits. Incorpora módulo de seguridad por hardware (HSM) y requiere lectura Bench con pines GPT o Bootloader.</td>
    </tr>
    <tr>
      <td><strong>PowerPC (MPC555, MPC5566, MPC56xx)</strong></td>
      <td>NXP / Freescale</td>
      <td>Bosch EDC16, Delphi DCM3.x, Magneti Marelli MJD</td>
      <td>Puerto BDM (Background Debug Mode) dedicado con pads circulares o conector para agujas en bastidor.</td>
    </tr>
    <tr>
      <td><strong>SuperH (SH7055, SH7058, RH850)</strong></td>
      <td>Renesas</td>
      <td>Denso (Toyota, Nissan, Mazda), Hitachi, Transtron</td>
      <td>Utilizado masivamente en marcas asiáticas. Conexión JTAG / AUD o lectura por línea serie K-Line/CAN.</td>
    </tr>
    <tr>
      <td><strong>C167 / ST10</strong></td>
      <td>Infineon / ST</td>
      <td>Bosch EDC15, ME7.x, Siemens MS42/MS43</td>
      <td>Microcontrolador de 16 bits de generaciones anteriores. Memoria Flash externa encapsulada en chip PSOP44 (29F400/29F800).</td>
    </tr>
  </tbody>
</table>
""", prefix="../") + box("2. Etapas de Potencia, Drivers Inteligentes y Protección", "calculate", r"""
<p>El microcontrolador trabaja con niveles lógicos de baja tensión (3,3 V o 5 V) y corrientes de apenas unos miliamperios. Para gobernar elementos que demandan decenas de amperios (inyectores piezoeléctricos o inductivos, bobinas de encendido, mariposa motorizada, calentadores diésel), la centralita incorpora <strong>etapas de potencia especializadas</strong>:</p>

<div class="callout aviso">
  <span class="cap">Diodos Flyback (Libre Circulación) y Picos Inductivos</span>
  <p>Al cortar súbitamente la corriente en una carga fuertemente inductiva (como un inyector o una electroválvula PWM), la ley de Faraday-Lenz genera una fuerza contraelectromotriz (f.e.m.) inversa que puede alcanzar picos de entre <strong>80 V y más de 400 V</strong>:
  \[ V_{ind} = -L \cdot \frac{di}{dt} \]
  Si el diodo supresor de libre circulación interno o la red de protección zener/TVS se cortocircuita o se abre, el transistor MOSFET asociado sufrirá una perforación por sobretensión en cuestión de milisegundos.</p>
</div>

<ol>
  <li><strong>Drivers Inteligentes (Smart Power ICs):</strong> Circuitos integrados que integran la lógica de disparo, sensores de corriente internos (<em>current shunt sensing</em>) y protección térmica contra cortocircuito a masa o a positivo. Comunican al microcontrolador cualquier fallo de línea mediante bus serie SPI.</li>
  <li><strong>Transistores MOSFET (Canal N):</strong> Utilizados preferentemente en conmutación por masa de actuadores PWM (válvulas de turbo N75, bombas eléctricas, válvulas EGR).</li>
  <li><strong>Transistores IGBT (Insulated Gate Bipolar Transistor):</strong> Empleados en las etapas de encendido de motores de gasolina para soportar la elevada tensión inducida en el primario de las bobinas (hasta 400 V de corte).</li>
  <li><strong>Convertidor DC-DC Elevador (Boost Converter):</strong> En motores Diésel Common Rail modernos e inyección directa de gasolina (GDI), la centralita incorpora bobinas toroidales y condensadores electrolíticos de alta capacidad para elevar los 12 V de la batería a tensiones de entre <strong>70 V y 150 V</strong>, necesarias para abrir con rapidez los inyectores piezoeléctricos.</li>
</ol>
""", prefix="../") + nav_block("01-arquitectura-hardware-ecu")


# ===============================================================
# TEMA 2: PROTOCOLOS Y MÉTODOS DE LECTURA Y ESCRITURA (FLASHEO)
# ===============================================================
BODIES["02-metodos-lectura-escritura"] = box("1. Comparativa de los 4 Métodos de Acceso a la Memoria", "calculate", r"""
<p>El acceso a la memoria de una centralita para realizar operaciones de clonación, lectura de seguridad o reprogramación de mapas se efectúa mediante 4 procedimientos técnicos diferenciados, con niveles crecientes de profundidad y complejidad mecánica:</p>

""" + figura("diagrama_metodos_lectura.svg", "Matriz comparativa de los métodos de conexión para lectura y escritura de ECUs", 2, prefix="../") + r"""

<table class="tabla-curso">
  <thead>
    <tr>
      <th>Método</th>
      <th>Puntos de Conexión</th>
      <th>Apertura de ECU</th>
      <th>Zonas Leídas</th>
      <th>Nivel de Seguridad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. OBD-II (DLC)</strong></td>
      <td>Toma de 16 pines del habitáculo (CAN pines 6/14; K-Line pin 7).</td>
      <td><strong>NO</strong></td>
      <td>Solo zona de calibración/mapas (a menudo lectura virtual VR en servidor).</td>
      <td>Medio. Requiere estabilizador estricto. Riesgo de corte por pasarela Gateway o desconexión.</td>
    </tr>
    <tr>
      <td><strong>2. Bench Mode</strong></td>
      <td>Pines exteriores del conector de la ECU (VCC, GND, CAN, K-Line, GPT1/GPT2).</td>
      <td><strong>NO</strong></td>
      <td>Flash interna, Flash externa y EEPROM completa (Micro TriCore / MPC).</td>
      <td><strong>Máximo</strong>. Muy seguro; permite copia 100% y clonación completa sin desprecintar la placa.</td>
    </tr>
    <tr>
      <td><strong>3. Boot Mode</strong></td>
      <td>Conector exterior + Resistencia de arranque (1 kΩ) a masa en pad de la PCB.</td>
      <td><strong>SÍ</strong></td>
      <td>Acceso total a memoria Flash y EEPROM forzando el modo de arranque de fábrica.</td>
      <td>Alto en electrónica; medio en mecánica (precaución al despegar silicona de la carcasa).</td>
    </tr>
    <tr>
      <td><strong>4. BDM / JTAG</strong></td>
      <td>Bastidor de agujas retráctiles (pogo pins) sobre pads de depuración de la PCB.</td>
      <td><strong>SÍ</strong></td>
      <td>Lectura física 1:1 directa al bus del microcontrolador (MPC5xx, Nexus, JTAG).</td>
      <td>Máximo para rescate. Método definitivo para desbrickear centralitas corruptas.</td>
    </tr>
  </tbody>
</table>

<div class="callout truco">
  <span class="cap">¿Qué son los Pines GPT en Bench Mode?</span>
  <p>En centralitas modernas con microcontroladores Infineon TriCore (Bosch EDC17 y MED17), los fabricantes introdujeron protecciones antituning avanzadas (TPROT). Para leerlas en banco sin abrir la carcasa, herramientas como Autotuner, K-Tag o Flex utilizan las líneas <strong>GPT (General Purpose Timer)</strong>. El programador inyecta una secuencia periódica de pulsos de frecuencia sincronizada por los pines GPT1 y GPT2 que desbloquea el microcontrolador mediante una contraseña de hardware (SOPT Password) almacenada en la EEPROM.</p>
</div>
""", prefix="../") + box("2. Equipamiento Profesional de Taller: Master vs Slave", "technology", r"""
<p>Al seleccionar equipamiento profesional de flasheo para el taller, el técnico debe comprender el modelo de licenciamiento de los principales fabricantes de herramientas:</p>

<div class="mag-grid">
  <div class="mag-card">
    <h4>Herramienta MASTER</h4>
    <div class="sym">.BIN</div>
    <div class="ud">Archivos abiertos sin encriptar</div>
    <p>Lee y escribe archivos en formato binario puro (<code>.bin</code> o <code>.ori</code>). El técnico puede abrir el archivo directamente en WinOLS, modificarlo o enviarlo a cualquier calibrador independiente.</p>
  </div>
  <div class="mag-card">
    <h4>Herramienta SLAVE</h4>
    <div class="sym">.ENC</div>
    <div class="ud">Archivos encriptados vinculados a un Master</div>
    <p>Coste de hardware más económico. Los archivos leídos quedan encriptados y solo pueden ser descifrados y modificados por la herramienta Master a la que está asociada la cuenta.</p>
  </div>
</div>

<h4>Herramientas de Referencia en el Sector</h4>
<ul>
  <li><strong>Autotuner:</strong> Herramienta rápida de referencia para Bench y OBD-II, sin cuotas anuales de suscripción y con protocolos automáticos de corrección de Checksum.</li>
  <li><strong>Flex (Magicmotorsport):</strong> Plataforma modular avanzada con módulos de OBD, Bench, Boot y BDM para motor y cajas de cambio automáticas (TCU).</li>
  <li><strong>Kess3 (Alientech):</strong> Sucesor unificado de Kess v2 y K-Tag, que integra flasheo por toma de diagnosis y operaciones directas en banco con bastidor.</li>
  <li><strong>Dimsport New Genius &amp; Trasdata:</strong> Equipos de gran robustez industrial con consolas táctiles autónomas para evitar fallos de portátiles.</li>
</ul>

<div class="callout peligro">
  <span class="cap">Regla de Oro en el Taller: El "Full Backup" Previo Obligatorio</span>
  <p><strong>NUNCA</strong> inicies una reprogramación o modificación de mapas sin haber realizado previamente una copia de seguridad íntegra de la memoria (<em>Full Backup</em> de Flash y EEPROM). Si la comunicación se interrumpe durante el borrado del bloque OBD, disponer de la lectura en banco o BDM permitirá restaurar la centralita a su estado operativo original en menos de 10 minutos.</p>
</div>
""", prefix="../") + nav_block("02-metodos-lectura-escritura")


# ===============================================================
# TEMA 3: REPROGRAMACIÓN DE MAPAS Y CHECKSUM
# ===============================================================
BODIES["03-modificacion-mapas-checksum"] = box("1. Estructura de los Mapas en la Memoria Flash", "roadmap", r"""
<p>La memoria Flash contiene el código ensamblador ejecutable del sistema operativo y miles de arrays de datos numéricos denominados <strong>mapas o matrices de calibración</strong>. Estos mapas pueden ser bidimensionales (curvas 2D) o tridimensionales (superficies 3D):</p>

""" + figura("diagrama_mapa_3d_inyeccion.svg", "Superficie 3D de un mapa motor y relación de ejes en WinOLS", 3, prefix="../") + r"""

<h4>Los 6 Mapas Fundamentales en Motores Diésel Common Rail</h4>
<ol>
  <li><strong>Mapa de Pedal (Driver Wish):</strong> Traduce el porcentaje de pisada del pedal del acelerador (%) y el régimen de giro (RPM) en una demanda de par motor (\(\text{Nm}\)) o caudal de inyección (\(\text{mg/ciclo}\)).</li>
  <li><strong>Limitador de Par (Torque Limiter):</strong> Curva de protección mecánica que restringe el par máximo admisible según el régimen (RPM) y la presión atmosférica, protegiendo el embrague, la caja de cambios y la biela.</li>
  <li><strong>Mapa de Humos / Lambda (Smoke Limiter):</strong> Define la relación estequiométrica mínima admisible de aire/combustible en función de la masa de aire medida por el caudalímetro (MAF) o la presión de admisión (MAP). Si se supera este límite, se produce emisión visible de partículas (humo negro).</li>
  <li><strong>Mapa de Presión de Raíl:</strong> Determina la presión del acumulador Common Rail (de 250 bar a ralentí hasta más de 2000 bar en plena carga) según las RPM y la cantidad de combustible inyectada.</li>
  <li><strong>Mapas de Avance (SOI - Start of Injection) y Duración:</strong>
    \[ \text{Ángulo SOI (}^\circ\text{ cigüeñal)} \quad \text{y} \quad \text{Tiempo de apertura (}\mu\text{s)} \]
    Garantizan que la combustión comience en el instante óptimo respecto al punto muerto superior (PMS).</li>
  <li><strong>Mapa de Sobrealimentación (Turbo Boost Map) y N75:</strong> Presión absoluta demandada al turbocompresor (en milibares, ej. 2400 mbar) y mapa del ciclo de trabajo PWM (Duty Cycle %) de la electroválvula de control de la geometría variable (VNT).</li>
</ol>
""", prefix="../") + box("2. Software de Edición y el Algoritmo del Checksum", "calculate", r"""
<p>Para localizar y modificar estos mapas en un archivo binario de varios megabytes se utilizan suites profesionales de calibración:</p>

<ul>
  <li><strong>WinOLS (EVC Electronic):</strong> El estándar de la industria. Permite visualizar el binario en formato hexadecimal (2D, 3D y texto), buscar mapas potenciales por heurística y cargar archivos <strong>DAMOS / A2L</strong> (map packs oficiales con la definición exacta de variables, factores de escala y offsets de ingeniería).</li>
  <li><strong>ECM Titanium (Alientech):</strong> Software estructurado orientado a taller rápido que utiliza drivers predefinidos para identificar automáticamente los mapas clave sin necesidad de buscar ejes manualmente.</li>
</ul>

<div class="callout peligro">
  <span class="cap">El Checksum: Qué Es y Por Qué Bloquea la ECU</span>
  <p>El <strong>Checksum (Suma de Verificación)</strong> es un valor numérico o firma criptográfica (algoritmos de redundancia cíclica CRC32, sumas de 16/32 bits o firmas RSA) calculado sobre bloques continuos de la memoria Flash.</p>
  <p>Al arrancar el vehículo, el microcontrolador ejecuta una rutina de autochequeo en la que recalcula el Checksum de todos los bloques de memoria y lo compara con el valor de referencia grabado en la cabecera. Si un solo byte ha sido modificado sin recalcular el Checksum:
  \[ \text{Checksum Calculado} \neq \text{Checksum Almacenado} \implies \text{BLOQUEO DE ARRANQUE} \]
  El microcontrolador aborta la secuencia de inyección, enciende el testigo de avería motor y el vehículo queda completamente inmovilizado. Afortunadamente, las herramientas de flasheo modernas y WinOLS recalculan e insertan automáticamente el Checksum correcto durante el guardado y escritura del archivo.</p>
</div>

<h4>Niveles Típicos de Modificación en Taller</h4>
<table class="tabla-curso">
  <thead>
    <tr>
      <th>Nivel</th>
      <th>Objetivo Técnico</th>
      <th>Intervención Mecánica Requerida</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Stage 1</strong></td>
      <td>Optimización de par y potencia (+15% a +30%) dentro de las tolerancias térmicas y mecánicas holgadas del fabricante.</td>
      <td><strong>Vehículo 100% de serie</strong>. Mantenimiento al día (filtros, aceite de especificación y distribución).</td>
    </tr>
    <tr>
      <td><strong>Stage 2</strong></td>
      <td>Incremento superior aprovechando mejoras en el flujo de gases y refrigeración.</td>
      <td>Exige modificaciones físicas: <em>intercooler</em> de mayor volumen, <em>downpipe</em> de baja contrapresión y admisión optimizada.</td>
    </tr>
    <tr>
      <td><strong>Clonación Integral</strong></td>
      <td>Traspasar el 100% de datos (Flash + EEPROM con inmovilizador y VIN) de una ECU averiada a una unidad donante idéntica.</td>
      <td>Ninguna en motor. En banco: volcado bit a bit para que la nueva centralita arranque a la primera (Plug &amp; Play).</td>
    </tr>
    <tr>
      <td><strong>Virginización</strong></td>
      <td>Resetear el área de inmovilizador de la EEPROM a valores de fábrica ("virgen").</td>
      <td>Permite que la ECU se autoempareje con el cuadro de instrumentos o BSI en el primer ciclo de contacto de llave.</td>
    </tr>
  </tbody>
</table>
""", prefix="../") + nav_block("03-modificacion-mapas-checksum")

# ===============================================================
# TEMA 4: DIAGNÓSTICO FÍSICO Y REPARACIÓN EN BANCO
# ===============================================================
BODIES["04-diagnostico-reparacion-hardware"] = box("1. Equipamiento del Puesto de Trabajo Electrónico", "experiment", r"""
<p>La reparación física de averías internas en una centralita requiere un laboratorio de electrónica debidamente acondicionado y aislado de las partículas de grasa y polvo del taller mecánico general:</p>

<div class="mag-grid">
  <div class="mag-card">
    <h4>Estación de Soldadura SMD</h4>
    <div class="sym">350°C</div>
    <div class="ud">Puntas finas de precisión (JBC / Hakko)</div>
    <p>Control térmico digital con reposo automático. Puntas tipo aguja y tipo cuchilla para desoldar y resoldar componentes miniatura 0603 y chips SOIC.</p>
  </div>
  <div class="mag-card">
    <h4>Pistola de Aire Caliente</h4>
    <div class="sym">HOT AIR</div>
    <div class="ud">Toberas circulares regulables</div>
    <p>Calentamiento sin contacto mecánico para la extracción limpia de chips multipin (QFP, TSSOP, SOIC) y precalentador inferior de PCB.</p>
  </div>
  <div class="mag-card">
    <h4>Microscopio Estereoscópico</h4>
    <div class="sym">40X</div>
    <div class="ud">Óptica binocular + Cámara HDMI</div>
    <p>Imprescindible para inspeccionar microfisuras en soldaduras BGA, pistas de cobre cortadas, sulfato bajo pines y alineación milimétrica.</p>
  </div>
  <div class="mag-card">
    <h4>Fuente Regulada CC</h4>
    <div class="sym">0-30V</div>
    <div class="ud">Limitador de corriente regulable (0-5A)</div>
    <p>Permite alimentar la ECU en banco limitando la corriente a 200-300 mA para evitar quemar pistas si existe un cortocircuito interno.</p>
  </div>
</div>

<div class="callout nota">
  <span class="cap">Cámara Termográfica de Banco: El Localizador Instantáneo de Cortos</span>
  <p>Cuando una centralita presenta un consumo excesivo en banco (ej. &gt; 1,5 A sin activar encendido), el método más rápido y no invasivo consiste en enfocar la placa con una <strong>cámara termográfica infrarroja</strong>. El componente defectuoso (generalmente un diodo supresor TVS, un condensador tantalio en corto o el propio chip regulador de 5V) brillará intensamente en pantalla al disipar potencia en forma de calor antes de que la pista se carbonice.</p>
</div>
""", prefix="../") + box("2. Diagnóstico y Reparación de las 5 Averías Más Comunes", "case", r"""
<p>En el taller de automoción, más del 80% de los fallos de hardware en UCEs se concentran en 5 patrones de avería perfectamente diagnosticables:</p>

""" + figura("diagrama_circuito_reparacion_5v.svg", "Esquema del circuito regulador de 5V de sensores y protocolo de comprobación", 4, prefix="../") + r"""

<h4>Las 5 Averías Frecuentes y su Reparación</h4>
<table class="tabla-curso">
  <thead>
    <tr>
      <th style="width:25%;">Avería de Campo</th>
      <th style="width:35%;">Causa Raíz Típica</th>
      <th style="width:40%;">Procedimiento de Reparación en Banco</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Pérdida de 5,0 V de Sensores</strong> (DTCs múltiples: MAP, TPS, presión combustible).</td>
      <td>Cortocircuito en el mazo exterior de cables del motor (cable de 5V rozado con el bloque del motor o sensor interno en corto).</td>
      <td>Comprobar resistencia entre el pin de 5V y masa. Si es &lt; 10 Ω en banco, el integrado regulador (Bosch 30344, 40048 o TLE4267) está perforado. Desoldar con aire caliente a 350 °C, limpiar pistas con malla y soldar chip nuevo.</td>
    </tr>
    <tr>
      <td><strong>2. Fallo de Inyección en un Cilindro</strong> (DTC circuito abierto inyector).</td>
      <td>Transistor MOSFET de canal N o driver inteligente quemado por sobrecorriente o solenoide de inyector comunicado.</td>
      <td>Medir caída de tensión en modo diodo con multímetro entre Drenador (Drain) y Fuente (Source). Un valor de 0,00 V indica cortocircuito franco. Sustituir el MOSFET SMD respetando la disipación térmica del pad inferior.</td>
    </tr>
    <tr>
      <td><strong>3. ECU "Muerta" sin Comunicación</strong> (No enciende, sin consumo).</td>
      <td>Inversión de polaridad en el vehículo (pinzas de arranque invertidas) o sobretensión por alternador desregulado.</td>
      <td>Revisar el diodo Schottky / TVS de entrada en la línea +12V. Si está en cortocircuito (0 Ω), bloquea la entrada. Desoldar el diodo y verificar si la línea de 12V recupera la impedancia normal antes de sustituirlo.</td>
    </tr>
    <tr>
      <td><strong>4. Fallos Intermitentes al Calentarse el Motor</strong></td>
      <td>Microfisuras en las bolas de estaño (BGA) bajo el microprocesador o patillas de conectores por vibración continua.</td>
      <td>Aplicar flux líquido sin residuo (<em>no-clean</em>) bajo el componente y realizar un ciclo de reflow térmico controlado con aire caliente a 230 °C - 240 °C durante 45 segundos, permitiendo que las esferas de estaño se refundan.</td>
    </tr>
    <tr>
      <td><strong>5. Corrosión por Entrada de Humedad o Agua</strong></td>
      <td>Defecto en el sellado de la carcasa plástica o penetración por capilaridad a través del cableado.</td>
      <td>Inmersión de la placa en cubeta de ultrasonidos con <strong>alcohol isopropílico (IPA) de alta pureza (99,9%)</strong> durante 10 minutos a 40 °C. Cepillado suave con cerdas antiestáticas y secado en horno térmico a 60 °C.</td>
    </tr>
  </tbody>
</table>
""", prefix="../") + nav_block("04-diagnostico-reparacion-hardware")


# ===============================================================
# TEMA 5: ESTÁNDAR PASS-THRU (SAE J2534) Y PORTALES OEM
# ===============================================================
BODIES["05-normativa-pass-thru-j2534"] = box("1. Normativa Europea y el Protocolo SAE J2534", "competencies", r"""
<p>Históricamente, la reprogramación y calibración oficial de los módulos de control estaba restringida a los concesionarios oficiales de marca mediante costosos equipos de diagnosis cautivos. Con la entrada en vigor de los <strong>Reglamentos Europeos Euro 5 (CE 715/2007) y Euro 6 (CE 595/2009)</strong>, los fabricantes de automóviles quedaron obligados por ley a facilitar a los talleres independientes el acceso estandarizado a sus servidores de telecarga y diagnosis bajo el principio de libre competencia (<em>Right to Repair</em>).</p>

<p>Para materializar esta directiva, se adoptó el estándar internacional de comunicaciones <strong>SAE J2534</strong>:</p>

<div class="mag-grid">
  <div class="mag-card">
    <h4>SAE J2534-1</h4>
    <div class="sym">VCI</div>
    <div class="ud">Emisiones y Motor</div>
    <p>Define la interfaz estándar de reprogramación obligatoria para todas las centralitas vinculadas a emisiones contaminantes (UCE de motor y transmisión).</p>
  </div>
  <div class="mag-card">
    <h4>SAE J2534-2</h4>
    <div class="sym">EXT</div>
    <div class="ud">Arquitectura Completa</div>
    <p>Extensión que habilita el acceso y telecarga sobre el resto de módulos del vehículo: ABS/ESP, airbags, dirección asistida, cuadro y unidades de carrocería (BCM).</p>
  </div>
</div>

""" + figura("diagrama_instalacion_passthru.svg", "Instalación de taller y requisitos de seguridad para reprogramación Pass-Thru", 5, prefix="../") + r"""

<h4>Portales Oficiales de Fabricantes para Talleres Multimarca</h4>
<table class="tabla-curso">
  <thead>
    <tr>
      <th>Fabricante / Grupo</th>
      <th>Software Oficial</th>
      <th>Portal de Acceso Web</th>
      <th>Modalidad de Tarifas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Grupo Volkswagen (Audi, VW, SEAT, Skoda)</strong></td>
      <td><strong>ODIS Service</strong></td>
      <td>erWin (con cuenta de seguridad GeKo)</td>
      <td>Tarifas por horas (ej. 1h / 1 día / suscripción anual) + coste de telecarga de firmware.</td>
    </tr>
    <tr>
      <td><strong>BMW Group (BMW, MINI)</strong></td>
      <td><strong>ISTA / AIR</strong></td>
      <td>BMW AOS (Aftersales Online System)</td>
      <td>Acceso por tickets horarios o diarios para programación de software (I-Level).</td>
    </tr>
    <tr>
      <td><strong>Mercedes-Benz</strong></td>
      <td><strong>Xentry Diagnosis</strong></td>
      <td>Mercedes-Benz B2B Connect</td>
      <td>Créditos horarios con autenticación de dos factores (2FA) para codificación SCN online.</td>
    </tr>
    <tr>
      <td><strong>Stellantis (Peugeot, Citroën, Opel, Fiat)</strong></td>
      <td><strong>Diagbox / wiTECH</strong></td>
      <td>Service Box / Stellantis Technical Info</td>
      <td>Tokens individuales de telecarga o pases temporales de diagnosis.</td>
    </tr>
    <tr>
      <td><strong>Renault Group</strong></td>
      <td><strong>Clip / ADT</strong></td>
      <td>Renault Infotech / ASDE</td>
      <td>Fichas horarias y compra de tokens para telecarga de calculadores de inyección.</td>
    </tr>
    <tr>
      <td><strong>Ford Motor Company</strong></td>
      <td><strong>FDRS / FJDS</strong></td>
      <td>Ford Service Info Portal</td>
      <td>Licencia diaria/mensual para reprogramación de módulos PCM, TCM y BCM.</td>
    </tr>
  </tbody>
</table>
""", prefix="../") + box("2. Requisitos Críticos de Taller: El Estabilizador de Tensión", "alert", r"""
<p>El proceso de flasheo oficial de una centralita mediante Pass-Thru implica el borrado completo de la memoria Flash y la grabación sucesiva de bloques de datos durante un tiempo que oscila entre <strong>15 minutos y más de 1 hora</strong>. Durante esta operación, el contacto está activado (KL15 ON), lo que provoca que los sistemas del vehículo permanezcan en alerta continua.</p>

<div class="callout peligro">
  <span class="cap">¿Por qué se Disparan los Electroventiladores a Máxima Potencia?</span>
  <p>Al iniciarse el borrado de la memoria Flash de la ECU motor, el microcontrolador cesa temporalmente la emisión de mensajes CAN de confirmación de temperatura de refrigerante. La centralita de carrocería o el módulo de electroventiladores interpreta esta ausencia como una condición de <strong>fallo catastrófico de seguridad</strong> (<em>fail-safe</em>), activando inmediatamente los ventiladores a su máxima velocidad. El consumo de corriente del vehículo salta instantáneamente de 15 A a <strong>más de 60 A - 80 A</strong>.</p>
  <p>Si el taller no dispone de un <strong>estabilizador de tensión profesional de 70 A a 100 A</strong>, la tensión de la batería colapsará por debajo de los 11,5 V en menos de 3 minutos. El microcontrolador abortará la escritura en mitad del proceso, dejando la centralita <strong>totalmente inservible (bricked)</strong>.</p>
</div>

<h4>Protocolo de Preparación del Vehículo antes de Iniciar Pass-Thru</h4>
<ol>
  <li><strong>Conectar un estabilizador de tensión</strong> de alto amperaje en modo <em>Diagnostic / Showroom</em> fijado a 13,8 V - 14,4 V con cables de sección mínima de 16 mm². Prohibido utilizar cargadores convencionales por su excesivo rizado de corriente alterna (<em>AC ripple</em>), que corrompe la trama de datos CAN.</li>
  <li><strong>Conectar el portátil a la red eléctrica de 230 V</strong> y desactivar completamente las opciones de suspensión, apagado de pantalla y desconexión selectiva de puertos USB en Windows.</li>
  <li><strong>Utilizar conexión a Internet obligatoriamente por CABLE ETHERNET (RJ45)</strong>. Desactivar el Wi-Fi del ordenador para evitar pérdidas momentáneas de paquetes de datos durante la telecarga.</li>
  <li><strong>Apagar todos los consumidores parásitos:</strong> Luces de cruce y diurnas, climatizador, radio/pantalla multimedia y asegurarse de no abrir ni cerrar puertas durante el proceso.</li>
</ol>
""", prefix="../") + nav_block("05-normativa-pass-thru-j2534")


# ===============================================================
# TEMA 6: CASOS PRÁCTICOS DE TALLER PASO A PASO
# ===============================================================
BODIES["06-casos-practicos-taller"] = box("1. Metodología de Intervención en 4 Casos Reales", "case", r"""
<p>A continuación se detallan 4 procedimientos de trabajo protocolizados que representan las situaciones cotidianas más complejas a las que se enfrenta un electromecánico en el taller:</p>

<div class="ejemplo">
  <div class="ej-head">
    <span>CASO 1: Clonación en Banco (Bench Mode) de UCE Bosch EDC17C64</span>
    <span class="badge">VAG 1.6 TDI</span>
  </div>
  <div class="ej-body">
    <div class="dato"><strong>Problema:</strong> Vehículo inmovilizado por entrada de agua en el conector de la ECU original. Se dispone de una centralita idéntica procedente de desguace (misma referencia hardware).</div>
    <div class="paso">
      <span class="n">1</span>
      <strong>Conexión de Pinout en Banco:</strong> Consultar el esquema de pines en la base de datos de la herramienta (ej. Autotuner/Flex). Conectar los pines de alimentación (+12V permanente, ignición KL15), masa GND, bus CAN (CAN-H y CAN-L) y los <strong>dos pines GPT (GPT1 y GPT2)</strong> en el conector de la centralita sin abrir la carcasa sellada.
    </div>
    <div class="paso">
      <span class="n">2</span>
      <strong>Lectura Completa (Full Read):</strong> Alimentar con la fuente regulada a 13,5 V. El software inyecta la frecuencia de desbloqueo GPT y extrae en banco la <strong>Flash interna (TC1797) y la EEPROM</strong> de la UCE original dañada. Guardar copia de seguridad fechada.
    </div>
    <div class="paso">
      <span class="n">3</span>
      <strong>Escritura en UCE Donante:</strong> Desconectar la centralita averiada y conectar la unidad de desguace con el mismo mazo de pines. Seleccionar la función de escritura completa volcando los archivos Flash y EEPROM leídos.
    </div>
    <div class="resultado">
      ✓ Resultado: La UCE donante hereda el 100% de los datos de inmovilizador, bastidor VIN y calibración. Se monta en el vehículo y arranca de inmediato sin necesidad de acudir al concesionario oficial.
    </div>
  </div>
</div>

<div class="ejemplo">
  <div class="ej-head">
    <span>CASO 2: Diagnóstico y Sustitución de Regulador de 5V en Placa</span>
    <span class="badge">Hardware SMD</span>
  </div>
  <div class="ej-body">
    <div class="dato"><strong>Problema:</strong> Centralita Bosch EDC16C34 de Peugeot/Ford. Registra avería simultánea en sensor de presión de raíl, caudalímetro y pedal del acelerador con código P0641 (Tensión de referencia de sensores A).</div>
    <div class="paso">
      <span class="n">1</span>
      <strong>Comprobación con Polímetro en Vehículo:</strong> Desconectar todos los sensores de la línea de 5V. La tensión entre el pin de alimentación del conector y masa sigue marcando 0,2 V (debería marcar 5,00 V al retirar la carga externa).
    </div>
    <div class="paso">
      <span class="n">2</span>
      <strong>Extracción y Apertura Segura en Banco:</strong> Retirar los tornillos Torx de la carcasa de la centralita. Aplicar calor perimetral a 90 °C con pistola de aire caliente para ablandar el sellador de silicona y abrir con palancas plásticas.
    </div>
    <div class="paso">
      <span class="n">3</span>
      <strong>Localización del Componente:</strong> Rastrear con la punta del multímetro en continuidad la pista del pin de 5V hasta el circuito integrado regulador (Bosch 30344 / 40048). Medir resistencia entre la patilla de salida y masa: marca <strong>1,2 Ω (cortocircuito franco interno)</strong>.
    </div>
    <div class="paso">
      <span class="n">4</span>
      <strong>Procedimiento de Sustitución SMD:</strong> Aplicar cinta Kapton sobre los componentes colindantes para protegerlos del calor. Añadir flux líquido y calentar uniformemente con tobera de aire caliente a 360 °C hasta que el estaño funda. Retirar el chip con pinzas de precisión. Limpiar los pads de la placa con malla de cobre y soldar el regulador de repuesto aplicando flux y soldadura nueva.
    </div>
    <div class="resultado">
      ✓ Resultado: Alimentada en banco a 12V, la salida mide <strong>5,01 V estables</strong>. Se sella con silicona técnica de poliuretano y la UCE vuelve a funcionar con normalidad.
    </div>
  </div>
</div>

<div class="ejemplo">
  <div class="ej-head">
    <span>CASO 3: Rescate de UCE Brickeada mediante Bootloader</span>
    <span class="badge">Recuperación</span>
  </div>
  <div class="ej-body">
    <div class="dato"><strong>Problema:</strong> Centralita Continental SID208 bloqueada por corte fortuito de batería durante una reprogramación por toma OBD-II. La UCE no responde a la diagnosis ni permite comunicación estándar.</div>
    <div class="paso">
      <span class="n">1</span>
      <strong>Apertura y Localización del Pad de Boot:</strong> Abrir la tapa metálica de la UCE. Consultar el esquema de conexión en modo Bootloader para el procesador TriCore TC1797.
    </div>
    <div class="paso">
      <span class="n">2</span>
      <strong>Conexión de Resistencia de Boot:</strong> Soldar un cable fino con una <strong>resistencia de 1 kΩ en serie</strong> conectada entre el pad de Boot de la placa y la masa (GND) del programador.
    </div>
    <div class="paso">
      <span class="n">3</span>
      <strong>Arranque en Modo Fábrica y Reescritura:</strong> Encender la fuente. El procesador, al tener el pin de boot en nivel bajo forzado por la resistencia, ignora el firmware corrupto de la Flash y ejecuta el microcódigo de fábrica residente en ROM. La herramienta reconoce la UCE y permite reescribir el archivo de calibración original (Backup).
    </div>
    <div class="resultado">
      ✓ Resultado: Se reescribe la Flash al 100%. Se desuelda el cable de boot, se cierra la centralita y se recupera completamente la comunicación OBD.
    </div>
  </div>
</div>
""", prefix="../") + nav_block("06-casos-practicos-taller")


# ===============================================================
# TEMA 7: MEDIATECA TÉCNICA
# ===============================================================
BODIES["07-mediateca-tecnica"] = box("1. Recursos Audiovisuales y Demostraciones Prácticas", "video", r"""
<p>Selección de recursos audiovisuales técnicos y demostraciones verificadas para afianzar los procedimientos de taller:</p>

""" + video_embed("cj50cas", "Principios de Control de Módulos y Divisores de Tensión", "Fundamentos del control electrónico, divisores resistivos para lectura multiplexada de señales y conmutación de etapas de potencia mediante relés y transistores.", "Autodata Training", "verified") + r"""

""" + video_embed("jc75cas", "Circuitos Elevadores y Reductores (Pull-Up y Pull-Down)", "Comprobación de líneas de tensión de referencia de 5V y monitorización de señales analógicas y digitales en sensores del motor.", "Autodata Training", "verified") + r"""

""" + video_embed("et00cas", "Procedimiento de Reprogramación Pass-Thru (SAE J2534)", "Protocolo oficial de conexión de interfaz VCI J2534, portales web de fabricantes de automóviles y requisitos indispensables de estabilizadores de tensión en el taller.", "Autodata Training", "verified") + r"""

<div class="callout nota">
  <span class="cap">Ampliación Práctica en el Taller</span>
  <p>Se recomienda complementar estos contenidos con prácticas directas de soldadura SMD en placas de desecho, familiarizándose con el uso de la estación de aire caliente, flux, desoldador de vacío y microscopio estereoscópico antes de intervenir en centralitas operativas.</p>
</div>
""", prefix="../") + nav_block("07-mediateca-tecnica")

# ===============================================================
# CUESTIONARIO DE EVALUACIÓN FINAL (50 PREGUNTAS / 20 ACTIVAS)
# ===============================================================
spec_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(spec_dir, "quiz_engine.html"), encoding="utf-8") as _f:
    _QUIZ_ENGINE = _f.read()

_PREGUNTAS_JS = r"""
// Configuración del motor interactivo SCORM 1.2:
var NUM_PREGUNTAS = 20;       // Número de preguntas activas mostradas de 1 en 1 por intento
var RANDOMIZE_OPTIONS = true; // Barajado dinámico de alternativas con guardián anti-patrones
var PASS = 50;                // Porcentaje mínimo de superación oficial

// Banco completo de 50 preguntas técnicas rigurosas para electromecánicos:
var PREGUNTAS = [
  {
    "q": "¿Qué función primordial desempeña la memoria EEPROM en una centralita de motor moderna?",
    "opts": [
      "Almacenar el sistema operativo en tiempo real (RTOS) y las tablas de inyección",
      "Custodiar datos no volátiles reescribibles como inmovilizador (IMMO), número de bastidor (VIN) y codificación de inyectores",
      "Guardar temporalmente los cálculos dinámicos de encendido que se borran al quitar el contacto",
      "Controlar la señal analógica del potenciómetro del pedal del acelerador"
    ],
    "correct": 1,
    "fb": "Correcto. La EEPROM almacena datos identificativos y de seguridad únicos del vehículo (IMMO, VIN, adaptaciones y codificaciones de inyectores) que no se pierden al quitar la batería."
  },
  {
    "q": "¿Por qué las placas de circuito impreso (PCB) de las ECUs de automoción son de tipo multicapa (multilayer)?",
    "opts": [
      "Para integrar planos de masa internos y apantallamiento contra interferencias electromagnéticas (EMI) en un tamaño compacto",
      "Para permitir la sustitución manual de pistas sin necesidad de herramientas de soldadura",
      "Para reducir el grosor de la placa a menos de 0,1 mm y abaratar costes de cobre",
      "Para evitar el uso de siliconas sellantes en las carcasas exteriores"
    ],
    "correct": 0,
    "fb": "Correcto. Las placas de 4 a 8 capas permiten crear planos de masa intermedios (ground planes) que blindan las señales débiles frente a las interferencias electromagnéticas generadas por las bobinas e inyectores."
  },
  {
    "q": "¿Qué tensión de referencia estándar entrega el circuito regulador de la ECU para alimentar la mayoría de sensores analógicos del motor?",
    "opts": [
      "12,0 V constantes procedentes del alternador",
      "3,3 V dedicados exclusivamente a componentes analógicos",
      "5,00 V ultraestables protegidos contra sobretensiones",
      "1,5 V correspondientes a la tensión del núcleo del procesador"
    ],
    "correct": 2,
    "fb": "Exacto. La línea de referencia de sensores trabaja a 5,00 V estabilizados, garantizando que variaciones en la tensión de batería (11V-14,5V) no alteren las mediciones de los sensores (MAP, TPS, presión de raíl, etc.)."
  },
  {
    "q": "En caso de inducirse un pico de sobretensión al conmutar un inyector inductivo, ¿qué componente protege al transistor de potencia en la ECU?",
    "opts": [
      "El microcontrolador principal mediante interrupción software",
      "Una resistencia NTC en serie con la bobina",
      "El condensador electrolítico del filtro de entrada",
      "Un diodo de libre circulación (flyback) o diodo zener supresor de transitorios (TVS)"
    ],
    "correct": 3,
    "fb": "Correcto. Los diodos flyback / supresores de transitorios derivan a masa o limitan la fuerza contraelectromotriz (picos de más de 100V-400V) que se produce al desconectar cargas inductivas."
  },
  {
    "q": "¿Qué familia de microcontroladores de 32 bits es la más habitual en centralitas Bosch EDC17 y MED17?",
    "opts": [
      "Motorola C167 de 16 bits",
      "Infineon TriCore (familias TC17xx y TC2xx)",
      "Microchip PIC16F84",
      "Intel Core i3 de bajo consumo"
    ],
    "correct": 1,
    "fb": "Correcto. La arquitectura Infineon TriCore domina la generación EDC17/MED17 de Bosch y muchas unidades Continental SID, destacando por su potencia de cálculo y módulos de protección antituning."
  },
  {
    "q": "¿Qué tipo de transistor se utiliza habitualmente en las etapas de encendido primario de motores de gasolina por su alta capacidad de bloqueo?",
    "opts": [
      "Transistores IGBT (Insulated Gate Bipolar Transistor)",
      "Transistores bipolares NPN genéricos de pequeña señal",
      "Relés mecánicos de micromuelle",
      "Triacs para corriente alterna"
    ],
    "correct": 0,
    "fb": "Efectivamente. Los IGBTs combinan la facilidad de excitación por tensión de un MOSFET con la capacidad de conducir elevadas corrientes y soportar tensiones de bloqueo de 400V-500V del transistor bipolar."
  },
  {
    "q": "¿Qué tensión suele utilizar el microcontrolador en su núcleo interno (Core VDD) en una UCE actual?",
    "opts": [
      "12,0 V",
      "5,0 V",
      "1,2 V a 1,5 V",
      "24,0 V"
    ],
    "correct": 2,
    "fb": "Correcto. El núcleo (core) del procesador funciona a tensiones reducidas (1,2V a 1,5V) para reducir el consumo térmico a altas frecuencias de reloj, mientras los puertos de E/S operan a 3,3V o 5V."
  },
  {
    "q": "¿Qué misión cumple el módulo de seguridad HSM (Hardware Security Module) integrado en los microcontroladores de última generación?",
    "opts": [
      "Impedir que el motor supere las 3000 RPM durante el rodaje",
      "Activar el airbag en caso de impacto frontal severo",
      "Regular la temperatura del refrigerante mediante control PID",
      "Proteger las claves criptográficas, autenticar las firmas de software y evitar modificaciones no autorizadas"
    ],
    "correct": 3,
    "fb": "Exacto. El HSM es un subsistema aislado dentro del microcontrolador que ejecuta algoritmos criptográficos para verificar la autenticidad del firmware y evitar manipulaciones antituning."
  },
  {
    "q": "¿Cuál es la función del transceptor (transceiver) CAN Bus como el TJA1040/1050 en la placa?",
    "opts": [
      "Calcular el tiempo de inyección según la señal del caudalímetro",
      "Convertir las señales lógicas digitales de 0/3,3V del micro en señales diferenciales CAN-H y CAN-L de bus de datos",
      "Alimentar directamente a los inyectores con 80V de tensión",
      "Filtrar el combustible antes de entrar en la bomba de alta presión"
    ],
    "correct": 1,
    "fb": "Correcto. El transceptor es el puente físico entre la lógica digital del microcontrolador (Rx/Tx) y las tensiones diferenciales de la línea física del bus (CAN-High y CAN-Low)."
  },
  {
    "q": "¿Qué ocurre si se cortocircuita el cable de alimentación de 5V de un sensor exterior contra el bloque del motor?",
    "opts": [
      "El circuito integrado regulador de 5V entra en protección térmica o se destruye, provocando múltiples códigos de avería de sensores",
      "La centralita aumenta automáticamente la potencia de inyección para compensar la caída",
      "Se borra instantáneamente la memoria Flash de calibración",
      "El alternador deja de cargar la batería inmediatamente"
    ],
    "correct": 0,
    "fb": "Correcto. Un cortocircuito externo en la línea de 5V provoca la caída a 0V de toda la línea de sensores de la centralita (código P0641 u homólogos), haciendo que el motor se detenga o no arranque."
  },
  {
    "q": "¿En qué consiste el método de flasheo por toma OBD-II?",
    "opts": [
      "En desoldar el microcontrolador y colocarlo en un zócalo de programación externo",
      "En conectar agujas de muelle directamente sobre las pistas de la placa electrónica",
      "En transferir los datos a través del conector de diagnosis de 16 pines del habitáculo sin desmontar la UCE",
      "En reprogramar el vehículo mediante señales de radiofrecuencia a distancia"
    ],
    "correct": 2,
    "fb": "Correcto. El puerto OBD-II permite reprogramar la UCE de forma no invasiva mediante el protocolo de diagnosis estándar (K-Line, CAN o DoIP)."
  },
  {
    "q": "¿Qué es la 'Lectura Virtual' (Virtual Read - VR) utilizada en muchas reprogramaciones por OBD-II?",
    "opts": [
      "Una simulación en 3D del motor funcionando en un banco de potencia",
      "La lectura por ultrasonidos del número de serie grabado en la carcasa metálica",
      "Un procedimiento que no necesita conectar ningún cable al vehículo",
      "La descarga del archivo original de calibración desde el servidor de la herramienta tras identificar la referencia software de la ECU"
    ],
    "correct": 3,
    "fb": "Exacto. En muchas ECUs con protección antituning en OBD, la herramienta solo lee los identificadores (ID) y descarga de su base de datos en la nube el archivo original de fábrica idéntico."
  },
  {
    "q": "¿Cuál es la principal ventaja técnica del método 'Bench Mode' frente a la lectura tradicional por Bootloader?",
    "opts": [
      "Que no requiere conectar ninguna fuente de alimentación externa",
      "Que permite la lectura y clonación completa sin necesidad de abrir ni desprecintar la carcasa de la centralita",
      "Que funciona aunque la centralita esté completamente quemada y calcinada",
      "Que sustituye automáticamente los inyectores defectuosos en el vehículo"
    ],
    "correct": 1,
    "fb": "Correcto. El modo Bench accede a la memoria completa conectando a los pines del conector exterior, evitando el riesgo de romper la placa o perder la estanqueidad de la silicona de fábrica."
  },
  {
    "q": "¿Qué papel cumplen los pines GPT (General Purpose Timer) en la lectura en banco de centralitas TriCore?",
    "opts": [
      "Inyectar una señal de frecuencia sincronizada para sortear la protección antituning y extraer la contraseña SOPT",
      "Medir la temperatura del estaño durante la soldadura",
      "Enviar la señal de disparo a las bujías de encendido",
      "Regular la velocidad del ventilador de la fuente de alimentación"
    ],
    "correct": 0,
    "fb": "Correcto. Los pines GPT1 y GPT2 reciben señales moduladas por la herramienta para autenticar el microcontrolador TriCore y desbloquear la lectura sin abrir la unidad."
  },
  {
    "q": "¿Qué elemento físico suele requerir el método de lectura 'Boot Mode' en la placa de la centralita?",
    "opts": [
      "Un puente directo de 230V de corriente alterna",
      "Un fusible de 50A soldado entre dos condensadores",
      "Una resistencia de arranque (típicamente 1 kΩ) conectada entre un pad de boot y masa",
      "Un condensador electrolítico de arranque en paralelo con la batería"
    ],
    "correct": 2,
    "fb": "Correcto. Poner el pin de Boot a nivel de masa (generalmente a través de una resistencia de 1 kΩ para limitar la corriente) fuerza al procesador a ejecutar su bootloader interno de recuperación."
  },
  {
    "q": "¿Para qué tipo de microcontroladores se desarrolló históricamente el puerto de programación BDM (Background Debug Mode)?",
    "opts": [
      "Para procesadores de 8 bits de mandos de garaje",
      "Para microprocesadores Intel de servidores de datos",
      "Para ordenadores cuánticos de vehículos autónomos",
      "Para procesadores de la familia Motorola / Freescale (como el MPC555 de Bosch EDC16)"
    ],
    "correct": 3,
    "fb": "Exacto. El puerto BDM de 10 o 14 pines fue el estándar para acceder al bus interno de los procesadores Motorola MPC5xx en generaciones como Bosch EDC16."
  },
  {
    "q": "¿Cuál es la diferencia fundamental entre una herramienta de flasheo en versión 'Master' y una 'Slave'?",
    "opts": [
      "La versión Slave es inalámbrica y la Master solo funciona por cable",
      "La herramienta Master genera y lee archivos binarios abiertos (.bin), mientras que la Slave trabaja con archivos encriptados ligados a un Master",
      "La versión Master solo sirve para camiones y la Slave para turismos",
      "La herramienta Slave no necesita estabilizador de tensión en ningún caso"
    ],
    "correct": 1,
    "fb": "Correcto. El usuario Master dispone de los archivos libres para editarlos en cualquier editor (WinOLS), mientras que el Slave depende de su proveedor Master para descifrar y calibrar los archivos."
  },
  {
    "q": "¿Por qué es obligatorio realizar un 'Full Backup' antes de modificar cualquier centralita?",
    "opts": [
      "Porque permite restaurar la centralita al 100% (Flash y EEPROM) si se interrumpe la escritura o se corrompe el archivo",
      "Porque la ITV exige un justificante en papel del archivo original",
      "Porque si no se hace el backup, la herramienta se bloquea y cobra una penalización",
      "Porque borra automáticamente los fallos mecánicos del motor"
    ],
    "correct": 0,
    "fb": "Efectivamente. El Full Backup es el seguro de vida del taller: ante cualquier fallo de comunicación o archivo defectuoso, se puede clonar o recuperar la unidad exactamente a su estado funcional."
  },
  {
    "q": "¿Qué precaución mecánica es crítica al abrir una centralita sellada con masilla de silicona técnica?",
    "opts": [
      "Sumergir la centralita en agua fría para endurecer el pegamento",
      "Usar un destornillador plano de gran tamaño haciendo palanca en el centro de la placa",
      "Calentar suavemente el perímetro para ablandar el sellante y usar palancas plásticas sin profundizar para no cortar pistas",
      "Cortar la carcasa metálica con una radial amoladora"
    ],
    "correct": 2,
    "fb": "Correcto. Introducir herramientas metálicas o flexionar la placa de circuito impreso puede romper pistas periféricas o microvías multicapa, provocando daños irreparables."
  },
  {
    "q": "¿Qué pines estándar del conector OBD-II (DLC) se emplean para la comunicación CAN de alta velocidad con la ECU motor?",
    "opts": [
      "Pin 1 y Pin 9",
      "Pin 4 y Pin 5 exclusivamente",
      "Pin 16 y Pin 8",
      "Pin 6 (CAN High) y Pin 14 (CAN Low)"
    ],
    "correct": 3,
    "fb": "Correcto. Según la norma SAE J1962, los pines 6 y 14 transportan las líneas diferenciales de CAN High y CAN Low de la red de tracción del vehículo."
  },
  {
    "q": "¿Qué variables físicas definen habitualmente los ejes X e Y de un mapa de inyección en tres dimensiones (3D)?",
    "opts": [
      "Eje X: Presión de neumáticos; Eje Y: Nivel de aceite",
      "Eje X: Régimen del motor (RPM); Eje Y: Carga del motor (presión de admisión MAP o masa de aire MAF)",
      "Eje X: Tensión de batería; Eje Y: Temperatura ambiente exterior",
      "Eje X: Velocidad del vehículo (km/h); Eje Y: Marcha engranada"
    ],
    "correct": 1,
    "fb": "Correcto. En la inmensa mayoría de mapas motor, el eje X representa las RPM del cigüeñal y el eje Y representa la carga o flujo de aire, dando como resultado (eje Z) el valor de inyección, avance o presión."
  },
  {
    "q": "¿Qué función cumple el 'Mapa de Pedal' (Driver Wish) en una UCE diésel Common Rail?",
    "opts": [
      "Convertir la posición angular del acelerador (%) y las RPM en una demanda de par motor (Nm) o caudal de combustible",
      "Calcular la presión necesaria en el pedal de freno para el sistema ABS",
      "Regular la dureza del pedal de embrague en vehículos manuales",
      "Avisar al conductor si está pisando el acelerador con demasiada fuerza"
    ],
    "correct": 0,
    "fb": "Exacto. El Driver Wish interpreta la intención del conductor: traduce el porcentaje de pisada del pedal y el régimen en par motor solicitado, que luego será procesado por los limitadores."
  },
  {
    "q": "¿Cuál es la misión principal del 'Limitador de Humos' (Smoke Limiter / Mapa Lambda)?",
    "opts": [
      "Encender un indicador en el cuadro cuando el filtro de habitáculo está sucio",
      "Evitar que el motor arranque si detecta humo en el vano motor",
      "Restringir la cantidad máxima de combustible inyectable según la masa de aire fresco disponible para evitar la emisión de hollín",
      "Aumentar la temperatura de los gases de escape abriendo la válvula EGR al 100%"
    ],
    "correct": 2,
    "fb": "Correcto. El limitador de humos garantiza que nunca se inyecte más combustible del que puede quemarse con la masa de aire medida por el caudalímetro, evitando la formación excesiva de partículas."
  },
  {
    "q": "¿Por qué es crucial el mapa de 'Avance de Inyección' (Start of Injection - SOI)?",
    "opts": [
      "Porque indica a qué velocidad debe girar el motor de arranque",
      "Porque apaga los inyectores cuando el coche baja una pendiente",
      "Porque calcula el volumen del depósito de combustible",
      "Porque determina el ángulo exacto del cigüeñal (grados antes del PMS) en el que se inicia la inyección para optimizar la combustión"
    ],
    "correct": 3,
    "fb": "Exacto. Un avance de inyección óptimo sitúa el pico de presión de combustión entre 12° y 15° después del PMS. Un avance excesivo provoca picado y sobrepresión; un retardo genera humo y pérdida de rendimiento."
  },
  {
    "q": "¿Qué representa el mapa de control de la electroválvula de sobrealimentación (N75)?",
    "opts": [
      "La presión del circuito de frenos en una frenada de emergencia",
      "El ciclo de trabajo en modulación por ancho de pulso (PWM Duty Cycle %) aplicado a la geometría variable del turbo",
      "El nivel de combustible restante en el depósito de reserva",
      "La temperatura del aceite de la caja de cambios"
    ],
    "correct": 1,
    "fb": "Correcto. La centralita modula el porcentaje de ciclo de trabajo PWM de la válvula N75 para variar el vacío o la posición electrónica de los álabes de la geometría variable del turbocompresor."
  },
  {
    "q": "¿Qué es un archivo DAMOS o A2L en el software de calibración WinOLS?",
    "opts": [
      "Un paquete de descripción técnica que identifica nombres de mapas, unidades físicas, factores de conversión y offsets",
      "Un virus informático diseñado para bloquear herramientas clon",
      "Un archivo de música que se reproduce durante la escritura de la ECU",
      "Una copia comprimida del manual de usuario del vehículo"
    ],
    "correct": 0,
    "fb": "Efectivamente. Los archivos DAMOS/A2L son la 'piedra Rosetta' del calibrador: proporcionan la información de ingeniería original del fabricante para saber exactamente qué representa cada byte de la memoria."
  },
  {
    "q": "¿Qué sucede en el vehículo si se reprograma la memoria Flash con un Checksum incorrecto?",
    "opts": [
      "El coche funciona perfectamente pero el reloj del cuadro se atrasa",
      "El motor consume un 10% más de combustible sin registrar avería",
      "El microcontrolador detecta incoherencia en su rutina de autochequeo y bloquea el arranque del motor",
      "Se enciende la radio en el volumen máximo de forma automática"
    ],
    "correct": 2,
    "fb": "Correcto. Un Checksum no recalculado o erróneo es detectado inmediatamente por la rutina de seguridad del procesador al dar contacto, impidiendo que el motor arranque (condición de bloqueo)."
  },
  {
    "q": "¿Qué caracteriza a una reprogramación de nivel 'Stage 1'?",
    "opts": [
      "Obliga a cambiar el turbocompresor, colectores y línea de escape completa",
      "Anula todos los sensores de temperatura y presión del motor",
      "Requiere utilizar exclusivamente combustible de competición de 102 octanos",
      "Aumenta par y potencia aprovechando los márgenes de diseño del fabricante manteniendo el vehículo 100% de serie"
    ],
    "correct": 3,
    "fb": "Exacto. Una calibración Stage 1 optimiza los parámetros de inyección y soplado dentro de las tolerancias térmicas y mecánicas holgadas de los componentes mecánicos de serie."
  },
  {
    "q": "¿En qué consiste la 'Virginización' de una centralita de motor de desguace?",
    "opts": [
      "En pintarla de color blanco para certificar que no tiene arañazos",
      "En borrar la zona del inmovilizador en la EEPROM para que se sincronice automáticamente al dar contacto en el coche receptor",
      "En sustituir todos los transistores de potencia por componentes nuevos",
      "En cambiar el aceite del motor antes de conectar la centralita"
    ],
    "correct": 1,
    "fb": "Correcto. Dejar una centralita en estado virgen borra los datos criptográficos del vehículo anterior, permitiendo que aprenda el código de llaves e inmovilizador del nuevo coche al dar contacto."
  },
  {
    "q": "¿Qué magnitud representa el 'Factor de Conversión' aplicado a un mapa en WinOLS?",
    "opts": [
      "El multiplicador matemático para convertir los valores hexadecimales brutos en unidades físicas reales (ej. RPM, mg, mbar)",
      "La tasa de cambio monetario entre euros y dólares para comprar el archivo",
      "El porcentaje de comisión que se cobra al cliente por la reprogramación",
      "El tiempo que tarda el soldador en alcanzar su temperatura máxima"
    ],
    "correct": 0,
    "fb": "Correcto. La memoria almacena enteros (ej. de 0 a 65535). El factor (ej. 0.01 o 0.05) y el offset traducen esos números a magnitudes de ingeniería como presión en mbar o temperatura en °C."
  },
  {
    "q": "¿Qué instrumento es imprescindible llevar puesto al manipular una placa de ECU abierta para evitar daños invisibles?",
    "opts": [
      "Gafas de buceo con filtro UV",
      "Guantes gruesos de soldadura de cuero vacuno",
      "Pulsera antiestática (ESD) conectada a una toma de tierra fiable",
      "Un reloj inteligente con pulsómetro"
    ],
    "correct": 2,
    "fb": "Correcto. La descarga electrostática humana (ESD) puede superar los 3.000 V sin ser sentida, perforando las delgadas capas aislantes de óxido de silicio de los microchips."
  },
  {
    "q": "¿A qué temperatura aproximada debe regularse la pistola de aire caliente para desoldar un chip SMD sin levantar pistas?",
    "opts": [
      "A 100 °C durante 30 minutos",
      "A 600 °C con flujo de aire máximo",
      "A 180 °C soplando a gran distancia",
      "Entre 340 °C y 370 °C con tobera adecuada y aplicación previa de flux"
    ],
    "correct": 3,
    "fb": "Exacto. El estaño libre de plomo (Lead-Free SAC) funde sobre 217 °C. Un flujo de aire a 350-370 °C con flux transfiere calor rápido sin quemar el epoxi de la placa ni despegar pistas."
  },
  {
    "q": "¿Qué producto químico se debe utilizar en la cubeta de ultrasonidos para limpiar una ECU sulfatada por agua?",
    "opts": [
      "Agua del grifo con jabón lavavajillas",
      "Alcohol isopropílico (IPA) de alta pureza (99,9%)",
      "Líquido de frenos DOT 4",
      "Gasóleo de automoción sin aditivos"
    ],
    "correct": 1,
    "fb": "Correcto. El alcohol isopropílico de pureza 99,9% no contiene agua, disuelve las sales y grasas de la corrosión, es dieléctrico y se evapora con rapidez sin dejar residuos conductores."
  },
  {
    "q": "¿Cómo se comprueba rápidamente en banco si un transistor MOSFET de canal N está cruzado (cortocircuitado)?",
    "opts": [
      "Midiendo en modo diodo con el multímetro entre Drenador (Drain) y Fuente (Source); si marca 0,00 V con pitido continuo, está perforado",
      "Midiendo la longitud física del encapsulado con un calibre vernier",
      "Comprobando si el transistor es atraído por un imán permanente",
      "Midiendo la resistencia entre la carcasa exterior y el terminal positivo de batería"
    ],
    "correct": 0,
    "fb": "Efectivamente. Un MOSFET en buen estado no debe presentar continuidad franca (0,00 V) entre drenador y fuente, sino una caída de diodo parásito interno (aprox. 0,5 V a 0,7 V) en un sentido y circuito abierto en el otro."
  },
  {
    "q": "¿Por qué es muy útil limitar la corriente a unos 250 mA en la fuente regulada al encender una ECU reparada por primera vez en banco?",
    "opts": [
      "Para ahorrar electricidad en la factura del taller",
      "Porque el microcontrolador necesita poca energía para cargar la batería del coche",
      "Para evitar que se quemen componentes o se carbonicen pistas si aún persiste un cortocircuito interno",
      "Porque a más corriente la herramienta de diagnosis transmite más despacio"
    ],
    "correct": 2,
    "fb": "Correcto. Limitar la corriente en la fuente protege la placa: si hay un cortocircuito, la tensión de la fuente caerá a casi cero voltios sin que circule una intensidad destructiva que queme las pistas."
  },
  {
    "q": "¿Qué tipo de programador físico de memorias se utiliza frecuentemente en taller para leer chips EEPROM serie desoldados (ej. 95080, 24C04)?",
    "opts": [
      "Un lector de tarjetas SIM de teléfono móvil",
      "Un cable OBD-II ELM327 conectado al ordenador",
      "Un comprobador de bujías de chispa",
      "Un programador de memoria universal con zócalo ZIF (como UPA-USB, XGecu T48/TL866 o VVDI Prog)"
    ],
    "correct": 3,
    "fb": "Exacto. Los programadores con zócalo ZIF o pinzas de prueba permiten leer y verificar directamente los datos binarios de memorias SPI e I2C desoldadas de la placa."
  },
  {
    "q": "¿Qué fallo típico produce en una ECU el diodo supresor de transitorios (TVS) de entrada tras un intento de arranque con pinzas mal conectadas?",
    "opts": [
      "Provoca que las ventanillas del coche se abran solas",
      "Se cortocircuita internamente a masa para proteger el resto del circuito, provocando que la ECU no encienda y tire a cero la fuente",
      "Multiplica la tensión de la batería por diez",
      "Descalibra la geometría variable del turbocompresor"
    ],
    "correct": 1,
    "fb": "Correcto. El diodo de protección 'se sacrifica': se pone en cortocircuito franco permanente entre la línea positiva y masa para evitar que los 12V invertidos destruyan los microchips más sensibles."
  },
  {
    "q": "¿Qué directiva comunitaria ampara legalmente a los talleres independientes para acceder a la reprogramación oficial de los fabricantes?",
    "opts": [
      "Los Reglamentos Europeos Euro 5 (CE 715/2007) y Euro 6 (CE 595/2009) y el principio del derecho a reparar (Right to Repair)",
      "El Código de Circulación de 1934",
      "La Ley de Propiedad Intelectual sobre programas informáticos",
      "El tratado de libre comercio marítimo internacional"
    ],
    "correct": 0,
    "fb": "Efectivamente. La legislación europea obliga a los fabricantes de vehículos a ofrecer la información técnica y los accesos de telecarga y reprogramación en condiciones no discriminatorias respecto a sus concesionarios oficiales."
  },
  {
    "q": "¿Qué define la norma SAE J2534 (Pass-Thru)?",
    "opts": [
      "Las dimensiones físicas del volante y los pedales",
      "El tipo de aceite sintético que debe utilizar cada motor",
      "Una interfaz de comunicación estandarizada (VCI) entre el software de diagnosis del fabricante y la red interna del vehículo",
      "La potencia máxima que puede emitir el equipo de sonido"
    ],
    "correct": 2,
    "fb": "Correcto. El estándar SAE J2534 asegura que una única interfaz VCI universal pueda comunicarse con el software oficial de diferentes marcas (ODIS, ISTA, Xentry, Clip, etc.)."
  },
  {
    "q": "¿Por qué es inaceptable utilizar un cargador de baterías convencional durante una reprogramación Pass-Thru en el vehículo?",
    "opts": [
      "Porque pesa demasiado para transportarlo por el taller",
      "Porque solo funciona si el motor del coche está en marcha a 2000 RPM",
      "Porque emite una luz verde que confunde al sensor de lluvia",
      "Porque genera un rizado de corriente alterna (AC ripple) y no suministra los 70 A - 100 A limpios requeridos, pudiendo corromper la comunicación CAN"
    ],
    "correct": 3,
    "fb": "Exacto. Los cargadores convencionales tienen un rizado de tensión inaceptable y no pueden mantener 13,8V-14,4V estables cuando entran en funcionamiento los electroventiladores, provocando la destrucción de la centralita."
  },
  {
    "q": "¿Qué software oficial de diagnosis y telecarga utiliza el Grupo Volkswagen (Audi, VW, SEAT, Skoda)?",
    "opts": [
      "BMW ISTA-P",
      "ODIS (Offboard Diagnostic Information System)",
      "Mercedes Xentry",
      "Renault Clip"
    ],
    "correct": 1,
    "fb": "Correcto. ODIS es el software oficial del consorcio VAG para diagnosis guiada y telecarga de unidades de control con conexión a los servidores centrales GeKo."
  },
  {
    "q": "¿Por qué se recomienda conectar el ordenador de taller a Internet mediante CABLE ETHERNET en lugar de Wi-Fi durante un flasheo Pass-Thru?",
    "opts": [
      "Para garantizar la latencia mínima y evitar microcortes o interferencias que cancelen la descarga del firmware a mitad de proceso",
      "Porque el cable Ethernet aumenta la velocidad de giro de los electroventiladores",
      "Porque el protocolo OBD solo funciona si hay un cable azul conectado al router",
      "Porque la Wi-Fi consume la batería del coche a través de la toma de diagnosis"
    ],
    "correct": 0,
    "fb": "Efectivamente. Cualquier microcorte de red Wi-Fi durante la transferencia de un bloque de datos puede causar el rechazo de la trama por parte de la pasarela Gateway y el bloqueo de la centralita."
  },
  {
    "q": "¿Qué tensión debe mantener ininterrumpidamente el estabilizador de taller durante una telecarga Pass-Thru?",
    "opts": [
      "Entre 9,0 V y 10,5 V",
      "Exactamente 24,0 V",
      "Entre 13,8 V y 14,4 V con cero oscilaciones",
      "Cualquier valor superior a 8,0 V es suficiente"
    ],
    "correct": 2,
    "fb": "Correcto. Los fabricantes especifican una tensión de mantenimiento constante entre 13,8 V y 14,4 V en modo 'Diagnostic/Showroom' para garantizar la alimentación lógica de todos los módulos del bus."
  },
  {
    "q": "¿Qué procedimiento suele ser imprescindible realizar en el vehículo justo después de flashear una nueva calibración en la ECU motor?",
    "opts": [
      "Pintar el parachoques delantero para proteger los sensores ADAS",
      "Sustituir inmediatamente los neumáticos delanteros",
      "Desconectar el alternador y circular 50 km solo con batería",
      "Borrar los DTCs residuales de la red, realizar el aprendizaje del pedal y calibrar los sensores básicos (ej. ángulo de dirección)"
    ],
    "correct": 3,
    "fb": "Exacto. Durante el flasheo se generan múltiples códigos de falta de comunicación en otros módulos. Tras finalizar, se debe realizar un borrado general de averías y ejecutar los ajustes básicos y adaptaciones requeridas."
  },
  {
    "q": "En el módulo de bloqueo de columna de dirección Audi J518, ¿cuál es la avería física más frecuente que impide que el coche dé contacto?",
    "opts": [
      "La rotura física del volante de dirección",
      "El fallo interno de los microrrelés de conmutación de motor y el desgaste de los microinterruptores de posición en la placa",
      "La evaporación del refrigerante del motor",
      "El bloqueo de la antena GPS del techo"
    ],
    "correct": 1,
    "fb": "Correcto. Los dos microrrelés y los microswitches mecánicos se desgastan por uso, bloqueando la señal hacia el procesador Motorola MC9S12 e impidiendo que el relé de borne 15 dé contacto al coche."
  },
  {
    "q": "¿Cómo se comprueba si el cortocircuito de la línea de 5V procede de un sensor externo o de la propia placa de la ECU?",
    "opts": [
      "Desconectando todos los sensores exteriores: si la tensión recupera los 5,00 V en el conector, la UCE está sana y el fallo es externo",
      "Cambiando el aceite del motor para ver si sube la tensión",
      "Midiendo la presión de inflado de las cuatro ruedas con un manómetro",
      "Pulsando diez veces seguidas el claxon con el contacto quitado"
    ],
    "correct": 0,
    "fb": "Efectivamente. Al desconectar los sensores externos uno a uno (o todos a la vez), si la tensión de 5V se restablece, el cortocircuito está en el mazo o en el sensor desconectado. Si sigue en 0V, el fallo reside en la placa de la centralita."
  },
  {
    "q": "¿Qué componente de la placa de la ECU suele dañarse si se produce una fuga de alta tensión en una bobina de encendido defectuosa?",
    "opts": [
      "El conector de plástico de entrada de aire",
      "La bocina de alarma del vehículo",
      "El transistor IGBT o driver de disparo de encendido en la etapa de potencia",
      "El cristal de cuarzo del reloj de la centralita"
    ],
    "correct": 2,
    "fb": "Correcto. Un arco voltaico de alta tensión que retorne por el cable de masa o primario de la bobina destruye instantáneamente el semiconductor IGBT de conmutación de ese cilindro."
  },
  {
    "q": "¿Qué instrumento de taller permite observar en tiempo real la forma de onda PWM que la ECU envía a la electroválvula de control del turbo?",
    "opts": [
      "Una lámpara de pruebas de 21W convencional",
      "Un densímetro de batería de vidrio",
      "Un micrómetro de exteriores de precisión",
      "Un osciloscopio digital automotriz de al menos 2 canales"
    ],
    "correct": 3,
    "fb": "Exacto. El osciloscopio permite verificar la frecuencia (Hz), el ciclo de trabajo (% Duty Cycle) y la ausencia de picos anómalos o tensiones parásitas en la señal de control."
  },
  {
    "q": "¿Qué ventaja aporta el uso de cinta Kapton durante las operaciones de desoldadura con aire caliente en placas de ECU?",
    "opts": [
      "Aumenta la velocidad de descarga del firmware en un 50%",
      "Resiste temperaturas de más de 300 °C y protege a los componentes diminutos adyacentes del calor y del soplado de aire",
      "Permite soldar sin necesidad de aportar estaño ni flux",
      "Convierte la placa en sumergible e impermeable para siempre"
    ],
    "correct": 1,
    "fb": "Correcto. La cinta de poliamida Kapton soporta el choque térmico y evita que los componentes SMD colindantes se desolden o se vuelen con la corriente de aire de la tobera."
  },
  {
    "q": "¿Cuál es la regla definitiva de seguridad profesional antes de entregar un vehículo al cliente tras reprogramar o reparar su ECU?",
    "opts": [
      "Realizar una diagnosis completa de la red, verificar la estanqueidad del sellado de la carcasa y probar el vehículo en carretera registrando valores dinámicos",
      "Borrar todos los números de bastidor para que nadie pueda rastrear la reparación",
      "Dejar la batería desconectada durante 24 horas para que el motor se enfríe",
      "Aconsejar al cliente que no pase nunca de 2000 RPM para no gastar los datos de la centralita"
    ],
    "correct": 0,
    "fb": "Efectivamente. La verificación final con prueba en carretera monitorizando presiones reales frente a demandadas, junto con la comprobación del sellado estanco de la carcasa, garantiza un trabajo profesional y seguro."
  }
];
"""

BODIES["cuestionario"] = box("Evaluación Final de la Unidad", "activity", r"""
<div class="quiz-intro">
  <h3>Test de Evaluación Técnica: Reprogramación y Reparación de ECUs</h3>
  <p>Esta evaluación consta de <strong>20 preguntas técnicas aleatorias</strong> seleccionadas automáticamente de un banco de 50 ítems en cada intento. Deberás responder una a una utilizando la barra de píldoras o los botones de navegación.</p>
  <div class="quiz-meta">
    <span>Preguntas por intento: <b>20 de 50</b></span>
    <span>Nota de corte: <b>50%</b></span>
    <span>Reporte SCORM: <b>Libro de Calificaciones Aula Virtual</b></span>
    <span>Opciones barajadas: <b>Activas (Guardián anti-patrón)</b></span>
  </div>
</div>
""", prefix="../") + _QUIZ_ENGINE.replace("/*__PREGUNTAS__*/", _PREGUNTAS_JS) + nav_block("cuestionario")

# ---------------------------------------------------------------------------
# 3. DESTINO GOOGLE DRIVE (SINCRONIZACIÓN Y ENTREGA)
# ---------------------------------------------------------------------------
GDRIVE_FOLDER_URL = "https://drive.google.com/drive/u/0/folders/1o-j5gmI5SAPdXOeng-EG7hUXc1Wg-RrK"
GDRIVE_FOLDER_ID = "1o-j5gmI5SAPdXOeng-EG7hUXc1Wg-RrK"
GDRIVE_LOCAL_PATH = None
GDRIVE_AUTO_EXPORT = True
