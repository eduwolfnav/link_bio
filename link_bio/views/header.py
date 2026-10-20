import reflex as rx

from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def header(details = True, live=False) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="Edu Wolf",
                    fallback="EW",
                    size="8",
                    src="avatar.png",
                    padding="0px",
                    border="4px solid",
                    border_color=Color.CONTENT.value,
                ),
                rx.cond(
                    live,
                    rx.box(
                        position="absolute",
                        bottom="-4px",
                        right="-4px",
                        width="22px",
                        height="22px",
                        border_radius="50%",
                        background_color=Color.PURPLE.value,
                        border=Color.BORDER.value,
                    ),
                ),
                position="relative",
                flex_shrink="0",
            ),
            rx.vstack(
                rx.heading(
                    "Edu Wolf"
                ),
                rx.text(
                    "@eduwolf.nav",
                    margin_top=Size.ZERO.value,
                    size="2",
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/icon_instagram.svg",
                        "https://www.instagram.com/edu.wolf.nav"
                    ),
                    link_icon(
                        "icons/icon_youtube.svg",
                        "https://www.youtube.com/@EduWolf-g3f"
                    ),
                    link_icon(
                        "icons/icon_github.svg",
                        "https://github.com/eduwolfnav"
                    ),
                    spacing="3"
                ),
                align_items="start",
                spacing="1",
                width="100%"
            ),
            spacing="4",
            width="100%",
            align="center"
        ),

        # Todo este bloque (estadísticas y texto) solo se muestra si details=True
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text("+20", "años de experiencia"),
                    info_text("+30", "app creadas"),
                    info_text("+10", "certificaciones"),
                    width="100%",
                    direction={"initial": "column", "sm": "row"},
                    justify="between",
                    align_items={"initial": "start", "sm": "center"},
                    spacing="4",
                    class_name="stats",
                ),
                rx.text(
                    """
                    Este es un proyecto de aprendizaje, espero crecer
                    mucho en estas nuevas metodologías, inspirándome a crear
                    arte, el arte de crear, docker.
                    """,
                    color=TextColor.BODY.value,
                    font_size=Size.MEDIUM.value,
                    width="100%",
                    text_align="start",
                    margin_top=Size.DEFAULT.value
                ),
                spacing="4",
                width="100%",
                padding_x="0px",
                padding_y="8px",
                align_items="start"
            )
        ),
        spacing="3"
    )