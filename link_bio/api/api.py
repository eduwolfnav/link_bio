"""
link_bio/api/api.py
-------------------
PROPÓSITO:
Capa de fachada (Facade) que expone funciones async para Reflex.
Centraliza llamadas a Twitch, Supabase y ConfigCat.

CÓMO SE CONECTA:
- Es importado por state/PageState.py y pages/index.py para obtener datos reactivos.
- Instancia TwitchAPI, SupabaseAPI y ConfigCatAPI como singletons del módulo.
- Cada función async es consumida como backend API por Reflex:
  - hello() -> mensaje de prueba async (simula carga backend)
  - live(user) -> consulta si usuario está en vivo (usa TwitchAPI)
  - featured() -> lista de destacados desde Supabase (usa SupabaseAPI)
  - schedule() -> horario de directos desde ConfigCat (usa ConfigCatAPI)

FLUJO COMPLETO:
api.py -> TwitchAPI/SupabaseAPI/ConfigCatAPI -> Live/Featured models -> PageState -> views/header, featured_link, live_schedule
"""

import asyncio
import link_bio.constants as const
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI
from .ConfigCatAPI import ConfigCatAPI
from link_bio.model.Live import Live
from link_bio.model.Featured import featured

# Singletons de APIs - reutilizan conexión y env vars cargadas
twitch_api = TwitchAPI()
supabase_api = SupabaseAPI()
configcat_api = ConfigCatAPI()

async def hello() -> str:
    """
    Endpoint de prueba async. Simula latencia de backend.
    Usado para verificar que el backend responde.
    """
    await asyncio.sleep(4)
    return "Backend: Mensaje cargado con exito."

async def live(user: str) -> Live:
    """
    Consulta estado en vivo de un usuario de Twitch.
    Delega a TwitchAPI.live() que maneja token OAuth y llamada a Helix.
    """
    return twitch_api.live(user)

async def featured() -> list[featured]:
    """
    Obtiene lista de links destacados desde Supabase.
    Delega a SupabaseAPI.featured() que hace select ordenado.
    """
    return supabase_api.featured()

async def schedule() -> dict:
    """
    Obtiene horario de directos desde ConfigCat.
    Delega a ConfigCatAPI.schedule() que resuelve flag live_schedule con fallback default.
    Retorna dict formato {"0": "18:00hrs", ...} donde 0=Lunes.
    """
    result = configcat_api.schedule()
    return result
