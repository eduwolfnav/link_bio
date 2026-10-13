import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_sponsor(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            height=Size.BIG.value,
            width="auto",       # Asegura que la imagen mantenga su proporción
            src=imagen
        ),
        href=url,
        is_external=True,
        width="auto"            # OVERRIDE: Sobreescribe el width="100%" de styles.py
    )