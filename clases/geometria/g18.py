import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G18():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G18: Homotecia — Ampliación y Reducción Vectorial")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # G18: Homotecia - Ampliación y Reducción Vectorial
    

    ---

    ### 🛡️ 1. Definición
    La homotecia es una transformación geométrica que permite obtener una figura semejante a otra a partir de un **centro de homotecia ($O$)** y una **razón de homotecia ($k$)**.

    ### ⚖️ 2. Tipos de Homotecia según la Razón ($k$)
    * **Directa ($k > 0$):** La figura resultante está al mismo lado del centro $O$ que la original.
        * Si $|k| > 1$: Ampliación.
        * Si $|k| < 1$: Reducción.
    * **Inversa ($k < 0$):** La figura resultante está al lado opuesto del centro $O$ (se ve "invertida").

    ### 📐 3. Propiedades Clave
    1. Los puntos $O$, $P$ (original) y $P'$ (homotético) son siempre **colineales**.
    2. La distancia del centro al punto nuevo es $k$ veces la distancia al punto original: $OP' = k \cdot OP$.
    3. Al igual que en semejanza:
        * Los lados están en razón $k$.
        * Los perímetros están en razón $|k|$.
        * Las áreas están en razón $k^2$.

    >  
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G18 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G18 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **1** | Aplicar homotecia con $k=3$ a un punto $P(2, 4)$ con centro $O(0,0)$. | 1. Multiplicar cada coordenada por $k$. <br>2. $(2 \cdot 3, 4 \cdot 3)$. | **$P'(6, 12)$** |
| **2** | Un triángulo de área 4 se somete a $k=-2$. Hallar área nueva. | 1. Razón de áreas es $k^2$. <br>2. $(-2)^2 = 4$. <br>3. $4 \cdot 4 = 16$. | **16 u²** |
| **3** | Si $OP = 5$ cm y $OP' = 15$ cm (en el mismo sentido), ¿cuánto es $k$? | 1. $k = OP' / OP$. <br>2. $k = 15 / 5$. | **$k = 3$** |
| **4** | ¿Qué sucede con la figura si $k = -1$? | 1. Se mantiene el tamaño ($|1|$) pero se invierte respecto al centro. | **Simetría Central** |
| **5** | Distancia $OP=10$. Si $k=0.5$, ¿dónde queda $P'$? | 1. $OP' = 10 \cdot 0.5 = 5$. | **A 5 unidades de O** |
""")

    with st.expander("❓ Cuestionario G18", expanded=False):
        quiz = [
            {'question': "En una homotecia, los puntos $O$ (centro), $A$ (original) y $A'$ (imagen) son siempre:", 'options': {'A': 'Vértices de un triángulo', 'B': 'Perpendiculares', 'C': 'Colineales', 'D': 'Equidistantes'}, 'answer': 'C', 'explanation': "Siempre están en la misma línea que sale desde el centro. Es la 'guía' de la transformación."},
            {'question': 'Si la razón de homotecia es $k = 0.5$, la figura resultante es:', 'options': {'A': 'Una ampliación', 'B': 'Una reducción', 'C': 'Igual a la original', 'D': 'Inversa y más grande'}, 'answer': 'B', 'explanation': 'Cualquier número entre 0 y 1 achica la figura. Piensa en porcentajes: 0.5 es el 50%.'},
            {'question': 'Una homotecia inversa ocurre cuando la razón $k$ es:', 'options': {'A': 'Mayor a 1', 'B': 'Entre 0 y 1', 'C': 'Menor que 0 (negativa)', 'D': 'Igual a 1'}, 'answer': 'C', 'explanation': "El signo negativo significa que la figura 'saltó' hacia el otro lado del centro."},
            {'question': 'Si el área de la figura original es $A$ y la razón es $k$, el área de la nueva figura es:', 'options': {'A': '$k \\cdot A$', 'B': '$k^2 \\cdot A$', 'C': '$2k \\cdot A$', 'D': '$A / k$'}, 'answer': 'B', 'explanation': 'Igual que en semejanza, el área siempre depende del cuadrado de la razón.'},
            {'question': 'Si aplicamos una homotecia con $k = 1$, la figura resultante es:', 'options': {'A': 'El doble de grande', 'B': 'La mitad de grande', 'C': 'Identica a la original (Congruente)', 'D': 'Un punto'}, 'answer': 'C', 'explanation': 'Típ: $k=1$ es el elemento neutro. No agranda, no achica, no mueve. Todo queda igual.'},
            {'question': 'En una homotecia con centro en el origen $(0,0)$ y $k = -3$, el punto $(1, -2)$ se transforma en:', 'options': {'A': '$(-3, 6)$', 'B': '$(3, -6)$', 'C': '$(-3, -6)$', 'D': '$(3, 6)$'}, 'answer': 'A', 'explanation': '$1 \\cdot (-3) = -3$ y $-2 \\cdot (-3) = 6$. Solo multiplica cada parte por $k$.'},
            {'question': "Si la distancia $OA'$ es el triple de $OA$ y están en sentidos opuestos, la razón $k$ es:", 'options': {'A': '3', 'B': '1/3', 'C': '-3', 'D': '-1/3'}, 'answer': 'C', 'explanation': 'Triple = 3. Sentidos opuestos = Negativo. Resultado: -3.'},
            {'question': 'Si $k = -2$, ¿cómo es el perímetro de la nueva figura respecto a la original?', 'options': {'A': 'El doble', 'B': 'El cuádruple', 'C': 'La mitad', 'D': 'Menos el doble'}, 'answer': 'A', 'explanation': 'El perímetro es lineal, usamos el valor absoluto de $k$. $'},
            {'question': 'Para que una figura homotética sea más pequeña e invertida, $k$ debe estar entre:', 'options': {'A': '$k > 1$', 'B': '$0 < k < 1$', 'C': '$-1 < k < 0$', 'D': '$k < -1$'}, 'answer': 'C', 'explanation': 'El signo $(-)$ la invierte y la fracción propia (como $-0.5$) la achica.'},
            {'question': 'La homotecia preserva:', 'options': {'A': 'La medida de los lados', 'B': 'El área', 'C': 'La medida de los ángulos (forma)', 'D': 'La posición original'}, 'answer': 'C', 'explanation': 'Típ: Como es una forma de semejanza, los ángulos no se tocan. La figura no se deforma, solo escala.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g18_quiz")
