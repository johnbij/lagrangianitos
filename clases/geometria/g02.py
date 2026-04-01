import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G02():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G02: Distancia entre Puntos")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    

    ---

    ### 🛡️ 1. La Fórmula del Alcance
    Para calcular la distancia entre $A(x_1, y_1)$ y $B(x_2, y_2)$, usamos el Teorema de Pitágoras aplicado al plano:

    $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

    ### ⚖️ 2. Procedimiento
    1. Resta las coordenadas $x$ y elévalas al cuadrado.
    2. Resta las coordenadas $y$ y elévalas al cuadrado.
    3. Suma ambos resultados y saca la raíz cuadrada.

    >
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G02 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G02 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Distancia entre $A(1, 2)$ y $B(4, 6)$ | 1. $(4-1)^2 + (6-2)^2 = 3^2 + 4^2$.<br>2. $\sqrt{9+16} = \sqrt{25}$. | **5 unidades** |
| **E02** | Distancia entre $C(-1, 3)$ y $D(2, -1)$ | 1. $(2-(-1))^2 + (-1-3)^2 = 3^2 + (-4)^2$.<br>2. $\sqrt{9+16} = \sqrt{25}$. | **5 unidades** |
| **E03** | Distancia de $P(0, 0)$ a $Q(3, 4)$ | 1. $(3-0)^2 + (4-0)^2 = 3^2 + 4^2$.<br>2. $\sqrt{9+16} = \sqrt{25}$. | **5 unidades** |
| **E04** | Distancia entre $A(1, 1)$ y $B(1, 5)$ | 1. $(1-1)^2 + (5-1)^2 = 0^2 + 4^2$.<br>2. $\sqrt{16}$. | **4 unidades** |
| **E05** | Distancia entre $A(2, 3)$ y $B(5, 3)$ | 1. $(5-2)^2 + (3-3)^2 = 3^2 + 0^2$.<br>2. $\sqrt{9}$. | **3 unidades** |
""")

    with st.expander("❓ Cuestionario G02", expanded=False):
        quiz = [
            {'question': 'La fórmula de la distancia entre dos puntos deriva de:', 'options': {'A': 'El Teorema de Tales', 'B': 'El Teorema de Pitágoras', 'C': 'La ecuación de la recta', 'D': 'La fórmula del punto medio'}, 'answer': 'B', 'explanation': 'La fórmula $d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ es literalmente Pitágoras ($a^2 + b^2 = c^2$) aplicado a los lados de un triángulo rectángulo imaginario formado por los puntos.'},
            {'question': '¿Cuál es la distancia entre los puntos $A(0, 0)$ y $B(0, 5)$?', 'options': {'A': '0 unidades', 'B': '3 unidades', 'C': '4 unidades', 'D': '5 unidades'}, 'answer': 'D', 'explanation': 'Si los puntos están en el mismo eje (en este caso el eje Y, ya que $x=0$), la distancia es simplemente la diferencia absoluta de las coordenadas que cambian: $'},
            {'question': '¿Cuál es la distancia entre los puntos $C(2, 0)$ y $D(6, 0)$?', 'options': {'A': '2 unidades', 'B': '4 unidades', 'C': '6 unidades', 'D': '8 unidades'}, 'answer': 'B', 'explanation': 'Los puntos están en el eje X ($y=0$). La distancia es $'},
            {'question': '¿Cuál es la distancia entre los puntos $E(1, 2)$ y $F(4, 6)$?', 'options': {'A': '3 unidades', 'B': '4 unidades', 'C': '5 unidades', 'D': '6 unidades'}, 'answer': 'C', 'explanation': 'Aplicamos la fórmula: $\\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9+16} = \\sqrt{25} = 5$.'},
            {'question': 'La distancia entre dos puntos en el plano cartesiano:', 'options': {'A': 'Puede ser negativa', 'B': 'Siempre es positiva o cero', 'C': 'Depende del orden de los puntos', 'D': 'Solo es positiva si los puntos están en el primer cuadrante'}, 'answer': 'B', 'explanation': 'La distancia mide longitud, y la longitud nunca es negativa. A lo sumo, es cero si los puntos son el mismo.'},
            {'question': '¿Cuál es la distancia entre $A(1, 1)$ y $B(4, 5)$?', 'options': {'A': '3', 'B': '4', 'C': '5', 'D': '7'}, 'answer': 'C', 'explanation': '$\\sqrt{(4-1)^2 + (5-1)^2} = \\sqrt{3^2 + 4^2} = 5$.'},
            {'question': 'Si la distancia entre $(1, 1)$ y $(1, y)$ es 3, ¿qué valor puede tomar $y$?', 'options': {'A': '3', 'B': '4', 'C': '5', 'D': '6'}, 'answer': 'B', 'explanation': 'La distancia es $'},
            {'question': '¿Cuál es la distancia entre $P(-1, -1)$ y $Q(2, 3)$?', 'options': {'A': '3', 'B': '4', 'C': '5', 'D': '6'}, 'answer': 'C', 'explanation': '$\\sqrt{(2-(-1))^2 + (3-(-1))^2} = \\sqrt{3^2 + 4^2} = 5$.'},
            {'question': 'Si la distancia entre $(x, 2)$ y $(5, 2)$ es 4, ¿qué valor puede tomar $x$?', 'options': {'A': '1', 'B': '2', 'C': '3', 'D': '4'}, 'answer': 'A', 'explanation': 'La distancia es $'},
            {'question': '¿Cuál es la distancia entre el origen $(0, 0)$ y el punto $(-3, -4)$?', 'options': {'A': '1', 'B': '5', 'C': '7', 'D': '25'}, 'answer': 'B', 'explanation': '$\\sqrt{(-3-0)^2 + (-4-0)^2} = \\sqrt{(-3)^2 + (-4)^2} = \\sqrt{9+16} = 5$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g02_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G02)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **B** | **Newton Tip:** "La fórmula $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ es literalmente Pitágoras ($a^2 + b^2 = c^2$) aplicado a los lados de un triángulo rectángulo imaginario formado por los puntos." |
| **2** | **D** | **Galileo Tip:** "Si los puntos están en el mismo eje (en este caso el eje Y, ya que $x=0$), la distancia es simplemente la diferencia absoluta de las coordenadas que cambian: $|5 - 0| = 5$." |
| **3** | **B** | **Hawking Tip:** "Los puntos están en el eje X ($y=0$). La distancia es $|6 - 2| = 4$." |
| **4** | **C** | **Curie Tip:** "Aplicamos la fórmula: $\sqrt{(4-1)^2 + (6-2)^2} = \sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5$." |
| **5** | **B** | **Newton Tip:** "La distancia mide longitud, y la longitud nunca es negativa. A lo sumo, es cero si los puntos son el mismo." |
| **6** | **C** | **Galileo Tip:** "$\sqrt{(4-1)^2 + (5-1)^2} = \sqrt{3^2 + 4^2} = 5$." |
| **7** | **B** | **Hawking Tip:** "La distancia es $|y-1|=3$. Por lo tanto, $y-1=3$ o $y-1=-3$, lo que da $y=4$ o $y=-2$. De las opciones, 4 es correcta." |
| **8** | **C** | **Curie Tip:** "$\sqrt{(2-(-1))^2 + (3-(-1))^2} = \sqrt{3^2 + 4^2} = 5$." |
| **9** | **A** | **Newton Tip:** "La distancia es $|5-x|=4$. Por lo tanto, $5-x=4$ o $5-x=-4$, lo que da $x=1$ o $x=9$. De las opciones, 1 es correcta." |
| **10** | **B** | **Galileo Tip:** "$\sqrt{(-3-0)^2 + (-4-0)^2} = \sqrt{(-3)^2 + (-4)^2} = \sqrt{9+16} = 5$." |
""")
