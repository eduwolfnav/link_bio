import asyncio
import link_bio.constants as const
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI
from .ConfigCatAPI import ConfigCatAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import featured

twitch_api = TwitchAPI()
supabase_api = SupabaseAPI()
configcat_api = ConfigCatAPI()

async def hello() -> str:
    await asyncio.sleep(4)
    return "Backend: Mensaje cargado con exito."

async def live(user: str) -> Live:
    return twitch_api.live(user)

async def featured() -> list[featured]:
    return supabase_api.featured()

async def schedule() -> dict: # FIX: era list[schedule]
    result = configcat_api.schedule()
    print(f"SCHEDULE DESDE API: {result}")
    return result # FIX: faltaba return
