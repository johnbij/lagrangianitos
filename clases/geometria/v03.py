import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_V03():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("V03: Módulo y Distancia — ¿Cuánto mide el vector?")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase V03: Módulo y Distancia - ¿Cuánto mide el vector?
    **Eje:** Vectores | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. Módulo de un Vector ($|\vec{v}|$)
    El módulo es la longitud o magnitud del vector. Representa la distancia desde el origen $(0,0)$ hasta el punto $(x, y)$.
    * **Fórmula:** Se basa directamente en el Teorema de Pitágoras.
    $$|\vec{v}| = \sqrt{x^2 + y^2}$$

    ### ⚖️ 2. Distancia entre dos puntos
    Si queremos saber la distancia entre el punto $A(x_1, y_1)$ y el punto $B(x_2, y_2)$, calculamos el módulo del vector $\vec{AB}$.
    * **Fórmula de Distancia ($d$):**
    $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

    ### 📐 3. Propiedades del Módulo
    1. **Siempre es positivo:** El módulo es una distancia, por lo tanto $|\vec{v}| \geq 0$.
    2. **Módulo de la ponderación:** $|k \cdot \vec{v}| = |k| \cdot |\vec{v}|$. Si multiplicas el vector por 3, su medida se triplica.
    3. **Vector Unitario:** Es aquel cuyo módulo es exactamente 1.

    > **Newton Tip:** "Seba, dile a tu alumno: el módulo es la hipotenusa de un triángulo imaginario donde los catetos son las coordenadas $x$ e $y$. ¡Si se sabe los tríos pitagóricos (3, 4, 5), ya tiene la mitad de los ejercicios resueltos!"
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica V03 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica V03 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Calcular el módulo del vector $\vec{v}(3, 4)$. | 1. Aplicar fórmula: $\sqrt{3^2 + 4^2}$.<br>2. $\sqrt{9 + 16} = \sqrt{25}$. | **5** |
| **E02** | Hallar la distancia entre $A(1, 2)$ y $B(4, 6)$. | 1. Calcular vector $\vec{AB}: (4-1, 6-2) = (3, 4)$.<br>2. Calcular su módulo (ver E01). | **5** |
| **E03** | ¿Cuál es el módulo del vector $\vec{w}(-6, 8)$? | 1. $\sqrt{(-6)^2 + 8^2} = \sqrt{36 + 64}$.<br>2. $\sqrt{100} = 10$. | **10** |
| **E04** | Si $|\vec{v}| = 13$ y su componente $x=5$, ¿cuánto vale $y$? | 1. $5^2 + y^2 = 13^2 \implies 25 + y^2 = 169$.<br>2. $y^2 = 144$. | **12** |
| **E05** | ¿Cuál es el módulo del vector nulo $(0, 0)$? | 1. $\sqrt{0^2 + 0^2} = 0$. | **0** |
""")

    with st.expander("❓ Cuestionario V03", expanded=False):
        quiz = [
            {'question': 'La magnitud o longitud de un vector se denomina:', 'options': {'A': 'Sentido', 'B': 'Dirección', 'C': 'Módulo', 'D': 'Trayectoria'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El módulo del vector $(-3, -4)$ es:', 'options': {'A': '-5', 'B': '7', 'C': '5', 'D': '25'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si un vector tiene módulo 10 y se pondera por $k = 3$, su nuevo módulo es:', 'options': {'A': '10', 'B': '13', 'C': '30', 'D': '100'}, 'answer': 'A', 'explanation': ''},
            {'question': 'La distancia entre los puntos $(0, 0)$ y $(12, 5)$ es:', 'options': {'A': '17', 'B': '13', 'C': '7', 'D': '$\\sqrt{17}$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si el módulo de un vector es 1, se dice que es un vector:', 'options': {'A': 'Nulo', 'B': 'Posición', 'C': 'Unitario', 'D': 'Isométrico'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El módulo del vector $(0, -7)$ es:', 'options': {'A': '-7', 'B': '0', 'C': '7', 'D': '49'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Para calcular la distancia entre dos puntos $P_1$ y $P_2$, aplicamos:', 'options': {'A': 'El Teorema de Tales', 'B': 'El Teorema de Pitágoras', 'C': 'El Teorema de Euclides', 'D': 'Solo una resta simple'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si un vector $\\vec{v}$ tiene módulo 5, ¿cuánto mide el vector $-2\\vec{v}$?', 'options': {'A': '-10', 'B': '10', 'C': '5', 'D': '3'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál de los siguientes vectores tiene el mayor módulo?', 'options': {'A': '$(1, 1)$', 'B': '$(0, 2)$', 'C': '$(-2, 0)$', 'D': '$(2, 1)$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si las componentes de un vector son iguales $(a, a)$, su módulo es:', 'options': {'A': '$2a$', 'B': '$a^2$', 'C': '$a\\sqrt{2}$', 'D': '$2a^2$'}, 'answer': 'A', 'explanation': ''}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="v03_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (V03)", expanded=False):
        st.markdown(r"""

""")
