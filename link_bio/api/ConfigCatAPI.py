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
        # FIX: default real, no vacío
        default_schedule_dict = {
            "0": "18:00hrs",
            "1": "19:00hrs",
            "2": "21:00hrs",
            "3": "22:00hrs",
            "4": "22:00hrs"
        }
        default_schedule_str = json.dumps(default_schedule_dict)

        if self.configcat is None:
            print(f"DEBUG: sin SDK KEY, usando default: {default_schedule_dict}")
            return default_schedule_dict

        response = self.configcat.get_value("live_schedule", default_schedule_str)
        print(f"DEBUG ConfigCat raw response: {response}") # ESTE SI SE VE

        if isinstance(response, dict):
            return response

        if isinstance(response, str) and response.strip():
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                return {"horario": response}

        return default_schedule_dict