import reflex as rx
from link_bio.api.api import live
from link_bio.api.SupabaseAPI import SupabaseAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import featured
from link_bio.api.ConfigCatAPI import ConfigCatAPI

USER = "eduwolfnav"

class PageState(rx.State):

    live_status: Live = Live(live=False, title="")
    live_schedule: dict = {"lunes": "19:00hrs", "martes": "19:00hrs"} # valor por defecto
    featured_info: list[featured] = []

    async def check_live(self):
        self.live_status = await live(USER)

    def featured_links(self):
        """Método que se conecta a Supabase y actualiza la lista"""
        api = SupabaseAPI()
        self.featured_info = api.featured()

    def get_live_schedule(self):
        api = ConfigCatAPI()
        self.live_schedule = api.schedule()
