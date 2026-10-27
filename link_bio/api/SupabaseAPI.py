import os
import dotenv
from supabase import create_client, Client
from link_bio.model.Featured import featured

class SupabaseAPI:
    def __init__(self):
        dotenv.load_dotenv()

    def featured(self) -> list[featured]:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")

        if not url or not key:
            return []

        supabase: Client = create_client(url, key)
        # Orden ascendente: 1, 2, 3...
        response = supabase.table("featured").select("*").order("id", desc=False).execute()

# Si los quieres al revés, 3, 2, 1:
# response = supabase.table("featured").select("*").order("id", desc=True).execute()

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

        print("Featured data:", featured_data)  # Debug printeado para verificar si los datos se carg
        return featured_data