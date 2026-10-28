import os
import dotenv
import configcatclient
import json

class ConfigCatAPI:

    def __init__(self) -> None:
        # Cargar .env siempre dentro del init, no a nivel de clase
        dotenv.load_dotenv()
        self.configcat_sdk_key = os.environ.get("CONFIGCAT_SDK_KEY")
        
        self.configcat = None
        if self.configcat_sdk_key:
            self.configcat = configcatclient.get(self.configcat_sdk_key)

    def schedule(self) -> dict:
        # Fallback por si no hay SDK key o no hay conexión
        default_schedule = {"lunes": "19:00hrs", "martes": "19:00hrs"}

        if self.configcat is None:
            return default_schedule

        # Pide el flag. Si en ConfigCat lo tienes como JSON, pon default como dict
        # Si lo tienes como TEXT, pon default como string JSON
        response = self.configcat.get_value("live_schedule", default_schedule)

        # Caso 1: ConfigCat ya te devolvió un dict (modo JSON)
        if isinstance(response, dict):
            return response

        # Caso 2: te devolvió un string, hay que parsearlo
        if isinstance(response, str) and response.strip():
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                # Si no es JSON válido, devuélvelo como texto
                return {"horario": response}

        return default_schedule