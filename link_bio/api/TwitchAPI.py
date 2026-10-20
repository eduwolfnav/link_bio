# pip install python-dotenv
# pip install requests

# pip install python-dotenv
# pip install requests

import os
import dotenv
import requests
import time

class TwitchAPI:
    dotenv.load_dotenv()

    CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")

    def __init__(self) -> None:
        self.token = None
        self.token_expired = 0

    def generate_token(self):
        response = requests.post(
            "https://id.twitch.tv/oauth2/token",
            data={
                "client_id": TwitchAPI.CLIENT_ID,
                "client_secret": TwitchAPI.CLIENT_SECRET,
                "grant_type": "client_credentials"
            }
        )

        if response.status_code == 200:
            data = response.json()
            self.token = data["access_token"]
            self.token_expired = time.time() + data["expires_in"]
        else:
            print("Error generando token:", response.json())
            self.token = None
            self.token_expired = 0

    def token_valid(self) -> bool:
        return self.token is not None and time.time() < self.token_expired

    def live(self, user: str) -> bool:
        if not self.token_valid():
            self.generate_token()

        if not self.token:
            return False

        clean_user = user.strip().lower()

        response = requests.get(
            f"https://api.twitch.tv/helix/streams?user_login={clean_user}",
            headers={
                "Client-ID": self.CLIENT_ID, 
                "Authorization": f"Bearer {self.token}"
            }      
        )

        print("ESTADO TWITCH:", response.status_code)
        print("RESPUESTA TWITCH:", response.json())

        if response.status_code == 200:
            data = response.json().get("data", [])
            if len(data) > 0:
                return True

        return False