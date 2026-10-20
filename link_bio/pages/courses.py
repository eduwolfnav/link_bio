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
        on_load=PageState.check_live        
)
def courses() -> rx.Component:
    # return rx.text("Hola Reflex!", color="blue")

    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(
                    False,
                    PageState.is_live
                ),
                courses_links(),
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