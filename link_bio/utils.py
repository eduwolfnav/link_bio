"""
link_bio/utils.py
-----------------
PROPÓSITO:
Utilidades compartidas: SEO, metadatos, zona horaria y cálculo de próximo directo.

CÓMO SE CONECTA:
- lang(), index_title, index_meta, cursos_title, etc. son importados por pages/index.py y pages/courses.py
  para configurar <head>, OpenGraph y SEO.
- next_date() y LOCAL_TIMEZONE_SCRIPT son usados por components/live_schedule.py para mostrar
  cuándo es el próximo directo en la zona horaria del cliente.
- MONTHS y WEEKDAYS centralizan la traducción a español, usados solo dentro de este módulo.
"""

from datetime import datetime, timedelta
import re
import reflex as rx
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

# --- Configuración de idioma y SEO base ---

def lang() -> rx.components:
    """
    Retorna script que fuerza lang='es' en <html>.
    Usado en el layout principal (pages/index.py).
    """
    return rx.script("document.documentElement.lang='es'")

# Imagen por defecto para OpenGraph (preview en redes sociales).
preview = "EduWolf.Nav.jpeg"

# Metadatos base que se comparten en todas las páginas.
_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview}
]

# --- Metadatos para página INDEX ---
index_title = "eduwolf.nav"
index_description = "Hola, mi nombre es Edu. Soy ingeniero en ejecución en informática, y me gusta escribir."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)

# --- Metadatos para página CURSOS ---
cursos_title = "eduwolf.nav | Cursos"
cursos_description = "Este es un listado de cursos gratis de programación y desarrollo web."

cursos_meta = [
    {"name": "og:title", "content": cursos_title},
    {"name": "og:description", "content": cursos_description}
]
cursos_meta.extend(_meta)

# --- Lógica de zona horaria para directos ---

# Script JS que obtiene la zona horaria del cliente (ej: America/Santiago).
LOCAL_TIMEZONE_SCRIPT = "Intl.DateTimeFormat().resolvedOptions().timeZone"

# Zona horaria base donde tú haces los directos.
BASE_TIMEZONE = "America/Santiago"

WEEKDAYS = {
    0: "Lunes",
    1: "Martes", 
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

MONTHS = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

def _parse_hour(raw: str) -> tuple[int, int] | None:
    """
    Parsea un string tipo '18:30' o '18' a (hora, minuto).
    Retorna None si el formato no es válido.
    Uso interno de next_date().
    """
    if not raw or not isinstance(raw, str):
        return None
    raw = raw.lower().strip()
    match = re.search(r"(\d{1,2})(?::(\d{2}))?", raw)
    if not match:
        return None
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        return hour, minute
    return None

def next_date(dates: dict, timezone: str = None) -> str:
    """
    Calcula el próximo directo según un diccionario de horarios.

    Args:
        dates: dict con formato { "0": "18:00", "2": "19:30" } donde la clave es weekday (0=Lunes).
        timezone: zona horaria del cliente (ej: "Europe/Madrid"). Si es None, usa la local del servidor.

    Retorna:
        String formateado tipo "Hoy, 02 de Noviembre a las 18:30 | Zona horaria: Santiago"
        o "" si no hay fechas válidas.

    Conexión:
        - Es llamado por components/live_schedule.py para mostrar el próximo directo.
        - Usa BASE_TIMEZONE como referencia y convierte a la zona del cliente.
        - Busca hasta 14 días adelante para cubrir cambios de día por zona horaria.
    """
    if not dates or len(dates) == 0:
        return ""
    
    try:
        client_tz = ZoneInfo(timezone) if timezone else datetime.now().astimezone().tzinfo
        base_tz = ZoneInfo(BASE_TIMEZONE)
    except (ZoneInfoNotFoundError, Exception):
        client_tz = datetime.now().astimezone().tzinfo
        base_tz = datetime.now().astimezone().tzinfo

    now_client = datetime.now(client_tz)
    now_base = datetime.now(base_tz)

    for index in range(14):
        day_key = str((now_base.weekday() + index) % 7)
        if day_key not in dates or not dates[day_key]:
            continue
        parsed = _parse_hour(str(dates[day_key]))
        if parsed is None:
            continue
        hour, minute = parsed

        # 1. Próximo directo en tu zona base (Santiago)
        next_date_base = (now_base + timedelta(days=index)).replace(
            hour=hour, minute=minute, second=0, microsecond=0
        )
        
        # Si es hoy pero ya pasó en tu zona base, lo saltamos
        if next_date_base < now_base and index == 0:
            continue

        # 2. Convertimos a zona del cliente
        next_date_client = next_date_base.astimezone(client_tz)

        # 3. Si sigue en el pasado para el cliente, lo saltamos
        if next_date_client < now_client:
            continue

        # Formato final estilo MoureDev
        if next_date_client.date() == now_client.date():
            formated_date = f"Hoy, {next_date_client.day:02d} de {MONTHS[next_date_client.month]}"
        else:
            formated_date = f"{WEEKDAYS[next_date_client.weekday()]}, {next_date_client.day:02d} de {MONTHS[next_date_client.month]}"

        tz_display = timezone.split("/")[-1].replace("_", " ") if timezone else "Local"
        
        return f"{formated_date} a las {next_date_client.hour:02d}:{next_date_client.minute:02d} | Zona horaria: {tz_display}"

    return ""
