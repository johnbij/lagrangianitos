# --- IMPORTACIONES ---
# Números
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

# Álgebra y Funciones
from clases.algebra.a01 import render_A01
from clases.algebra.a02 import render_A02
from clases.algebra.a03 import render_A03
from clases.algebra.a04 import render_A04
from clases.algebra.a05 import render_A05
from clases.algebra.f01 import render_F01
from clases.algebra.f02 import render_F02
from clases.algebra.f03 import render_F03
from clases.algebra.f04 import render_F04
from clases.algebra.f05 import render_F05

# Geometría
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

# Datos y Azar
from clases.datos.d01 import render_D01
from clases.datos.d02 import render_D02
from clases.datos.d03 import render_D03
from clases.datos.d04 import render_D04
from clases.datos.d05 import render_D05
from clases.datos.pb01 import render_PB01
from clases.datos.pb02 import render_PB02
from clases.datos.pb03 import render_PB03
from clases.datos.pb04 import render_PB04
from clases.datos.pb05 import render_PB05

CONTENIDOS = {
    "📐 Matemáticas": {
        "subcategorias": {
            "Números": {
                "N01": {"label": "📖 N01: Conjuntos Numéricos", "render": render_N01},
                "N02": {"label": "📖 N02: Operaciones en Z", "render": render_N02},
                "N03": {"label": "📖 N03: Valor Absoluto", "render": render_N03},
                "N04": {"label": "📖 N04: Prioridad Operaciones", "render": render_N04},
                "N05": {"label": "📖 N05: Números Racionales", "render": render_N05},
                "N06": {"label": "📖 N06: Potencias", "render": render_N06},
                "N07": {"label": "📖 N07: Raíces", "render": render_N07},
                "N08": {"label": "📖 N08: Logaritmos", "render": render_N08},
                "N09": {"label": "📖 N09: Porcentajes", "render": render_N09},
                "N10": {"label": "📖 N10: Interés Simple", "render": render_N10},
                "N11": {"label": "📖 N11: Interés Compuesto", "render": render_N11},
                "N12": {"label": "📖 N12: Aproximaciones", "render": render_N12},
                "N13": {"label": "📖 N13: Notación Científica", "render": render_N13},
                "N14": {"label": "📖 N14: Razones y Proporciones", "render": render_N14},
                "N15": {"label": "📖 N15: Proporcionalidad Directa", "render": render_N15},
                "N16": {"label": "📖 N16: Proporcionalidad Inversa", "render": render_N16},
                "N17": {"label": "📖 N17: Repaso de Números I", "render": render_N17},
                "N18": {"label": "📖 N18: Repaso de Números II", "render": render_N18},
                "N19": {"label": "📖 N19: Repaso de Números III", "render": render_N19},
                "N20": {"label": "📖 N20: Repaso de Números IV", "render": render_N20},
                "N21": {"label": "📖 N21: Ensayo Números", "render": render_N21},
            },
            "Álgebra y Funciones": {
                "A01": {"label": "📐 A01: Lenguaje Algebraico", "render": render_A01},
                "A02": {"label": "📐 A02: Productos Notables", "render": render_A02},
                "A03": {"label": "📐 A03: Factorización", "render": render_A03},
                "A04": {"label": "📐 A04: Ecuaciones de 1° Grado", "render": render_A04},
                "A05": {"label": "📐 A05: Inecuaciones", "render": render_A05},
                "F01": {"label": "📈 F01: Concepto de Función", "render": render_F01},
                "F02": {"label": "📈 F02: Función Lineal y Afín", "render": render_F02},
                "F03": {"label": "📈 F03: Función Cuadrática", "render": render_F03},
                "F04": {"label": "📈 F04: Función Exponencial", "render": render_F04},
                "F05": {"label": "📈 F05: Función Logarítmica", "render": render_F05},
            },
            "Geometría": {
                "G01": {"label": "📏 G01: Conceptos Básicos", "render": render_G01},
                "G02": {"label": "📏 G02: Triángulos I", "render": render_G02},
                "G03": {"label": "📏 G03: Triángulos II", "render": render_G03},
                "G04": {"label": "📏 G04: Cuadriláteros", "render": render_G04},
                "G05": {"label": "📏 G05: Circunferencia I", "render": render_G05},
                "G06": {"label": "📏 G06: Circunferencia II", "render": render_G06},
                "G07": {"label": "📏 G07: Transformaciones Isométricas", "render": render_G07},
                "G08": {"label": "📏 G08: Homotecia", "render": render_G08},
                "G09": {"label": "📏 G09: Teorema de Thales", "render": render_G09},
                "G10": {"label": "📏 G10: Semejanza", "render": render_G10},
                "G11": {"label": "📏 G11: Teorema de Pitágoras", "render": render_G11},
                "G12": {"label": "📏 G12: Teorema de Euclides", "render": render_G12},
                "G13": {"label": "📏 G13: Perímetros y Áreas I", "render": render_G13},
                "G14": {"label": "📏 G14: Perímetros y Áreas II", "render": render_G14},
                "G15": {"label": "📏 G15: Cuerpos Geométricos I", "render": render_G15},
                "G16": {"label": "📏 G16: Cuerpos Geométricos II", "render": render_G16},
                "G17": {"label": "📏 G17: Geometría Analítica I", "render": render_G17},
                "G18": {"label": "📏 G18: Geometría Analítica II", "render": render_G18},
                "G19": {"label": "📏 G19: Repaso Geometría I", "render": render_G19},
                "G20": {"label": "📏 G20: Repaso Geometría II", "render": render_G20},
                "G21": {"label": "📏 G21: Ensayo Geometría", "render": render_G21},
                "V01": {"label": "🏹 V01: Vectores en el Plano", "render": render_V01},
                "V02": {"label": "🏹 V02: Vectores en el Espacio", "render": render_V02},
                "V03": {"label": "🏹 V03: Producto Escalar", "render": render_V03},
                "V04": {"label": "🏹 V04: Rectas en el Espacio", "render": render_V04},
                "V05": {"label": "🏹 V05: Planos en el Espacio", "render": render_V05},
            },
            "Probabilidad y Estadística": {
                "D01": {"label": "📊 D01: Tablas de Frecuencia", "render": render_D01},
                "D02": {"label": "📊 D02: Medidas Tendencia Central", "render": render_D02},
                "D03": {"label": "📊 D03: Medidas de Posición", "render": render_D03},
                "D04": {"label": "📊 D04: Medidas de Dispersión", "render": render_D04},
                "D05": {"label": "📊 D05: Gráficos Estadísticos", "render": render_D05},
                "PB01": {"label": "🎲 PB01: Conceptos Básicos", "render": render_PB01},
                "PB02": {"label": "🎲 PB02: Reglas de Probabilidad", "render": render_PB02},
                "PB03": {"label": "🎲 PB03: Probabilidad Condicional", "render": render_PB03},
                "PB04": {"label": "🎲 PB04: Técnicas de Conteo", "render": render_PB04},
                "PB05": {"label": "🎲 PB05: Distribución Binomial", "render": render_PB05},
            }
        }
    }
}
