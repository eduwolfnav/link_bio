"""
link_bio/components/link_sponsor.py
------------------------------------
PROPÓSITO:
Logo de sponsor/tecnología clickeable. Mantiene proporción original.

CÓMO SE CONECTA:
- Usado por views/sponsors.py para renderizar las 8 tecnologías (Python, Reflex, etc.).
- Sobrescribe width="100%" de BASE_STYLE con width="auto" para no estirar logos.
- Cada logo es imagen en assets/ (ej: python.jpg, reflexlogo.jpg).
- Caso sensible a mayúsculas en Linux (Reflex.jpg vs reflex.jpg) documentado en README.
"""

import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_sponsor(imagen: str, url: str) -> rx.Component:
    """
    Logo de sponsor con link externo.

    Args:
        imagen: Ruta en assets/ (ej: python.jpg)
        url: URL del sponsor/tecnología

    Conexión:
        - Llamado en bucle desde views/sponsors.py
        - Mantiene width auto para proporción original del logo
    """
    return rx.link(
        rx.image(
            height=Size.BIG.value,
            width="auto",
            src=imagen
        ),
        href=url,
        is_external=True,
        width="auto"
    )
