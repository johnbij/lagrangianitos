import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G11():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G11: Teorema de Pitágoras — La Llave Maestra")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase G11: Teorema de Pitágoras - La Llave Maestra
    **Eje:** Geometría | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. El Teorema Universal
    En todo **triángulo rectángulo** (aquel que tiene un ángulo de 90°), el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos:

    $$a^2 + b^2 = c^2$$

    Donde **$a$** y **$b$** son los catetos (lados que forman el ángulo recto) y **$c$** es la hipotenusa (el lado más largo frente al ángulo de 90°).

    ### ⚖️ 2. Tríos Pitagóricos (Ahorro de Tiempo)
    Existen combinaciones de números enteros que siempre cumplen el teorema. Si te los aprendes, no necesitas calcular raíces:
    * **(3, 4, 5):** El más común ($9 + 16 = 25$).
    * **(5, 12, 13):** Muy usado en la PAES ($25 + 144 = 169$).
    * **(8, 15, 17):** El nivel experto.
    * **Amplificaciones:** Cualquier múltiplo también funciona (ej: 6, 8, 10 es un 3, 4, 5 al doble).

    > **Newton Tip:** "Seba, dile a tu alumno: si no hay ángulo de 90°, Pitágoras está de vacaciones. ¡No lo fuerces donde no hay un ángulo recto!"
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G11 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G11 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Catetos miden 3 y 4. Hallar hipotenusa. | 1. $3^2 + 4^2 = 9 + 16 = 25$.<br>2. $\sqrt{25} = 5$. | **5** |
| **E02** | Hipotenusa 13, un cateto 12. Hallar el otro. | 1. $x^2 + 12^2 = 13^2$.<br>2. $x^2 + 144 = 169 \implies x^2 = 25$. | **5** |
| **E03** | Diagonal de un rectángulo de lados 6 y 8. | 1. La diagonal forma un triángulo rectángulo.<br>2. Reconocer trío (3,4,5) al doble. | **10** |
| **E04** | Calcular hipotenusa si catetos son 1 y 1. | 1. $1^2 + 1^2 = 2$.<br>2. Aplicar raíz cuadrada. | **$\sqrt{2}$** |
| **E05** | ¿Es rectángulo un triángulo de lados 7, 24 y 25? | 1. $7^2 + 24^2 = 49 + 576 = 625$.<br>2. $25^2 = 625$. | **Sí, es rectángulo** |
""")

    with st.expander("❓ Cuestionario G11", expanded=False):
        quiz = [
            {'question': 'El Teorema de Pitágoras solo se puede aplicar en triángulos:', 'options': {'A': 'Equiláteros', 'B': 'Isósceles', 'C': 'Rectángulos', 'D': 'Obtusángulos'}, 'answer': 'C', 'explanation': 'Sin el ángulo de 90°, la relación de los cuadrados no se cumple de forma exacta.'},
            {'question': 'En la fórmula $a^2 + b^2 = c^2$, la letra "c" representa siempre:', 'options': {'A': 'El cateto menor', 'B': 'El cateto mayor', 'C': 'La hipotenusa', 'D': 'La altura'}, 'answer': 'C', 'explanation': 'La hipotenusa es el lado VIP: siempre va sola al otro lado del signo igual.'},
            {'question': 'Si los catetos de un triángulo miden 6 y 8 cm, la hipotenusa mide:', 'options': {'A': '10 cm', 'B': '12 cm', 'C': '14 cm', 'D': '100 cm'}, 'answer': 'A', 'explanation': 'Es el trío (3, 4, 5) multiplicado por 2. $3\\times2=6, 4\\times2=8, 5\\times2=10$.'},
            {'question': '¿Cuál de estos es un trío pitagórico básico?', 'options': {'A': '(1, 2, 3)', 'B': '(3, 4, 5)', 'C': '(2, 3, 4)', 'D': '(5, 10, 15)'}, 'answer': 'B', 'explanation': 'Es el trío más famoso de la historia. Recuérdalo y ahorrarás minutos valiosos.'},
            {'question': 'Si la hipotenusa mide 10 y un cateto mide 6, el otro cateto mide:', 'options': {'A': '4', 'B': '8', 'C': '16', 'D': '36'}, 'answer': 'B', 'explanation': 'Típ: Si conoces la hipotenusa, restas los cuadrados: $100 - 36 = 64$. Raíz de 64 es 8.'},
            {'question': '¿Cuál es el valor de la diagonal de un cuadrado de lado 1?', 'options': {'A': '1', 'B': '2', 'C': '$\\sqrt{2}$', 'D': '$\\sqrt{3}$'}, 'answer': 'C', 'explanation': 'La diagonal de cualquier cuadrado siempre es $lado \\times \\sqrt{2}$.'},
            {'question': 'Un triángulo de lados 5, 12 y 13 es:', 'options': {'A': 'Acutángulo', 'B': 'Obtusángulo', 'C': 'Rectángulo', 'D': 'Equilátero'}, 'answer': 'C', 'explanation': 'Se cumple perfecto: $25 + 144 = 169$. Es un triángulo rectángulo puro.'},
            {'question': 'Si los catetos miden 5 y 5, la hipotenusa mide:', 'options': {'A': '10', 'B': '25', 'C': '$5\\sqrt{2}$', 'D': '$2\\sqrt{5}$'}, 'answer': 'C', 'explanation': 'Aplica la fórmula: $\\sqrt{5^2 + 5^2} = \\sqrt{25 + 25} = \\sqrt{50} = 5\\sqrt{2}$.'},
            {'question': 'Para que un triángulo de lados 9, 12 y $x$ sea rectángulo (siendo $x$ la hipotenusa), $x$ debe valer:', 'options': {'A': '15', 'B': '21', 'C': '18', 'D': '25'}, 'answer': 'A', 'explanation': 'Es el trío (3, 4, 5) multiplicado por 3. $3\\times3=9, 4\\times3=12, 5\\times3=15$.'},
            {'question': 'Si en un triángulo $a^2 + b^2$ es mayor que $c^2$ (siendo $c$ el lado mayor), el triángulo es:', 'options': {'A': 'Rectángulo', 'B': 'Acutángulo', 'C': 'Obtusángulo', 'D': 'Imposible'}, 'answer': 'B', 'explanation': "Típ: Si los catetos 'ganan', el ángulo se cierra y es acutángulo. Si la hipotenusa gana, se abre y es obtusángulo."}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g11_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G11)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **C** | **Galileo Tip:** "Sin el ángulo de 90°, la relación de los cuadrados no se cumple de forma exacta." |
| **2** | **C** | **Newton Tip:** "La hipotenusa es el lado VIP: siempre va sola al otro lado del signo igual." |
| **3** | **A** | **Hawking Tip:** "Es el trío (3, 4, 5) multiplicado por 2. $3\times2=6, 4\times2=8, 5\times2=10$." |
| **4** | **B** | **Curie Tip:** "Es el trío más famoso de la historia. Recuérdalo y ahorrarás minutos valiosos." |
| **5** | **B** | **Statham Tip:** "Típ: Si conoces la hipotenusa, restas los cuadrados: $100 - 36 = 64$. Raíz de 64 es 8." |
| **6** | **C** | **Newton Tip:** "La diagonal de cualquier cuadrado siempre es $lado \times \sqrt{2}$." |
| **7** | **C** | **Galileo Tip:** "Se cumple perfecto: $25 + 144 = 169$. Es un triángulo rectángulo puro." |
| **8** | **C** | **Hawking Tip:** "Aplica la fórmula: $\sqrt{5^2 + 5^2} = \sqrt{25 + 25} = \sqrt{50} = 5\sqrt{2}$." |
| **9** | **A** | **Curie Tip:** "Es el trío (3, 4, 5) multiplicado por 3. $3\times3=9, 4\times3=12, 5\times3=15$." |
| **10** | **B** | **Statham Tip:** "Típ: Si los catetos 'ganan', el ángulo se cierra y es acutángulo. Si la hipotenusa gana, se abre y es obtusángulo." |
""")
