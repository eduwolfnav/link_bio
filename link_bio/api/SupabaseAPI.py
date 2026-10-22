import os
import dotenv
from supabase import create_client, Client

class SupabaseAPI:
    def __init__(self):
        dotenv.load_dotenv()

    def featured(self) -> list:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
        
        # Si las variables no están presentes (como durante el build en GitHub), 
        # retorna una lista vacía en lugar de romper la compilación.
        if not url or not key:
            return []
            
        supabase: Client = create_client(url, key)
        response = supabase.table("featured").select("*").execute()
        print("RESPUESTA SUPABASE:", response.data)
        return response.data if response.data else []

