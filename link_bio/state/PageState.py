import reflex as rx
from link_bio.api.api import live, featured
from link_bio.api.SupabaseAPI import SupabaseAPI

USER = "eduwolfnav"

class PageState(rx.State):

    is_live: bool = False
    live_title: str = ""
    featured_info: list

    async def check_live(self):
        live_data = await live(USER)
        self.is_live = live_data.get("live", False)
        self.live_title = live_data.get("title") or ""

    featured_info: list[dict] = []

    async def featured_links(self):
        """Método que se conecta a Supabase y actualiza la lista"""
        api = SupabaseAPI()
        self.featured_info = api.featured()
