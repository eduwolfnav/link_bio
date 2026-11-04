"""
link_bio/styles/styles.py
-------------------------
PROPÓSITO:
Define el sistema de diseño: tamaños, estilos globales, stylesheets y estilos
específicos de componentes. Es el puente entre colors.py/fonts.py y toda la UI.

CÓMO SE CONECTA:
- Importa Color, TextColor desde .colors y Font, FontWeight desde .fonts.
- BASE_STYLE es usado en link_bio/link_bio.py al crear rx.App(style=BASE_STYLE).
- STYLESHEETS es usado en el mismo rx.App para cargar Google Fonts y animate.css.
- Los dicts navbar_title_style, title_style, etc. son importados por:
  - components/navbar.py -> navbar_title_style
  - components/title.py -> title_style
  - components/link_button.py -> button_title_style y button_body_style
"""

import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

# Ancho máximo del contenido central. Usado en views/ para centrar la columna.
MAX_WIDTH = "600px"

class Size(Enum):
    """Escala de tamaños consistente. Evita valores mágicos en px/em por toda la app."""

    ZERO = "0px"
    SMALL = "0.7em"    # Descripciones de botones
    MEDIUM = "0.9em"   # Texto secundario
    DEFAULT = "1em"   # Tamaño base y padding estándar
    LARGE = "1.5em"   # Espaciados grandes
    BIG = "2em"       # Títulos destacados

# Fuentes y animaciones externas. Se inyectan en <head> vía rx.App(stylesheets=...).
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap",
    "https://fonts.googleapis.com/css2?family=Rationale&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/animations.css"  # Archivo local en assets/
]

# Estilo global aplicado a toda la app. Define fondo, fuente base y estilos por defecto de rx.heading, rx.button, rx.link.
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    "box_sizing": "border-box",
    "overflow_x": "hidden",
    "max_width": "100%",
    rx.heading: {
        "size": "6",
        "color": TextColor.BODY.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.BODY.value,
        "background_color": Color.SECONDARY.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {"background_color": Color.CONTENT.value}
    },
    rx.link: {"width": "100%", "text_decoration": "none", "_hover": {}}
}

# Estilo específico para el título del navbar (logo).
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight="700",
    font_size=Size.DEFAULT.value
)

# Estilo para títulos de sección (usado en components/title.py).
title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.FOOTER.value,
    font_family=Font.DEFAULT.value
)

# Estilo para el título dentro de link_button (nombre del link).
button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    color=TextColor.BODY.value
)

# Estilo para la descripción dentro de link_button.
button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.SMALL.value,
    color=TextColor.FOOTER.value
)
