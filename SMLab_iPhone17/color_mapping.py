# color_mapping.py

COLOR_MAP = {
    # Blau
    "blau": "blau",
    "nebelblau": "blau",
    "hellblau": "blau",
    "dunkelblau": "blau",
    "marineblau": "blau",

    # Rot
    "rot": "rot",
    "hellrot": "rot",
    "dunkelrot": "rot",
    "weinrot": "rot",

    # Grün
    "grün": "grün",
    "green": "grün",
    "gruen": "grün",
    "hellgrün": "grün",
    "hellgruen": "grün",
    "dunkelgrün": "grün",
    "salbei": "grün",
    "sage": "grün",

    # Lila
    "lila": "lila",
    "violett": "lila",
    "lavendel": "lila",
    "lavender": "lila",
    "lila - lavandel": "lila",


    # Schwarz / Weiß
    "schwarz": "schwarz",
    "black": "schwarz", 
    "weiß": "weiß",
    "weiss": "weiß",
    "white": "weiß",
    "siler": "weiß",
    "blanco": "weiß",
}


def clean_color_column(series):
    cleaned = series.astype(str).str.strip().str.lower()
    return cleaned.map(COLOR_MAP).fillna(cleaned)