"""
link_bio/views/header.py
------------------------
PROPÓSITO:
Vista del encabezado principal de la página. Contiene avatar, redes, botón de live y bio.

CÓMO SE CONECTA:
- Es usado por pages/index.py como primera sección de la página.
- Usa components/link_icon.py para iconos de redes sociales.
- Usa components/link_button.py para botón "En vivo" / "Próximo live".
- Usa components/info_text.py para estadísticas (experiencia, apps, certs).
- Usa components/live_schedule.py para horario, con datos de state/PageState.py.
- Usa model/Live.py para tipar el estado live.
- BLINK_CLASS e ICON_BLINK_CLASS vienen de assets/animations.css.
- Color y Size vienen de styles/ para mantener diseño consistente.

FLUJO DE LIVE:
TwitchAPI/SupabaseAPI -> Live (DB) -> PageState.live_schedule y live -> header()
"""

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

# Clase CSS para animación de borde parpadeante (definida en assets/animations.css)
BLINK_CLASS = "border-blink"

# Clase CSS para halo pulsante del icono de Twitch sobre el avatar
ICON_BLINK_CLASS = "icon-blink"

def header(details=True, live=Live(live=False, title=""), next_live="") -> rx.Component:
    """
    Encabezado principal con 5 bloques.

    Args:
        details: Si False oculta estadísticas, schedule y bio (modo compacto para cursos)
        live: Objeto Live (live: bool, title: str) - indica si estás en directo
        next_live: String con fecha/hora del próximo live

    Estructura:
        1. Perfil: avatar + nombre + @ + iconos redes (link_icon)
        2. Botón En vivo: link_button con borde morado animado si live.live=True
        3. Estadísticas: info_text en flex row/column responsivo
        4. Live Schedule: componente live_schedule con PageState.live_schedule
        5. Bio: textos descriptivos sobre stack tecnológico
    """
    return rx.vstack(
        # 1. Perfil principal: avatar con badge de Twitch si está en vivo
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="Edu Wolf",
                    fallback="EW",
                    size="8",
                    src="EduWolf.Nav.jpeg",
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
                            class_name=ICON_BLINK_CLASS,
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
                rx.heading("Edu Wolf", font_weight="700"),
                rx.text(
                    "@eduwolf.nav",
                    margin_top=Size.ZERO.value,
                    size="2",
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("icons/icon_instagram.svg", "https://www.instagram.com/edu.wolf.nav"),
                    link_icon("icons/icon_youtube.svg", "https://www.youtube.com/@EduWolf-g3f"),
                    link_icon("icons/icon_github.svg", "https://github.com/eduwolfnav"),
                    spacing="2"
                ),
                align_items="start",
                spacing="1",
                width="100%"
            ),
            spacing="4",
            width="100%",
            align="center"
        ),

        # 2. Botón En vivo / Próximo live - borde parpadeante via CSS
        rx.cond(
            live.live,
            rx.box(
                link_button(
                    "En vivo",
                    live.title,
                    "/icons/twitch.svg",
                    "https://www.twitch.tv/eduwolfnav",
                    is_external=True,
                    background_color=Color.BACKGROUND.value,
                    border_color="#9146ff",
                    border_width="2px",
                    animated=False
                ),
                width="100%",
                border_radius=Size.DEFAULT.value,
                class_name=BLINK_CLASS,
            ),
            rx.cond(
                next_live,
                rx.box(
                    link_button(
                        "Proximo live",
                        next_live,
                        "/icons/twitch.svg",
                        "https://www.twitch.tv/eduwolfnav",
                        is_external=True,
                        background_color=Color.BACKGROUND.value,
                        border_color=Color.PURPLE.value,
                        border_width="2px",
                        animated=False
                    ),
                    width="100%",
                    border_radius=Size.DEFAULT.value,
                    class_name=BLINK_CLASS,
                ),
            ),
        ),

        # 3. Estadísticas (solo si details=True)
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

        # 4. Live Schedule (horario desde PageState)
        rx.cond(
            details,
            rx.box(
                live_schedule(PageState.live_schedule),
                margin_top=Size.SMALL.value,
                width="100%"
            ),
        ),

        # 5. Texto bio descriptivo
        rx.cond(
            details,
            rx.box(
                rx.vstack(
                    rx.text("Este proyecto nace como un espacio de aprendizaje continuo y experimentación. Mi objetivo es dominar nuevas metodologías que impulsen mi crecimiento técnico, inspirándome en el verdadero arte de crear software.", color=TextColor.BODY.value, size="3"),
                    rx.text("Para dar vida a este ecosistema, combino la potencia de Python y FastAPI para el desarrollo de servicios web y la integración con la API de Twitch, la agilidad de Reflex para la interfaz y la confiabilidad de Supabase como base de datos.", color=TextColor.BODY.value, size="3"),
                    rx.text("En cuanto a infraestructura e integración, confío en GitHub para el control de versiones, Docker para la contenerización, y despliegues modernos a través de Vercel y Railway. Más que código, cada endpoint es una expresión de artesanía digital.", color=TextColor.BODY.value, size="3"),
                    rx.text("Gracias ", rx.link("https://moure.dev/", href="https://moure.dev/", is_external=True, color="#38bdf8", font_weight="bold", text_decoration="underline"), color=TextColor.BODY.value, size="3"),
                    spacing="3",
                    width="100%"
                ),
                padding=Size.DEFAULT.value,
                background_color=Color.CONTENT.value,
                border_radius="12px",
                border=f"1px solid {Color.BORDER.value}",
                width="100%",
                margin_top=Size.SMALL.value
            )
        ),
        spacing="3",
        width="100%"
    )
