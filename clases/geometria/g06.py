import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G06():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G06: Triángulos — Los Cimientos de la Geometría")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    
    ---

    ### 🛡️ 1. Definición y Elementos
    Un triángulo es un polígono de tres lados que se forma al unir tres puntos no colineales mediante segmentos de recta. Sus elementos principales son: **Vértices**, **Lados** y **Ángulos** (internos y externos).

    ### ⚖️ 2. Propiedades Fundamentales (Teoremas)
    * **Suma de Ángulos Internos:** En todo triángulo, la suma de sus tres ángulos interiores es siempre **180°**.
    * **Suma de Ángulos Externos:** La suma de los ángulos exteriores (uno por vértice) es siempre **360°**.
    * **Teorema del Ángulo Exterior:** La medida de un ángulo exterior es igual a la suma de los dos ángulos interiores no adyacentes a él.
    * **Desigualdad Triangular:** En todo triángulo, la suma de las longitudes de dos de sus lados debe ser mayor que la longitud del tercer lado ($a + b > c$).

    > 
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G06 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G06 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Hallar el tercer ángulo si dos miden 50° y 60°. | 1. Sumar los ángulos conocidos: $50 + 60 = 110$.<br>2. Restar el total a la suma interna: $180 - 110 = 70$. | **70°** |
| **E02** | Determinar el ángulo exterior $\delta$ si los interiores no adyacentes son 45° y 35°. | 1. Aplicar el Teorema del Ángulo Exterior.<br>2. Sumar directamente los ángulos opuestos: $45 + 35 = 80$. | **80°** |
| **E03** | ¿Es posible construir un triángulo con lados de 4 cm, 5 cm y 10 cm? | 1. Sumar los dos lados menores: $4 + 5 = 9$.<br>2. Comparar con el tercer lado: $9$ no es mayor que $10$. | **No es posible** |
| **E04** | En un triángulo rectángulo, un ángulo agudo mide 28°. Hallar el otro. | 1. Sabemos que uno es 90°.<br>2. Los agudos deben sumar 90°: $90 - 28 = 62$. | **62°** |
| **E05** | Si los ángulos de un triángulo están en razón $1:2:3$, ¿cuánto miden? | 1. Plantear la ecuación: $1x + 2x + 3x = 180$.<br>2. $6x = 180 \implies x = 30$.<br>3. Multiplicar: $1(30), 2(30), 3(30)$. | **30°, 60° y 90°** |
""")

    with st.expander("❓ Cuestionario G06", expanded=False):
        quiz = [
            {'question': 'La suma de los ángulos interiores de cualquier triángulo es:', 'options': {'A': '90°', 'B': '180°', 'C': '270°', 'D': '360°'}, 'answer': 'B', 'explanation': 'Es la regla de oro de los triángulos en el plano. Grábatelo: siempre 180.'},
            {'question': 'Si un triángulo tiene ángulos de 90°, 45° y 45°, se clasifica como:', 'options': {'A': 'Acutángulo', 'B': 'Obtusángulo', 'C': 'Rectángulo', 'D': 'Equilátero'}, 'answer': 'C', 'explanation': 'Basta con que tenga UN ángulo de 90° para que sea rectángulo.'},
            {'question': 'El ángulo exterior de un triángulo es igual a:', 'options': {'A': 'El ángulo interior adyacente', 'B': 'La suma de los dos ángulos interiores no adyacentes', 'C': 'Siempre 180°', 'D': 'La mitad del ángulo interior'}, 'answer': 'B', 'explanation': 'Es una herramienta potente para resolver problemas de ángulos rápido sin pasar por el suplementario.'},
            {'question': '¿Cuál de los siguientes tríos de medidas pueden ser lados de un triángulo?', 'options': {'A': '1, 2, 3', 'B': '5, 5, 12', 'C': '3, 4, 5', 'D': '2, 2, 5'}, 'answer': 'C', 'explanation': 'En el trío 3, 4, 5, se cumple que $3+4 > 5$. En los demás, la suma es menor o igual al tercero.'},
            {'question': 'En un triángulo equilátero, cada ángulo interno mide:', 'options': {'A': '45°', 'B': '60°', 'C': '90°', 'D': '180°'}, 'answer': 'B', 'explanation': 'Típ: Si los 3 lados son iguales, los 3 ángulos también. $180 / 3 = 60$.'},
            {'question': 'Si un triángulo tiene un ángulo de 110°, se clasifica como:', 'options': {'A': 'Acutángulo', 'B': 'Rectángulo', 'C': 'Obtusángulo', 'D': 'Isósceles'}, 'answer': 'C', 'explanation': 'Si tiene un ángulo mayor a 90°, es un triángulo obtuso (u obtusángulo).'},
            {'question': 'La suma de los ángulos exteriores de un triángulo es:', 'options': {'A': '180°', 'B': '360°', 'C': '540°', 'D': '720°'}, 'answer': 'B', 'explanation': 'Esta regla aplica para todos los polígonos, pero en el triángulo es donde más se pregunta.'},
            {'question': 'Si dos ángulos de un triángulo suman 100°, el tercer ángulo mide:', 'options': {'A': '100°', 'B': '80°', 'C': '90°', 'D': '180°'}, 'answer': 'B', 'explanation': 'Simple aritmética: $180 - 100 = 80$.'},
            {'question': 'En un triángulo isósceles, los ángulos de la base son:', 'options': {'A': 'Siempre 90°', 'B': 'Diferentes', 'C': 'Iguales', 'D': 'Complementarios'}, 'answer': 'C', 'explanation': 'Lados iguales se oponen a ángulos iguales. Esa es la esencia del isósceles.'},
            {'question': 'La propiedad que indica que la suma de dos lados debe ser mayor al tercero es:', 'options': {'A': 'Teorema de Pitágoras', 'B': 'Desigualdad Triangular', 'C': 'Teorema de Tales', 'D': 'Propiedad de Euclides'}, 'answer': 'B', 'explanation': "Típ: Si no se cumple esto, las líneas nunca se 'alcanzan' para cerrar la figura."}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g06_quiz")
