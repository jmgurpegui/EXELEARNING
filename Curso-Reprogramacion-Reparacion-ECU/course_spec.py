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
    return f"""<div class="figura-taller" style="text-align:center;margin:1.6em 0;">
  <img src="{prefix}content/img/{img_file}" alt="{caption}" style="max-width:100%;height:auto;border-radius:8px;border:1px solid #cbd5e1;box-shadow:0 3px 10px rgba(0,0,0,0.06);">
  <div class="fig-cap" style="font-size:0.88rem;color:#475569;margin-top:0.6em;font-weight:500;line-height:1.4;">{num_str}{caption}</div>
</div>"""

def video_embed(video_id, title, desc, author="Demostración Técnica", badge="Vídeo Técnico", badge_color="#2563eb"):
    return f"""<div class="video-card" style="border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;margin:1.6em 0;background:#ffffff;box-shadow:0 3px 10px rgba(0,0,0,0.05);">
  <div class="video-card-header" style="background:#0f172a;color:#ffffff;padding:0.7em 1.1em;display:flex;justify-content:space-between;align-items:center;">
    <div>
      <h4 style="margin:0;color:#ffffff;font-size:0.98rem;font-weight:600;">{title}</h4>
      <span style="font-size:0.78rem;color:#94a3b8;">Canal / Autor: {author}</span>
    </div>
    <span class="video-badge" style="background:{badge_color};color:#ffffff;padding:0.25em 0.7em;border-radius:4px;font-size:0.75rem;font-weight:700;">{badge}</span>
  </div>
  <div class="video-container" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;background:#000;">
    <iframe src="https://www.youtube-nocookie.com/embed/{video_id}" title="{title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"></iframe>
  </div>
  <div style="padding:0.9em 1.1em;">
    <p class="video-desc" style="margin:0 0 0.7em;font-size:0.92rem;color:#334155;line-height:1.5;">{desc}</p>
    <a class="video-link-ext" href="https://www.youtube.com/watch?v={video_id}" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:6px;font-size:0.85rem;font-weight:600;color:#0284c7;text-decoration:none;">
      <span>▶️ Abrir y reproducir en YouTube (Ventana Completa)</span>
    </a>
  </div>
</div>"""

def autodata_card(code, title, desc, takeaways, duration, transcript_snippet):
    takeaways_html = "".join(f"<li>{t}</li>" for t in takeaways)
    return f"""<div class="autodata-card" style="border:1px solid #cbd5e1;border-radius:10px;overflow:hidden;margin:1.6em 0;background:#f8fafc;box-shadow:0 3px 10px rgba(0,0,0,0.04);">
  <div style="background:#047857;color:#ffffff;padding:0.7em 1.1em;display:flex;justify-content:space-between;align-items:center;">
    <h4 style="margin:0;color:#ffffff;font-size:0.98rem;display:flex;align-items:center;gap:8px;">
      <span style="background:#065f46;padding:2px 8px;border-radius:4px;font-size:0.75rem;letter-spacing:0.5px;font-weight:700;">AUTODATA TRAINING</span>
      {title}
    </h4>
    <span style="background:#10b981;color:#ffffff;padding:0.2em 0.7em;border-radius:4px;font-size:0.75rem;font-weight:700;">Módulo: {code}</span>
  </div>
  <div style="padding:1.1em 1.3em;">
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin-bottom:0.9em;font-size:0.85rem;color:#334155;background:#e2e8f0;padding:8px 12px;border-radius:6px;">
      <span><strong>📁 Archivo audiovisual:</strong> <code>{code} (540p).mp4</code></span>
      <span><strong>⏱️ Duración:</strong> {duration}</span>
      <span><strong>📂 Ubicación en taller / aula:</strong> <code>Autodata_Videos/módulos de control/</code></span>
    </div>
    <p style="margin:0 0 0.8em;font-size:0.92rem;color:#1e293b;line-height:1.5;">{desc}</p>
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #047857;border-radius:6px;padding:0.8em 1em;margin:0.8em 0;">
      <strong style="color:#047857;display:block;margin-bottom:0.4em;font-size:0.88rem;">🎯 Competencias y Puntos Clave de Aprendizaje:</strong>
      <ul style="margin:0;padding-left:1.2em;font-size:0.88rem;color:#334155;line-height:1.6;">
        {takeaways_html}
      </ul>
    </div>
    <details style="margin-top:0.8em;background:#f1f5f9;border:1px solid #cbd5e1;border-radius:6px;padding:0.6em 0.9em;">
      <summary style="font-weight:600;color:#0f766e;cursor:pointer;font-size:0.85rem;">📄 Ver extracto de la locución técnica del módulo (transcripción oficial)</summary>
      <div style="margin-top:0.6em;font-size:0.82rem;color:#475569;max-height:160px;overflow-y:auto;line-height:1.6;padding:8px;background:#ffffff;border-radius:4px;border:1px solid #e2e8f0;font-style:italic;">
        "{transcript_snippet}"
      </div>
    </details>
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
    <span>Diagnóstico SMD &amp; Soldadura</span>
    <span>Pass-Thru SAE J2534</span>
    <span>Clonación &amp; Desinmovilización</span>
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
BODIES["01-arquitectura-hardware-ecu"] = box("1. Anatomía y Blindaje de la Placa PCB Automotriz", "technology", r"""
<p>Una Unidad de Control Electrónico (UCE / ECU) del motor es un ordenador de grado automotriz diseñado para operar en condiciones extremas de vibración (hasta 30G), humedad y temperatura (-40 °C a +125 °C en vano motor). Su hardware interno se monta sobre una <strong>placa de circuito impreso multicapa (PCB de 4 a 8 capas)</strong> donde las pistas intermedias actúan como planos de masa (<em>ground planes</em>) y apantallamiento contra interferencias electromagnéticas (EMI).</p>

""" + figura("aspecto_diferentes_uce.png", "Tipos y aspectos constructivos de UCEs en automoción: UCE de gestión motor Bosch con conector sellado, UCE antibloqueo ABS/ESP montada sobre bloque hidráulico, caja electrónica de transferencia y módulo de cuadro de instrumentos digital.", 1, prefix="../") + r"""

<p>Para resistir la severa radiación electromagnética producida por el sistema de encendido, bobinas de inyección de alta tensión y motores eléctricos, las centralitas van alojadas en carcasas de fundición de aluminio inyectado dotadas de <strong>apantallamiento Jaula de Faraday</strong>:</p>

""" + figura("jaula_faraday_blindaje_emc.png", "Carcasa metálica de aluminio inyectado con blindaje interno de Jaula de Faraday y junta hermética de estanqueidad para protección contra interferencias electromagnéticas (EMI).", 2, prefix="../") + r"""

""" + figura("diagrama_arquitectura_ecu.svg", "Arquitectura interna funcional de una centralita electrónica de motor.", 3, prefix="../") + r"""

<div class="mag-grid">
  <div class="mag-card">
    <h4>Microcontrolador Central (MCU)</h4>
    <div class="sym">MCU</div>
    <div class="ud">TriCore / MPC5xx / Renesas</div>
    <p>Núcleo de 32 bits a 150-300 MHz. Ejecuta el ciclo de cómputo en tiempo real calculando el avance de encendido, tiempo de inyección y presión de sobrealimentación a partir de las señales de entrada.</p>
  </div>
  <div class="mag-card">
    <h4>Gestión de Alimentación (PMIC)</h4>
    <div class="sym">PMIC</div>
    <div class="ud">Reguladores LDO / Step-Down</div>
    <p>Convierte los 12V ruidosos del alternador (con picos de hasta 40V) en tensiones reguladas estables: 5,0V para sensores analógicos, 3,3V para el microcontrolador y 1,2V para el núcleo de cómputo.</p>
  </div>
  <div class="mag-card">
    <h4>Etapas Finales de Potencia</h4>
    <div class="sym">DRIVERS</div>
    <div class="ud">MOSFET / Smart Switches</div>
    <p>Transistores de efecto de campo en configuración High-Side (conmutación a positivo) o Low-Side (conmutación a masa) para activar inyectores, bobinas de encendido, electroválvulas y relés.</p>
  </div>
  <div class="mag-card">
    <h4>Transceptores de Bus</h4>
    <div class="sym">BUS IC</div>
    <div class="ud">CAN / LIN / FlexRay / SENT</div>
    <p>Chips de interfaz de línea física (ej. TJA1050, PCA82C250) que convierten los niveles lógicos del procesador a las tensiones diferenciales requeridas por las redes del vehículo (CAN_H / CAN_L).</p>
  </div>
</div>
""", prefix="../") + box("2. Composición Interna y Ciclo de Ejecución de la UCE", "calculate", r"""
<p>El funcionamiento de una centralita responde a un ciclo continuo de adquisición, procesamiento y actuación en tiempo real:</p>

""" + figura("figura_composicion_uce.png", "Composición funcional del sistema microprocesador de la UCE: acondicionamiento de entradas analógicas/digitales con convertidor A/D, microprocesador (Unidad de Control y Unidad Aritmético-Lógica UAL), buses de control/direcciones/datos, memorias RAM/ROM/EEPROM, convertidor D/A y etapas finales de potencia hacia los actuadores.", 4, prefix="../") + r"""

<h4>El Reloj Maestro y la Sincronización Temporal</h4>
<p>Todos los cálculos del microprocesador están sincronizados por una señal de reloj de onda cuadrada generada por un <strong>oscilador de cristal de cuarzo piezoeléctrico</strong>. La frecuencia de este cristal determina la velocidad de cálculo del procesador:</p>

""" + figura("foto_cristal_cuarzo_reloj.png", "Circuito oscilador de reloj maestro gobernado por cristal de cuarzo piezoeléctrico de 21.000 MHz (OSC1) con condensadores y resistencias de ajuste de compensación de fase.", 5, prefix="../") + r"""

<div class="callout aviso">
  <span class="cap">Verificación con Osciloscopio en Taller</span>
  <p>Cuando una centralita no enciende ni responde a la diagnosis en banco, uno de los primeros pasos obligatorios consiste en medir la señal del cristal oscilador con osciloscopio y sonda 10X. Si no existe una onda senoidal perfecta de la frecuencia nominal (ej. 21 MHz o 40 MHz), el procesador está en estado de reset continuo y nunca arrancará.</p>
</div>

<h4>Arquitecturas de Alta Fiabilidad: Redundancia y Multiprocesador</h4>
<p>En aplicaciones diésel de alta exigencia e inyección directa, los fabricantes han recurrido a arquitecturas multiprocesador donde varios microcontroladores cooperan en la misma placa, supervisándose mutuamente a través del bus interno:</p>

""" + figura("placa_uce_opel_triple_micro.png", "Arquitectura de alta fiabilidad en placa PCB: UCE diésel Opel Omega con disposición redundante de triple microordenador y osciladores de cuarzo independientes para control de inyección y supervisión de seguridad.", 6, prefix="../") + r"""
""", prefix="../") + box("3. Mapa de Memoria: RAM, ROM, Flash y EEPROM", "roadmap", r"""
<p>En el hardware de una centralita conviven cuatro tecnologías de memoria distintas, cada una con una misión específica:</p>

""" + figura("estructura_matriz_ram.png", "Estructura interna de la matriz de memoria de lectura/escritura RAM: celdas dinámicas formadas por transistor MOS de conmutación y condensador de almacenamiento de carga por celda binaria.", 7, prefix="../") + r"""

""" + figura("estructura_matriz_rom.png", "Estructura interna de una matriz de memoria de solo lectura ROM: matriz cruzada de líneas de dirección y columnas de datos interconectadas por diodos semiconductores permanentes.", 8, prefix="../") + r"""

<table class="tabla-curso">
  <thead>
    <tr>
      <th style="width:18%;">Tipo de Memoria</th>
      <th style="width:20%;">Volatilidad y Acceso</th>
      <th style="width:32%;">Contenido Almacenado</th>
      <th style="width:30%;">Referencias Típicas en Taller</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>RAM (SRAM)</strong></td>
      <td>Volátil (pierde datos al quitar alimentación KL30). Lectura/escritura ultrarrápida.</td>
      <td>Variables dinámicas de cálculo: régimen actual, temperatura de motor, corrección de riqueza Lambda a corto plazo y buffers de diagnosis.</td>
      <td>Integrada en el silicio del MCU (64 KB a 512 KB).</td>
    </tr>
    <tr>
      <td><strong>ROM / OTP</strong></td>
      <td>No volátil. Grabada en fábrica por máscara de silicio o fusible térmico irreversible (OTP).</td>
      <td>Código de arranque primario (<em>Bootloader de nivel 0</em>) y rutinas de inicialización de los buses de hardware. No se puede borrar ni reescribir.</td>
      <td>Bloque interno protegido de fábrica en MCU TriCore / ST10.</td>
    </tr>
    <tr>
      <td><strong>Flash (NOR)</strong></td>
      <td>No volátil. Re-escribible por bloques (sectores) eléctricamente mediante pulsos de programación.</td>
      <td><strong>Firmware del motor y cartografía completa:</strong> curvas de inyección, avance, presión de turbo, limitadores de par y tablas lambda. Es el objetivo principal de la reprogramación.</td>
      <td>AM29F400BT (512 KB), 28F200 (256 KB), Flash interna TriCore TC1796 (2 MB), TC1797 (4 MB), TC297 (8 MB).</td>
    </tr>
    <tr>
      <td><strong>EEPROM (Serie)</strong></td>
      <td>No volátil. Lectura y escritura byte a byte por bus SPI o I2C. Conserva datos durante más de 20 años sin batería.</td>
      <td><strong>Datos de personalización del vehículo:</strong> código secreto del inmovilizador (PIN), número de chasis (VIN), kilometraje, codificación IMA de inyectores y códigos de avería (DTCs).</td>
      <td>Chips SOIC-8 de 8 patillas: familias SPI 95080, 95160, 95320, 95640, 95128 y familias I2C 24C02, 24C04, 24C16.</td>
    </tr>
  </tbody>
</table>
""", prefix="../") + nav_block("01-arquitectura-hardware-ecu")


# ===============================================================
# TEMA 2: PROTOCOLOS Y MÉTODOS DE LECTURA Y FLASHEO
# ===============================================================
BODIES["02-metodos-lectura-escritura"] = box("1. Panorama General de Métodos de Acceso a la Memoria", "calculate", r"""
<p>Para leer el archivo original de una ECU o escribir una nueva calibración modificada, el electromecánico dispone de <strong>cuatro métodos de trabajo</strong> con niveles crecientes de invasividad y seguridad:</p>

""" + figura("diagrama_metodos_lectura.svg", "Árbol de decisión para seleccionar el método de lectura y escritura según el nivel de acceso y protección antituning.", 9, prefix="../") + r"""

""" + figura("herramientas_lectura_kess3_flex.png", "Equipamiento profesional de lectura y programación automotriz: Alientech KESS3, Magicmotorsport FLEX, Autotuner, caja Bench Box con adaptadores GPT/Tricore, New Genius y sondas de agujas pogo para marco de posicionamiento BDM.", 10, prefix="../") + r"""

<div class="mag-grid">
  <div class="mag-card">
    <h4>1. Puerto OBD-II / EOBD</h4>
    <div class="sym">OBD</div>
    <div class="ud">Sin desmontar la ECU</div>
    <p>Conexión directa a la toma de 16 pines del vehículo. Rapidez máxima (5-15 min). Solo lee la zona de calibración de mapas; no extrae la EEPROM completa.</p>
  </div>
  <div class="mag-card">
    <h4>2. Modo Banco (Bench Mode)</h4>
    <div class="sym">BENCH</div>
    <div class="ud">ECU extraída, sin abrir carcasa</div>
    <p>Conexión al conector exterior mediante cableado pinout y señales GPT. Permite clonación completa (Full Flash + EEPROM) sin peligro de rotura mecánica.</p>
  </div>
  <div class="mag-card">
    <h4>3. Bootloader / BDM</h4>
    <div class="sym">BOOT</div>
    <div class="ud">Carcasa abierta, contacto en PCB</div>
    <p>Conexión de sondas o resistencias a pines de arranque del procesador (TriCore Boot) o conector de depuración de 10-14 pines (BDM MPC5xx). Permite revivir centralitas bloqueadas.</p>
  </div>
  <div class="mag-card">
    <h4>4. Programador Directo</h4>
    <div class="sym">CHIP</div>
    <div class="ud">Lectura con pinza o desoldado</div>
    <p>Lectura directa de la EEPROM SOIC-8 o memoria Flash en programador universal (Dataman 48Pro2). Método definitivo para extracción de PIN o Immo-Off cuando el procesador está dañado.</p>
  </div>
</div>
""", prefix="../") + box("2. Lectura y Diagnóstico por Puerto Serie EOBD / OBD-II", "technology", r"""
<p>El estándar OBD-II utiliza protocolos de comunicación serie para transferir datos entre la interfaz de diagnosis y la centralita. Antes de intentar cualquier lectura de mapas, es imprescindible realizar una sesión de identificación del software:</p>

""" + figura("identificacion_ecu_diagnosis_edc15.png", "Identificación técnica de UCE por toma OBD-II: lectura de referencia de hardware/software Bosch 038 906 012 EM, familia EDC 15V y codificación de variantes en Seat Ibiza 1.9 SDI.", 11, prefix="../") + r"""

<p>Una vez identificada la referencia exacta del hardware y la versión del software, el equipo de flasheo inicia la sesión de transferencia de datos descargando la memoria Flash:</p>

""" + figura("lectura_obd2_eobd1250.png", "Secuencia de comunicación serie para identificación de software y lectura completa de volcado Flash por toma de diagnosis EOBD2 1250 de FG Technology.", 12, prefix="../") + r"""

<div class="callout alerta">
  <span class="cap">Regla de Oro en Lectura y Flasheo por OBD-II</span>
  <p>Durante la lectura o escritura por OBD-II, el electroventilador del motor puede activarse a máxima velocidad por protocolo de seguridad de la ECU, provocando una caída drástica de tensión. Es <strong>estrictamente obligatorio conectar un estabilizador de taller de 70 A a 100 A</strong> que mantenga la batería entre 13,8 V y 14,4 V constantes durante todo el proceso. Una caída por debajo de 12,0 V durante la fase de borrado del sector dejará la centralita completamente bloqueada (<em>bricked</em>).</p>
</div>
""", prefix="../") + box("3. Bench Mode (GPT), Bootloader Tricore y Programadores Universales", "experiment", r"""
<p>Cuando una centralita incorpora protección <strong>antituning (TPROT)</strong> a nivel de procesador, el puerto OBD bloquea las solicitudes de flasheo no autorizadas. En este escenario, el método preferente en el taller es el <strong>Modo Banco (Bench Mode)</strong> con sincronización por pines GPT (<em>General Purpose Timer</em>):</p>

<ul class="ra-list">
  <li><strong>Sincronización GPT:</strong> La herramienta emite pulsos de frecuencia calibrada por dos pines de sensores del conector exterior. El microcontrolador Infineon TriCore valida estos pulsos y conmuta a modo de servicio de fábrica sin necesidad de abrir la carcasa de aluminio sellada.</li>
  <li><strong>Extracción Full Backup:</strong> Bench Mode permite leer de forma íntegra la memoria Flash interna (Micro Flash), la Flash externa (si existe) y la memoria EEPROM física o emulada, permitiendo la clonación perfecta 1:1 de la ECU.</li>
</ul>

<h4>Programación Directa de Memorias con Estación Dataman 48Pro2</h4>
<p>En casos de recuperación de módulos dañados por agua, sobretensión o clonaciones complejas donde el procesador central ha quedado inoperativo, la lectura física del chip de memoria EEPROM o Flash es el único camino viable:</p>

""" + figura("lectura_eeprom_clip_dataman48pro2.png", "Estaciones de lectura y programación de memorias: (a) Pinza SOIC-8 clip pogo de lectura rápida sobre placa sin desoldar, (b) Zócalo de inserción nula (ZIF) de programador BeeProg2, (c) Estación universal de programación Dataman 48Pro2 (www.dataman.com) con zócalo ZIF de 48 pines y conectores ISP para lectura de EEPROM y Flash de automoción.", 13, prefix="../") + r"""

<div class="callout nota">
  <span class="cap">Ventajas Técnicas del Programador Dataman 48Pro2 (www.dataman.com)</span>
  <p>La estación universal <strong>Dataman 48Pro2</strong> incorpora 48 terminales independientes universales (<em>pin-drivers</em>) con capacidad de comprobación automática de continuidad de patillas (<em>pin continuity check</em>) antes de iniciar cualquier operación. Esto evita corrupciones accidentales si una de las patillas del chip SOIC-8 presenta restos de laca o mal contacto. Además, admite programación en circuito (ISP) para leer la memoria directamente sobre la placa sin desoldar.</p>
</div>
""", prefix="../") + nav_block("02-metodos-lectura-escritura")


# ===============================================================
# TEMA 3: REPROGRAMACIÓN DE MAPAS Y CHECKSUM
# ===============================================================
BODIES["03-modificacion-mapas-checksum"] = box("1. Cartografía Motor: Organización y Localización en Memoria Flash", "roadmap", r"""
<p>El archivo binario (volcado crudo .bin u .ori) extraído de la memoria Flash contiene dos partes fundamentales: el <strong>código ejecutable del sistema operativo del motor</strong> y el <strong>bloque de calibración (datos de mapas)</strong>. Los mapas son matrices matemáticas de consulta (<em>lookup tables</em>) que relacionan las variables de entrada con las decisiones de control del actuador:</p>

""" + figura("diagrama_mapa_3d_inyeccion.svg", "Estructura matemática tridimensional de un mapa de inyección en función del régimen de giro (RPM) y la carga del motor.", 14, prefix="../") + r"""

<p>Para localizar, visualizar y modificar estos mapas en un archivo binario, el software estándar por excelencia en la industria automotriz mundial es <strong>EVC WinOLS</strong> (<a href="https://www.evc.de/" target="_blank" rel="noopener">www.evc.de</a>):</p>

""" + figura("winols_visualizacion_hex_2d_3d.png", "Entorno de ingeniería de calibración EVC WinOLS (www.evc.de): visualización sincronizada en volcado hexadecimal/decimal crudo, modo gráfico lineal 2D y representación de superficie tridimensional 3D con reconocimiento de ejes.", 15, prefix="../") + r"""

<h4>El Mosaico de Mapas Principales en una Centralita Diésel / Gasolina</h4>
<p>Una calibración profesional requiere entender la interdependencia entre los distintos mapas de gestión de par y alimentación:</p>

""" + figura("coleccion_mapas_3d_winols.png", "Mosaico de mapas tridimensionales característicos en EVC WinOLS: mapa de límite de par, inyección básica de arranque, presión de raíl Common Rail, avance de inyección/encendido, presión absoluta de turbo y mapa de humos/factor lambda.", 16, prefix="../") + r"""

<div class="mag-grid">
  <div class="mag-card">
    <h4>Deseo del Conductor (Driver Wish)</h4>
    <div class="sym">DW</div>
    <div class="ud">Ejes: RPM vs Posición Pedal (%)</div>
    <p>Convierte el recorrido físico del pedal del acelerador en una demanda de par motor expresada en Newton-metro (Nm) o caudal de combustible (mg/carrera).</p>
  </div>
  <div class="mag-card">
    <h4>Limitador de Par (Torque Limiter)</h4>
    <div class="sym">TL</div>
    <div class="ud">Ejes: RPM vs Presión Atmosférica</div>
    <p>Curva de seguridad mecánica y térmica que limita el par máximo del motor para proteger la caja de cambios, embrague, bielas y pistones.</p>
  </div>
  <div class="mag-card">
    <h4>Mapa de Humos / Lambda</h4>
    <div class="sym">SMOKE</div>
    <div class="ud">Ejes: RPM vs Masa de Aire (MAF mg/h)</div>
    <p>Limita el combustible máximo inyectable en función del aire admitido por el motor para evitar emisiones de partículas visibles y exceso de hollín.</p>
  </div>
  <div class="mag-card">
    <h4>Presión de Sobrealimentación (Turbo)</h4>
    <div class="sym">BOOST</div>
    <div class="ud">Ejes: RPM vs Caudal Combustible (mg)</div>
    <p>Fija la presión absoluta de soplado del turbocompresor en hectopascales (hPa) y regula la válvula de geometría variable (VNT / wastegate).</p>
  </div>
</div>

<h4>Detalle de Curva 2D: Limitador de Par Motor</h4>
<p>La vista bidimensional lineal en WinOLS permite comprobar con precisión micrométrica la forma de la curva y verificar que no existan discontinuidades abruptas que generen tirones o sobrepresiones destructivas:</p>

""" + figura("winols_curva_2d_limite_par.png", "Curva analítica 2D en WinOLS del mapa limitador de par motor en función del régimen de giro (RPM) y límite térmico de caudal.", 17, prefix="../") + r"""
""", prefix="../") + box("2. El Algoritmo Checksum (Suma de Verificación) y Bloqueo Antituning", "calculate", r"""
<p>El <strong>Checksum</strong> es un valor matemático de control criptográfico calculado a partir de la suma ponderada de todos los bytes contenidos en los bloques de memoria Flash. Su finalidad principal en la automoción es garantizar la <strong>integridad de los datos</strong> contra ruidos electromagnéticos o corrupciones en memoria.</p>

<div class="callout alerta">
  <span class="cap">Peligro Crítico: Checksum Incorrecto = Bloqueo Irreversible</span>
  <p>Cuando se modifica aunque sea un solo bit en un mapa de potencia (ej. aumentar el tiempo de inyección en un 5%), el Checksum matemático de la Flash cambia por completo. Si se graba el archivo modificado en la centralita sin haber recalculado previamente el Checksum, la rutina de arranque del microcontrolador detectará una discrepancia matemática en la verificación inicial (KL15) y <strong>bloqueará el procesador impidiendo el arranque del vehículo</strong>.</p>
</div>

<h4>Mecanismo de Recálculo Automático</h4>
<p>En la práctica profesional moderna, el cálculo del Checksum nunca se realiza de forma manual debido a su extrema complejidad (algoritmos RSA, polinomios CRC32 y firmas digitales en familias Bosch EDC17/MED17 y MD1/MG1). Se emplean dos mecanismos:</p>
<ul class="ra-list">
  <li><strong>Plugins de Checksum en WinOLS:</strong> Módulos software desarrollados por EVC Electronic que identifican automáticamente la familia de la ECU al guardar el archivo y actualizan los bloques de verificación correspondientes.</li>
  <li><strong>Recálculo en Flasheo por Hardware:</strong> Interfaces profesionales como KESS3 o FLEX analizan el archivo en tiempo real durante la fase previa de flasheo y corrigen el Checksum automáticamente sobre la marcha.</li>
</ul>
""", prefix="../") + box("3. Recursos de Calibración: EVC Electronic y Dataman Programmers", "objectives", r"""
<p>El trabajo riguroso en ingeniería de centralitas requiere apoyarse en las herramientas estándar del sector y en la documentación técnica oficial:</p>

""" + figura("enlaces_web_evc_dataman_qr.png", "Accesos directos y códigos QR a los portales tecnológicos de referencia: EVC Electronic (www.evc.de) para software WinOLS, módulos de Checksum y bases de datos Damos, y Dataman Programmers (www.dataman.com) para estaciones universales de hardware y adaptadores de zócalo.", 18, prefix="../") + r"""

<div class="mag-grid">
  <div class="mag-card">
    <h4>EVC Electronic (www.evc.de)</h4>
    <div class="sym">EVC</div>
    <div class="ud">Estándar Industrial Alemán</div>
    <p>Desarrollador de <strong>WinOLS</strong>, simuladores de memoria OLS300/OLS501 y archivos de definición oficial <strong>DAMOS / ASAP2 (A2L)</strong>, que contienen los nombres reales de los ejes, factores de conversión y fórmulas físicas de cada variable.</p>
  </div>
  <div class="mag-card">
    <h4>Dataman Programmers (www.dataman.com)</h4>
    <div class="sym">DATAMAN</div>
    <div class="ud">Equipos de Laboratorio y Microelectrónica</div>
    <p>Líder internacional en programadores universales de chips de 48 pines (<strong>Dataman 48Pro2</strong>), adaptadores BGA/TSOP/SOIC de alta precisión y software de lectura hexadecimal con comprobación de integridad eléctrica pin a pin.</p>
  </div>
</div>
""", prefix="../") + nav_block("03-modificacion-mapas-checksum")


# ===============================================================
# TEMA 4: DIAGNÓSTICO FÍSICO Y REPARACIÓN EN BANCO
# ===============================================================
BODIES["04-diagnostico-reparacion-hardware"] = box("1. Equipamiento del Puesto de Trabajo Electrónico", "experiment", r"""
<p>La reparación física de averías internas en una centralita requiere un puesto de laboratorio debidamente acondicionado y aislado del polvo y grasas del taller mecánico general:</p>

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

<h4>Anatomía Clásica de Centralitas Bosch con Memoria EPROM UV</h4>
<p>El conocimiento de la evolución de las centralitas permite entender la disposición de los buses de datos y las etapas de potencia desde las primeras inyecciones electrónicas hasta los sistemas modernos:</p>

""" + figura("despiece_centralita_bosch_eprom_uv.png", "Despiece y anatomía constructiva de centralita Bosch clásica: encapsulado de memoria EPROM con ventana de cuarzo para borrado por luz ultravioleta (UV), búferes de interfaz de bus de datos y microprocesador central.", 19, prefix="../") + r"""
""", prefix="../") + box("2. Diagnóstico y Reparación de las Averías Más Frecuentes en Placa", "case", r"""
<p>En el taller de automoción, más del 80% de los fallos de hardware en UCEs se concentran en 5 patrones de avería perfectamente diagnosticables:</p>

""" + figura("diagrama_circuito_reparacion_5v.svg", "Esquema del circuito regulador de 5V de sensores y protocolo de comprobación en banco ante cortocircuitos externos.", 20, prefix="../") + r"""

<h4>Inspección a Doble Cara en Placas Bosch</h4>
<p>Las placas de centralitas modernas montan componentes en ambas caras para maximizar la densidad de integración y disipar el calor hacia el chasis metálico:</p>

""" + figura("placa_uce_bosch_ambas_caras.png", "Inspección y diagnóstico a doble cara de placa PCB Bosch: cara superior con microcontrolador, oscilador de cuarzo y transistores MOSFET de potencia; cara inferior con memoria serie EEPROM SOIC-8 y condensadores de desacoplo SMD.", 21, prefix="../") + r"""

<h4>Protocolo de Reparación de las 5 Averías Frecuentes</h4>
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
""", prefix="../") + box("3. Sistemas Inmovilizadores, Clonación y Desinmovilización (Immo-Off)", "technology", r"""
<p>El sistema inmovilizador electrónico impide el arranque no autorizado del vehículo mediante un intercambio criptográfico entre la llave del conductor y la centralita motor:</p>

""" + figura("sistema_inmovilizador_citroen.png", "Esquema general del sistema inmovilizador de automoción: llave con transponder de radiofrecuencia (RFID), bobina antena en bombín de contacto, UCE de gestión motor / módulo inmovilizador y electroválvula o relé de corte de inyección.", 22, prefix="../") + r"""

<h4>Identificación de la Memoria EEPROM del Inmovilizador</h4>
<p>En muchas centralitas de inyección de gasolina y diésel, los datos del inmovilizador no residen en la Flash del procesador, sino en un chip EEPROM serie independiente de 8 patillas:</p>

""" + figura("placa_uce_gasolina_eeprom_inmo.png", "Placa de circuito de UCE de gasolina: diferenciación física entre la memoria de gestión de motor y la memoria EEPROM de 8 pines dedicada a los códigos del sistema inmovilizador.", 23, prefix="../") + r"""

<h4>Comparativa con Módulos de Seguridad y Airbag</h4>
<p>El tratamiento de memorias en centralitas de seguridad pasiva (Airbag) comparte metodología con las UCE de motor, requiriendo la lectura de EEPROM para el borrado de datos de impacto (<em>crash data clear</em>):</p>

""" + figura("placas_uce_airbag_y_nissan.png", "Disposición de módulos auxiliares y de seguridad: placa de UCE de airbag con condensadores electrolíticos de reserva de energía para disparo pirotécnico y acelerómetro de impacto, junto a placa de UCE de gestión de motor Nissan.", 24, prefix="../") + r"""
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
    <div class="sym">J2534-1</div>
    <div class="ud">Reprogramación de Emisiones</div>
    <p>Estándar base obligatorio que cubre la reprogramación de cualquier módulo relacionado con emisiones (ECU de motor y TCM de caja de cambios automática).</p>
  </div>
  <div class="mag-card">
    <h4>SAE J2534-2</h4>
    <div class="sym">J2534-2</div>
    <div class="ud">Módulos de Carrocería y Confort</div>
    <p>Extensión avanzada para telecarga y codificación de módulos de carrocería (BCM), frenos (ABS/ESP), dirección asistida, cuadro y unidades multimedia.</p>
  </div>
</div>

""" + figura("diagrama_instalacion_passthru.svg", "Esquema de conexión para reprogramación Pass-Thru en taller con estabilizador de tensión y portal oficial OEM.", 25, prefix="../") + r"""

<h4>Condiciones Obligatorias de Taller para Telecarga Pass-Thru</h4>
<ul class="ra-list">
  <li><strong>Estabilizador de Tensión Grado Taller (70 A - 100 A):</strong> Una telecarga oficial OEM puede prolongarse de 20 minutos a más de 1 hora. Durante este tiempo, la bomba de combustible, ventiladores y centralitas secundarias permanecen activas, consumiendo entre 25 A y 50 A. El estabilizador debe mantener la red entre 13,8 V y 14,4 V sin rizado ni oscilaciones.</li>
  <li><strong>Conexión a Internet Robusta por Cable Ethernet:</strong> Prohibido terminantemente el uso de redes Wi-Fi inestables. Si la conexión se interrumpe durante la descarga o validación del certificado digital, el proceso puede abortar en plena escritura.</li>
  <li><strong>Interfaz VCI Homologada:</strong> Uso de cabezales compatibles de alta calidad (Bosch KTS 560/590, DrewTech CarDAQ-Plus 3, Actia PassThru XS 2G).</li>
  <li><strong>Portales Oficiales de Fabricante:</strong> Registro profesional en portales oficiales (VAG erWin, BMW AOS, Mercedes B2B Connect, Ford FDRS, Stellantis) con adquisición de suscripciones por horas o por sesión de vehículo.</li>
</ul>
""", prefix="../") + nav_block("05-normativa-pass-thru-j2534")


# ===============================================================
# TEMA 6: CASOS PRÁCTICOS DE TALLER PASO A PASO
# ===============================================================
BODIES["06-casos-practicos-taller"] = box("1. Caso Práctico 1: Clonación de ECU Bosch EDC17C64 en Banco (Bench Mode)", "case", r"""
<h4>Vehículo: Volkswagen Golf VII 2.0 TDI (Centralita quemada por cortocircuito externo)</h4>
<ol class="pasos-taller">
  <li><strong>Fase 1: Conexión en Banco sin abrir la carcasa.</strong> Identificar el pinout del conector exterior de la ECU EDC17C64 en el software de la herramienta (FLEX o KESS3). Conectar alimentación (+12V permanente, +12V bajo contacto KL15, masa GND), línea CAN-High (pin 67), línea CAN-Low (pin 68) y los dos canales de sincronización GPT (GPT1 y GPT2).</li>
  <li><strong>Fase 2: Lectura del Backup Completo de la ECU Original.</strong> Alimentar a 13,5 V y ejecutar la lectura en Modo Bench. El software sincroniza las frecuencias GPT y descarga tres archivos: Micro Flash interna (TC1797, 4 MB), Flash externa (si existe) y memoria EEPROM (donde residen los datos del inmovilizador, bastidor y codificación).</li>
  <li><strong>Fase 3: Volcado en la ECU de Desguace (Donante).</strong> Conectar la centralita donante con la misma referencia de hardware Bosch (0 281 xxx xxx). Realizar la escritura completa del archivo Micro Flash y EEPROM de la unidad original. El software adapta automáticamente la firma digital y el Checksum.</li>
  <li><strong>Fase 4: Verificación en Vehículo.</strong> Montar la ECU clonada en el vehículo. Realizar diagnosis completa con VCDS u ODIS. Borrar DTCs esporádicos y verificar el arranque inmediato del motor sin parpadeo del testigo de inmovilizador.</li>
</ol>
""", prefix="../") + box("2. Caso Práctico 2: Reparación de Regulador de 5V y Línea en Corto en Delphi DCM3.7", "experiment", r"""
<h4>Vehículo: Kia Sportage 1.7 CRDi (Avería: DTC P0642 - Tensión de referencia del sensor A baja)</h4>
<ol class="pasos-taller">
  <li><strong>Diagnóstico Previo en Vehículo:</strong> Medir tensión con multímetro en el sensor de presión de raíl y sensor MAP. Se registra 0,42 V en lugar de los 5,00 V preceptivos. Al desconectar todos los sensores del motor, la tensión no sube, confirmando que la avería reside dentro de la ECU o en el mazo.</li>
  <li><strong>Comprobación en Banco:</strong> Conectar la ECU Delphi en la fuente de laboratorio limitando la corriente a 300 mA. Medir la resistencia entre la salida de 5V de sensores y masa: el multímetro pita marcando 2,1 Ω (cortocircuito franco).</li>
  <li><strong>Localización Térmica:</strong> Con la fuente alimentando a 12V, enfocar la placa con la cámara termográfica. El circuito integrado regulador de tensión multipin se calienta instantáneamente a 75 °C mientras el resto de la placa permanece a 22 °C.</li>
  <li><strong>Procedimiento de Rework SMD:</strong> Aplicar flux en pasta en las patillas del integrado. Con la tobera circular de aire caliente a 360 °C y caudal medio, calentar de forma homogénea durante 35 segundos hasta la fusión del estaño. Retirar con pinzas de vacío.</li>
  <li><strong>Limpieza y Montaje:</strong> Limpiar los pads con malla de desoldar y alcohol isopropílico. Posicionar el chip regulador nuevo (recambio original), aplicar flux líquido y soldar patilla a patilla con soldador de punta fina a 340 °C. Verificar la impedancia de salida (> 10 kΩ) y alimentar: la línea entrega 5,02 V estables.</li>
</ol>
""", prefix="../") + nav_block("06-casos-practicos-taller")


# ===============================================================
# TEMA 7: MEDIATECA TÉCNICA: RECURSOS AUDIOVISUALES
# ===============================================================
BODIES["07-mediateca-tecnica"] = box("1. Demostraciones Prácticas de Taller en Vídeo (YouTube Verificados)", "video", r"""
<p>Selección de recursos audiovisuales técnicos y demostraciones verificadas en laboratorio automotriz para afianzar los procedimientos de programación y reparación:</p>

""" + video_embed("en3G5PQPeXc", "Lectura y Escritura de ECU en Banco (Bench Mode) con Alientech KESS3", "Demostración práctica paso a paso del conexionado de pines de alimentación (+12V, GND), línea de comunicación CAN High/Low y pines de sincronización GPT en una centralita Bosch EDC17CP44 sin necesidad de abrir la carcasa de aluminio.", "ReproRACE - Formación Técnica", "Demostración Bench", "#2563eb") + r"""

""" + video_embed("0GdRhVLkLPM", "WinOLS para Principiantes: Localización e Interpretación de Mapas 2D y 3D", "Guía profesional sobre el uso del software estándar de la industria EVC WinOLS (www.evc.de). Métodos de búsqueda de curvas de inyección, reconocimiento visual de mapas en 2D, interpretación de ejes X/Y y representación tridimensional 3D.", "High Performance Academy (HPA)", "Calibración WinOLS", "#059669") + r"""

""" + video_embed("F1S3lB2_N2k", "Procedimiento de Reprogramación Pass-Thru (SAE J2534) en Taller", "Configuración de una interfaz VCI Pass-Thru universal (Drew Technologies CarDAQ), conexión al puerto OBD-II, puesta en marcha del estabilizador de taller y proceso de flasheo oficial de firmware OEM.", "Drew Technologies / Opus IVS", "Pass-Thru J2534", "#d97706") + r"""

""" + video_embed("-MUyW6gUB8o", "Técnicas Profesionales de Soldadura y Desoldadura SMD en Placas de Automoción", "Manejo de estación de soldadura con aire caliente a temperatura controlada, aplicación de flux no-clean, desoldado con pinzas de vacío y microsoldadura de circuitos integrados SOIC-8 y QFP sin dañar pistas.", "SDG Electronics / Laboratorio", "Taller de Soldadura", "#dc2626") + r"""

""" + video_embed("2IuZa-357zQ", "Diagnóstico de Centralitas en Banco con Trazador de Curvas y Osciloscopio", "Procedimiento avanzado de localización de averías en banco mediante trazador de curvas por componentes y osciloscopio digital. Comprobación de líneas de excitación de inyectores y bobinas.", "ElectroAuto Training", "Diagnosis en Banco", "#7c3aed") + r"""
""", prefix="../") + box("2. Módulos Audiovisuales de Referencia Autodata Training (Taller / Aula)", "competencies", r"""
<p>Guía de estudio técnico para los módulos audiovisuales oficiales de Autodata Training disponibles en el archivo local de la mediateca del taller (<code>H:\0-TRAINING\Autodata_Videos\módulos de control/</code>):</p>

""" + autodata_card(
    "cj50cas",
    "Principios de Control de Módulos y Divisores de Tensión",
    "Fundamentos del control electrónico en automoción: divisores resistivos para lectura analógica de sensores de posición y temperatura, multiplexado de señales, y conmutación de etapas de potencia mediante relés de 4 clavijas y transistores.",
    [
        "Funcionamiento de los divisores resistivos en la lectura de sensores NTC y potenciómetros.",
        "Diagnóstico de caída de tensión en contactos de relé y conmutadores.",
        "Interpretación de los estados lógicos de control en módulos electrónicos del vehículo."
    ],
    "12 min 30 s",
    "Los módulos de control dependen de una alimentación precisa y constante. Cuando analizamos las entradas analógicas, el microprocesador utiliza una red de resistencias en divisor de tensión para convertir las variaciones de resistencia del sensor en una señal de tensión medible por el convertidor analógico-digital..."
) + r"""

""" + autodata_card(
    "jc75cas",
    "Circuitos Elevadores y Reductores (Pull-Up y Pull-Down)",
    "Comprobación de líneas de tensión de referencia de 5V y polarización de señales en sensores de régimen, fase y posición. Protocolos de comprobación de cableado y detección de cortocircuitos a positivo o masa.",
    [
        "Diferenciación práctica entre circuitos Pull-Up (resistencia a 5V/12V) y Pull-Down (resistencia a masa).",
        "Métodos de comprobación de la línea de 5V de referencia con multímetro y osciloscopio.",
        "Identificación de averías cuando la señal se queda flotante por rotura de resistencia de polarización."
    ],
    "14 min 15 s",
    "Un circuito Pull-Up mantiene una línea de entrada digital en nivel lógico alto mientras el interruptor o sensor de efecto Hall está abierto. Al cerrarse, la línea cae a masa. Si la resistencia interna de la ECU se abre, la señal quedará en un nivel indefinido..."
) + r"""

""" + autodata_card(
    "jc85cas",
    "Lógica Interna y Detección de Averías en Módulos de Control",
    "Arquitectura interna de conmutación de módulos, accionadores High-Side y Low-Side, y sistemas de protección electrónica activa sin fusibles basados en la detección de corriente por shunts y transistores inteligentes.",
    [
        "Conmutación por el lado positivo (High-Side) vs conmutación por el lado de masa (Low-Side).",
        "Sistemas de protección térmica y de sobrecorriente que sustituyen a los fusibles tradicionales.",
        "Diagnóstico de drivers inteligentes y lectura de códigos de avería de circuito abierto o cortocircuito."
    ],
    "15 min 40 s",
    "Las unidades de control modernas prescinden de fusibles individuales en muchos de sus circuitos de salida. En su lugar, incorporan transistores de efecto de campo inteligentes que monitorizan la corriente que fluye a través de ellos..."
) + r"""

""" + autodata_card(
    "et00cas",
    "Reprogramación Pass-Thru SAE J2534 y Calibración OEM",
    "Procedimiento integral de reprogramación oficial mediante interfaces Pass-Thru J2534 y servidores en la nube de los fabricantes de automóviles. Diferenciación entre firmware base y calibración de mapas, y requisitos de alimentación estabilizada.",
    [
        "Marco normativo Euro 5 y Euro 6 para el acceso independiente a telecargas de software.",
        "Conexión paso a paso del interfaz J2534 entre el PC del taller, la toma OBD-II y el servidor OEM.",
        "Protocolo obligatorio de estabilización de tensión: mantenimiento estricto entre 13,8 V y 14,4 V durante todo el proceso."
    ],
    "18 min 20 s",
    "El estándar SAE J2534 define una capa de abstracción entre el software del fabricante del vehículo y el hardware del interfaz de diagnosis. Durante el proceso de telecarga, cualquier fluctuación de tensión por debajo de 12,0 V puede interrumpir la escritura en la memoria Flash..."
) + r"""
""", prefix="../") + box("3. Centros de Referencia Oficiales y Enlaces a Portales Industriales", "roadmap", r"""
<p>Consulte las herramientas, documentación y especificaciones oficiales en los portales de referencia del sector:</p>

""" + figura("enlaces_web_evc_dataman_qr.png", "Accesos directos y códigos QR a los portales tecnológicos de referencia: EVC Electronic (www.evc.de) para software WinOLS, módulos de Checksum y bases de datos Damos, y Dataman Programmers (www.dataman.com) para estaciones universales de hardware y adaptadores de zócalo.", 26, prefix="../") + r"""

<div class="mag-grid">
  <div class="mag-card">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
      <img src="../content/img/logo_evc.png" alt="Logo EVC Electronic" style="height:32px;width:auto;">
      <h4 style="margin:0;">EVC Electronic</h4>
    </div>
    <div class="ud">Alemania · <a href="https://www.evc.de/" target="_blank" rel="noopener">www.evc.de</a></div>
    <p>Empresa de referencia mundial para la ingeniería de calibración de software motor. Desarrolladora de <strong>WinOLS</strong>, módulos de recálculo matemático de Checksum para más de 100 familias de centralitas, y base de datos de calibración con archivos Damos y proyectos ASAM MCD 2MC (A2L).</p>
  </div>
  <div class="mag-card">
    <h4>Dataman Programmers</h4>
    <div class="ud">Reino Unido / USA · <a href="https://www.dataman.com/" target="_blank" rel="noopener">www.dataman.com</a></div>
    <p>Fabricante especializado en programadores universales de chips de grado industrial y automotriz. Su modelo <strong>Dataman 48Pro2</strong> es la herramienta de referencia para lectura, copia y clonación directa de memorias Flash y EEPROM (SPI, I2C, Microwire, Paralelas) en laboratorio.</p>
  </div>
</div>
""", prefix="../") + nav_block("07-mediateca-tecnica")


# ---------------------------------------------------------------------------
# 2. MOTOR DE EVALUACIÓN INTERACTIVA (TEST ALEATORIO 20/50 PREGUNTAS)
# ---------------------------------------------------------------------------
with open(os.path.join(os.path.dirname(__file__), "quiz_engine.html"), "r", encoding="utf-8") as _f:
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
