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
    border_width: str = "2px",
    animated: bool = False
) -> rx.Component:
    
    custom_style = {"width": "100%"}
    
    if background_color:
        custom_style["background_color"] = background_color
    if border_color:
        custom_style["border"] = f"{border_width} solid {border_color}"

    # Animación directa - no depende de clases raras
    if animated:
        if border_color == "#9146ff":
            custom_style["animation"] = "live-pulse-red 1.2s infinite"
        else:
            custom_style["animation"] = "live-pulse 2.5s infinite"

    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src=image, width=Size.BIG.value, height=Size.BIG.value, margin=Size.MEDIUM.value, alt=title),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start", spacing="1", margin=Size.ZERO.value, width="100%"
                ),
                align="center", width="100%", spacing="3"
            ),
            style=custom_style
        ),
        href=url, width="100%", is_external=is_external
    )