"""
link_bio/components/ant_components.py
-------------------------------------
PROPÓSITO:
Componentes flotantes/ant design reutilizables. Actualmente expone float_button.

CÓMO SE CONECTA:
- Importado por components/navbar.py -> float_button se muestra fijo abajo a la derecha.
- Usa Color.SECONDARY y CONTENT desde styles/colors.py para mantener paleta.
- Es independiente de views/, puede usarse en cualquier página.
"""

import reflex as rx
from link_bio.styles.colors import Color

def float_button(icon: str, href: str) -> rx.Component:
    """
    Botón flotante fijo en esquina inferior derecha.

    Args:
        icon: Ruta del icono en assets/ (ej: /icons/donate.svg)
        href: URL destino del botón

    Retorna:
        rx.Component box fijo. Usado en navbar.py como acceso rápido a donación/home.
    """
    return rx.box(
        rx.link(
            rx.image(
                src=icon,
                width="24px",
                height="24px",
            ),
            href=href,
            target="_blank",
        ),
        position="fixed",
        right="2rem",
        bottom="2rem",
        z_index="999",
        background_color=Color.SECONDARY.value,
        border_radius="full",
        padding="12px",
        box_shadow="lg",
        _hover={
            "background_color": Color.CONTENT.value,
        },
    )
