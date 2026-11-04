"""
link_bio/styles/colors.py
-------------------------
PROPÓSITO:
Define la paleta de colores central de la app. Evita colores hardcodeados en componentes.

CÓMO SE CONECTA:
- Es importado por link_bio/styles/styles.py -> BASE_STYLE usa Color.BACKGROUND, SECONDARY, etc.
- Es usado indirectamente por todos los components/ y views/ a través de styles.py.
- Si cambias PRIMARY aquí, cambia el acento en toda la UI.
"""

from enum import Enum

class Color(Enum):
    """Colores base de la UI. Usados en styles.py como Color.BACKGROUND.value"""

    PRIMARY = "#70b8ff"      # Acento principal (links destacados)
    SECONDARY = "#0d2849"    # Fondo de botones (link_button)
    BACKGROUND = "#0c0c0c"   # Fondo global de la app (BASE_STYLE)
    CONTENT = "#1a5195"      # Hover de botones y bordes activos
    PURPLE = "#9146ff"       # Color Twitch / destacado especial
    BORDER = "4px solid #1a5195"  # Borde usado en algunos contenedores

class TextColor(Enum):
    """Colores de texto, separados para mantener contraste."""

    HEADER = "#3b9eff"  # Títulos de header
    BODY = "#dbdbe0"    # Texto principal (botones, títulos)
    FOOTER = "#a3a3a4"  # Texto secundario / descripciones
