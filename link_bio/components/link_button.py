import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_button(
    title: str, 
    body: str, 
    image: str, 
    url: str, 
    is_external=True, 
    background_color: str = None,
    border_color: str = None,
    border_width: str = "1px"
) -> rx.Component:
    
    # Creamos un diccionario de estilo base para el botón
    custom_style = {"width": "100%"}
    
    # Si se proporciona un color de fondo, configuramos el fondo normal y el hover
    if background_color:
        custom_style["background_color"] = background_color
        # Definimos un tono ligeramente más claro para cuando pases el mouse (puedes ajustarlo a tu gusto)
        custom_style["_hover"] = {
            "background_color": "#9146FF"  # Un tono de morado/twitch más vivo para el hover
        }

    # Si se proporciona un color de borde, lo aplicamos
    if border_color:
        custom_style["border"] = f"{border_width} solid {border_color}"

    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(
                        title,
                        style=styles.button_title_style
                    ),
                    rx.text(
                        body,
                        style=styles.button_body_style
                    ),
                    align_items="start",
                    spacing="1",
                    margin=Size.ZERO.value,
                    width="100%"
                ),
                align="center",
                width="100%",
                spacing="3"
            ),
            style=custom_style
        ),
        href=url,
        width="100%",
        is_external=is_external
    )