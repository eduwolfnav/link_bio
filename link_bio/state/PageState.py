import reflex as rx
import link_bio.utils as utils
from link_bio.api.api import live, schedule
from link_bio.api.SupabaseAPI import SupabaseAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import featured
from link_bio.api.ConfigCatAPI import ConfigCatAPI
import asyncio

USER = "eduwolfnav"

class PageState(rx.State):
    live_status: Live = Live(live=False, title="")
    live_schedule: dict = {"lunes": "19:00hrs", "martes": "19:00hrs"}
    featured_info: list[featured] = []
    next_live: str = ""
    is_loading: bool = True

    # --- MÉTODO NUEVO, EL BUENO ---
    @rx.event
    async def load_index_data(self):
        self.is_loading = True
        yield
        
        self.live_status = await live(USER)
        
        # Corremos Supabase y ConfigCat en paralelo
        schedule_data, featured_data = await asyncio.gather(
            asyncio.to_thread(ConfigCatAPI().schedule),
            asyncio.to_thread(SupabaseAPI().featured)
        )
        
        self.live_schedule = schedule_data
        self.featured_info = featured_data
        self.next_live = utils.next_date(schedule_data)
        self.is_loading = False

    # --- MÉTODOS VIEJOS, para que courses.py no se caiga ---
    # Son wrappers que llaman al nuevo

    @rx.event
    async def check_live(self):
        self.live_status = await live(USER)
        if not self.live_status.live:
            result = await asyncio.to_thread(ConfigCatAPI().schedule)
            self.live_schedule = result
            self.next_live = utils.next_date(result)

    @rx.event
    def featured_links(self):
        self.featured_info = SupabaseAPI().featured()

    @rx.event
    def get_live_schedule(self):
        result = ConfigCatAPI().schedule()
        self.live_schedule = result
        self.next_live = utils.next_date(result)
