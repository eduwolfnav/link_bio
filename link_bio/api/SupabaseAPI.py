"""
link_bio/api/SupabaseAPI.py
---------------------------
PROPÓSITO:
Cliente para Supabase. Obtiene links destacados desde tabla "featured".

CÓMO SE CONECTA:
- Usado por api/api.py -> featured() que alimenta views/index_links.py vía featured_link component.
- Requiere env vars SUPABASE_URL y SUPABASE_PUBLISHABLE_KEY.
- Si faltan credenciales, retorna lista vacía (no rompe app).
- Tabla esperada: featured(id, title, image, url) ordenada asc por id, limit 2.

FLUJO:
Supabase table featured -> SupabaseAPI.featured() -> api.featured() -> PageState -> featured_link -> index_links
"""

import os
import dotenv
from supabase import create_client, Client
from link_bio.model.Featured import featured

class SupabaseAPI:
    """Cliente Supabase para tabla featured. Maneja fallback sin credenciales."""

    def __init__(self):
        dotenv.load_dotenv()

    def featured(self) -> list[featured]:
        """
        Obtiene destacados desde Supabase.

        - Crea cliente con URL y key de env vars.
        - Hace select * from featured order by id asc limit 2.
        - Mapea cada row a modelo Pydantic featured(title, image, url).

        Returns:
            Lista de featured. Vacía si no hay credenciales o no hay datos.
        """
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")

        if not url or not key:
            return []

        supabase: Client = create_client(url, key)
        response = supabase.table("featured").select("*").order("id", desc=False).limit(2).execute()

        featured_data = []
        if response.data:
            for item in response.data:
                featured_data.append(
                    featured(
                        title=item["title"], 
                        image=item["image"], 
                        url=item["url"]
                    )
                )

        return featured_data
