import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

MAX_WIDTH = "600px"

class Size(Enum):
    ZERO = "0px"
    SMALL = "0.7em"
    MEDIUM = "0.9em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap",
    "https://fonts.googleapis.com/css2?family=Rationale&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/animations.css"
]

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

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight="700",
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
