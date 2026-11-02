import os
import dotenv
import configcatclient
import json

class ConfigCatAPI:

    def __init__(self) -> None:
        dotenv.load_dotenv()
        self.configcat_sdk_key = os.environ.get("CONFIGCAT_SDK_KEY")
        
        self.configcat = None
        if self.configcat_sdk_key:
            self.configcat = configcatclient.get(self.configcat_sdk_key)

    def schedule(self) -> dict:
        # Tu diccionario real para usar en la app
        default_schedule_dict = {"lunes": "19:00hrs", "martes": "19:00hrs"}
        # El mismo, pero convertido a texto para que ConfigCat no se queje
        default_schedule_str = json.dumps(default_schedule_dict)

        if self.configcat is None:
            return default_schedule_dict

        # AQUÍ ESTÁ EL ARREGLO: le pasamos STRING, no dict
        response = self.configcat.get_value("live_schedule", default_schedule_str)

        # Si ya viene como dict (por si en el futuro lo cambias a JSON real)
        if isinstance(response, dict):
            return response

        # Si viene como string (como lo tienes ahora en ConfigCat)
        if isinstance(response, str) and response.strip():
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                return {"horario": response}

        return default_schedule_dict