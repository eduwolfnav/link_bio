import reflex as rx
from link_bio.styles.colors import Color

def float_button(icon: str, href: str) -> rx.Component:
    return rx.box(
        rx.link(
            rx.image(
                src=icon,
                width="24px",
                height="24px",
            ),
            href=href,
            target="_blank",
        ),
        position="fixed",
        right="2rem",
        bottom="2rem",
        z_index="999",
        background_color=Color.SECONDARY.value,
        border_radius="full",
        padding="12px",
        box_shadow="lg",
        _hover={
            "background_color": Color.CONTENT.value,
        },
    )

# float_button = FloatButton.create