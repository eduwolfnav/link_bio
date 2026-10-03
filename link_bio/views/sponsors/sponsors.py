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
            spacing="4",
            wrap="wrap", # Permite que bajen si la pantalla es muy estrecha
            width="100%",
            justify_content="start" # Alinea todo el contenido a la izquierda
        ),
        width="100%",
        align_items="start" # Alinea el título y el bloque a la izquierda
    )