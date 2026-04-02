import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G15():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G15: Teoremas de Euclides — Proporciones en el Triángulo Rectángulo")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase G15: Teoremas de Euclides - Proporciones en el Triángulo Rectángulo
    **Eje:** Geometría | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. El Escenario
    Para aplicar Euclides, necesitamos un **triángulo rectángulo** y trazar la **altura ($h_c$)** desde el ángulo recto hacia la hipotenusa. Esta altura divide a la hipotenusa en dos segmentos llamados **proyecciones** ($p$ y $q$).

    ### ⚖️ 2. Los Dos Teoremas Fundamentales
    * **Teorema de la Altura:** El cuadrado de la altura es igual al producto de las proyecciones de los catetos.
      $$h_c^2 = p \cdot q$$

    * **Teorema del Cateto:** El cuadrado de cada cateto es igual al producto de su proyección por la hipotenusa completa ($c$).
      $$a^2 = p \cdot c$$
      $$b^2 = q \cdot c$$

    ### 📐 3. Relación Adicional (Área)
    También se cumple que el producto de los catetos es igual al producto de la hipotenusa por la altura:
    $$a \cdot b = c \cdot h_c$$

    > **Newton Tip:** "Seba, dile a tu alumno: Euclides es el hermano de Pitágoras. Si con uno no puedes sacar el lado, el otro seguro te da la respuesta usando las proyecciones."
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G15 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G15 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Las proyecciones miden 4 y 9. Hallar la altura $h$. | 1. Aplicar Teorema de la Altura: $h^2 = 4 \cdot 9$.<br>2. $h^2 = 36 \implies \sqrt{36}$. | **6** |
| **E02** | Proyección $p=2$, hipotenusa $c=8$. Hallar cateto $a$. | 1. Aplicar Teorema del Cateto: $a^2 = 2 \cdot 8$.<br>2. $a^2 = 16 \implies \sqrt{16}$. | **4** |
| **E03** | Si $h=4$ y una proyección es 2, ¿cuánto mide la otra? | 1. $4^2 = 2 \cdot q \implies 16 = 2q$.<br>2. Despejar $q = 16 / 2$. | **8** |
| **E04** | Catetos 3 y 4, hipotenusa 5. Hallar la altura $h$. | 1. Usar relación de área: $3 \cdot 4 = 5 \cdot h$.<br>2. $12 = 5h \implies h = 12/5$. | **2.4** |
| **E05** | En un triángulo, $p=1$ y $q=4$. Hallar el cateto sobre $p$. | 1. Hipotenusa $c = 1 + 4 = 5$.<br>2. $a^2 = 1 \cdot 5 = 5 \implies \sqrt{5}$. | **$\sqrt{5}$** |
""")

    with st.expander("❓ Cuestionario G15", expanded=False):
        quiz = [
            {'question': 'El Teorema de Euclides relaciona elementos de un triángulo:', 'options': {'A': 'Equilátero', 'B': 'Obtusángulo', 'C': 'Rectángulo', 'D': 'Isósceles acutángulo'}, 'answer': 'C', 'explanation': 'Euclides solo funciona cuando hay un ángulo de 90° desde donde tirar la altura.'},
            {'question': 'La fórmula $h^2 = p \\cdot q$ corresponde al Teorema de:', 'options': {'A': 'Pitágoras', 'B': 'La Altura', 'C': 'El Cateto', 'D': 'Tales'}, 'answer': 'B', 'explanation': 'Es la fórmula que conecta las dos partes de la hipotenusa con la línea que las divide.'},
            {'question': 'Si las proyecciones de los catetos miden 3 y 12, la altura mide:', 'options': {'A': '6', 'B': '15', 'C': '36', 'D': '9'}, 'answer': 'A', 'explanation': '$3 \\cdot 12 = 36$. La raíz de 36 es 6.'},
            {'question': 'Si un cateto mide 6 y su proyección es 4, la hipotenusa mide:', 'options': {'A': '24', 'B': '10', 'C': '9', 'D': '12'}, 'answer': 'C', 'explanation': '$6^2 = 4 \\cdot c \\implies 36 = 4c$. Por lo tanto, $c = 9$.'},
            {'question': 'El Teorema del Cateto establece que $a^2$ es igual a:', 'options': {'A': '$p \\cdot q$', 'B': '$p \\cdot c$', 'C': '$h \\cdot c$', 'D': '$b \\cdot c$'}, 'answer': 'B', 'explanation': "Típ: El cateto al cuadrado es 'su' pedacito de hipotenusa por el total."},
            {'question': 'En un triángulo rectángulo, la suma de las proyecciones $p + q$ es igual a:', 'options': {'A': 'La altura', 'B': 'Un cateto', 'C': 'La hipotenusa', 'D': 'El perímetro'}, 'answer': 'C', 'explanation': 'Las proyecciones son simplemente los dos segmentos en los que se corta la hipotenusa.'},
            {'question': 'Si la hipotenusa es 10 y una proyección es 2, el cateto adyacente a esa proyección mide:', 'options': {'A': '$\\sqrt{20}$', 'B': '20', 'C': '5', 'D': '8'}, 'answer': 'A', 'explanation': '$a^2 = 2 \\cdot 10 = 20$. Entonces $a = \\sqrt{20}$ o $2\\sqrt{5}$.'},
            {'question': 'Si la altura es 10 y una proyección es 5, la otra proyección mide:', 'options': {'A': '5', 'B': '10', 'C': '20', 'D': '50'}, 'answer': 'C', 'explanation': '$10^2 = 5 \\cdot q \\implies 100 = 5q$. Despejando, $q = 20$.'},
            {'question': 'Para aplicar Euclides, la altura debe ser trazada desde:', 'options': {'A': 'Cualquier vértice', 'B': 'El ángulo recto', 'C': 'El punto medio de un lado', 'D': 'El incentro'}, 'answer': 'B', 'explanation': 'Si la tiras desde otro ángulo, las relaciones de proporcionalidad cambian.'},
            {'question': 'Si los catetos son $a$ y $b$, la altura $h$ y la hipotenusa $c$, se cumple que:', 'options': {'A': '$a+b = c+h$', 'B': '$a \\cdot b = c \\cdot h$', 'C': '$a^2+b^2 = h^2$', 'D': '$p \\cdot q = c^2$'}, 'answer': 'B', 'explanation': 'Típ: Esta fórmula viene de igualar dos formas de calcular el área del mismo triángulo.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g15_quiz")
