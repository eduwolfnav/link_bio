"""
link_bio/components/live_schedule.py
-------------------------------------
PROPÓSITO:
Muestra el horario de directos (Live Schedule) con días y horas.

CÓMO SE CONECTA:
- Recibe schedule dict desde state/PageState.py o api/api.py (formato {"0": "18:00", ...}).
- Usa _dia_nombre() para traducir key Var (0-6) a nombre de día con rx.cond (necesario porque key es Var reactiva, no string Python).
- Es usado por views/header.py o index para mostrar cuándo es el próximo directo.
- Usa Color.PURPLE para borde y Color.BORDER para separadores.
"""

import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def _dia_nombre(key):
    """
    Traduce key de día (Var reactiva "0"-"6") a nombre en español.
    Usa rx.cond anidado porque no se puede hacer dict lookup con Var en Reflex.
    """
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
                                key
                            )
                        )
                    )
                )
            )
        )
    )

def live_schedule(schedule: dict) -> rx.Component:
    """
    Renderiza horario de directos.

    Args:
        schedule: dict reactivo { "0": "18:00", "2": "19:30" } donde 0=Lunes

    Conexión:
        - Datos vienen de SupabaseAPI o TwitchAPI vía PageState
        - rx.foreach itera cada entrada y muestra día + hora con borde inferior
    """
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
