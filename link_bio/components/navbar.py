import reflex as rx
import link_bio.styles.styles as styles

from link_bio.components.ant_components import float_button

from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.routes import Route

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.text("edu", color=Color.PRIMARY.value),
                rx.text("wolf.nav", color=Color.CONTENT.value),
                spacing="0",
            ),
            href=Route.INDEX.value,  # O la URL / ruta destino (por ejemplo, "/")
            underline="none",        # Quita el subrayado por defecto del enlace
        ),
        float_button("/icons/donate.svg", "/"),
        width="100%",
        height="40px",
        justify="start",
        align="center",
        position="sticky",
        top="0",
        bg=Color.SECONDARY.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        spacing="0",
        style=styles.navbar_title_style,
    )