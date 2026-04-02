import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_V01():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("V01: Introducción a los Vectores — El Mapa del Movimiento")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase V01: Introducción a los Vectores - El Mapa del Movimiento
    **Eje:** Vectores | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. ¿Qué es un Vector?
    A diferencia de un número común (escalar), un vector es una herramienta que nos indica tres cosas fundamentales:
    1. **Módulo (Magnitud):** Cuán "largo" es el vector (su valor numérico).
    2. **Dirección:** La recta sobre la que descansa el vector (indicada por el ángulo).
    3. **Sentido:** Hacia dónde apunta la flecha (indicado por la punta).

    ### ⚖️ 2. Representación en el Plano
    Un vector $\vec{v}$ en el plano cartesiano se representa como un par ordenado $(x, y)$.
    * **Componente $x$:** Desplazamiento horizontal.
    * **Componente $y$:** Desplazamiento vertical.

    ### 📐 3. Vector entre dos puntos
    Si tenemos un punto inicial $A(x_1, y_1)$ y un punto final $B(x_2, y_2)$, el vector $\vec{AB}$ se calcula restando:
    $$\vec{AB} = (x_2 - x_1, y_2 - y_1)$$

    > **Newton Tip:** "Seba, dile a tu alumno: el vector no es un punto, es un RECORRIDO. El punto te dice dónde estás, el vector te dice cómo moverte de un lugar a otro."
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica V01 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica V01 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Identificar componentes del vector que va de $(0,0)$ a $(3, 5)$. | 1. Restar final menos inicial: $(3-0, 5-0)$. | **$\vec{v}(3, 5)$** |
| **E02** | Hallar el vector $\vec{AB}$ con $A(1, 2)$ y $B(4, 6)$. | 1. Componente $x: 4 - 1 = 3$.<br>2. Componente $y: 6 - 2 = 4$. | **$\vec{v}(3, 4)$** |
| **E03** | Si un vector es $(-2, 3)$, ¿qué significa gráficamente? | 1. Se mueve 2 unidades a la izquierda.<br>2. Sube 3 unidades. | **Izquierda y Arriba** |
| **E04** | ¿Cuál es el vector posición del punto $P(-5, 8)$? | 1. El vector posición siempre sale desde el origen $(0,0)$. | **$\vec{v}(-5, 8)$** |
| **E05** | Hallar punto final si el inicial es $(1, 1)$ y el vector es $(2, 3)$. | 1. Sumar inicial + vector: $(1+2, 1+3)$. | **$B(3, 4)$** |
""")

    with st.expander("❓ Cuestionario V01", expanded=False):
        quiz = [
            {'question': 'Un vector queda totalmente definido por su:', 'options': {'A': 'Color, tamaño y posición', 'B': 'Módulo, dirección y sentido', 'C': 'Eje x y eje y solamente', 'D': 'Ángulo y punto de origen'}, 'answer': 'B', 'explanation': "Es el 'tridente' de la física. Si falta uno, no es un vector completo."},
            {'question': 'El componente horizontal de un vector $(x, y)$ es:', 'options': {'A': 'El valor de $y$', 'B': 'La suma $x + y$', 'C': 'El valor de $x$', 'D': 'El módulo'}, 'answer': 'C', 'explanation': 'En el plano cartesiano, $x$ siempre manda en lo horizontal (izquierda/derecha).'},
            {'question': 'Si un vector tiene sentido hacia la derecha y hacia abajo, sus componentes son:', 'options': {'A': '$(+, +)$', 'B': '$(-, -)$', 'C': '$(+, -)$', 'D': '$(-, +)$'}, 'answer': 'C', 'explanation': 'Derecha es $x$ positivo, abajo es $y$ negativo. Simple lógica de cuadrantes.'},
            {'question': 'El vector que une el origen $(0,0)$ con un punto $P$ se llama:', 'options': {'A': 'Vector nulo', 'B': 'Vector posición', 'C': 'Vector unitario', 'D': 'Vector resultante'}, 'answer': 'B', 'explanation': 'Es como el GPS: te dice exactamente dónde estás respecto al punto $(0,0)$.'},
            {'question': 'Para obtener el vector $\\vec{AB}$, debemos calcular:', 'options': {'A': '$A + B$', 'B': '$A - B$\n) $B - A$\nD) $A \\cdot B$\n\n**6. Si el vector $\\vec{v}$ es $(0, -5)$, este apunta hacia:**\nA) Arriba\nB) Abajo', 'C': 'Izquierda', 'D': 'Derecha'}, 'answer': 'C', 'explanation': 'Típ: Siempre es Final menos Inicial. Si lo haces al revés, la flecha apuntará al lado contrario.'},
            {'question': 'Dos vectores son iguales (congruentes) si tienen igual:', 'options': {'A': 'Punto de inicio solamente', 'B': 'Color y grosor', 'C': 'Módulo, dirección y sentido', 'D': 'Solo el mismo módulo'}, 'answer': 'C', 'explanation': 'Pueden estar en distintos lugares del plano, pero si miden lo mismo y apuntan igual, son el mismo vector.'},
            {'question': 'La "flecha" de la representación gráfica de un vector indica su:', 'options': {'A': 'Dirección', 'B': 'Sentido', 'C': 'Módulo', 'D': 'Origen'}, 'answer': 'B', 'explanation': 'La inclinación es la dirección, pero la punta de la flecha es el sentido.'},
            {'question': 'Si el punto $A$ es $(2, 2)$ y el vector $\\vec{AB}$ es $(1, 0)$, el punto $B$ es:', 'options': {'A': '$(3, 2)$', 'B': '$(2, 3)$', 'C': '$(1, 2)$', 'D': '$(2, 1)$'}, 'answer': 'A', 'explanation': 'Suma el desplazamiento al punto original: $(2+1, 2+0) = (3, 2)$.'},
            {'question': 'Un vector cuya componente $x$ es cero es un vector:', 'options': {'A': 'Horizontal', 'B': 'Vertical', 'C': 'Nulo', 'D': 'Diagonal'}, 'answer': 'B', 'explanation': 'Típ: Si no se mueve de lado a lado, solo le queda subir o bajar. Eso es vertical.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="v01_quiz")
