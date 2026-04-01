import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G03():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G03: El Punto Medio")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    
    ---

    ### 🛡️ 1. Definición
    El punto medio $M$ es aquel que divide a un segmento de recta en dos partes iguales. Es el "centro" entre dos puntos $A(x_1, y_1)$ y $B(x_2, y_2)$.

    ### ⚖️ 2. La Fórmula
    Para encontrar las coordenadas del punto medio $M(x_m, y_m)$, calculamos el promedio de las coordenadas de los extremos:

    $$x_m = \frac{x_1 + x_2}{2}, \quad y_m = \frac{y_1 + y_2}{2}$$

    >
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G03 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G03 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Punto medio entre $A(1, 2)$ y $B(3, 4)$ | 1. $x_m = (1+3)/2 = 2$.<br>2. $y_m = (2+4)/2 = 3$. | **$M(2, 3)$** |
| **E02** | Punto medio entre $C(-1, 5)$ y $D(3, 1)$ | 1. $x_m = (-1+3)/2 = 1$.<br>2. $y_m = (5+1)/2 = 3$. | **$M(1, 3)$** |
| **E03** | Punto medio entre $P(0, 0)$ y $Q(4, 6)$ | 1. $x_m = (0+4)/2 = 2$.<br>2. $y_m = (0+6)/2 = 3$. | **$M(2, 3)$** |
| **E04** | Punto medio entre $A(2, 3)$ y $B(2, 7)$ | 1. $x_m = (2+2)/2 = 2$.<br>2. $y_m = (3+7)/2 = 5$. | **$M(2, 5)$** |
| **E05** | Punto medio entre $A(1, 4)$ y $B(5, 4)$ | 1. $x_m = (1+5)/2 = 3$.<br>2. $y_m = (4+4)/2 = 4$. | **$M(3, 4)$** |
""")

    with st.expander("❓ Cuestionario G03", expanded=False):
        quiz = [
            {'question': 'La fórmula del punto medio calcula:', 'options': {'A': 'La distancia entre dos puntos', 'B': 'El promedio de las coordenadas de los extremos', 'C': 'La pendiente de la recta', 'D': 'El área del segmento'}, 'answer': 'B', 'explanation': 'Punto medio es sinónimo de promedio: $\\frac{\\text{suma}}{2}$.'},
            {'question': '¿Cuál es el punto medio entre $A(0, 0)$ y $B(0, 8)$?', 'options': {'A': '$(0, 0)$', 'B': '$(0, 4)$', 'C': '$(0, 8)$', 'D': '$(4, 0)$'}, 'answer': 'B', 'explanation': 'Promedio en X: $(0+0)/2 = 0$. Promedio en Y: $(0+8)/2 = 4$.'},
            {'question': '¿Cuál es el punto medio entre $C(2, 0)$ y $D(10, 0)$?', 'options': {'A': '$(4, 0)$', 'B': '$(5, 0)$', 'C': '$(6, 0)$', 'D': '$(8, 0)$'}, 'answer': 'C', 'explanation': 'Promedio en X: $(2+10)/2 = 6$. Promedio en Y: $(0+0)/2 = 0$.'},
            {'question': '¿Cuál es el punto medio entre $E(1, 3)$ y $F(5, 7)$?', 'options': {'A': '$(2, 4)$', 'B': '$(3, 5)$', 'C': '$(4, 6)$', 'D': '$(6, 10)$'}, 'answer': 'B', 'explanation': 'Promedio en X: $(1+5)/2 = 3$. Promedio en Y: $(3+7)/2 = 5$.'},
            {'question': 'Si el punto medio es $(2, 2)$ y un extremo es $(0, 0)$, ¿cuál es el otro extremo?', 'options': {'A': '$(1, 1)$', 'B': '$(2, 2)$', 'C': '$(4, 4)$', 'D': '$(-2, -2)$'}, 'answer': 'C', 'explanation': 'El doble del punto medio menos el extremo conocido da el extremo desconocido: $2(2)-0 = 4$.'},
            {'question': '¿Cuál es el punto medio entre $A(-2, -4)$ y $B(4, 8)$?', 'options': {'A': '$(1, 2)$', 'B': '$(2, 4)$', 'C': '$(3, 6)$', 'D': '$(-1, -2)$'}, 'answer': 'A', 'explanation': 'Promedio en X: $(-2+4)/2 = 1$. Promedio en Y: $(-4+8)/2 = 2$.'},
            {'question': 'Si el punto medio es $(3, 3)$ y un extremo es $(1, 1)$, ¿cuál es el otro extremo?', 'options': {'A': '$(2, 2)$', 'B': '$(4, 4)$', 'C': '$(5, 5)$', 'D': '$(6, 6)$'}, 'answer': 'C', 'explanation': 'Doblar el medio y restar el extremo: $2(3)-1 = 5$.'},
            {'question': '¿Cuál es el punto medio entre $P(-3, 5)$ y $Q(3, -5)$?', 'options': {'A': '$(0, 0)$', 'B': '$(3, 5)$', 'C': '$(-3, -5)$', 'D': '$(0, 10)$'}, 'answer': 'A', 'explanation': 'Promedio en X: $(-3+3)/2 = 0$. Promedio en Y: $(5-5)/2 = 0$.'},
            {'question': 'Si el punto medio es $(1, 2)$ y un extremo es $(3, 4)$, ¿cuál es el otro extremo?', 'options': {'A': '$(2, 3)$', 'B': '$(-1, 0)$', 'C': '$(0, -1)$', 'D': '$(-2, -2)$'}, 'answer': 'B', 'explanation': 'Doblar el medio y restar el extremo: $2(1)-3 = -1$ (para X) y $2(2)-4 = 0$ (para Y).'},
            {'question': '¿Cuál es el punto medio entre el origen $(0, 0)$ y el punto $(x, y)$?', 'options': {'A': '$(x, y)$', 'B': '$(x/2, y/2)$', 'C': '$(2x, 2y)$', 'D': '$(0, 0)$'}, 'answer': 'B', 'explanation': 'Promedio con cero es simplemente dividir por dos.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g03_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G03)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **B** | **Newton Tip:** "Punto medio es sinónimo de promedio: $\frac{\text{suma}}{2}$." |
| **2** | **B** | **Galileo Tip:** "Promedio en X: $(0+0)/2 = 0$. Promedio en Y: $(0+8)/2 = 4$." |
| **3** | **C** | **Hawking Tip:** "Promedio en X: $(2+10)/2 = 6$. Promedio en Y: $(0+0)/2 = 0$." |
| **4** | **B** | **Curie Tip:** "Promedio en X: $(1+5)/2 = 3$. Promedio en Y: $(3+7)/2 = 5$." |
| **5** | **C** | **Newton Tip:** "El doble del punto medio menos el extremo conocido da el extremo desconocido: $2(2)-0 = 4$." |
| **6** | **A** | **Galileo Tip:** "Promedio en X: $(-2+4)/2 = 1$. Promedio en Y: $(-4+8)/2 = 2$." |
| **7** | **C** | **Hawking Tip:** "Doblar el medio y restar el extremo: $2(3)-1 = 5$." |
| **8** | **A** | **Curie Tip:** "Promedio en X: $(-3+3)/2 = 0$. Promedio en Y: $(5-5)/2 = 0$." |
| **9** | **B** | **Newton Tip:** "Doblar el medio y restar el extremo: $2(1)-3 = -1$ (para X) y $2(2)-4 = 0$ (para Y)." |
| **10** | **B** | **Galileo Tip:** "Promedio con cero es simplemente dividir por dos." |
""")
