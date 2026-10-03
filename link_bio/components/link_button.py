import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(
                        title,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        body,
                        style=styles.button_body_style
                    ),
                    align_items="start",
                    spacing="1",
                    margin=Size.ZERO.value,
                    width="100%"  # <-- Asegura que tome el ancho disponible
                ),
                align="center",
                width="100%",
                spacing="3"
            ),
            width="100%"
        ),
        href=url,
        width="100%",
        is_external=True
    )