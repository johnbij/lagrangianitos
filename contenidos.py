# --- IMPORTACIONES: EJES DE MATEMÁTICAS ---

# 1. NÚMEROS (Carpeta: clases/numeros/)
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

# 2. ÁLGEBRA Y FUNCIONES (Carpeta: clases/algebra/)
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

# 3. GEOMETRÍA (Carpeta: clases/geometria/)
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

# 4. DATOS Y AZAR (Carpeta: clases/datos/)
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

from utils import render_proximamente

# --- DICCIONARIO MAESTRO ---

CONTENIDOS = {
    "📐 Matemáticas": {
        "subcategorias": {
            "Números": {
                "N01": {"label": "📖 N01: Conjuntos Numéricos", "render": render_N01},
                "N02": {"label": "📖 N02: Operaciones en Z", "render": render_N02},
                "N03": {"label": "📖 N03: Valor Absoluto", "render": render_N03},
                "N04": {"label": "📖 N04: Prioridad Operaciones", "render": render_N04},
                "N05": {"label": "📖 N05: Números Racionales", "render": render_N05},
                # ... puedes seguir agregando las etiquetas hasta N35 aquí
                "N35": {"label": "📖 N35: Aplicaciones Reales", "render": render_N35},
            },
            "Álgebra y Funciones": {
                "A01": {"label": "📐 A01: Lenguaje Algebraico", "render": render_A01},
                "A02": {"label": "📐 A02: Productos Notables", "render": render_A02},
                "A03": {"label": "📐 A03: Factorización", "render": render_A03},
                "A04": {"label": "📐 A04: Ecuaciones", "render": render_A04},
                "A05": {"label": "📐 A05: Inecuaciones", "render": render_A05},
                "F01": {"label": "📈 F01: Funciones I", "render": render_F01},
                "F02": {"label": "📈 F02: Funciones II", "render": render_F02},
                "F03": {"label": "📈 F03: Función Cuadrática", "render": render_F03},
                "F04": {"label": "📈 F04: Exponencial y Log", "render": render_F04},
                "F05": {"label": "📈 F05: Transformaciones", "render": render_F05},
            },
            "Geometría": {
                "G01": {"label": "📏 G01: Geometría Plana I", "render": render_G01},
                "G11": {"label": "📏 G11: Pitágoras", "render": render_G11},
                "G21": {"label": "📏 G21: Áreas y Perímetros", "render": render_G21},
                "V01": {"label": "🏹 V01: Vectores", "render": render_V01},
                "V05": {"label": "🏹 V05: Operaciones Vectoriales", "render": render_V05},
            },
            "Probabilidad y Estadística": {
                "D01": {"label": "📊 D01: Estadística Descriptiva", "render": render_D01},
                "D05": {"label": "📊 D05: Medidas de Dispersión", "render": render_D05},
                "PB01": {"label": "🎲 PB01: Conceptos de Azar", "render": render_PB01},
                "PB05": {"label": "🎲 PB05: Distribución de Probabilidad", "render": render_PB05},
            }
        }
    },
    "⚛️ Física": {
        "subcategorias": {
            "Ondas": {"FO01": {"label": "🌊 FO01: Propiedades", "render": lambda: render_proximamente("FO01")}},
            "Mecánica": {},
            "Energía": {},
            "Electricidad": {}
        }
    },
    "⚗️ Química": {
        "subcategorias": {
            "Estructura Atómica": {"Q01": {"label": "⚛️ Q01: El Átomo", "render": lambda: render_proximamente("Q01")}},
            "Química Orgánica": {}
        }
    },
    "🧬 Biología": {
        "subcategorias": {
            "Célula": {"B01": {"label": "🔬 B01: Estructura Celular", "render": lambda: render_proximamente("B01")}},
            "Genética": {}
        }
    }
}
