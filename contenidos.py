# ── Números ──────────────────────────────────────────────────
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
from clases.numeros.n17 import render_N17
from clases.numeros.n18 import render_N18
from clases.numeros.n19 import render_N19
from clases.numeros.n20 import render_N20
from clases.numeros.n21 import render_N21
from clases.numeros.n22 import render_N22
from clases.numeros.n23 import render_N23
from clases.numeros.n24 import render_N24
from clases.numeros.n25 import render_N25
from clases.numeros.n26 import render_N26
from clases.numeros.n27 import render_N27
from clases.numeros.n28 import render_N28
from clases.numeros.n29 import render_N29
from clases.numeros.n30 import render_N30
from clases.numeros.n31 import render_N31
from clases.numeros.n32 import render_N32
from clases.numeros.n33 import render_N33
from clases.numeros.n34 import render_N34
from clases.numeros.n35 import render_N35

# ── Álgebra ───────────────────────────────────────────────────
from clases.algebra.a01 import render_A01
from clases.algebra.a02 import render_A02
from clases.algebra.a03 import render_A03
from clases.algebra.a04 import render_A04
from clases.algebra.a05 import render_A05

# ── Funciones ─────────────────────────────────────────────────
from clases.algebra.f01 import render_F01
from clases.algebra.f02 import render_F02
from clases.algebra.f03 import render_F03
from clases.algebra.f04 import render_F04
from clases.algebra.f05 import render_F05

# ── Datos ─────────────────────────────────────────────────────
from clases.datos.d01 import render_D01
from clases.datos.d02 import render_D02
from clases.datos.d03 import render_D03
from clases.datos.d04 import render_D04
from clases.datos.d05 import render_D05

# ── Probabilidad ──────────────────────────────────────────────
from clases.datos.pb01 import render_PB01
from clases.datos.pb02 import render_PB02
from clases.datos.pb03 import render_PB03
from clases.datos.pb04 import render_PB04
from clases.datos.pb05 import render_PB05

from clases.geometria.g01 import render_G01
from clases.geometria.g02 import render_G02
from clases.geometria.g03 import render_G03
from clases.geometria.g04 import render_G04
from clases.geometria.g05 import render_G05
from clases.geometria.g06 import render_G06
from clases.geometria.g07 import render_G07
from clases.geometria.g08 import render_G08
from clases.geometria.g09 import render_G09
from clases.geometria.g10 import render_G10
from clases.geometria.g11 import render_G11
from clases.geometria.g12 import render_G12
from clases.geometria.g13 import render_G13
from clases.geometria.g14 import render_G14
from clases.geometria.g15 import render_G15
from clases.geometria.g16 import render_G16
from clases.geometria.g17 import render_G17
from clases.geometria.g18 import render_G18
from clases.geometria.g19 import render_G19
from clases.geometria.g20 import render_G20
from clases.geometria.g21 import render_G21
from clases.geometria.v01 import render_V01
from clases.geometria.v02 import render_V02
from clases.geometria.v03 import render_V03
from clases.geometria.v04 import render_V04
from clases.geometria.v05 import render_V05

from utils import render_proximamente

CONTENIDOS = {
    "⚛️ Física": {
        "color_subcats": "cian",
        "subcategorias": {
            "Ondas": {
                "FO01": {"label": "📖 FO01: Naturaleza de las Ondas",          "render": lambda: render_proximamente("FO01")},
                "FO02": {"label": "📖 FO02: Propiedades de las Ondas",          "render": lambda: render_proximamente("FO02")},
                "FO03": {"label": "📖 FO03: Sonido y Acústica",                 "render": lambda: render_proximamente("FO03")},
                "FO04": {"label": "📖 FO04: Luz y Óptica",                      "render": lambda: render_proximamente("FO04")},
                "FO05": {"label": "📖 FO05: Fenómenos Ondulatorios",            "render": lambda: render_proximamente("FO05")},
            },
            "Mecánica": {
                "FM01": {"label": "📖 FM01: Cinemática — Movimiento y Velocidad","render": lambda: render_proximamente("FM01")},
                "FM02": {"label": "📖 FM02: Dinámica — Fuerzas y Leyes de Newton","render": lambda: render_proximamente("FM02")},
                "FM03": {"label": "📖 FM03: Trabajo y Energía Mecánica",        "render": lambda: render_proximamente("FM03")},
                "FM04": {"label": "📖 FM04: Cantidad de Movimiento",            "render": lambda: render_proximamente("FM04")},
                "FM05": {"label": "📖 FM05: Movimiento Circular y Gravitación", "render": lambda: render_proximamente("FM05")},
            },
            "Energía": {
                "FE01": {"label": "📖 FE01: Concepto de Energía",               "render": lambda: render_proximamente("FE01")},
                "FE02": {"label": "📖 FE02: Energía Cinética y Potencial",      "render": lambda: render_proximamente("FE02")},
                "FE03": {"label": "📖 FE03: Conservación de la Energía",        "render": lambda: render_proximamente("FE03")},
                "FE04": {"label": "📖 FE04: Calor y Temperatura",               "render": lambda: render_proximamente("FE04")},
                "FE05": {"label": "📖 FE05: Termodinámica Básica",              "render": lambda: render_proximamente("FE05")},
            },
            "Electricidad": {
                "FEL01": {"label": "📖 FEL01: Carga Eléctrica y Campo",           "render": lambda: render_proximamente("FEL01")},
                "FEL02": {"label": "📖 FEL02: Corriente Eléctrica",               "render": lambda: render_proximamente("FEL02")},
                "FEL03": {"label": "📖 FEL03: Circuitos Eléctricos",              "render": lambda: render_proximamente("FEL03")},
                "FEL04": {"label": "📖 FEL04: Magnetismo",                        "render": lambda: render_proximamente("FEL04")},
                "FEL05": {"label": "📖 FEL05: Inducción Electromagnética",        "render": lambda: render_proximamente("FEL05")},
            },
        },
    },
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
                "N08": {"label": "📖 N08: Primos y Divisibilidad",             "render": render_N08},
                "N09": {"label": "📖 N09: El Infinito ♾️",                     "render": render_N09},
                "N10": {"label": "📖 N10: Mecánica de Operatoria (PAPOMUDAS)", "render": render_N10},
                "N11": {"label": "📖 N11: Racionales I - Fracciones",          "render": render_N11},
                "N12": {"label": "📖 N12: Racionales II - Operatoria en ℚ",    "render": render_N12},
                "N13": {"label": "📖 N13: Racionales III - Decimales",         "render": render_N13},
                "N14": {"label": "📖 N14: El Lenguaje del Reparto",            "render": render_N14},
                "N15": {"label": "📖 N15: ADN de los Números",                 "render": render_N15},
                "N16": {"label": "📖 N16: El Orden en los Racionales",         "render": render_N16},
            },
            "Potencias y Raíces": {
                "N17": {"label": "📖 N17: Potencias",                          "render": render_N17},
                "N18": {"label": "📖 N18: Notación Científica",                "render": render_N18},
                "N19": {"label": "📖 N19: Aproximaciones",                     "render": render_N19},
                "N20": {"label": "📖 N20: Raíces",                             "render": render_N20},
                "N21": {"label": "📖 N21: Racionalización Básica",             "render": render_N21},
                "N22": {"label": "📖 N22: Racionalización Avanzada",           "render": render_N22},
            },
            "Razones y Proporciones": {
                "N23": {"label": "📖 N23: Razones",                                    "render": render_N23},
                "N24": {"label": "📖 N24: Proporciones",                               "render": render_N24},
                "N25": {"label": "📖 N25: Simetría - Las 8 Caras de la Proporción",    "render": render_N25},
                "N26": {"label": "📖 N26: Composición y Descomposición",               "render": render_N26},
                "N27": {"label": "📖 N27: Reparto Proporcional Directo",               "render": render_N27},
                "N28": {"label": "📖 N28: Reparto Inversamente Proporcional",          "render": render_N28},
                "N29": {"label": "📖 N29: Manipulación de Fórmulas Científicas",       "render": render_N29},
                "N30": {"label": "📖 N30: El Mapa de las Proporciones",                "render": render_N30},
                "N31": {"label": "📖 N31: Proporcionalidad Directa",                   "render": render_N31},
                "N32": {"label": "📖 N32: Proporcionalidad Inversa",                   "render": render_N32},
                "N33": {"label": "📖 N33: Proporcionalidad Compuesta",                 "render": render_N33},
                "N34": {"label": "📖 N34: De las Proporciones a las Igualdades",       "render": render_N34},
                "N35": {"label": "📖 N35: Aplicaciones Maestras de las Proporciones",  "render": render_N35},
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
                "A01": {"label": "📖 A01: Expresiones Algebraicas",     "render": render_A01},
                "A02": {"label": "📖 A02: Productos Notables",           "render": render_A02},
                "A03": {"label": "📖 A03: Factorización",                "render": render_A03},
                "A04": {"label": "📖 A04: Ecuaciones de Primer Grado",   "render": render_A04},
                "A05": {"label": "📖 A05: Inecuaciones y Sistemas",      "render": render_A05},
            },
            "Funciones": {
                "F01": {"label": "📖 F01: Concepto de Función",                     "render": render_F01},
                "F02": {"label": "📖 F02: Función Lineal y Afín",                   "render": render_F02},
                "F03": {"label": "📖 F03: Función Cuadrática",                      "render": render_F03},
                "F04": {"label": "📖 F04: Función Exponencial y Logarítmica",       "render": render_F04},
                "F05": {"label": "📖 F05: Composición y Transformaciones",          "render": render_F05},
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
            "Plano y Coordenadas": {
                "G01": {"label": "📖 G01: Topografía Inicial — El Plano Cartesiano",       "render": render_G01},
                "G02": {"label": "📖 G02: Distancia entre Puntos",                         "render": render_G02},
                "G03": {"label": "📖 G03: El Punto Medio",                                 "render": render_G03},
                "G04": {"label": "📖 G04: Ángulos y Clasificación",                        "render": render_G04},
                "G05": {"label": "📖 G05: Ángulos entre Paralelas y una Transversal",      "render": render_G05},
            },
            "Triángulos": {
                "G06": {"label": "📖 G06: Triángulos — Los Cimientos de la Geometría",     "render": render_G06},
                "G07": {"label": "📖 G07: Clasificación de Triángulos (por Ángulos)",      "render": render_G07},
                "G08": {"label": "📖 G08: Clasificación de Triángulos (por Lados)",        "render": render_G08},
                "G09": {"label": "📖 G09: Elementos Secundarios I — Alturas y Bisectrices","render": render_G09},
                "G10": {"label": "📖 G10: Elementos Secundarios II — Simetrales y Transversales", "render": render_G10},
            },
            "Pitágoras, Áreas y Círculo": {
                "G11": {"label": "📖 G11: Teorema de Pitágoras — La Llave Maestra",        "render": render_G11},
                "G12": {"label": "📖 G12: Áreas y Perímetros I — Triángulos y Cuadriláteros", "render": render_G12},
                "G13": {"label": "📖 G13: Círculo y Circunferencia — La Perfección del Radio", "render": render_G13},
                "G14": {"label": "📖 G14: Ángulos en la Circunferencia",                   "render": render_G14},
                "G15": {"label": "📖 G15: Teoremas de Euclides — Proporciones en el Triángulo Rectángulo", "render": render_G15},
            },
            "Semejanza y Transformaciones": {
                "G16": {"label": "📖 G16: Teorema de Tales — Proporcionalidad entre Paralelas", "render": render_G16},
                "G17": {"label": "📖 G17: Semejanza de Triángulos — Misma Forma, Distinto Tamaño", "render": render_G17},
                "G18": {"label": "📖 G18: Homotecia — Ampliación y Reducción Vectorial",   "render": render_G18},
                "G19": {"label": "📖 G19: Transformaciones Isométricas — Movimiento sin Deformación", "render": render_G19},
            },
            "Cuerpos 3D": {
                "G20": {"label": "📖 G20: Cuerpos 3D I — Prismas y Cilindros",             "render": render_G20},
                "G21": {"label": "📖 G21: Cuerpos 3D II — Pirámides, Conos y Esfera",      "render": render_G21},
            },
            "Vectores": {
                "V01": {"label": "📖 V01: Introducción a los Vectores — El Mapa del Movimiento", "render": render_V01},
                "V02": {"label": "📖 V02: Operaciones con Vectores — Combinando Movimientos", "render": render_V02},
                "V03": {"label": "📖 V03: Módulo y Distancia — ¿Cuánto mide el vector?",   "render": render_V03},
                "V04": {"label": "📖 V04: Vectores e Isometrías — El Motor del Movimiento", "render": render_V04},
                "V05": {"label": "📖 V05: Vectores en el Espacio — La Tercera Dimensión",  "render": render_V05},
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
                "D01": {"label": "📖 D01: Tipos de Datos y Tablas",      "render": render_D01},
                "D02": {"label": "📖 D02: Medidas de Tendencia Central",  "render": render_D02},
                "D03": {"label": "📖 D03: Medidas de Dispersión",         "render": render_D03},
                "D04": {"label": "📖 D04: Gráficos Estadísticos",         "render": render_D04},
                "D05": {"label": "📖 D05: Análisis y Correlación",        "render": render_D05},
            },
            "Probabilidad": {
                "PB01": {"label": "📖 PB01: Espacio Muestral y Eventos",         "render": render_PB01},
                "PB02": {"label": "📖 PB02: Probabilidad Clásica",               "render": render_PB02},
                "PB03": {"label": "📖 PB03: Probabilidad Compuesta",             "render": render_PB03},
                "PB04": {"label": "📖 PB04: Técnicas de Conteo",                 "render": render_PB04},
                "PB05": {"label": "📖 PB05: Variable Aleatoria y Distribuciones","render": render_PB05},
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
