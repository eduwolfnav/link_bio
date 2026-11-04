"""
link_bio/components/navbar.py
------------------------------
PROPÓSITO:
Navbar fija superior con logo y botón flotante.

CÓMO SE CONECTA:
- Usado en todas las páginas (pages/index.py, pages/courses.py) como cabecera fija.
- Usa Route.INDEX para linkear logo al home.
- Importa float_button desde ant_components.py (botón donación flotante en esquina).
- Usa styles.navbar_title_style para tipografía del logo "edu wolf.nav".
- Color.SECONDARY como fondo, con z_index 999 para quedar sobre el contenido.
"""

import reflex as rx
import link_bio.styles.styles as styles

from link_bio.components.ant_components import float_button
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.routes import Route

def navbar() -> rx.Component:
    """
    Navbar fija con logo y botón flotante.

    Estructura:
    - Box fijo top 0 con hstack: logo (edu + wolf.nav) a la izquierda, float_button a la derecha
    - Box espaciador de 60px para evitar que el contenido quede debajo del navbar fijo

    Conexión:
    - Se renderiza al inicio de cada página en pages/
    """
    return rx.fragment(
        rx.box(
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.text(
                            "edu", 
                            color=Color.PRIMARY.value,
                            style=styles.navbar_title_style
                        ),
                        rx.text(
                            "wolf.nav", 
                            color=Color.CONTENT.value,
                            style=styles.navbar_title_style
                        ),
                        spacing="0",
                    ),
                    href=Route.INDEX.value,
                    underline="none",
                ),
                float_button("/icons/donate.svg", "/"),
                width="100%",
                height="40px",
                justify="between",
                align="center",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            ),
            position="fixed",
            top="0",
            left="0",
            right="0",
            width="100%",
            bg=Color.SECONDARY.value,
            z_index="999",
        ),
        rx.box(
            height="60px",
            width="100%",
        )
    )
