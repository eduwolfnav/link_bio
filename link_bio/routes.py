"""
link_bio/routes.py
------------------
PROPÓSITO:
Define de forma tipada todas las rutas de la app. Evita strings mágicos y
centraliza el routing.

CÓMO SE CONECTA:
- Es usado por link_bio/pages/ para registrar cada página en Reflex.
- Es usado por components/navbar.py y link_button.py para navegar entre páginas.
- Si agregas una nueva página, agrégala aquí primero.
"""

from enum import Enum

class Route(Enum):
    """Rutas principales de la aplicación."""

    INDEX = "/"  # Página principal, renderiza pages/index.py
    COURSES = "/cursos"  # Listado de cursos, renderiza pages/courses.py
    TESTASYNCIO = "/testasyncio"  # Página de pruebas async, renderiza pages/testasyncio.py
