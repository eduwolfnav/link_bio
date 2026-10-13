import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                "python.png",
                url="https://www.python.org/"
            ),
            link_sponsor(
                "mongodb.png",
                url="https://www.mongodb.com/es"
            ),
            link_sponsor(
                "Reflex.jpg",
                url="https://reflex.dev/"
            ),
            spacing="3",
            align="center"
        ),
        width="100%",
        align_items="start",
        spacing="3"
    )