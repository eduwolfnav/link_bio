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
    live_schedule: dict = {}
    featured_info: list[featured] = []
    next_live: str = ""
    is_loading: bool = True
    timezone: str = "UTC"

    @rx.event
    def set_timezone(self, tz: str):
        """Se ejecuta desde el navegador, trae 'America/Santiago'"""
        if tz and isinstance(tz, str):
            self.timezone = tz
            print(f"TIMEZONE CLIENTE: {self.timezone}")
            if self.live_schedule:
                self.next_live = utils.next_date(self.live_schedule, self.timezone)
                print(f"NEXT LIVE CON TZ: {self.next_live}")

    @rx.event
    async def load_index_data(self):
        self.is_loading = True
        yield
        
        self.live_status = await live(USER)
        print(f"ESTADO TWITCH: {self.live_status}")

        schedule_data, featured_data = await asyncio.gather(
            asyncio.to_thread(ConfigCatAPI().schedule),
            asyncio.to_thread(SupabaseAPI().featured)
        )

        print(f"SCHEDULE: {schedule_data}")
        self.live_schedule = schedule_data
        self.featured_info = featured_data
        self.next_live = utils.next_date(schedule_data, self.timezone)
        print(f"NEXT LIVE: {self.next_live}")
        
        self.is_loading = False

    # Wrappers para no romper courses.py / testasyncio.py
    @rx.event
    async def check_live(self):
        self.live_status = await live(USER)
        if not self.live_status.live and self.live_schedule:
            self.next_live = utils.next_date(self.live_schedule, self.timezone)

    @rx.event
    def featured_links(self):
        api = SupabaseAPI()
        self.featured_info = api.featured()

    @rx.event
    def get_live_schedule(self):
        api = ConfigCatAPI()
        result = api.schedule()
        self.live_schedule = result
        self.next_live = utils.next_date(result, self.timezone)
