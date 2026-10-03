import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(

        rx.hstack(
            rx.avatar(
                name="Edu Wolf", 
                fallback="EW", 
                size="8",
                src="avatar.png",
                padding="0px",
                border="4px solid",
                border_color=Color.CONTENT.value,
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
                    )
                ),    
                aling_items="stars",
                width="100%"
            ),
            spacing="4",
        ),
        rx.flex(
            info_text("+20", "años de experiecia"),
            info_text("+30", "app creadas"),
            info_text("+10", "certificaciones"),
            width="100%",
            gap="1em",
            class_name="stats",
        ),
        rx.text(
            """
            Este es un proyecto de aprendizaje, espero crecer
            mucho en estas nuevas metodologías, inspirándome a crear
            arte, el arte de crear.
            """,
            color=TextColor.BODY.value,
            font_size=Size.MEDIUM.value
        ),
        spacing="4",
        width="100%",
        padding_x="0px",
        padding_y="8px",
        aling_items="stars"
    )