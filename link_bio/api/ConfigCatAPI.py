"""
link_bio/api/ConfigCatAPI.py
----------------------------
PROPÓSITO:
Cliente para ConfigCat (feature flags). Obtiene horario de directos configurable sin redeploy.

CÓMO SE CONECTA:
- Es usado por api/api.py -> schedule() que es consumido por PageState.live_schedule.
- Requiere env var CONFIGCAT_SDK_KEY en .env o Railway.
- Si no hay SDK key, usa fallback default local.
- El flag en ConfigCat Dashboard se llama "live_schedule" y guarda JSON string o dict.

FLUJO:
ConfigCat Dashboard (flag live_schedule) -> ConfigCatAPI.schedule() -> api.schedule() -> PageState -> components/live_schedule.py
"""

import os
import dotenv
import configcatclient
import json

class ConfigCatAPI:
    """Cliente de ConfigCat para flags remotos. Maneja fallback si no hay SDK key."""

    def __init__(self) -> None:
        dotenv.load_dotenv()
        self.configcat_sdk_key = os.environ.get("CONFIGCAT_SDK_KEY")
        
        self.configcat = None
        if self.configcat_sdk_key:
            self.configcat = configcatclient.get(self.configcat_sdk_key)

    def schedule(self) -> dict:
        """
        Obtiene horario de directos desde ConfigCat.

        Lógica:
        - Si no hay cliente (sin SDK key), retorna default local.
        - Si respuesta es dict, retorna directo.
        - Si es string JSON, parsea a dict.
        - Si falla parseo, retorna default.

        Returns:
            dict con formato {"0": "18:00hrs", "1": "19:00hrs", ...} 0=Lunes
        """
        default_schedule_dict = {
            "0": "18:00hrs",
            "1": "19:00hrs",
            "2": "21:00hrs",
            "3": "22:00hrs",
            "4": "22:00hrs"
        }
        default_schedule_str = json.dumps(default_schedule_dict)

        if self.configcat is None:
            return default_schedule_dict

        response = self.configcat.get_value("live_schedule", default_schedule_str)

        if isinstance(response, dict):
            return response

        if isinstance(response, str) and response.strip():
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                return {"horario": response}

        return default_schedule_dict
