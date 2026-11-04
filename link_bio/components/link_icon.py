"""
link_bio/components/link_icon.py
---------------------------------
PROPÓSITO:
Icono pequeño linkeable (redes sociales en header).

CÓMO SE CONECTA:
- Usado por views/header.py para mostrar iconos de GitHub, Instagram, etc.
- Tamaño viene de styles.Size.MEDIUM para mantener consistencia.
"""

import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_icon(image: str, url: str) -> rx.Component:
    """
    Icono linkeable pequeño.

    Args:
        image: Ruta del icono en assets/
        url: URL externa

    Usado en header para redes sociales.
    """
    return rx.link(
        rx.image(
            src=image,
            width=Size.MEDIUM.value
        ),
        href=url,
        is_external=True
    )
