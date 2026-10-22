import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "600px"  # Puedes bajarlo a 500px o 600px

# Sizes
class Size(Enum):
    ZERO = "0px"
    SMALL = "0.5em"
    MEDIUM = "0.9em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Rationale&display=swap",
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;700&display=swap",
    "/responsive.css",
    "/animations.css",  # <--- Agregado aquí
]

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    
    # REGLAS CRÍTICAS PARA EL RESPONSIVE:
    "box_sizing": "border-box",  # <-- Corregido con guion medio en 'border-box'
    "overflow_x": "hidden",      # Previene cualquier scroll horizontal
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
        "_hover": {
            "background_color": Color.CONTENT.value
        }
    },
    rx.link: {
        "width": "100%",
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.FOOTER.value,
    font_family=Font.DEFAULT.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    color=TextColor.BODY.value
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.SMALL.value,
    color=TextColor.FOOTER.value
)
