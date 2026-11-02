import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

print(">>> CARGANDO components/live_schedule.py V4 FIX VAR")

def _dia_nombre(key):
    # Mapeo con rx.cond anidado porque key es Var, no string de Python
    return rx.cond(
        key == "0", "Lunes",
        rx.cond(
            key == "1", "Martes",
            rx.cond(
                key == "2", "Miércoles",
                rx.cond(
                    key == "3", "Jueves",
                    rx.cond(
                        key == "4", "Viernes",
                        rx.cond(
                            key == "5", "Sábado",
                            rx.cond(
                                key == "6", "Domingo",
                                key  # fallback: muestra el key original
                            )
                        )
                    )
                )
            )
        )
    )

def live_schedule(schedule: dict) -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Live Schedule",
            size="4",
            color=TextColor.BODY.value,
            width="100%",
            padding_top=Size.ZERO.value,
            margin_top=Size.ZERO.value
        ),
        rx.box(
            rx.vstack(
                rx.foreach(
                    schedule,
                    lambda item: rx.hstack(
                        rx.text(
                            _dia_nombre(item[0]), 
                            color=TextColor.BODY.value, 
                            size="2"
                        ),
                        rx.text(item[1], color=TextColor.BODY.value, size="2"),
                        justify="between",
                        width="100%",
                        padding_y="6px",
                        border_bottom=f"1px solid {Color.BORDER.value}",
                    )
                ),
                width="100%",
                spacing="0",
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
        padding_top=Size.ZERO.value,
        margin_top=Size.ZERO.value,
        align_items="start",
    )