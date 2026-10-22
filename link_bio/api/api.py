import asyncio
import link_bio.constants as const
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI

twitch_api = TwitchAPI()
supabase_api = SupabaseAPI()

async def hello() -> str:
    await asyncio.sleep(4)
    return "Mensaje cargado con exito..."

async def live(user: str) -> dict:
    return twitch_api.live(user)
    
    #if user == "eduwolfnav":
    #    return True
    #return False

async def featured() -> list:
    return supabase_api.featured()
