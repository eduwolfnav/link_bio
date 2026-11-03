import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
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
                    # si agregas un décimo acá, se irá solo a la 2da fila
                    columns="7", # <- máximo 7 por línea
                    spacing="3",
                    width="100%",
                ),
                width="100%",
                align_items="start",
                spacing="3"
            )