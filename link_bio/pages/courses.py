"""
link_bio/pages/courses.py
-------------------------
PROPÓSITO:
Página de cursos (ruta /courses). Muestra cursos recomendados de Python.

CÓMO SE CONECTA:
- Usa @rx.page con Route.COURSES.value (/courses) definido en routes.py.
- on_load=PageState.load_index_data para reutilizar carga de live_status y sponsors.
- Usa views/header.py con details=False (modo compacto sin bio ni stats).
- Usa views/courses_links.py con lista estática de cursos de YouTube.
- Usa views/sponsors.py y components/footer.py igual que index.
- SEO viene de utils.cursos_title/description/meta.

Es independiente de featured, pero comparte lógica de live con index.
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
from link_bio.state.PageState import PageState

@rx.page(
    route=Route.COURSES.value,
    title=utils.cursos_title,
    description=utils.cursos_description,
    image=utils.preview,
    meta=utils.cursos_meta,
    on_load=PageState.load_index_data
)
def courses() -> rx.Component:
    """Página de cursos con header compacto y lista de cursos."""
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.cond(
                PageState.is_loading,
                rx.center(rx.spinner(size="3"), height="60vh", width="100%"),
                rx.vstack(
                    header(
                        details=False,
                        live=PageState.live_status,
                        next_live=PageState.next_live
                    ),
                    courses_links(),
                    sponsors(),
                    width="100%",
                    max_width=styles.MAX_WIDTH,
                    align_items="start",
                    margin_y=Size.DEFAULT.value,
                    padding_x=Size.DEFAULT.value,
                    spacing="4"
                ),
            ),
            width="100%",
        ),
        footer()
    )
