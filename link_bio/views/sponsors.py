import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                "python.jpg",
                url="https://www.python.org/"
            ),
            link_sponsor(
                "fastapi.jpg",
                url="https://fastapi.tiangolo.com/"
            ),
            link_sponsor(
                "reflexlogo.jpg",
                url="https://reflex.dev/"
            ),
            link_sponsor(
                "dockerfile.jpg",
                url="https://www.docker.com/"
            ),
            link_sponsor(
                "github.jpg",
                url="https://github.com/"
            ),
            link_sponsor(
                "vercel.jpg",
                url="https://vercel.com/"
            ),
            link_sponsor(
                "railway.jpg",
                url="https://railway.com/"
            ),
            link_sponsor(
                "supabase.jpg",
                url="https://supabase.com/"
            ),
            spacing="3",
            align="center"
        ),
        width="100%",
        align_items="start",
        spacing="3"
    )