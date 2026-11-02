from datetime import datetime, timedelta
import re
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

# Date
DIAS = {
    "0": "Lunes",
    "1": "Martes", 
    "2": "Miércoles",
    "3": "Jueves",
    "4": "Viernes",
    "5": "Sábado",
    "6": "Domingo"
}

def _parse_hour(raw: str) -> tuple[int, int] | None:
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

def next_date(dates: dict) -> str:
    if not dates or len(dates) == 0:
        return ""
    now = datetime.now().astimezone()
    current_weekday = now.weekday()

    for index in range(7):
        day_key = str((current_weekday + index) % 7)
        if day_key not in dates or not dates[day_key]:
            continue
        parsed = _parse_hour(str(dates[day_key]))
        if parsed is None:
            continue
        hour, minute = parsed
        candidate_datetime = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if candidate_datetime > now or index > 0:
            next_date_obj = now + timedelta(days=index)
            if index == 0:
                formated_next_date = next_date_obj.strftime("Hoy, %d/%m")
            else:
                nombre_dia = DIAS.get(day_key, day_key)
                formated_next_date = f"{nombre_dia}, {next_date_obj.strftime("%d/%m")}"
            formated_next_time = f"{hour:02d}:{minute:02d}"
            return f"{formated_next_date} a las {formated_next_time} ({dates[day_key]} UTC)"

    return ""