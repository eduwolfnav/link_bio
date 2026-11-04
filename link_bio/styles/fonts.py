"""
link_bio/styles/fonts.py
------------------------
PROPÓSITO:
Centraliza familias y pesos de fuente. Permite cambiar tipografía en un solo lugar.

CÓMO SE CONECTA:
- Importado por link_bio/styles/styles.py -> BASE_STYLE usa Font.DEFAULT y FontWeight.LIGHT.
- Font.LOGO se usa en components/navbar.py para el logo.
- Si agregas una nueva fuente, agrégala aquí y en STYLESHEETS de styles.py.
"""

from enum import Enum

class Font(Enum):
    """Familias de fuente disponibles en la app."""

    LOGO = "Rationale"   # Usada en navbar_title_style (logo superior)
    DEFAULT = "Poppins"  # Fuente base de toda la UI (BASE_STYLE)
    TITLE = "Poppins"    # Fuente para headings (h1, h2)

class FontWeight(Enum):
    """Pesos de fuente. Corresponden a los pesos cargados en Google Fonts."""

    LIGHT = "300"   # Peso por defecto en BASE_STYLE y button_body_style
    MEDIUM = "500"  # Usado en títulos de botones y headings
