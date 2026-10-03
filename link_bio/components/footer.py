import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            width="77px",
            height="77px",
            alt="Logotipo de EduWolf. Un cabeza de lobo arriba de frente, con Edu Wolf escrito abajo."
            ),
        rx.link(
            f"HomePage @{datetime.date.today().year} https://eduwolf.nav",
            href="https://eduwolf.nav",
            is_external=True,
            font_size=Size.MEDIUM.value,
            text_align="center",  # Centra el texto dentro del enlace
            width="100%"
        ),
        rx.text(
            "By Edu Wolf 🐺",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        width="100%",
        justify="center",
        align="center",
        top="0",
        padding_x="16px",
        padding_y="8px",
        margin_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )