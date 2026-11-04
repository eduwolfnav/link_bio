"""
rxconfig.py
-----------
PROPÓSITO:
Configuración central de Reflex. Define cómo se construye y dónde se conecta
el frontend con el backend.

CÓMO SE CONECTA:
- Es leído automáticamente por Reflex al hacer `reflex run` o `reflex export`.
- `api_url` se inyecta desde la variable de entorno API_URL_PROD (Railway en producción).
  Si no existe, Reflex usa localhost:8000 (desarrollo local).
- `cors_allowed_origins` permite que el frontend en Vercel y localhost hablen con el backend.
- Los plugins (Sitemap, Tailwind, Radix) son usados por todos los componentes en link_bio/components/ y views/.
"""

import os
import reflex as rx

# URL del backend en producción (Railway). En local se deja vacía y Reflex usa localhost:8000.
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
