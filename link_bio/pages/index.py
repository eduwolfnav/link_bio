"""
link_bio/pages/index.py
-----------------------
PROPÓSITO:
Página principal (ruta /). Es la landing de link_bio con header, links y sponsors.

CÓMO SE CONECTA:
- Usa @rx.page sin route explícita -> es index ("/") por convención de Reflex.
- on_load=PageState.load_index_data carga datos iniciales (live, featured, schedule, timezone).
- Usa components/navbar.py como cabecera fija.
- Usa views/header.py con details=True (muestra bio completa) y datos live desde PageState.
- Usa views/index_links.py con PageState.featured_info (desde Supabase vía api).
- Usa views/sponsors.py para grid de tecnologías.
- Usa components/footer.py como cierre.
- Usa utils.lang() para meta lang, y utils.index_title/description/meta para SEO.
- on_mount llama LOCAL_TIMEZONE_SCRIPT que setea zona horaria del cliente en PageState.

FLUJO:
PageState.load_index_data -> api.live, api.featured, api.schedule -> header, index_links, live_schedule
"""

import reflex as rx
import link_bio.utils as utils
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.components.footer import footer
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.state.PageState import PageState

@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta,
        on_load=PageState.load_index_data       
)
def index() -> rx.Component:
    """Página principal con loading state y contenido completo."""
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.cond(
                PageState.is_loading,
                rx.center(
                    rx.vstack(
                        rx.spinner(size="3"),
                        rx.text("Loading...", color=TextColor.FOOTER.value),
                        align="center",
                        spacing="3",
                    ),
                    height="60vh",
                    width="100%",
                ),
                rx.vstack(
                    header(
                        details=True, 
                        live=PageState.live_status,
                        next_live=PageState.next_live
                    ),
                    index_links(PageState.featured_info),
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
        footer(),
        on_mount=rx.call_script(
            utils.LOCAL_TIMEZONE_SCRIPT,
            callback=PageState.set_timezone
        )
    )
