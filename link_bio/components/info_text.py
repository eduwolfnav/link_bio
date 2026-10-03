import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            title, 
            weight="bold", 
            color=Color.PRIMARY.value
        ),
        rx.text(body),
        font_size=Size.MEDIUM.value,
        color=TextColor.FOOTER.value
    )