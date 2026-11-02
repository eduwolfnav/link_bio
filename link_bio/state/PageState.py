import reflex as rx
import link_bio.utils as utils
from link_bio.api.api import live, schedule
from link_bio.api.SupabaseAPI import SupabaseAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import featured
from link_bio.api.ConfigCatAPI import ConfigCatAPI

USER = "eduwolfnav"

class PageState(rx.State):

    live_status: Live = Live(live=False, title="")
    live_schedule: dict = {"lunes": "19:00hrs", "martes": "19:00hrs"}
    featured_info: list[featured] = []
    next_live: str = ""


    async def check_live(self):
        self.live_status = await live(USER)
        print(f"ESTADO TWITCH: {self.live_status}")
        if not self.live_status.live:
            result = await schedule()
            print(f"SCHEDULE CUANDO ESTOY LIVE: {result}")
            self.live_schedule = result
            # FIX: next_date NO es async, no lleva await
            self.next_live = utils.next_date(result)
            print(f"NEXT LIVE: {self.next_live}")

    def featured_links(self):
        api = SupabaseAPI()
        self.featured_info = api.featured()

    def get_live_schedule(self):
        api = ConfigCatAPI()
        result = api.schedule()
        print(f"SCHEDULE INICIAL: {result}")
        self.live_schedule = result
        self.next_live = utils.next_date(result)
