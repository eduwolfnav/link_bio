import asyncio
import link_bio.constants as const
from .TwitchAPI import TwitchAPI

twitch_api = TwitchAPI()

async def hello() -> str:
    await asyncio.sleep(4)
    return "Mensaje cargado con exito..."

async def live(user: str) -> bool:
    return twitch_api.live(user)
    
    #if user == "eduwolfnav":
    #    return True
    #return False
