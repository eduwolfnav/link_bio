"""
link_bio/api/TwitchAPI.py
-------------------------
PROPÓSITO:
Cliente para Twitch Helix API. Consulta si un usuario está en directo.

CÓMO SE CONECTA:
- Usado por api/api.py -> live(user) que alimenta model/Live y PageState.
- Requiere TWITCH_CLIENT_ID y TWITCH_CLIENT_SECRET en env vars.
- Maneja generación y renovación de token OAuth client_credentials.
- Retorna modelo Live(live=True/False, title="") usado en views/header.py.

FLUJO:
Twitch Helix /streams?user_login= -> TwitchAPI.live() -> Live model -> api.live() -> PageState -> header (botón En vivo + badge morado)
"""

import os
import dotenv
import requests
import time

from link_bio.model.Live import Live

class TwitchAPI:
    """Cliente Twitch API con manejo de token OAuth. Consulta estado live."""

    dotenv.load_dotenv()

    CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")

    def __init__(self) -> None:
        self.token = None
        self.token_expired = 0

    def generate_token(self):
        """
        Genera token OAuth2 client_credentials para Helix.
        Guarda access_token y tiempo de expiración.
        """
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
            self.token = None
            self.token_expired = 0

    def token_valid(self) -> bool:
        """Verifica si token actual aún no expira."""
        return self.token is not None and time.time() < self.token_expired

    def live(self, user: str) -> Live:
        """
        Consulta si usuario está en directo.

        Args:
            user: username de Twitch (ej: eduwolfnav)

        Returns:
            Live(live=True, title=... ) si está en vivo, Live(live=False, title="") si no.
        """
        if not self.token_valid():
            self.generate_token()

        if not self.token:
            return Live(live=False, title="")

        clean_user = user.strip().lower()

        response = requests.get(
            f"https://api.twitch.tv/helix/streams?user_login={clean_user}",
            headers={
                "Client-ID": self.CLIENT_ID, 
                "Authorization": f"Bearer {self.token}"
            }      
        )

        if response.status_code == 200:
            data = response.json().get("data", [])
            if len(data) > 0:
                return Live(live=True, title=data[0]["title"])

        return Live(live=False, title="")
