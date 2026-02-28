from clases.numeros.n01 import render_N01
from clases.numeros.n02 import render_N02
from clases.numeros.n03 import render_N03
from clases.numeros.n04 import render_N04
from clases.numeros.n05 import render_N05
from clases.numeros.n06 import render_N06
from clases.numeros.n07 import render_N07
from clases.numeros.n08 import render_N08
from clases.numeros.n09 import render_N09
from clases.numeros.n10 import render_N10
from clases.numeros.n11 import render_N11
from clases.numeros.n12 import render_N12
from clases.numeros.n13 import render_N13
from clases.numeros.n14 import render_N14
from clases.numeros.n15 import render_N15
from clases.numeros.n16 import render_N16
from utils import render_proximamente

# =============================================================================
# DICCIONARIO CENTRAL DE CONTENIDOS
# Estructura: EJE > SUBCATEGORÍA > CÓDIGO > {label, render}
# =============================================================================

CONTENIDOS = {
    "🔢 Números": {
        "color_subcats": "rojo",
        "subcategorias": {
            "Conjuntos": {
                "N01": {"label": "📖 N01: Teoría de Conjuntos",        "render": render_N01},
                "N02": {"label": "📖 N02: Números Naturales",           "render": render_N02},
                "N03": {"label": "📖 N03: Números Cardinales",          "render": render_N03},
                "N04": {"label": "📖 N04: Números Enteros",             "render": render_N04},
                "N05": {"label": "📖 N05: Números Racionales",          "render": render_N05},
                "N06": {"label": "📖 N06: Números Irracionales",        "render": render_N06},
                "N07": {"label": "📖 N07: Números Reales",              "render": render_N07},
            },
            "Operatoria": {
                "N08": {"label": "📖 N08: Primos y Divisibilidad",            "render": render_N08},
                "N09": {"label": "📖 N09: El Infinito ♾️",                    "render": render_N09},
                "N10": {"label": "📖 N10: Mecánica de Operatoria (PAPOMUDAS)", "render": render_N10},
                "N11": {"label": "📖 N11: Racionales I - Fracciones",         "render": render_N11},
                "N12": {"label": "📖 N12: Racionales II - Operatoria en ℚ",   "render": render_N12},
                "N13": {"label": "📖 N13: Racionales III - Decimales",        "render": render_N13},
                "N14": {"label": "📖 N14: El Lenguaje del Reparto",           "render": render_N14},
                "N15": {"label": "📖 N15: ADN de los Números",                "render": render_N15},
                "N16": {"label": "📖 N16: El Orden en los Racionales",        "render": render_N16},
            },
            "Razones y Proporciones": {
                "R01": {"label": "📖 R01: Próximamente", "render": lambda: render_proximamente("R01")},
                "R02": {"label": "📖 R02: Próximamente", "render": lambda: render_proximamente("R02")},
                "R03": {"label": "📖 R03: Próximamente", "render": lambda: render_proximamente("R03")},
                "R04": {"label": "📖 R04: Próximamente", "render": lambda: render_proximamente("R04")},
                "R05": {"label": "📖 R05: Próximamente", "render": lambda: render_proximamente("R05")},
            },
            "Ejercitación": {
                "NE01": {"label": "📝 NE01: Próximamente", "render": lambda: render_proximamente("NE01")},
                "NE02": {"label": "📝 NE02: Próximamente", "render": lambda: render_proximamente("NE02")},
                "NE03": {"label": "📝 NE03: Próximamente", "render": lambda: render_proximamente("NE03")},
                "NE04": {"label": "📝 NE04: Próximamente", "render": lambda: render_proximamente("NE04")},
                "NE05": {"label": "📝 NE05: Próximamente", "render": lambda: render_proximamente("NE05")},
            },
        },
    },
    "📉 Álgebra": {
        "color_subcats": "verde",
        "subcategorias": {
            "Álgebra": {
                "A01": {"label": "📖 A01: Próximamente", "render": lambda: render_proximamente("A01")},
                "A02": {"label": "📖 A02: Próximamente", "render": lambda: render_proximamente("A02")},
                "A03": {"label": "📖 A03: Próximamente", "render": lambda: render_proximamente("A03")},
                "A04": {"label": "📖 A04: Próximamente", "render": lambda: render_proximamente("A04")},
                "A05": {"label": "📖 A05: Próximamente", "render": lambda: render_proximamente("A05")},
            },
            "Funciones": {
                "F01": {"label": "📖 F01: Próximamente", "render": lambda: render_proximamente("F01")},
                "F02": {"label": "📖 F02: Próximamente", "render": lambda: render_proximamente("F02")},
                "F03": {"label": "📖 F03: Próximamente", "render": lambda: render_proximamente("F03")},
                "F04": {"label": "📖 F04: Próximamente", "render": lambda: render_proximamente("F04")},
                "F05": {"label": "📖 F05: Próximamente", "render": lambda: render_proximamente("F05")},
            },
            "Ejercitación": {
                "AE01": {"label": "📝 AE01: Próximamente", "render": lambda: render_proximamente("AE01")},
                "AE02": {"label": "📝 AE02: Próximamente", "render": lambda: render_proximamente("AE02")},
                "AE03": {"label": "📝 AE03: Próximamente", "render": lambda: render_proximamente("AE03")},
                "AE04": {"label": "📝 AE04: Próximamente", "render": lambda: render_proximamente("AE04")},
                "AE05": {"label": "📝 AE05: Próximamente", "render": lambda: render_proximamente("AE05")},
            },
        },
    },
    "📐 Geometría": {
        "color_subcats": "morado",
        "subcategorias": {
            "Formas y Figuras": {
                "G01": {"label": "📖 G01: Próximamente", "render": lambda: render_proximamente("G01")},
                "G02": {"label": "📖 G02: Próximamente", "render": lambda: render_proximamente("G02")},
                "G03": {"label": "📖 G03: Próximamente", "render": lambda: render_proximamente("G03")},
                "G04": {"label": "📖 G04: Próximamente", "render": lambda: render_proximamente("G04")},
                "G05": {"label": "📖 G05: Próximamente", "render": lambda: render_proximamente("G05")},
            },
            "Perímetro, Área y Volumen": {
                "P01": {"label": "📖 P01: Próximamente", "render": lambda: render_proximamente("P01")},
                "P02": {"label": "📖 P02: Próximamente", "render": lambda: render_proximamente("P02")},
                "P03": {"label": "📖 P03: Próximamente", "render": lambda: render_proximamente("P03")},
                "P04": {"label": "📖 P04: Próximamente", "render": lambda: render_proximamente("P04")},
                "P05": {"label": "📖 P05: Próximamente", "render": lambda: render_proximamente("P05")},
            },
            "Vectores": {
                "V01": {"label": "📖 V01: Próximamente", "render": lambda: render_proximamente("V01")},
                "V02": {"label": "📖 V02: Próximamente", "render": lambda: render_proximamente("V02")},
                "V03": {"label": "📖 V03: Próximamente", "render": lambda: render_proximamente("V03")},
                "V04": {"label": "📖 V04: Próximamente", "render": lambda: render_proximamente("V04")},
                "V05": {"label": "📖 V05: Próximamente", "render": lambda: render_proximamente("V05")},
            },
            "Ejercitación": {
                "GE01": {"label": "📝 GE01: Próximamente", "render": lambda: render_proximamente("GE01")},
                "GE02": {"label": "📝 GE02: Próximamente", "render": lambda: render_proximamente("GE02")},
                "GE03": {"label": "📝 GE03: Próximamente", "render": lambda: render_proximamente("GE03")},
                "GE04": {"label": "📝 GE04: Próximamente", "render": lambda: render_proximamente("GE04")},
                "GE05": {"label": "📝 GE05: Próximamente", "render": lambda: render_proximamente("GE05")},
            },
        },
    },
    "📊 Datos y Azar": {
        "color_subcats": "naranja",
        "subcategorias": {
            "Estadística": {
                "D01": {"label": "📖 D01: Próximamente", "render": lambda: render_proximamente("D01")},
                "D02": {"label": "📖 D02: Próximamente", "render": lambda: render_proximamente("D02")},
                "D03": {"label": "📖 D03: Próximamente", "render": lambda: render_proximamente("D03")},
                "D04": {"label": "📖 D04: Próximamente", "render": lambda: render_proximamente("D04")},
                "D05": {"label": "📖 D05: Próximamente", "render": lambda: render_proximamente("D05")},
            },
            "Probabilidad": {
                "PR01": {"label": "📖 PR01: Próximamente", "render": lambda: render_proximamente("PR01")},
                "PR02": {"label": "📖 PR02: Próximamente", "render": lambda: render_proximamente("PR02")},
                "PR03": {"label": "📖 PR03: Próximamente", "render": lambda: render_proximamente("PR03")},
                "PR04": {"label": "📖 PR04: Próximamente", "render": lambda: render_proximamente("PR04")},
                "PR05": {"label": "📖 PR05: Próximamente", "render": lambda: render_proximamente("PR05")},
            },
            "Ejercitación": {
                "DE01": {"label": "📝 DE01: Próximamente", "render": lambda: render_proximamente("DE01")},
                "DE02": {"label": "📝 DE02: Próximamente", "render": lambda: render_proximamente("DE02")},
                "DE03": {"label": "📝 DE03: Próximamente", "render": lambda: render_proximamente("DE03")},
                "DE04": {"label": "📝 DE04: Próximamente", "render": lambda: render_proximamente("DE04")},
                "DE05": {"label": "📝 DE05: Próximamente", "render": lambda: render_proximamente("DE05")},
            },
        },
    },
}
