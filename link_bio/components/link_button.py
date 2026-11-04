"""
link_bio/components/link_button.py
-----------------------------------
PROPÓSITO:
Botón principal de link_bio. Es el bloque más usado: imagen + título + descripción + link.

CÓMO SE CONECTA:
- Usado por views/index_links.py y views/courses_links.py para listar todos los links.
- Usa styles.button_title_style y button_body_style para tipografía.
- Soporta animación live-pulse para indicar directo activo (usado con TwitchAPI).
- background_color y border_color opcionales permiten variantes (ej: borde morado para live).
"""

import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_button(
    title: str, 
    body: str, 
    image: str, 
    url: str, 
    is_external=True, 
    background_color: str = None,
    border_color: str = None,
    border_width: str = "2px",
    animated: bool = False
) -> rx.Component:
    """
    Botón de link con icono y textos.

    Args:
        title: Título principal del botón
        body: Descripción corta
        image: Ruta del icono en assets/
        url: URL destino
        is_external: Si abre en nueva pestaña
        background_color: Color de fondo opcional (override de SECONDARY)
        border_color: Color de borde opcional
        animated: Si True aplica animación live-pulse (para estado en vivo)

    Conexión:
        - Cada instancia es un item en index_links.py
        - El hover y colores vienen de BASE_STYLE en styles.py
    """
    
    custom_style = {"width": "100%"}
    
    if background_color:
        custom_style["background_color"] = background_color
    if border_color:
        custom_style["border"] = f"{border_width} solid {border_color}"

    # Animación para estado live (borde morado = Twitch, otro = genérico)
    if animated:
        if border_color == "#9146ff":
            custom_style["animation"] = "live-pulse-red 1.2s infinite"
        else:
            custom_style["animation"] = "live-pulse 2.5s infinite"

    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src=image, width=Size.BIG.value, height=Size.BIG.value, margin=Size.MEDIUM.value, alt=title),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start", spacing="1", margin=Size.ZERO.value, width="100%"
                ),
                align="center", width="100%", spacing="3"
            ),
            style=custom_style
        ),
        href=url, width="100%", is_external=is_external
    )
