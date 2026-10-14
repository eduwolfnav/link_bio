import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://eduwolfnav.up.railway.app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)