import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G17():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G17: Semejanza de Triángulos — Misma Forma, Distinto Tamaño")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase G17: Semejanza de Triángulos - Misma Forma, Distinto Tamaño
    **Eje:** Geometría | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. Definición de Semejanza ($\sim$)
    Dos triángulos son semejantes si tienen sus **ángulos internos respectivamente iguales** (congruentes) y sus **lados homólogos proporcionales**.
    * **Lados homólogos:** Son los que están en la misma posición relativa (frente a ángulos iguales).

    ### ⚖️ 2. Criterios de Semejanza (Cómo reconocerlos)
    Para no medir todo, usamos estos criterios mínimos:
    * **AA (Ángulo-Ángulo):** Si tienen dos ángulos iguales, el tercero también lo será. Es el más usado.
    * **LAL (Lado-Ángulo-Lado):** Tienen dos lados proporcionales y el ángulo comprendido entre ellos es igual.
    * **LLL (Lado-Lado-Lado):** Sus tres lados son proporcionales entre sí.

    ### 📐 3. La Razón de Semejanza ($k$)
    Si dividimos un lado del triángulo grande por su homólogo del pequeño, obtenemos la constante $k$.
    * **Perímetros:** Están en razón $k$.
    * **Áreas:** Estarán en razón $k^2$ (¡Ojo con esto en la PAES!).

    > **Newton Tip:** "Seba, dile a tu alumno: Semejanza es como ver una foto en el celular y hacer zoom. El triángulo no cambia sus ángulos, solo se hace más grande o más chico."
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G17 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G17 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Triángulo A (lados 3, 4, 5) y B (lados 6, 8, $x$). Hallar $x$. | 1. La razón es $6/3 = 2$.<br>2. Multiplicar 5 por la razón: $5 \cdot 2$. | **$x = 10$** |
| **E02** | Dos triángulos son semejantes en razón $1:3$. Si el área del pequeño es 5. | 1. La razón de áreas es $k^2 = (3)^2 = 9$.<br>2. Área grande: $5 \cdot 9$. | **45 u²** |
| **E03** | ¿Son semejantes un triángulo de (40°, 60°) y otro de (60°, 80°)? | 1. Sumar en el primero: $40+60=100 \implies$ falta 80°.<br>2. Tienen los mismos tres ángulos. | **Sí (por AA)** |
| **E04** | Los perímetros de dos figuras semejantes están en razón 2:5. | 1. La razón de sus lados es la misma que la de sus perímetros. | **2:5** |
| **E05** | Un poste de 3 m proyecta sombra de 1,5 m. ¿Qué sombra proyecta un edificio de 12 m? | 1. Triángulos semejantes por rayos de sol.<br>2. $3 / 1,5 = 12 / x \implies 2 = 12/x$. | **6 m** |
""")

    with st.expander("❓ Cuestionario G17", expanded=False):
        quiz = [
            {'question': 'El símbolo matemático para indicar semejanza es:', 'options': {'A': '$\\cong$', 'B': '$=$', 'C': '$\\sim$', 'D': '$\\parallel$'}, 'answer': 'C', 'explanation': "La tilde de la eñe representa que las figuras son 'parecidas' pero no idénticas."},
            {'question': 'El criterio AA de semejanza significa que los triángulos tienen:', 'options': {'A': 'Dos lados iguales', 'B': 'Dos ángulos iguales', 'C': 'Área y Altura iguales', 'D': 'Ángulos agudos'}, 'answer': 'B', 'explanation': 'Es el criterio más práctico. Si dos ángulos coinciden, el triángulo tiene la misma forma obligatoriamente.'},
            {'question': 'Si dos triángulos son semejantes, sus lados homólogos son siempre:', 'options': {'A': 'Iguales', 'B': 'Paralelos', 'C': 'Proporcionales', 'D': 'Perpendiculares'}, 'answer': 'C', 'explanation': 'Significa que si uno crece al doble, todos sus lados crecen al doble.'},
            {'question': 'Si la razón de semejanza entre dos triángulos es $k = 4$, la razón entre sus áreas es:', 'options': {'A': '4', 'B': '8', 'C': '16', 'D': '2'}, 'answer': 'C', 'explanation': 'El área es bidimensional, por eso la razón se eleva al cuadrado: $4^2 = 16$.'},
            {'question': 'El criterio LLL indica que dos triángulos son semejantes si:', 'options': {'A': 'Sus tres ángulos son iguales', 'B': 'Sus tres lados miden lo mismo', 'C': 'Sus tres lados son proporcionales', 'D': 'Tienen el mismo perímetro'}, 'answer': 'C', 'explanation': 'Típ: No confundas con congruencia. En semejanza basta con que mantengan la proporción (ej: todos al triple).'},
            {'question': 'Si un triángulo tiene lados 5, 12, 13 y otro tiene 10, 24, 26, son semejantes por:', 'options': {'A': 'AA', 'B': 'LAL', 'C': 'LLL', 'D': 'No son semejantes'}, 'answer': 'C', 'explanation': 'Cada lado del segundo triángulo es exactamente el doble del primero.'},
            {'question': 'En la semejanza, los ángulos correspondientes son siempre:', 'options': {'A': 'Proporcionales', 'B': 'Iguales (congruentes)', 'C': 'Suplementarios', 'D': 'Complementarios'}, 'answer': 'B', 'explanation': '¡Mucho ojo! Los lados son proporcionales, pero los ángulos NUNCA cambian, son iguales.'},
            {'question': 'Si la razón entre los perímetros de dos triángulos semejantes es 1:2, la razón entre sus lados es:', 'options': {'A': '1:2', 'B': '1:4', 'C': '2:1', 'D': '1:1'}, 'answer': 'A', 'explanation': 'El perímetro es una medida lineal (1D), así que mantiene la misma razón que los lados.'},
            {'question': 'Para que se cumpla el criterio LAL, el ángulo igual debe estar:', 'options': {'A': 'Opuesto al lado mayor', 'B': 'Entre los dos lados proporcionales', 'C': 'En la base', 'D': 'En el vértice superior'}, 'answer': 'B', 'explanation': "El ángulo debe estar 'atrapado' por los lados que estamos comparando."},
            {'question': 'Si el área de un triángulo aumenta 100 veces, su lado aumentó:', 'options': {'A': '100 veces', 'B': '50 veces', 'C': '10 veces', 'D': '200 veces'}, 'answer': 'C', 'explanation': 'Típ: Como el área es $k^2$, buscamos la raíz de 100, que es 10.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g17_quiz")
