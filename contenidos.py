from clases.numeros.n01 import render_N01
from utils import render_proximamente

# =============================================================================
# DICCIONARIO CENTRAL DE CONTENIDOS
# Para agregar una clase nueva:
#   1. Crea clases/eje/nXX.py con su función render_NXX()
#   2. Importa la función arriba
#   3. Reemplaza el lambda de "Próximamente" con la función importada
# =============================================================================

CONTENIDOS = {
    "🔢 Números": {
        "Teoria": {
            "N01": {"label": "📖 N01: Teoría de Conjuntos",    "render": render_N01},
            "N02": {"label": "📖 N02: Próximamente",            "render": lambda: render_proximamente("N02")},
            "N03": {"label": "📖 N03: Próximamente",            "render": lambda: render_proximamente("N03")},
        },
        "Ejercitacion": {
            "NE01": {"label": "📝 NE01: Ejercicios Conjuntos",  "render": lambda: render_proximamente("NE01")},
        },
    },
    "📉 Álgebra": {
        "Teoria": {
            "A01": {"label": "📖 A01: Expresiones Algebraicas", "render": lambda: render_proximamente("A01")},
            "A02": {"label": "📖 A02: Ecuaciones",              "render": lambda: render_proximamente("A02")},
        },
        "Ejercitacion": {
            "AE01": {"label": "📝 AE01: Ejercicios Álgebra",    "render": lambda: render_proximamente("AE01")},
        },
    },
    "📐 Geometría": {
        "Teoria": {
            "G01": {"label": "📖 G01: Geometría Plana",         "render": lambda: render_proximamente("G01")},
            "G02": {"label": "📖 G02: Geometría del Espacio",   "render": lambda: render_proximamente("G02")},
        },
        "Ejercitacion": {
            "GE01": {"label": "📝 GE01: Ejercicios Geometría",  "render": lambda: render_proximamente("GE01")},
        },
    },
    "📊 Datos y Azar": {
        "Teoria": {
            "D01": {"label": "📖 D01: Estadística Descriptiva", "render": lambda: render_proximamente("D01")},
            "D02": {"label": "📖 D02: Probabilidades",          "render": lambda: render_proximamente("D02")},
        },
        "Ejercitacion": {
            "DE01": {"label": "📝 DE01: Ejercicios Datos",      "render": lambda: render_proximamente("DE01")},
        },
    },
}
