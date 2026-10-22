import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.routes import Route


def index_links(featured: list[dict]) -> rx.Component:
    return rx.vstack(
        title("Ejemplo Asyncio"),
        link_button(
            "@ Ejemplo Asyncio",
            "Ejemplo Asyncio @eduwolf.nav.",
            "icons/async.svg",
            Route.TESTASYNCIO.value,
            is_external=False
        ),

        rx.cond(
            featured.length() > 0,
            rx.vstack(
                title("Destacados"),
                rx.vstack(
                    rx.foreach(
                        featured.to(list[dict]),
                        lambda item: rx.link(
                            rx.vstack(
                                rx.image(
                                    src=item["image"],
                                    width="100%",
                                    height="auto",
                                    border_radius="8px",
                                    object_fit="cover",
                                ),
                                rx.text(
                                    item["title"],
                                    font_weight="medium",
                                    font_size="0.95em",
                                    color="white",
                                ),
                                width="100%",
                                spacing="3",
                                align_items="start",
                            ),
                            href=item["url"],
                            is_external=True,
                            width="100%",
                            padding="14px",
                            border_radius="12px",
                            border="1px solid",
                            border_color="#1e293b",
                            background_color="#0f172a",
                            _hover={
                                "border_color": "#3b82f6",
                                "transform": "scale(1.01)",
                                "transition": "all 0.2s ease-in-out",
                            },
                        ),
                    ),
                    width="100%",
                    spacing="3",
                ),
                width="100%",
            ),
            rx.fragment(),
        ),
        
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