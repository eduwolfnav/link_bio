import reflex as rx

from link_bio.components.link_icon import link_icon
from link_bio.components.link_button import link_button
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.model.Live import Live

from link_bio.components.live_schedule import live_schedule
from link_bio.state.PageState import PageState

def header(details = True, live = Live(live=False, title="")) -> rx.Component:
    return rx.vstack(
        # 1. Perfil principal (Avatar, nombre y redes sociales - siempre visible)
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
                    live.live,
                    rx.link(
                        rx.box(
                            rx.image(
                                src="/icons/twitch.svg",
                                width="12px",
                                height="12px",
                            ),
                            position="absolute",
                            bottom="-4px",
                            right="-4px",
                            width="22px",
                            height="22px",
                            border_radius="50%",
                            background_color=Color.PURPLE.value,
                            border=Color.BORDER.value,
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            animation="pulse 1.0s infinite ease-in-out",
                        ),
                        href="https://www.twitch.tv/eduwolfnav",
                        is_external=True,
                    ),
                    rx.fragment(),
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

        # 3. Botón En vivo (Se muestra si live=True en cualquier página)
        rx.cond(
            live.live,
            link_button(
                "En vivo",
                live.title,
                "icons/twitch.svg",
                "https://www.twitch.tv/eduwolfnav",
                is_external=True,
                background_color=Color.BACKGROUND.value,
                border_color=Color.PURPLE.value,
                border_width="2px"
            ),
        ),

        # 2. Estadísticas (Años de experiencia, apps, certificaciones - solo si details=True)
        rx.cond(
            details,
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
            )
        ),

        # 2.5 LIVE SCHEDULE - ConfigCat (minimalista, ordenado) - TU LÍNEA ROJA
        rx.cond(
            details,
            live_schedule(PageState.live_schedule),
        ),
        

        # 4. Texto descriptivo (Solo si details=True)
        rx.cond(
            details,
            rx.box(
                rx.vstack(
                    rx.text(
                        "Este proyecto nace como un espacio de aprendizaje continuo y experimentación. Mi objetivo es dominar nuevas metodologías que impulsen mi crecimiento técnico, inspirándome en el verdadero arte de crear software.",
                        color=TextColor.BODY.value,
                        size="3",
                        text_align="start",
                    ),
                    rx.text(
                        "Para dar vida a este ecosistema, combino la potencia de Python y FastAPI para el desarrollo de servicios web y la integración con la API de Twitch, la agilidad de Reflex para la interfaz y la confiabilidad de Supabase como base de datos.",
                        color=TextColor.BODY.value,
                        size="3",
                        text_align="start",
                    ),
                    rx.text(
                        "En cuanto a infraestructura e integración, confío en GitHub para el control de versiones, Docker para la contenerización, y despliegues modernos a través de Vercel y Railway. Más que código, cada endpoint es una expresión de artesanía digital.",
                        color=TextColor.BODY.value,
                        size="3",
                        text_align="start",
                    ),
                    rx.text(
                        "Gracias ",
                        rx.link(
                            "https://moure.dev/",
                            href="https://moure.dev/",
                            is_external=True,
                            color="#38bdf8",
                            font_weight="bold",
                            text_decoration="underline",
                            _hover={
                                "color": "#93c5fd",
                            },
                        ),
                        color=TextColor.BODY.value,
                        size="3",
                        text_align="start",
                    ),
                    spacing="3",
                    width="100%"
                ),
                padding=Size.DEFAULT.value,
                background_color=Color.CONTENT.value,
                border_radius="12px",
                border=f"1px solid {Color.BORDER.value}",
                width="100%",
                margin_top=Size.DEFAULT.value
            )
        ),

        spacing="4",
        width="100%"
    )