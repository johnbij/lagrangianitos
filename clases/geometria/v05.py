import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_V05():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("V05: Vectores en el Espacio — La Tercera Dimensión")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase V05: Vectores en el Espacio - La Tercera Dimensión
    **Eje:** Vectores | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. El Sistema de Coordenadas 3D
    Para representar el espacio, añadimos un tercer eje perpendicular a los otros dos:
    * **Eje X:** Ancho (Abscisas)
    * **Eje Y:** Largo (Ordenadas)
    * **Eje Z:** Alto (Cotas)
    Un punto o vector se expresa como una terna ordenada: $\vec{v}(x, y, z)$.

    ### ⚖️ 2. Operaciones en 3D
    Se mantienen las mismas reglas que en el plano, pero aplicadas a las tres componentes:
    * **Suma/Resta:** $(x_1, y_1, z_1) \pm (x_2, y_2, z_2) = (x_1 \pm x_2, \space y_1 \pm y_2, \space z_1 \pm z_2)$
    * **Ponderación:** $k \cdot (x, y, z) = (kx, ky, kz)$

    ### 📐 3. Módulo en el Espacio
    Para hallar la medida de un vector en 3D, extendemos el Teorema de Pitágoras:
    $$|\vec{v}| = \sqrt{x^2 + y^2 + z^2}$$

    > **Newton Tip:** "Seba, dile a tu alumno: trabajar en 3D es como estar en una habitación. El eje $X$ es una pared, el $Y$ es la otra y el $Z$ es la altura del techo. ¡La matemática no cambia, solo se vuelve más profunda!"
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica V05 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica V05 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Sumar $\vec{u}(1, 2, 3)$ y $\vec{v}(0, -1, 4)$. | 1. Sumar cada eje: $(1+0, 2-1, 3+4)$. | **$(1, 1, 7)$** |
| **E02** | Calcular el módulo del vector $\vec{w}(2, 2, 1)$. | 1. $\sqrt{2^2 + 2^2 + 1^2} = \sqrt{4 + 4 + 1}$.<br>2. $\sqrt{9} = 3$. | **3** |
| **E03** | Ponderar $\vec{a}(5, -10, 15)$ por $k = 0,2$. | 1. Multiplicar cada parte por $0,2$ (o dividir por 5). | **$(1, -2, 3)$** |
| **E04** | Hallar vector $\vec{AB}$ con $A(1, 1, 1)$ y $B(2, 3, 4)$. | 1. Restar $B - A: (2-1, 3-1, 4-1)$. | **$(1, 2, 3)$** |
| **E05** | Distancia entre el origen $(0,0,0)$ y el punto $(3, 0, 4)$. | 1. Es el módulo de $(3, 0, 4) = \sqrt{3^2 + 0^2 + 4^2}$. | **5** |
""")

    with st.expander("❓ Cuestionario V05", expanded=False):
        quiz = [
            {'question': 'El tercer eje que se añade en el espacio 3D se conoce como eje de las:', 'options': {'A': 'Abscisas', 'B': 'Ordenadas', 'C': 'Cotas', 'D': 'Diagonales'}, 'answer': 'C', 'explanation': 'X es ancho, Y es profundidad, Z es la cota o altura.'},
            {'question': 'El módulo del vector $(1, 1, 1)$ es:', 'options': {'A': '1', 'B': '3', 'C': '$\\sqrt{3}$', 'D': '$\\sqrt{1}$'}, 'answer': 'C', 'explanation': '$\\sqrt{1^2 + 1^2 + 1^2} = \\sqrt{1+1+1} = \\sqrt{3}$. No la confundas con 3.'},
            {'question': 'Si sumamos $(2, 4, 6)$ con $(-2, -4, -6)$, obtenemos:', 'options': {'A': '$(0, 0, 0)$', 'B': '$(4, 8, 12)$', 'C': '$(1, 1, 1)$', 'D': 'Un punto en el infinito'}, 'answer': 'A', 'explanation': 'Sumar un vector con su opuesto siempre nos lleva de vuelta al reposo, el vector nulo.'},
            {'question': 'La ponderación de $(-3, 6, 9)$ por $k = -1/3$ resulta en:', 'options': {'A': '$(1, 2, 3)$', 'B': '$(1, -2, -3)$', 'C': '$(-1, 2, 3)$', 'D': '$(3, -6, -9)$'}, 'answer': 'B', 'explanation': 'El signo negativo invierte todo y el $1/3$ reduce los valores a la tercera parte.'},
            {'question': 'Un vector en el espacio que solo tiene componente en el eje Z es un vector:', 'options': {'A': 'Horizontal', 'B': 'Vertical (en el plano XY)', 'C': 'Perpendicular al suelo (plano XY)', 'D': 'Nulo'}, 'answer': 'C', 'explanation': "Típ: Si no tiene ancho ni largo, solo le queda 'subir' desde el plano del suelo."},
            {'question': 'El módulo del vector $(0, 12, 5)$ es:', 'options': {'A': '12', 'B': '17', 'C': '13', 'D': '5'}, 'answer': 'C', 'explanation': 'Es el trío pitagórico (5, 12, 13) pero en una posición distinta. La matemática no miente.'},
            {'question': 'Si el punto inicial es $(1, 2, 3)$ y el vector es $(1, 1, 1)$, el punto final es:', 'options': {'A': '$(0, 0, 0)$', 'B': '$(2, 3, 4)$', 'C': '$(1, 1, 1)$', 'D': '$(2, 2, 2)$'}, 'answer': 'B', 'explanation': 'Suma componente a componente para trasladar el punto en el espacio.'},
            {'question': 'En 3D, ¿cuántos planos de referencia se forman (XY, XZ, YZ)?', 'options': {'A': '1', 'B': '2', 'C': '3', 'D': '4'}, 'answer': 'C', 'explanation': 'Imagina el rincón de una caja: tienes el piso y dos paredes laterales.'},
            {'question': 'El vector $(x, y, z)$ se encuentra en el origen si:', 'options': {'A': '$x = y$', 'B': '$z = 0$', 'C': '$x = 0, y = 0, z = 0$', 'D': '$x+y+z = 0$'}, 'answer': 'C', 'explanation': 'El origen es el punto de partida absoluto $(0,0,0)$.'},
            {'question': 'La distancia entre $(1, 0, 0)$ y $(1, 0, 5)$ es:', 'options': {'A': '1', 'B': '5', 'C': '6', 'D': '$\\sqrt{26}$'}, 'answer': 'B', 'explanation': 'Típ: Como $x$ e $y$ son iguales, la distancia es simplemente la diferencia en $z$: $5 - 0 = 5$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="v05_quiz")
