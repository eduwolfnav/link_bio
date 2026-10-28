import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
from link_bio.components.title import title

def live_schedule(schedule: dict) -> rx.Component:
    return rx.vstack(
        title("Live Schedule"),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text("Lunes", color=TextColor.BODY.value, size="2"),
                    rx.text(schedule.get("lunes","--"), color=TextColor.BODY.value, size="2"),
                    justify="between", width="100%", 
                    padding_y="6px",
                    border_bottom=f"1px solid {Color.BORDER.value}",
                ),
                rx.hstack(
                    rx.text("Martes", color=TextColor.BODY.value, size="2"),
                    rx.text(schedule.get("martes","--"), color=TextColor.BODY.value, size="2"),
                    justify="between", width="100%", 
                    padding_y="6px",
                ),
                width="100%", spacing="0",
            ),
            width="100%",
            padding_y="10px",
            padding_x="16px",
            background_color=Color.BACKGROUND.value,
            border_radius="12px",
            border=f"2px solid {Color.PURPLE.value}",
        ),
        width="100%",
        spacing="2",
        padding_top=Size.SMALL.value,
        align_items="start",
    )