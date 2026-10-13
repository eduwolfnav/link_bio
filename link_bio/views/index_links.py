import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.routes import Route


def index_links() -> rx.Component:
    return rx.vstack(
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
        align_items="start",  # Alinea títulos y botones exactamente a la izquierda
        spacing="4"
    )