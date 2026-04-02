import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G07():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G07: Clasificación de Triángulos (por Ángulos)")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    
    ---

    ### 🛡️ 1. Criterio de Clasificación
    Para clasificar un triángulo según sus ángulos, debemos observar la medida del ángulo más grande o la naturaleza de sus tres ángulos interiores.

    ### ⚖️ 2. Los Tres Tipos Fundamentales
    * **Acutángulo:** Sus **tres** ángulos interiores son agudos (menores a 90°).
    * **Rectángulo:** Tiene **un** ángulo recto (exactamente 90°). Los otros dos ángulos son agudos y complementarios (suman 90°).
    * **Obtusángulo:** Tiene **un** ángulo obtuso (mayor a 90° y menor a 180°).

    ### 📐 3. Relación con Pitágoras (Identificación)
    Si conocemos los lados $a, b$ y $c$ (siendo $c$ el mayor), podemos saber el tipo de ángulo sin transportador:
    * Si $a^2 + b^2 = c^2 \implies$ **Rectángulo**.
    * Si $a^2 + b^2 > c^2 \implies$ **Acutángulo**.
    * Si $a^2 + b^2 < c^2 \implies$ **Obtusángulo**.

    > **Típ:** "Seba, dile a tu alumno que un triángulo nunca puede tener dos ángulos rectos ni dos obtusos, porque se pasaría de los 180° antes de cerrar la figura. ¡Física elemental!"
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G07 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G07 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Clasificar: ángulos de 70°, 60° y 50°. | 1. Observar el ángulo mayor: 70°.<br>2. Como todos son menores a 90°. | **Acutángulo** |
| **E02** | Clasificar: ángulos de 90°, 30° y 60°. | 1. Identificar la presencia de un ángulo recto (90°). | **Rectángulo** |
| **E03** | Clasificar: ángulos de 110°, 40° y 30°. | 1. Observar el ángulo de 110°.<br>2. Al ser mayor que 90°. | **Obtusángulo** |
| **E04** | ¿Qué tipo de triángulo tiene lados 3, 4 y 5? | 1. $3^2 + 4^2 = 9 + 16 = 25$.<br>2. $5^2 = 25$.<br>3. Como $25 = 25$, se cumple Pitágoras. | **Rectángulo** |
| **E05** | Si un triángulo es equilátero, ¿qué es según sus ángulos? | 1. Todos sus ángulos miden 60°.<br>2. 60° es menor que 90°. | **Acutángulo** |
""")

    with st.expander("❓ Cuestionario G07", expanded=False):
        quiz = [
            {'question': 'Un triángulo acutángulo es aquel que tiene:', 'options': {'A': 'Un ángulo agudo', 'B': 'Dos ángulos agudos', 'C': 'Tres ángulos agudos', 'D': 'Un ángulo recto'}, 'answer': 'C', 'explanation': 'Ojo aquí: para ser acutángulo NO basta con tener un ángulo agudo, ¡tienen que ser los tres!'},
            {'question': 'Si un triángulo tiene un ángulo de 100°, se clasifica como:', 'options': {'A': 'Acutángulo', 'B': 'Rectángulo', 'C': 'Obtusángulo', 'D': 'Equilátero'}, 'answer': 'C', 'explanation': 'Cualquier ángulo mayor a 90° convierte automáticamente al triángulo en obtusángulo.'},
            {'question': 'En un triángulo rectángulo, los ángulos que no son rectos deben ser:', 'options': {'A': 'Obtusos', 'B': 'Rectos', 'C': 'Agudos', 'D': 'Suplementarios'}, 'answer': 'C', 'explanation': 'Como ya gastaste 90° en el ángulo recto, solo te quedan 90° para repartir entre los otros dos. Por ende, ambos deben ser menores a 90°.'},
            {'question': 'Un triángulo con ángulos de 60°, 60° y 60° es:', 'options': {'A': 'Obtusángulo', 'B': 'Rectángulo', 'C': 'Acutángulo', 'D': 'Extendido'}, 'answer': 'C', 'explanation': 'El equilátero es el acutángulo por excelencia. Todos sus ángulos son de 60°.'},
            {'question': '¿Es posible que un triángulo sea rectángulo y obtusángulo a la vez?', 'options': {'A': 'Sí, si es escaleno', 'B': 'Sí, si es isósceles', 'C': 'No, es imposible', 'D': 'Solo en geometría del espacio'}, 'answer': 'C', 'explanation': 'Típ: $90 + (\\text{algo} > 90)$ ya suma más de 180. Los ángulos interiores no permiten esa mezcla.'},
            {'question': 'Si los lados de un triángulo son 6, 8 y 10, el triángulo es:', 'options': {'A': 'Acutángulo', 'B': 'Rectángulo', 'C': 'Obtusángulo', 'D': 'No existe tal triángulo'}, 'answer': 'B', 'explanation': 'Es el trío pitagórico (3-4-5) amplificado al doble. $36 + 64 = 100$. Es rectángulo.'},
            {'question': 'Un triángulo con ángulos de 89°, 45° y 46° es:', 'options': {'A': 'Acutángulo', 'B': 'Rectángulo', 'C': 'Obtusángulo', 'D': 'Isósceles'}, 'answer': 'A', 'explanation': 'No te dejes engañar por el 89°. Sigue siendo menor que 90°, por lo tanto, es acutángulo.'},
            {'question': 'En el triángulo rectángulo, el lado opuesto al ángulo de 90° se llama:', 'options': {'A': 'Cateto', 'B': 'Base', 'C': 'Hipotenusa', 'D': 'Bisectriz'}, 'answer': 'C', 'explanation': "La hipotenusa es siempre el lado más largo y el que 'mira' al ángulo recto."},
            {'question': 'Si dos ángulos de un triángulo miden 20° y 30°, el triángulo es:', 'options': {'A': 'Acutángulo', 'B': 'Rectángulo', 'C': 'Obtusángulo', 'D': 'Equilátero'}, 'answer': 'C', 'explanation': 'Suma: $20 + 30 = 50$. El tercer ángulo es $180 - 50 = 130$. Como 130 > 90, es obtusángulo.'},
            {'question': 'La suma de los ángulos agudos de un triángulo rectángulo es siempre:', 'options': {'A': '45°', 'B': '90°', 'C': '180°', 'D': 'Variable'}, 'answer': 'B', 'explanation': 'Típ: Se llaman ángulos complementarios. $90 + 90 = 180$. Corta.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g07_quiz")
