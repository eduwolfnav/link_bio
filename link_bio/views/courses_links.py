"""
link_bio/views/courses_links.py
--------------------------------
PROPÓSITO:
Vista específica para la página de cursos. Lista cursos de Python.

CÓMO SE CONECTA:
- Usado por pages/courses.py como contenido principal.
- Reutiliza components/link_button.py y components/title.py.
- Todos los links son externos a YouTube (Brais Moure).
- Route.COURSES es la ruta /courses definida en routes.py.

Es independiente de Supabase, lista estática de cursos recomendados.
"""

import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.routes import Route

def courses_links() -> rx.Component:
    """Lista de cursos recomendados. Mostrada en pages/courses.py."""
    return rx.vstack(
        title("Cursos recomendados"),
        link_button(
            "@ PYTHON desde CERO by Brais Moure",
            "@Youtube",
            "icons/icon_youtube.svg",
            "https://www.youtube.com/watch?v=Kp4Mvapo5kc&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_"
        ),
        link_button(
            "@ PYTHON desde CERO [Intermedio] by Brais Moure",
            "@Youtube",
            "icons/icon_youtube.svg",
            "https://www.youtube.com/watch?v=TbcEqkabAWU&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=2"
        ),
        link_button(
            "@ PYTHON desde CERO para BACKEND by Brais Moure",
            "@Youtube",
            "icons/icon_youtube.svg",
            "https://www.youtube.com/watch?v=_y9qQZXE24A&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=3"
        ),
        width="100%",
        align_items="start",
        spacing="4"
    )
