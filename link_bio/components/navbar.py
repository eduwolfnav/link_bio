import reflex as rx
import link_bio.styles.styles as styles

from link_bio.components.ant_components import float_button
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.routes import Route

def navbar() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.text(
                            "edu", 
                            color=Color.PRIMARY.value,
                            style=styles.navbar_title_style
                        ),
                        rx.text(
                            "wolf.nav", 
                            color=Color.CONTENT.value,
                            style=styles.navbar_title_style
                        ),
                        spacing="0",
                    ),
                    href=Route.INDEX.value,
                    underline="none",
                ),
                float_button("/icons/donate.svg", "/"),
                width="100%",
                height="40px",
                justify="between",
                align="center",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.DEFAULT.value,
            ),
            position="fixed",
            top="0",
            left="0",
            right="0",
            width="100%",
            bg=Color.SECONDARY.value,
            z_index="999",
        ),
        rx.box(
            height="60px",
            width="100%",
        )
    )