"""
link_bio/model/Live.py
----------------------
PROPÓSITO:
Modelo de base de datos para estado de directo. Define si estás en vivo y el título.

CÓMO SE CONECTA:
- Es una tabla SQLModel (table=True) -> crea tabla Live en la DB de Reflex.
- Es usado por state/PageState.py para consultar/actualizar estado en vivo.
- Es consultado por api/api.py en el endpoint /live/{user} para exponer estado a frontend.
- Requiere reflex[db] y greenlet (ver requirements.txt).

FLUJO:
TwitchAPI / SupabaseAPI -> Live (DB) -> PageState -> components/live_schedule.py
"""

import reflex as rx
from sqlmodel import SQLModel, Field

class Live(SQLModel, table=True):
    """Tabla que guarda el estado de directo. Usada por PageState y api.live."""

    id: int | None = Field(default=None, primary_key=True)  # PK autoincremental
    live: bool  # True si estás en directo
    title: str  # Título del directo actual
