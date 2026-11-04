"""
link_bio/views/index_links.py
-----------------------------
PROPÓSITO:
Vista que agrupa todos los links principales de la página de inicio.

CÓMO SE CONECTA:
- Usado por pages/index.py como bloque central de links.
- Usa components/link_button.py para cada botón.
- Usa components/title.py para separar secciones (Asyncio, Cursos, Social...).
- Usa components/featured_link.py para mostrar destacados desde Supabase (featured param).
- Usa routes.Route para navegación interna (TESTASYNCIO, COURSES) sin recargar página.
- Los links externos van a Instagram, YouTube, GitHub, email.

Args:
    featured: lista de modelo Featured (title, image, url) que viene de PageState o SupabaseAPI
"""

import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.components.featured_link import featured_link
from link_bio.routes import Route
from link_bio.model.Featured import featured

def index_links(featured: list[featured]) -> rx.Component:
    """
    Lista de links de la página principal.

    Estructura:
    - Ejemplo Asyncio (link interno)
    - Destacados (grid desde featured_link)
    - Cursos recomendados (link interno a /courses)
    - Social (Instagram, YouTube)
    - Recursos (GitHub)
    - Contacto (email)
    """
    return rx.vstack(
        title("Ejemplo Asyncio"),
        link_button(
            "@ Ejemplo Asyncio",
            "Ejemplo Asyncio @eduwolf.nav.",
            "icons/async.svg",
            Route.TESTASYNCIO.value,
            is_external=False
        ),

        # Grid de destacados que viene de Supabase - si hay datos se muestra, si no rx.fragment()
        featured_link(featured),
        
        title("Cursos recomendados"),
        link_button(
            "@ Cursos recomendados",
            "Aprende programación @Youtube.",
            "icons/icon_youtube.svg",
            Route.COURSES.value,
            is_external=False
        ),
        title("Social"),
        link_button(
            "@ Instagram",
            "Perfil de @Instagram",
            "icons/icon_instagram.svg",
            "https://www.instagram.com/edu.wolf.nav"
        ),
        link_button(
            "@ YouTube",
            "Canal de @YouTube",
            "icons/icon_youtube.svg",
            "https://www.youtube.com/@EduWolf-g3f"
        ),
        title("Recursos"),
        link_button(
            "@ GitHub",
            "Repositorio de @GitHub",
            "icons/icon_github.svg",
            "https://github.com/eduwolfnav"
        ),
        title("Contacto"),
        link_button(
            "@ E-mail",
            "E-mail de contacto",
            "icons/icon_email.svg",
            "mailto:edu.wolf.nav@gmail.com"
        ), 
        width="100%",
        align_items="start", 
        spacing="4"
    )
