"""
link_bio/pages/testasyncio.py
-----------------------------
PROPÓSITO:
Página de prueba para eventos async (ruta /testasyncio). Demuestra carga async desde backend.

CÓMO SE CONECTA:
- Usa @rx.page con Route.TESTASYNCIO.value definido en routes.py.
- Define IndexState interno con estado say_hello y loading, y evento load_hello que llama api.hello().
- on_load=[IndexState.load_hello, PageState.check_live] ejecuta dos cargas al entrar.
- Usa views/header.py compacto, y muestra mensaje del backend con rx.cond loading.
- Es ejemplo didáctico de rx.State + async/await en Reflex.

FLUJO:
IndexState.load_hello -> api.hello() -> asyncio.sleep(4) -> mensaje -> UI
"""

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
    """Estado local de prueba para demo async. No es PageState global."""

    say_hello: str = ""
    loading: bool = True

    @rx.event
    async def load_hello(self):
        """Evento async que llama backend api.hello() con manejo de error."""
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
    """Página de prueba async con botón para recargar mensaje del backend."""
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    details=False,
                    live=PageState.live_status,
                    next_live=PageState.next_live
                ),
                
                rx.vstack(
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
                    align_items="center",
                    margin_y="2em"
                ),
                
                sponsors(),
                width="100%",
                max_width=styles.MAX_WIDTH,
                align_items="start",
                margin_y=Size.DEFAULT.value,
                padding_x=Size.DEFAULT.value,
                spacing="4"
            ),
            width="100%",
        ),
        footer()
    )
