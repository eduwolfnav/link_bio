import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://eduwolfnav.up.railway.app",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://eduwolfnav.vercel.app"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)