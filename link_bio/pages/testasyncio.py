import reflex as rx
import link_bio.utils as utils
import link_bio.constants as const
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.views.courses_links import courses_links
from link_bio.components.footer import footer
from link_bio.views.sponsors import sponsors
from link_bio.styles.styles import Size as Size
from link_bio.routes import Route
from link_bio.api.api import hello
from link_bio.state.PageState import PageState
import asyncio

class IndexState(rx.State):
    say_hello: str = ""
    loading: bool = True  # arranca mostrando "Cargando..."

    @rx.event
    async def load_hello(self):
        print(">>> load_hello se ejecutó")
        self.loading = True
        yield
        try:
            self.say_hello = await hello()
        except Exception as e:
            self.say_hello = f"Error: {e}"
        finally:
            self.loading = False

@rx.page(
        route=Route.TESTASYNCIO.value,
        title=utils.cursos_title,
        description=utils.cursos_description,
        image=utils.preview,
        on_load=[IndexState.load_hello, PageState.check_live],
        meta=utils.cursos_meta       
)
def testasyncio() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    False,
                    PageState.is_live
                ),
                
                # Contenedor para lo amarillo con espacio extra arriba y abajo
                rx.vstack(
                    # Centramos lo rojo usando rx.center o width="100%" con text_align
                    rx.center(
                        rx.cond(
                            IndexState.loading,
                            rx.text("Cargando mensaje del backend..."),
                            rx.text(IndexState.say_hello),
                        ),
                        width="100%"
                    ),
                    rx.button("Probar evento", on_click=IndexState.load_hello),
                    width="100%",
                    align_items="center",  # Centra los elementos horizontalmente en este bloque
                    margin_y="2em"         # <--- Aquí le das más espacio arriba y abajo (ajusta los "em" a tu gusto)
                ),
                
                sponsors(),
                width="100%",
                max_width=styles.MAX_WIDTH,
                align_items="start",
                margin_y=Size.BIG.value,
                padding_x=Size.DEFAULT.value,
                spacing="4"
            ),
            width="100%",
        ),
        footer()
    )