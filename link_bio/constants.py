"""
link_bio/constants.py
---------------------
PROPÓSITO:
Centraliza todas las URLs externas y el ID de analytics. Evita hardcodear links
en múltiples componentes y facilita el mantenimiento.

CÓMO SE CONECTA:
- Es importado por views/header.py, views/sponsors.py, components/link_button.py, etc.
- link_bio.py lo usa para G_TAG (Google Analytics).
- Si cambias una URL aquí, se actualiza en toda la app automáticamente.
"""

# --- Analytics ---
G_TAG = "G-PMDZDF543W"  # ID de Google Analytics, usado en link_bio.py

# --- Cabecera / Perfiles principales ---
GITHUB_URL = "https://github.com/mouredev"
INSTAGRAM_URL = "https://instagram.com/mouredev"
SPOTIFY_URL = "https://open.spotify.com/show/0HFmaAOJTJ57nc6mQD4vJA"

# --- Comunidad ---
YOUTUBE_URL = "https://youtube.com/@mouredev"
DISCORD_URL = "https://discord.gg/mouredev"
TWITCH_URL = "https://twitch.tv/mouredev"

# --- Newsletter ---
NEWSLETTER_URL = ""

# --- Recursos y más ---
RESOURCES_URL = "https://mouredev.pro/recursos"
BOOK_URL = "https://mouredev.com/libro-git"
YOUTUBE_SECONDARY_URL = "https://youtube.com/@mouredevtv"
BOOKS_URL = "https://amazon.es/shop/mouredev/list/2ZIHJJFJ9AVZ3"
SETUP_URL = "https://mouredev.com/setup"
MOUREDEV_URL = "https://mouredev.com"
COFFEE_URL = "https://buymeacoffee.com/mouredev"
REPO_URL = "https://github.com/mouredev/python-web"

# --- Contacto ---
MYPUBLICINBOX_URL = "https://mypublicinbox.com/mouredev"
EMAIL = "braismoure@mouredev.com"

# --- Sponsors ---
GITHUB_STAR_URL = "https://stars.github.com/profiles/mouredev"

# --- Cursos ---
JAVA_COURSE_URL = "https://mouredev.link/java"
PYTHON_COURSE_URL = "https://mouredev.link/python"
GIT_COURSE_URL = "https://mouredev.link/git"
SQL_COURSE_URL = "https://mouredev.link/sql"
LANGUAGES_COURSE_URL = "https://mouredev.link/lenguajes"
