import os
import reflex as rx

# En local no defines nada y Reflex usa localhost:8000.
# En Railway/Vercel defines API_URL_PROD con la URL del backend.
api_url = os.getenv("API_URL_PROD")

config = rx.Config(
    app_name="link_bio",
    **({"api_url": api_url} if api_url else {}),
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://eduwolfnav.vercel.app",
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ],
)