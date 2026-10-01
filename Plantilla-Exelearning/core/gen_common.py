# -*- coding: utf-8 -*-
"""
HTML block generation helpers for eXeLearning-compatible course pages.

These helpers are called by the course-specific spec file
(see plantilla/course_spec.py), which imports this module and overrides
gen_common.COURSE and gen_common.PAGES before build_course.py renders the SCOs.
"""
import html as _html

COURSE = "TITULO DEL CURSO"

# Page list (order matters). index.html is at root; the rest under html/.
# icon = file name (without extension) in theme/icons/
PAGES = [
    dict(slug="index", pid="page-00", title="Portada", nav="Portada", icon="objectives"),
]

def _href(from_slug, to_slug):
    """Relative link between pages given the folder layout."""
    if to_slug == "index":
        target = "index.html" if from_slug == "index" else "../index.html"
    else:
        target = ("html/" if from_slug == "index" else "") + to_slug + ".html"
    return target

def _prefix(slug):
    """Relative prefix to reach package root from a page."""
    return "" if slug == "index" else "../"

def head(slug, title, extra_head=""):
    p = _prefix(slug)
    desc = f"{COURSE} - Material didáctico interactivo para automoción y formación profesional."
    # MathJax config + local engine (SVG output, self-contained)
    mathjax = (
        '<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]],'
        'displayMath:[["\\\\[","\\\\]"]]},svg:{fontCache:"global"},'
        'options:{renderActions:{addMenu:[]}}};</script>\n'
        f'<script defer src="{p}libs/mathjax/tex-svg.js"></script>'
    )
    return f"""<!DOCTYPE html>
<html lang="es" id="exe-index">
<head>
<meta charset="utf-8">
<meta name="generator" content="eXeLearning v4.0.1">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="license" type="text/html" href="https://creativecommons.org/licenses/by-sa/4.0/">
<title>{_html.escape(title)} | {_html.escape(COURSE)}</title>
<link rel="icon" type="image/x-icon" href="{p}libs/favicon.ico">
<meta name="description" content="{_html.escape(desc)}">
<script>document.querySelector("html").classList.add("js");</script>
<script src="{p}libs/jquery/jquery.min.js"> </script>
<script src="{p}libs/common_i18n.js"> </script>
<script src="{p}libs/common.js"> </script>
<script src="{p}libs/exe_export.js"> </script>
<script src="{p}libs/xapi/exe_xapi.js"> </script>
<script src="{p}libs/bootstrap/bootstrap.bundle.min.js"> </script>
<link rel="stylesheet" href="{p}libs/bootstrap/bootstrap.min.css">
<script src="{p}idevices/text/text.js"></script>
<link rel="stylesheet" href="{p}idevices/text/text.css">
<script src="{p}libs/exe_atools/exe_atools.js"> </script>
<link rel="stylesheet" href="{p}libs/exe_atools/exe_atools.css">
<script src="{p}libs/exe_effects/exe_effects.js"> </script>
<link rel="stylesheet" href="{p}libs/exe_effects/exe_effects.css">
<link rel="stylesheet" href="{p}content/css/base.css">
<script src="{p}theme/style.js"> </script>
<link rel="stylesheet" href="{p}theme/style.css">
<link rel="stylesheet" href="{p}content/css/curso.css">
{mathjax}
<script src="{p}libs/SCORM_API_wrapper.js"></script>
<script src="{p}libs/SCOFunctions.js"></script>
<script>/* Usamos MathJax propio (libs/mathjax): desactivamos el motor de fórmulas de eXe para evitar conflictos */
if(window.$exe&&$exe.math){{$exe.math.init=function(){{}};}}</script>
{extra_head}
</head>"""

def nav_block(slug):
    """Prev / Next navigation."""
    idx = next(i for i,pg in enumerate(PAGES) if pg["slug"] == slug)
    prev_pg = PAGES[idx-1] if idx > 0 else None
    next_pg = PAGES[idx+1] if idx < len(PAGES)-1 else None
    parts = ['<nav class="curso-nav" aria-label="Navegación de la unidad">']
    if prev_pg:
        parts.append(
            f'<a class="prev" href="{_href(slug, prev_pg["slug"])}">'
            f'<span class="lbl">&larr; Anterior</span>'
            f'<span class="ttl">{_html.escape(prev_pg["nav"])}</span></a>')
    else:
        parts.append('<a class="prev disabled" aria-disabled="true"><span class="lbl">&larr; Anterior</span><span class="ttl">Inicio</span></a>')
    if next_pg:
        parts.append(
            f'<a class="next" href="{_href(slug, next_pg["slug"])}">'
            f'<span class="lbl">Siguiente &rarr;</span>'
            f'<span class="ttl">{_html.escape(next_pg["nav"])}</span></a>')
    else:
        parts.append('<a class="next disabled" aria-disabled="true"><span class="lbl">Siguiente &rarr;</span><span class="ttl">Fin</span></a>')
    parts.append('</nav>')
    return "\n".join(parts)

_idevice_counter = [0]
def _idevice_attrs():
    _idevice_counter[0] += 1
    iid = f"idevice-elec-{_idevice_counter[0]:03d}"
    return (f'data-idevice-path="idevices/text/" data-idevice-type="text" '
            f'data-idevice-component-type="json" '
            f'data-idevice-json-data="{{&quot;ideviceId&quot;:&quot;{iid}&quot;}}"')

def box(title, icon, inner, no_header=False, prefix=""):
    """eXe-style content box (static; not hooked into eXe's idevice JS engine)."""
    if no_header:
        return (f'<article class="box no-header">\n'
                f'<header class="box-head no-icon">\n'
                f'<button class="box-toggle box-toggle-on" title="Mostrar/ocultar"><span>Mostrar/ocultar</span></button>'
                f'</header>\n<div class="box-content">\n'
                f'<div class="exe-static-content">\n{inner}\n</div>\n</div>\n</article>')
    icon_file = icon if ("." in icon) else f"{icon}.svg"
    return (f'<article class="box">\n'
            f'<header class="box-head">\n'
            f'<div class="box-icon exe-icon"><img src="{prefix}theme/icons/{icon_file}" alt=""></div>\n'
            f'<h1 class="box-title">{_html.escape(title)}</h1>\n'
            f'<button class="box-toggle box-toggle-on" title="Mostrar/ocultar"><span>Mostrar/ocultar</span></button>'
            f'</header>\n<div class="box-content">\n'
            f'<div class="exe-static-content">\n{inner}\n</div>\n</div>\n</article>')

def page(slug, title, body, body_class_extra="", onunload='unloadPage()'):
    p = _prefix(slug)
    pg = next(pg for pg in PAGES if pg["slug"] == slug)
    foot_text = globals().get('FOOTER_TEXT', 'Material didáctico interactivo · Formación Profesional')
    footer = (
        '<footer id="siteFooter"><div id="siteFooterContent">'
        '<div id="packageLicense" class="cc cc-by-sa"><p>'
        '<span class="license-label">Licencia: </span>'
        '<a href="https://creativecommons.org/licenses/by-sa/4.0/" class="license">'
        'Creative Commons: Reconocimiento - Compartir Igual 4.0</a></p></div>'
        f'<p style="font-size:.8rem;color:#777;margin-top:.4em;">{_html.escape(foot_text)}</p>'
        '</div></footer>')
    return f"""{head(slug, title)}
<body class="exe-export exe-scorm exe-scorm12 {body_class_extra}" onload="loadPage()" onunload="{onunload}" onbeforeunload="{onunload}">
<script>document.body.className+=" js"</script>
<div class="exe-content exe-export pre-js siteNav-hidden"><main id="{pg['pid']}" class="page">
<header class="main-header">
<div class="package-header"><p class="package-title">{_html.escape(COURSE)}</p></div>
<div class="page-header"><h1 class="page-title">{_html.escape(title)}</h1></div>
</header><div id="page-content-{pg['pid']}" class="page-content">
{body}
</div></main>
{footer}
</div>
</body>
</html>"""
