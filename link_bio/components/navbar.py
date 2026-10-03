import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("edu", color=Color.PRIMARY.value),
        rx.text("wolf.nav", color=Color.CONTENT.value),
        width="100%",
        height="40px",
        justify="start",
        align="center",
        position="sticky",
        top="0",
        bg=Color.SECONDARY.value,
        padding_x=Size.DEFAULT.value,  # Cambiado de Size.BIG.value a Size.DEFAULT.value
        padding_y=Size.DEFAULT.value,
        z_index="999",
        spacing="0",
        style=styles.navbar_title_style
    )