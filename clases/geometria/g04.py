import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G04():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G04: Ángulos y Clasificación")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    

    ---

    ### 🛡️ 1. Definición
    Un ángulo es la región del plano comprendida entre dos semirrectas con un origen común llamado vértice.

    ### ⚖️ 2. Clasificación según su medida
    * **Agudo:** Mayor que 0° y menor que 90°.
    * **Recto:** Mide exactamente 90°.
    * **Obtuso:** Mayor que 90° y menor que 180°.
    * **Extendido/Llana:** Mide exactamente 180°.
    * **Completo:** Mide exactamente 360°.

    ### 📏 3. Clasificación según la suma
    * **Complementarios:** Suman 90°.
    * **Suplementarios:** Suman 180°.

    > 
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G04 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G04 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Clasificar ángulo de 45° | 1. Es menor que 90°. | **Agudo** |
| **E02** | Clasificar ángulo de 120° | 1. Es mayor que 90° y menor que 180°. | **Obtuso** |
| **E03** | Complemento de 30° | 1. $90° - 30° = 60°$. | **60°** |
| **E04** | Suplemento de 110° | 1. $180° - 110° = 70°$. | **70°** |
| **E05** | Suma de ángulos adyacentes en línea recta | 1. Forman un ángulo extendido. | **180°** |
""")

    with st.expander("❓ Cuestionario G04", expanded=False):
        quiz = [
            {'question': 'Un ángulo que mide 90 grados se conoce como:', 'options': {'A': 'Agudo', 'B': 'Obtuso', 'C': 'Recto', 'D': 'Extendido'}, 'answer': 'C', 'explanation': 'El ángulo recto es la definición de perpendicularidad.'},
            {'question': 'Dos ángulos son complementarios si suman:', 'options': {'A': '45°', 'B': '90°', 'C': '180°', 'D': '360°'}, 'answer': 'B', 'explanation': "Complementarios se 'completan' para formar un ángulo recto (90°)."},
            {'question': 'Un ángulo de 150° es clasificado como:', 'options': {'A': 'Agudo', 'B': 'Obtuso', 'C': 'Recto', 'D': 'Completo'}, 'answer': 'B', 'explanation': 'Más de 90° pero menos de 180° es la definición de obtuso.'},
            {'question': '¿Cuál es el suplemento de un ángulo de 80°?', 'options': {'A': '10°', 'B': '20°', 'C': '100°', 'D': '120°'}, 'answer': 'C', 'explanation': 'Suplementarios suman 180°. $180 - 80 = 100$.'},
            {'question': 'La suma de los ángulos internos de un triángulo es:', 'options': {'A': '90°', 'B': '180°', 'C': '270°', 'D': '360°'}, 'answer': 'B', 'explanation': 'Es una propiedad fundamental de la geometría euclidiana.'},
            {'question': '¿Qué ángulo es complementario a uno de 15°?', 'options': {'A': '15°', 'B': '75°', 'C': '165°', 'D': '345°'}, 'answer': 'B', 'explanation': '$90 - 15 = 75$.'},
            {'question': 'Un ángulo mayor a 180° pero menor a 360° se llama:', 'options': {'A': 'Obtuso', 'B': 'Extendido', 'C': 'Cóncavo', 'D': 'Completo'}, 'answer': 'C', 'explanation': 'También conocido como ángulo reflejo.'},
            {'question': 'Si dos ángulos son suplementarios y uno mide 120°, el otro mide:', 'options': {'A': '30°', 'B': '60°', 'C': '90°', 'D': '180°'}, 'answer': 'B', 'explanation': '$180 - 120 = 60$.'},
            {'question': '¿Cuál es la medida de un ángulo recto?', 'options': {'A': '45°', 'B': '90°', 'C': '180°', 'D': '360°'}, 'answer': 'B', 'explanation': 'Es el ángulo estándar de referencia.'},
            {'question': 'Los ángulos opuestos por el vértice son:', 'options': {'A': 'Complementarios', 'B': 'Suplementarios', 'C': 'Iguales', 'D': 'Adyacentes'}, 'answer': 'C', 'explanation': 'Al cruzarse dos rectas, los ángulos opuestos son siempre congruentes (iguales).'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g04_quiz")
