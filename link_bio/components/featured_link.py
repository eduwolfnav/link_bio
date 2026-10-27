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
                                    height="100%",
                                    object_fit="contain",
                                    object_position="center",
                                ),
                                width="100%",
                                height="220px",
                                border_radius="8px",
                                overflow="hidden",
                                background_color="#0f172a",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                            ),
                            rx.text(
                                item["title"],
                                style=styles.button_title_style,
                                no_of_lines=2,
                                width="100%",
                            ),
                            width="100%",
                            spacing="3",
                            align_items="start",
                        ),
                        href=item["url"],
                        is_external=True,
                        display="block",
                        width="100%",
                        height="100%",
                        padding="14px",
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
            ),
            width="100%",
            spacing="4",
            align_items="stretch",
        ),
        rx.fragment(),
    )