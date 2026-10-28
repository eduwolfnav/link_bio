import asyncio
import link_bio.constants as const
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import featured

twitch_api = TwitchAPI()
supabase_api = SupabaseAPI()

async def hello() -> str:
    await asyncio.sleep(4)
    return "Backend: Mensaje cargado con exito."

async def live(user: str) -> Live:
    return twitch_api.live(user)
    
    #if user == "eduwolfnav":
    #    return True
    #return False

async def featured() -> list[featured]:
    return supabase_api.featured()
