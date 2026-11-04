"""
link_bio/model/Featured.py
--------------------------
PROPÓSITO:
Modelo Pydantic para links destacados (featured). Representa un link con imagen
que se muestra de forma prominente.

CÓMO SE CONECTA:
- Es usado por components/featured_link.py para tipar y renderizar cada featured link.
- Es usado por views/index_links.py o views/courses_links.py para construir la lista de destacados.
- No es tabla de DB, es solo modelo de validación/transporte.
"""

from pydantic import BaseModel

class featured(BaseModel):
    """Modelo de link destacado. Usado en featured_link component."""

    title: str  # Título visible del destacado
    image: str  # Ruta en assets/ (ej: python.jpg)
    url: str    # URL externa a la que apunta
