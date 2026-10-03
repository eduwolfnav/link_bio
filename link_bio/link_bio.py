import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
from link_bio.views.sponsors.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    # return rx.text("Hola Reflex!", color="blue")

    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                width="100%",
                max_width=styles.MAX_WIDTH,
                align_items="start",       # Permite que el header y links aprovechen todo el ancho sin deformarse
                margin_y=Size.BIG.value,
                padding_x=Size.DEFAULT.value,    # Padding lateral para evitar que toque los bordes en móviles
                spacing="3"
            ),
            width="100%",
        ),
        footer()
    )
        

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS
)
app.add_page(
    index,
    title="eduwolf.nav",
    description="Hola, mi nombre es Edu. Soy ingeniero en ejecución en informática, y me gusta escribir.",
    image="avatar.png"
)
# app.compile()

# reflex run
# pip install --upgrade reflex # Actualiza reflex
# pip install --upgrade pip # Actualiza el gestor de dependencias

# Para cambiar version de Reflex.

# C:\UTIL\Python\webPython\link_bio\requirements.txt
# reflex==0.9.12
# reflex==0.3.2

# pip install -r ./requirements.txt
# reflex --version


### DESPIEGUE

# reflex login

# reflex deploy

# reflex cloud apps list
# reflex cloud project list

# reflex export --frontend-only # crear Build de Produccion empaquetada en un .zip
# unzip frontend.zip -d public
# Expand-Archive -Path frontend.zip -DestinationPath public

# reflex cloud apps status 7bcb5522-4ceb-4b9d-9a9f-10aced36a231 --watch

# Crear fichero build.sh
# sh build.sh