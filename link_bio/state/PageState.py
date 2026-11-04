"""
link_bio/state/PageState.py
---------------------------
PROPÓSITO:
Estado global de la app (rx.State). Centraliza datos reactivos que usan todas las páginas.

CÓMO SE CONECTA:
- Es el cerebro de la app. Todas las páginas (pages/index.py, pages/courses.py) usan on_load=PageState.load_index_data.
- Usa api/api.py -> live() para consultar Twitch (TwitchAPI -> Live model).
- Usa SupabaseAPI.featured() para destacados y ConfigCatAPI.schedule() para horario.
- Usa utils.next_date() para calcular próximo live según timezone del cliente.
- Expone variables reactivas:
  - live_status: Live (live: bool, title: str) -> usado en views/header.py
  - live_schedule: dict {"0": "18:00hrs", ...} -> usado en components/live_schedule.py
  - featured_info: list[featured] -> usado en views/index_links.py vía featured_link
  - next_live: str -> usado en header para "Próximo live"
  - is_loading: bool -> usado en pages/index.py para spinner
  - timezone: str -> seteado desde navegador via set_timezone (LOCAL_TIMEZONE_SCRIPT)

FLUJO COMPLETO:
TwitchAPI / SupabaseAPI / ConfigCatAPI -> api.py -> PageState.load_index_data (asyncio.gather paralelo) -> live_status, featured_info, live_schedule, next_live -> header, index_links, live_schedule, footer
"""

import reflex as rx
import link_bio.utils as utils
from link_bio.api.api import live, schedule
from link_bio.api.SupabaseAPI import SupabaseAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import featured
from link_bio.api.ConfigCatAPI import ConfigCatAPI
import asyncio

# Usuario de Twitch a consultar. Debe coincidir con env var o nombre real.
USER = "eduwolfnav"

class PageState(rx.State):
    """Estado global reactivo. Maneja carga inicial y zona horaria del cliente."""

    live_status: Live = Live(live=False, title="")
    live_schedule: dict = {}
    featured_info: list[featured] = []
    next_live: str = ""
    is_loading: bool = True
    timezone: str = "UTC"

    @rx.event
    def set_timezone(self, tz: str):
        """
        Callback desde el navegador. Recibe timezone del cliente via LOCAL_TIMEZONE_SCRIPT.

        Args:
            tz: String tipo "America/Santiago" desde Intl.DateTimeFormat().resolvedOptions().timeZone

        Actualiza next_live recalculando con la zona horaria real del usuario.
        """
        if tz and isinstance(tz, str):
            self.timezone = tz
            if self.live_schedule:
                self.next_live = utils.next_date(self.live_schedule, self.timezone)

    @rx.event
    async def load_index_data(self):
        """
        Carga inicial de la app. Usado en on_load de pages/index.py y pages/courses.py.

        - Activa is_loading para mostrar spinner
        - Consulta live_status async (TwitchAPI)
        - En paralelo (asyncio.gather) consulta schedule (ConfigCat) y featured (Supabase) en threads
        - Calcula next_live con utils.next_date y desactiva loading

        Paralelización evita bloqueo secuencial de APIs.
        """
        self.is_loading = True
        yield
        
        self.live_status = await live(USER)

        schedule_data, featured_data = await asyncio.gather(
            asyncio.to_thread(ConfigCatAPI().schedule),
            asyncio.to_thread(SupabaseAPI().featured)
        )

        self.live_schedule = schedule_data
        self.featured_info = featured_data
        self.next_live = utils.next_date(schedule_data, self.timezone)
        
        self.is_loading = False

    # Wrappers de compatibilidad para no romper pages que usaban métodos antiguos
    @rx.event
    async def check_live(self):
        """Wrapper que solo actualiza live_status y next_live. Usado en testasyncio.py."""
        self.live_status = await live(USER)
        if not self.live_status.live and self.live_schedule:
            self.next_live = utils.next_date(self.live_schedule, self.timezone)

    @rx.event
    def featured_links(self):
        """Wrapper sincrónico para recargar solo featured. Útil para debug o refresh manual."""
        api = SupabaseAPI()
        self.featured_info = api.featured()

    @rx.event
    def get_live_schedule(self):
        """Wrapper sincrónico para recargar solo schedule. Recalcula next_live."""
        api = ConfigCatAPI()
        result = api.schedule()
        self.live_schedule = result
        self.next_live = utils.next_date(result, self.timezone)
