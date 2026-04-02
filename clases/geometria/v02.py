import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_V02():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("V02: Operaciones con Vectores — Combinando Movimientos")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase V02: Operaciones con Vectores - Combinando Movimientos
    **Eje:** Vectores | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. Suma de Vectores
    Para sumar dos vectores $\vec{u}(x_1, y_1)$ y $\vec{v}(x_2, y_2)$, sumamos sus componentes respectivas:
    $$\vec{u} + \vec{v} = (x_1 + x_2, \space y_1 + y_2)$$
    * **Gráficamente:** Se usa el **Método del Paralelogramo** o el **Método del Triángulo** (poner el inicio de uno en la punta del otro).

    ### ⚖️ 2. Resta de Vectores
    Restar es sumar el opuesto. Si a $\vec{u}$ le restamos $\vec{v}$:
    $$\vec{u} - \vec{v} = (x_1 - x_2, \space y_1 - y_2)$$
    * **Gráficamente:** El vector resultante va desde la punta de $\vec{v}$ hasta la punta de $\vec{u}$.

    ### 📐 3. Ponderación por un Escalar ($k \cdot \vec{v}$)
    Multiplicar un vector por un número real $k$ (escalar):
    $$k \cdot (x, y) = (k \cdot x, \space k \cdot y)$$
    * **Si $k > 1$:** El vector se alarga (amplificación).
    * **Si $0 < k < 1$:** El vector se acorta (reducción).
    * **Si $k < 0$:** El vector cambia de sentido (punta hacia el lado opuesto).

    > **Newton Tip:** "Seba, dile a tu alumno: sumar vectores es como dar pasos. Si caminas 3 pasos al norte y luego 2 al este, el vector resultante es el camino directo desde donde empezaste hasta donde terminaste."
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica V02 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica V02 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Sumar $\vec{u}(2, 3)$ y $\vec{v}(5, -1)$. | 1. Sumar $x: 2 + 5 = 7$.<br>2. Sumar $y: 3 + (-1) = 2$. | **$(7, 2)$** |
| **E02** | Restar $\vec{a}(4, 8) - \vec{b}(1, 2)$. | 1. Restar $x: 4 - 1 = 3$.<br>2. Restar $y: 8 - 2 = 6$. | **$(3, 6)$** |
| **E03** | Ponderar el vector $\vec{w}(-2, 4)$ por $k=3$. | 1. Multiplicar cada parte por 3: $(-2 \cdot 3, 4 \cdot 3)$. | **$(-6, 12)$** |
| **E04** | Hallar el inverso aditivo de $\vec{v}(5, -7)$. | 1. Multiplicar por $-1$: $(-5, 7)$. | **$(-5, 7)$** |
| **E05** | Calcular $2\vec{u} + \vec{v}$ si $\vec{u}(1, 2)$ y $\vec{v}(3, 0)$. | 1. $2\vec{u} = (2, 4)$.<br>2. Sumar con $\vec{v}: (2+3, 4+0)$. | **$(5, 4)$** |
""")

    with st.expander("❓ Cuestionario V02", expanded=False):
        quiz = [
            {'question': 'La suma de los vectores $(3, 5)$ y $(-1, 2)$ es:', 'options': {'A': '$(2, 7)$', 'B': '$(4, 7)$', 'C': '$(2, 3)$', 'D': '$(4, 3)$'}, 'answer': 'A', 'explanation': 'Suma componente a componente: $3-1=2$ y $5+2=7$.'},
            {'question': 'Si ponderamos el vector $(2, -4)$ por $k = 0,5$, el resultado es:', 'options': {'A': '$(4, -8)$', 'B': '$(1, -2)$', 'C': '$(1, 2)$', 'D': '$(2, -2)$'}, 'answer': 'B', 'explanation': 'Ponderar por 0,5 es lo mismo que dividir por 2. Mitad de cada uno.'},
            {'question': 'El vector opuesto (inverso aditivo) de $\\vec{v}(a, b)$ es:', 'options': {'A': '$(b, a)$', 'B': '$(-a, b)$', 'C': '$(a, -b)$', 'D': '$(-a, -b)$'}, 'answer': 'D', 'explanation': "El opuesto es el que 'anula' al original, por eso ambos signos deben cambiar."},
            {'question': 'Gráficamente, al sumar dos vectores por el método "punta y cola", el vector resultante une:', 'options': {'A': 'Las dos puntas', 'B': 'Los dos orígenes', 'C': 'El origen del primero con la punta del segundo', 'D': 'El origen del segundo con la punta del primero'}, 'answer': 'C', 'explanation': 'Es el camino más corto entre el inicio del viaje y el final del segundo tramo.'},
            {'question': 'Si $k = -2$ y $\\vec{v} = (3, 1)$, entonces $k \\vec{v}$ es:', 'options': {'A': '$(-6, -2)$', 'B': '$(6, 2)$', 'C': '$(-6, 2)$', 'D': '$(1, -1)$'}, 'answer': 'A', 'explanation': 'Típ: El $-2$ multiplica a ambos, cambiando signos y duplicando valores.'},
            {'question': '¿Qué ocurre con la dirección de un vector al multiplicarlo por $k = -1$?', 'options': {'A': 'Cambia la dirección', 'B': 'Se mantiene la dirección pero cambia el sentido', 'C': 'Se vuelve perpendicular', 'D': 'Se reduce a la mitad'}, 'answer': 'B', 'explanation': 'Ojo aquí: la recta (dirección) es la misma, solo que ahora la flecha mira hacia atrás.'},
            {'question': 'Al restar $\\vec{u} - \\vec{u}$, el resultado es:', 'options': {'A': '$1$', 'B': '$\\vec{u}$', 'C': '$\\vec{0}(0, 0)$', 'D': '$-\\vec{u}$'}, 'answer': 'C', 'explanation': 'Cualquier vector restado por sí mismo nos devuelve al origen, el vector nulo.'},
            {'question': 'Si $3 \\cdot (x, 4) = (6, 12)$, el valor de $x$ es:', 'options': {'A': '2', 'B': '3', 'C': '6', 'D': '18'}, 'answer': 'A', 'explanation': 'Simplemente despeja: $3x = 6$, entonces $x = 2$.'},
            {'question': 'La operación $2 \\cdot (1, 3) + (0, -2)$ da como resultado:', 'options': {'A': '$(2, 4)$', 'B': '$(2, 1)$', 'C': '$(1, 4)$', 'D': '$(2, 6)$'}, 'answer': 'A', 'explanation': 'Primero el producto: $(2, 6)$. Luego la suma: $(2+0, 6-2) = (2, 4)$.'},
            {'question': 'Dos vectores son paralelos si uno es la _____ del otro por un escalar:', 'options': {'A': 'Suma', 'B': 'Resta', 'C': 'Ponderación', 'D': 'Potencia'}, 'answer': 'C', 'explanation': 'Típ: Si puedes obtener un vector multiplicando el otro por un número, es que tienen la misma inclinación.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="v02_quiz")
