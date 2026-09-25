---
name: exelearning-builder
description: >-
  Crea, redacta, maqueta y compila cursos interactivos en formato SCORM 1.2
  compatibles al 100% con eXeLearning y validados para Moodle y EducaMadrid.
  Úsalo cuando el usuario solicite crear un curso nuevo, convertir apuntes o PDFs a SCORM,
  diseñar cuestionarios de autoevaluación o compilar paquetes SCORM listos para el aula virtual.
---

# Generador de Cursos eXeLearning SCORM 1.2

Este skill permite a Antigravity crear cursos interactivos completos empaquetados en SCORM 1.2 con validación automática y firmas XML auténticas (`content.xml`, `content.dtd`, `imslrm.xml`, `imsmanifest.xml`).

---

## Flujo de Trabajo Paso a Paso

### 1. Inicializar la Estructura del Curso
Cuando el usuario pida crear un nuevo curso (por ejemplo, `Curso-Seguridad-Digital`):
1. Determina la carpeta de trabajo del curso.
2. Copia la plantilla base ubicada en el directorio de recursos de este skill:
   `resources/Plantilla-Exelearning/`
   hacia la carpeta destino del curso:
   ```bash
   cp -r "<ruta_al_skill>/resources/Plantilla-Exelearning" "<ruta_del_curso>"
   ```
   *(Si el usuario ya está dentro de una carpeta de curso con `course_spec.py` y `build.py`, trabaja directamente sobre ella).*

---

### 2. Redactar y Maquetar `course_spec.py`
Edita el archivo `course_spec.py` del curso siguiendo las directrices pedagógicas:

1. **Metadatos Generales (`COURSE`)**:
   - `id`: Identificador alfanumérico sin espacios (ej. `seguridad_digital_01`).
   - `title`: Título formal del curso.
   - `description`: Resumen pedagógico del curso.
   - `author`: Nombre del autor o institución.
   - `lang`: Código de idioma (`es`).
   - `license`: Licencia (ej. `Creative Commons BY-SA 4.0`).

2. **Estructura de Temas (`PAGES`)**:
   - Lista ordenada de tuplas `(slug, titulo)`.
   - La primera página SIEMPRE debe ser `("index", "Portada / Inicio")`.
   - Ejemplo:
     ```python
     PAGES = [
         ("index", "Inicio del Curso"),
         ("unidad-1", "1. Fundamentos y Normativa"),
         ("unidad-2", "2. Medidas Preventivas"),
         ("evaluacion", "Autoevaluación Final"),
     ]
     ```

3. **Contenido de las Páginas (`BODIES`)**:
   - Utiliza la función `box(titulo, icono, contenido_html, prefix)` de `gen_common`:
     - En `index`: `prefix=""`
     - En páginas interiores: `prefix="../"`
   - Usa cajas informativas estructuradas:
     ```html
     <div class="callout nota">
       <span class="cap">Nota Técnica</span>
       <p>Información relevante para el alumno.</p>
     </div>
     ```
   - Agrega bloques de navegación al final de cada página con `nav_block(slug)`.

4. **Fórmulas Matemáticas**:
   - Si el tema incluye matemáticas o física, usa delimitadores TeX estándar: `\( v = \frac{d}{t} \)` o `\[ W = F \cdot d \]`.

5. **Cuestionario Final SCORM (`PREGUNTAS`, `PASS` y `RANDOMIZE_OPTIONS`)**:
   - **Distribución aleatoria obligatoria**: Las respuestas correctas (`correct`) DEBEN repartirse de forma variada y equilibrada entre las distintas posiciones (0 = A, 1 = B, 2 = C, 3 = D). **NUNCA** pongas la respuesta correcta siempre en la primera opción (`correct: 0`) ni sigas secuencias monótonas.
   - El motor `quiz_engine.html` soporta `RANDOMIZE_OPTIONS = true;` (activo por defecto), barajando las opciones aleatoriamente en cada intento del alumno. Si alguna pregunta requiere mantener el orden de sus opciones (ej. "Todas las anteriores"), añade `shuffle: false`.
   - En la página de evaluación, incluye preguntas bien fundamentadas y variadas:
     ```javascript
     var RANDOMIZE_OPTIONS = true; // Barajar alternativas automáticamente en el navegador
     var PREGUNTAS = [
       {
         q: "¿Cuál de las siguientes es una buena práctica de ciberseguridad?",
         opts: [
           "Compartir contraseñas por correo",
           "Activar la autenticación de doble factor",
           "Usar la misma clave en todos los servicios",
           "Desactivar las actualizaciones del sistema"
         ],
         correct: 1, // Opción B
         fb: "Correcto. El doble factor (2FA) añade una capa crítica de protección."
       },
       {
         q: "¿Qué principio rige la gestión de accesos según el modelo de menor privilegio?",
         opts: [
           "Conceder exclusivamente los permisos mínimos necesarios para cada función",
           "Asignar permisos de administrador a todos los usuarios del equipo",
           "Permitir acceso total durante el horario laboral sin restricciones",
           "Deshabilitar las políticas de auditoría en entornos de producción"
         ],
         correct: 0, // Opción A
         fb: "Exacto. El principio de menor privilegio limita los accesos a lo estrictamente indispensable."
       },
       {
         q: "¿Cómo debe procederse ante la sospecha de un incidente de seguridad?",
         opts: [
           "Borrar los registros del sistema para evitar alarmas",
           "Desconectar las alertas del cortafuegos y esperar",
           "Aislar el dispositivo afectado y notificar al equipo responsable según el protocolo",
           "Apagar el router general del edificio inmediatamente"
         ],
         correct: 2, // Opción C
         fb: "Correcto. Aislar el equipo y notificar al responsable es la respuesta adecuada del protocolo."
       }
     ];
     var PASS = 70; // Porcentaje de aprobación
     ```

---

### 3. Compilación y Validación
1. Sitúate en la carpeta del curso y ejecuta:
   ```bash
   python3 build.py
   ```
2. Revisa el resultado de la consola:
   - Verificación de consistencia del manifiesto.
   - Conformidad XML estricta contra `content.dtd`.
   - Generación del archivo final comprimido: **`<Nombre_Curso>_SCORM.zip`**.
3. Asegúrate de que termine con **0 errores**. Si hay algún error en rutas o sintaxis XML, corrígelo y vuelve a compilar.

---

### 4. Entrega y Almacenamiento
Informa al usuario de:
- La ubicación del paquete `.zip` listo para subir a EducaMadrid / Moodle.
- Opción de sincronizar o subir el `.zip` a **Google Drive** para compartirlo o almacenarlo en la nube.
