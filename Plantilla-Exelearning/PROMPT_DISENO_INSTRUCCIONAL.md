# Guía y Prompt de Diseño Instruccional eXeLearning para Formación Profesional (EducaMadrid / Moodle)

Este documento contiene la especificación y el **prompt maestro** de diseño instruccional para la creación y generación de unidades didácticas técnicas en Formación Profesional (Grado Medio y Superior), garantizando la compatibilidad total con el estándar **SCORM 1.2** y el registro automático de calificaciones en el Aula Virtual de **EducaMadrid (Moodle)**.

---

## 📋 Prompt Maestro de Diseño Instruccional

> **Instrucciones para el docente, diseñador o asistente de IA:**  
> Copia y utiliza el siguiente bloque de texto sustituyendo los campos entre corchetes con los datos específicos de tu módulo o unidad formativa.

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

## 🛠️ Fundamentos Técnicos del Registro de Calificaciones en Moodle

### 1. ¿Por qué solo debe calificar la "Evaluación Final"?
* En los paquetes SCORM multi-página generados con eXeLearning, **cada página actúa como un SCO**.
* Si se insertan actividades evaluables en páginas intermedias, se produce una **colisión de variables** `cmi.core.score.raw` en Moodle, sobrescribiéndose las notas de unas páginas con otras según el orden de navegación del alumno.
* **Regla de oro:** Las páginas intermedias deben contener explicaciones (iDevice *Texto*) y preguntas de autoevaluación formativa (sin comunicación de nota SCORM). La calificación oficial de la unidad debe reservarse **exclusivamente en la página final denominada `Evaluación Final`**.

### 2. Calificación en Escala sobre 10 vs Escala sobre 100
* En el sistema educativo español y en Formación Profesional (EducaMadrid), las calificaciones oficiales se expresan en **escala decimal de 0 a 10** (aprobado con 5,0).
* La plantilla está configurada por defecto con `SCORE_SCALE = 10`. Al enviar la nota mediante `cmi.core.score.raw` y `cmi.core.score.max = 10`, Moodle traslada directamente la nota exacta al Libro de Calificaciones sin distorsiones ni redondeos extraños.
* En el manifiesto `imsmanifest.xml`, se declara automáticamente `<adlcp:masteryscore>5</adlcp:masteryscore>` para la Evaluación Final, garantizando que el parámetro de Moodle *"El puntaje de dominio anula el estado"* evalúe el corte aprobado/suspenso con total coherencia.

### 3. Evitar el Estado "No intentado" (Not Attempted)
* La plantilla 2026 inicializa la sesión en cuanto el alumno entra a la página como `"incomplete"`, impidiendo que el intento quede congelado como `"not attempted"`.
* La página de evaluación incorpora el botón **`💾 Confirmar y Guardar Calificación Oficial`**, que ejecuta `LMSCommit` y `LMSFinish` de forma segura antes de cerrar el navegador, evitando la pérdida de datos provocada por el cierre involuntario de pestañas.

---

## ⚙️ Ajustes Obligatorios de la Actividad en EducaMadrid / Moodle

Al añadir el archivo `.zip` en tu curso del Aula Virtual:
1. **Apariencia**:
   * **Visualización del paquete**: `En la página actual` (evita ventanas emergentes bloqueadas por el navegador).
2. **Calificación**:
   * **Método de calificación**: `Calificación más alta`.
   * **Calificación máxima**: `10` (coincidente con la escala de Formación Profesional).
3. **Ajustes de compatibilidad**:
   * **El puntaje de dominio anula el estado**: Dejar en `Sí` (coincide con el mastery score de 5 sobre 10) o marcar `No` si se desea computar la superación por lectura.
4. **Finalización de actividad**:
   * Seleccionar: *Mostrar la actividad como completada cuando se cumplan las condiciones*.
   * Marcar: **`Requerir estado: Pasado`** y **`Requerir estado: Completado`**.
