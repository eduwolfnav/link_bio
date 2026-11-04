"""
link_bio/link_bio.py
--------------------
PROPÓSITO:
Entry point de la aplicación. Aquí se ensambla todo: crea el backend FastAPI,
registra las APIs personalizadas y monta la app de Reflex con estilos y analytics.

CÓMO SE CONECTA:
- Importa styles.BASE_STYLE y STYLESHEETS desde link_bio/styles/ -> define el look global.
- Importa const.G_TAG desde link_bio/constants.py -> inyecta Google Analytics.
- Importa las páginas index, courses, testasyncio desde link_bio/pages/ -> son las rutas que Reflex renderiza.
- Importa hello y live desde link_bio/api/api.py -> son endpoints que se exponen vía FastAPI.
- FastAPI app se inyecta en Reflex vía api_transformer, permitiendo que /hola y /live/{user} convivan con la UI.

FLUJO:
FastAPI (api) + Reflex (UI) -> rx.App -> se exporta a public/ para Vercel y se ejecuta en Railway.
"""

import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as const

from fastapi import FastAPI
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.pages.testasyncio import testasyncio
from link_bio.api.api import hello, live

# Backend FastAPI para exponer endpoints propios junto a la API interna de Reflex.
fastapi_app = FastAPI()

# Registro de rutas API personalizadas. Estas rutas son consumidas por componentes como live_schedule.
fastapi_app.add_api_route("/hola", hello)
fastapi_app.add_api_route("/live/{user}", live)

# App principal de Reflex. Aquí se une frontend + backend + estilos + analytics.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}",
            async_=True,
        ),
        rx.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-PMDZDF543W');
            """
        ),
    ],
    api_transformer=fastapi_app,  # Conecta FastAPI con Reflex para que /hola y /live funcionen en prod.
)
