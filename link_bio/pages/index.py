import reflex as rx
import link_bio.utils as utils
import link_bio.constants as const
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.components.footer import footer
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.state.PageState import PageState
import asyncio

@rx.page(
        title=utils.index_title,
        description=utils.index_description,
        image=utils.preview,
        meta=utils.index_meta,
        on_load=[PageState.check_live, PageState.featured_links]       
)
def index() -> rx.Component:
    # return rx.text("Hola Reflex!", color="blue")

    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    live=PageState.is_live,
                    live_title=PageState.live_title
                ),
                index_links(PageState.featured_info),
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

