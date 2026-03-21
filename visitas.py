import json
import os

VISITAS_FILE = os.path.join(os.path.dirname(__file__), "visitas.json")


def _cargar_visitas():
    """Carga el contador de visitas desde el archivo JSON."""
    if not os.path.exists(VISITAS_FILE):
        return {"total": 0}
    try:
        with open(VISITAS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"total": 0}


def _guardar_visitas(data):
    """Guarda el contador de visitas en el archivo JSON."""
    try:
        with open(VISITAS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError:
        pass


def registrar_visita():
    """Incrementa el contador de visitas y retorna el nuevo total."""
    data = _cargar_visitas()
    data["total"] = data.get("total", 0) + 1
    _guardar_visitas(data)
    return data["total"]


def obtener_visitas():
    """Retorna el número total de visitas registradas."""
    return _cargar_visitas().get("total", 0)
