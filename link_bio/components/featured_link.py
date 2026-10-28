import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.title import title

def featured_link(featured_items) -> rx.Component:
    return rx.cond(
        featured_items.length() > 0,
        rx.vstack(
            title("Destacados"),
            rx.grid(
                rx.foreach(
                    featured_items.to(list[dict]),
                    lambda item: rx.link(
                        rx.vstack(
                            rx.box(
                                rx.image(
                                    src=item["image"],
                                    width="100%",
                                    height="auto",
                                    object_fit="contain",
                                ),
                                width="100%",
                                flex="1", # <- esto hace que ambas cajas midan lo mismo
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                border_radius="8px",
                                overflow="hidden",
                                background_color="#0f172a",
                            ),
                            rx.text(
                                item["title"],
                                style=styles.button_body_style,
                                no_of_lines=2,
                                width="100%",
                            ),
                            width="100%",
                            height="100%",
                            spacing="3",
                            align_items="start",
                        ),
                        href=item["url"],
                        is_external=True,
                        width="100%",
                        height="100%",
                        display="flex",
                        flex_direction="column",
                        padding="12px", # un poco menos de padding para que sea compacto
                        border_radius="12px",
                        border="1px solid",
                        border_color="#1e293b",
                        background_color="#0f172a",
                        _hover={"border_color": "#3b82f6"},
                        transition="all 0.2s ease-in-out",
                    ),
                ),
                columns={
                    "initial": "1",
                    "sm": "2",
                },
                gap="24px",
                width="100%",
                align_items="stretch", # <- fuerza a que la fila tenga la altura de la imagen más alta
            ),
            width="100%",
            spacing="4",
            align_items="stretch",
        ),
        rx.fragment(),
    )