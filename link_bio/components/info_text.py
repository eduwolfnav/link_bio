"""
link_bio/components/info_text.py
--------------------------------
PROPÓSITO:
Componente pequeño para mostrar pares clave-valor (ej: info del header).

CÓMO SE CONECTA:
- Usado por views/header.py para mostrar datos como experiencia, ubicación, etc.
- Usa styles.Size para tamaño de fuente y colors para contraste.
"""

import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    """
    Muestra un dato en formato 'Título: Valor'.

    Args:
        title: Etiqueta en negrita y color primario
        body: Valor en color footer

    Usado en header.py para listar detalles del perfil.
    """
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
