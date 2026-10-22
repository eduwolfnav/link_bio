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
            f"HomePage @{datetime.date.today().year} https://eduwolfnav.vercel.app/",
            href="https://eduwolfnav.vercel.app/",
            is_external=True,
            font_size=Size.MEDIUM.value,
            text_align="center",
            width="100%"
        ),
        rx.hstack(
            rx.link(
                rx.image(
                    src="icons/icon_github.svg",
                    width=Size.LARGE.value,
                    height=Size.LARGE.value
                ),
                href="https://github.com/eduwolfnav/link_bio",
                is_external=True
            ),
            rx.text(
                "By Edu Wolf 🐺",
                font_size=Size.MEDIUM.value,
                white_space="nowrap"  # <-- Evita que el texto salte de línea
            ),
            align="center",
            spacing="3",  # Espacio entre el icono y el texto
        ),
        width="100%",
        justify="center",
        align="center",
        top="0",
        padding_x="16px",
        padding_y="8px",
        margin_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
        spacing="0"
    )