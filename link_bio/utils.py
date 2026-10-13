import reflex as rx

# Común

def lang() -> rx.components:
    return rx.script("document.documentElement.lang='es'")

preview="avatar.png"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview}
]

# Index
index_title = "eduwolf.nav"
index_description="Hola, mi nombre es Edu. Soy ingeniero en ejecución en informática, y me gusta escribir."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)


# Cursos
cursos_title = "eduwolf.nav | Cursos"
cursos_description="Este es un listado de cursos gratis de programación y desarrollo web."

cursos_meta = [
    {"name": "og:title", "content": cursos_title},
    {"name": "og:description", "content": cursos_description}
]
cursos_meta.extend(_meta)