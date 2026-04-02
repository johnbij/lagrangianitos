import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G08():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G08: Clasificación de Triángulos (por Lados)")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase G08: Clasificación de Triángulos (Lados)
    **Eje:** Geometría | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. Criterio de Clasificación
    Este criterio se basa en la comparación de las longitudes de los tres segmentos que forman el triángulo. La medida de los lados determina directamente la medida de los ángulos opuestos.

    ### ⚖️ 2. Los Tres Tipos Fundamentales
    * **Equilátero:** Sus **tres** lados son de igual medida. Esto implica que sus tres ángulos internos también son iguales (cada uno mide 60°).
    * **Isósceles:** Tiene al menos **dos** lados de igual medida. Los ángulos opuestos a estos lados (ángulos de la base) también son iguales entre sí.
    * **Escaleno:** Sus **tres** lados tienen medidas distintas. En consecuencia, sus tres ángulos internos también son diferentes.

    ### 📐 3. Propiedad de Correspondencia
    En todo triángulo, al lado de mayor longitud se opone el ángulo de mayor medida, y al lado de menor longitud se opone el ángulo de menor medida.

    > **Típ:** "Seba, dile a tu alumno que el equilátero es un caso especial de isósceles. Si tiene tres lados iguales, ¡por lógica tiene al menos dos! Pero en la PAES, el isósceles suele ser el que tiene 'solo' dos iguales."
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G08 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G08 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Clasificar: lados de 5 cm, 5 cm y 5 cm. | 1. Observar que los tres lados miden lo mismo. | **Equilátero** |
| **E02** | Clasificar: lados de 7 cm, 7 cm y 10 cm. | 1. Identificar que hay exactamente dos lados iguales. | **Isósceles** |
| **E03** | Clasificar: lados de 3 cm, 4 cm y 5 cm. | 1. Los tres valores son distintos entre sí. | **Escaleno** |
| **E04** | En un isósceles, el ángulo del vértice mide 40°. | 1. $180 - 40 = 140$.<br>2. Como los de la base son iguales: $140 / 2 = 70$. | **70° cada base** |
| **E05** | ¿Puede un triángulo equilátero tener un ángulo de 90°? | 1. No, porque si es equilátero, sus tres ángulos DEBEN ser de 60°. | **Imposible** |
""")

    with st.expander("❓ Cuestionario G08", expanded=False):
        quiz = [
            {'question': 'Un triángulo con tres lados de distinta medida se llama:', 'options': {'A': 'Isósceles', 'B': 'Equilátero', 'C': 'Escaleno', 'D': 'Rectángulo'}, 'answer': 'C', 'explanation': "Escaleno viene de una palabra que significa 'cojo' o 'desigual'. Ningún lado coincide."},
            {'question': 'En un triángulo equilátero de lado "a", el perímetro es:', 'options': {'A': '$a^2$', 'B': '$2a$', 'C': '$3a$', 'D': '$a/3$'}, 'answer': 'C', 'explanation': "El perímetro es la suma de los lados. Si son 3 lados iguales a 'a', entonces $a+a+a = 3a$."},
            {'question': 'Si un triángulo tiene dos ángulos de 70° cada uno, es:', 'options': {'A': 'Escaleno', 'B': 'Equilátero', 'C': 'Isósceles', 'D': 'Rectángulo'}, 'answer': 'C', 'explanation': 'Si tiene dos ángulos iguales, por propiedad de correspondencia, DEBE tener dos lados iguales.'},
            {'question': 'El triángulo que tiene sus tres ángulos internos de 60° es:', 'options': {'A': 'Escaleno', 'B': 'Equilátero', 'C': 'Obtusángulo', 'D': 'Isósceles (pero no equilátero)'}, 'answer': 'B', 'explanation': 'Es el triángulo más simétrico que existe. 180 dividido en 3 partes iguales da 60.'},
            {'question': 'En un triángulo isósceles, los ángulos opuestos a los lados iguales se llaman:', 'options': {'A': 'Ángulos del vértice', 'B': 'Ángulos de la base', 'C': 'Ángulos rectos', 'D': 'Ángulos exteriores'}, 'answer': 'B', 'explanation': "Típ: La 'base' no es necesariamente el lado que está abajo, sino el lado que es distinto a los otros dos."},
            {'question': 'Si los lados miden 12, 12 y 15, el triángulo es:', 'options': {'A': 'Equilátero', 'B': 'Isósceles', 'C': 'Escaleno', 'D': 'Acutángulo'}, 'answer': 'B', 'explanation': 'Dos lados de 12 lo delatan. Es isósceles.'},
            {'question': 'Un triángulo escaleno puede ser rectángulo:', 'options': {'A': 'Nunca', 'B': 'Siempre', 'C': 'A veces', 'D': 'Solo si es equilátero'}, 'answer': 'C', 'explanation': 'El famoso triángulo 3-4-5 es escaleno (lados distintos) y rectángulo ($3^2+4^2=5^2$). Así que sí, se puede.'},
            {'question': '¿Cuál es la medida de cada ángulo en un triángulo equilátero?', 'options': {'A': '45°', 'B': '60°', 'C': '90°', 'D': '180°'}, 'answer': 'B', 'explanation': 'Es una constante universal. Si te dicen equilátero, ya conoces sus ángulos sin que te los den.'},
            {'question': 'Si un triángulo tiene lados 8, 10 y 12, se clasifica como:', 'options': {'A': 'Isósceles', 'B': 'Equilátero', 'C': 'Escaleno', 'D': 'Rectángulo'}, 'answer': 'C', 'explanation': '8, 10 y 12 son todos diferentes. Es escaleno de tomo y lomo.'},
            {'question': 'En un triángulo isósceles rectángulo, los ángulos agudos miden:', 'options': {'A': '30° y 60°', 'B': '45° y 45°', 'C': '20° y 70°', 'D': '10° y 80°'}, 'answer': 'B', 'explanation': 'Típ: Si es rectángulo, tienes 90°. Si es isósceles, los otros dos son iguales. $(180-90)/2 = 45$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g08_quiz")
