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
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.cond(
                PageState.is_loading,
                # Pantalla de carga: spinner + texto, centrado entre navbar y footer
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
        # Zona horaria del cliente: directo en el root y sin lambda
        on_mount=rx.call_script(
            utils.LOCAL_TIMEZONE_SCRIPT,
            callback=PageState.set_timezone
        )
    )