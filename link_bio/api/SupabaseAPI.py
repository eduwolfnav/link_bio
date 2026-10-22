import os
import dotenv
from supabase import create_client, Client


class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_PUBLISHABLE_KEY = os.environ.get("SUPABASE_PUBLISHABLE_KEY")

    supabase: Client = create_client(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)

    def featured(self) -> list:
        response = self.supabase.table("featured").select("*").execute()
        print("RESPUESTA SUPABASE:", response.data)  # <-- Esto saldrá en tu terminal
        return response.data if response.data else []

