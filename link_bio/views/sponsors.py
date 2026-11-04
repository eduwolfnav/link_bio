"""
link_bio/views/sponsors.py
--------------------------
PROPÓSITO:
Vista de sponsors / tecnologías. Muestra grid de logos de las tecnologías usadas.

CÓMO SE CONECTA:
- Usado por pages/index.py como sección final antes del footer.
- Usa components/title.py para título "Colaboran".
- Usa components/link_sponsor.py para cada logo (mantiene proporción con width auto).
- Grid con columns="7" máximo por línea, responsive.

Si agregas un décimo logo, se va automáticamente a segunda fila por el grid.
"""

import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
    """
    Grid de logos de tecnologías.
    Cada link_sponsor es logo clickeable a web oficial.
    Stack: Python, FastAPI, Reflex, Docker, GitHub, Vercel, Railway, Supabase, ConfigCat.
    """
    return rx.vstack(
                title("Colaboran"),
                rx.grid(
                    link_sponsor(
                        "python.png",
                        url="https://www.python.org/"
                    ),
                    link_sponsor(
                        "fastapi.png",
                        url="https://fastapi.tiangolo.com/"
                    ),
                    link_sponsor(
                        "reflex.png",
                        url="https://reflex.dev/"
                    ),
                    link_sponsor(
                        "dockerfile.png",
                        url="https://www.docker.com/"
                    ),
                    link_sponsor(
                        "github.png",
                        url="https://github.com/"
                    ),
                    link_sponsor(
                        "vercel.png",
                        url="https://vercel.com/"
                    ),
                    link_sponsor(
                        "railway.png",
                        url="https://railway.com/"
                    ),
                    link_sponsor(
                        "supabase.png",
                        url="https://supabase.com/"
                    ),
                    link_sponsor(
                        "configcat.png",
                        url="https://configcat.com/"
                    ),
                    columns="7",
                    spacing="3",
                    width="100%",
                ),
                width="100%",
                align_items="start",
                spacing="3"
            )
