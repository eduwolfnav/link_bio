"""
link_bio/components/title.py
-----------------------------
PROPÓSITO:
Componente de título de sección reutilizable.

CÓMO SE CONECTA:
- Usado por views/sponsors.py, views/index_links.py, components/featured_link.py
  para títulos como "Tecnologías", "Destacados", "Recursos", etc.
- Usa styles.title_style definido en styles/styles.py (padding_top, color FOOTER).
"""

import reflex as rx
import link_bio.styles.styles as styles

def title(text: str) -> rx.Component:
    """
    Título de sección.

    Args:
        text: Texto del título (ej: "Sponsors", "Links")

    Usado en views/ para separar secciones visualmente.
    """
    return rx.heading(
            text,
            size="4",
            style=styles.title_style
        )
