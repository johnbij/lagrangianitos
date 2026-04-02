import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G13():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G13: Círculo y Circunferencia — La Perfección del Radio")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # G13: Círculo y Circunferencia - La Perfección del Radio
    

    ---

    ### 🛡️ 1. Conceptos Fundamentales
    Aunque se usan como sinónimos, técnicamente son distintos:
    * **Circunferencia:** Es la línea curva y cerrada donde todos sus puntos están a la misma distancia del centro (el borde).
    * **Círculo:** Es la superficie interior encerrada por la circunferencia (el área).

    ### ⚖️ 2. Elementos Clave
    * **Radio ($r$):** Segmento que une el centro con cualquier punto de la circunferencia.
    * **Diámetro ($d$):** Cuerda que pasa por el centro. Equivale a dos radios ($d = 2r$).
    * **Cuerda:** Segmento que une dos puntos de la circunferencia.
    * **Tangente:** Recta que toca a la circunferencia en un solo punto (siempre perpendicular al radio en ese punto).

    ### 📐 3. Fórmulas de Cálculo
    * **Perímetro (Longitud):** $P = 2 \cdot \pi \cdot r$  o  $P = \pi \cdot d$
    * **Área:** $A = \pi \cdot r^2$

    > 
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G13 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G13 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **1** | Perímetro de una circunferencia de radio 5. | 1. Aplicar fórmula: $2 \cdot \pi \cdot 5$.<br>2. Multiplicar números. | **$10\pi$** |
| **2** | Área de un círculo con diámetro 12. | 1. Hallar el radio: $12 / 2 = 6$.<br>2. Aplicar fórmula: $\pi \cdot 6^2$. | **$36\pi$** |
| **3** | Si el perímetro es $16\pi$, ¿cuánto mide el radio? | 1. Igualar: $2\cdot\pi\cdot r = 16\pi$.<br>2. Despejar $r$: $16 / 2 = 8$. | **8** |
| **4** | Área de un círculo si su radio es 1. | 1. Aplicar fórmula: $\pi \cdot 1^2$.<br>2. $1 \cdot \pi = \pi$. | **$\pi$** |
| **5** | ¿Cuánto avanza una rueda de radio 10 en una vuelta? | 1. Una vuelta es igual al perímetro.<br>2. $P = 2 \cdot \pi \cdot 10$. | **$20\pi$** |
""")

    with st.expander("❓ Cuestionario G13", expanded=False):
        quiz = [
            {'question': 'El segmento que une el centro con un punto de la circunferencia se llama:', 'options': {'A': 'Diámetro', 'B': 'Cuerda', 'C': 'Radio', 'D': 'Secante'}, 'answer': 'C', 'explanation': 'Es la medida base. Todo en el círculo nace del radio.'},
            {'question': 'Si el radio de un círculo es 4, su área es:', 'options': {'A': '$4\\pi$', 'B': '$8\\pi$', 'C': '$16\\pi$', 'D': '$64\\pi$'}, 'answer': 'C', 'explanation': 'Área = $\\pi \\cdot r^2$. Entonces $4^2 = 16$. Respuesta: $16\\pi$.'},
            {'question': 'La longitud de una circunferencia de diámetro 10 es:', 'options': {'A': '$5\\pi$', 'B': '$10\\pi$', 'C': '$20\\pi$', 'D': '$100\\pi$'}, 'answer': 'B', 'explanation': 'Perímetro es $\\pi \\cdot d$. Si el diámetro es 10, es directo: $10\\pi$.'},
            {'question': 'Una recta que toca a la circunferencia en un solo punto se denomina:', 'options': {'A': 'Secante', 'B': 'Cuerda', 'C': 'Tangente', 'D': 'Arco'}, 'answer': 'C', 'explanation': "La tangente es 'tímida', solo roza a la circunferencia en un punto."},
            {'question': 'Si el área de un círculo es $25\\pi$, su radio mide:', 'options': {'A': '5', 'B': '10', 'C': '25', 'D': '12.5'}, 'answer': 'A', 'explanation': 'Típ: Busca qué número al cuadrado da 25. Es el 5.'},
            {'question': '¿Cuántos radios equivalen a un diámetro?', 'options': {'A': '1', 'B': '2', 'C': '3', 'D': '4'}, 'answer': 'B', 'explanation': 'El diámetro cruza de lado a lado pasando por el centro, por eso son 2 radios.'},
            {'question': 'Si el perímetro de un círculo se duplica, su radio:', 'options': {'A': 'Se mantiene igual', 'B': 'Se duplica', 'C': 'Se cuadruplica', 'D': 'Se reduce a la mitad'}, 'answer': 'B', 'explanation': 'Como el perímetro es lineal ($2\\pi r$), crece en la misma proporción que el radio.'},
            {'question': 'El valor aproximado de la constante $\\pi$ es:', 'options': {'A': '2,14', 'B': '3,14', 'C': '4,14', 'D': '1,14'}, 'answer': 'B', 'explanation': 'Es la razón entre el perímetro y el diámetro de cualquier círculo del universo.'},
            {'question': 'La cuerda de mayor longitud en una circunferencia es:', 'options': {'A': 'El radio', 'B': 'La tangente', 'C': 'El diámetro', 'D': 'El arco'}, 'answer': 'C', 'explanation': 'Cualquier otra cuerda que no pase por el centro será más corta que el diámetro.'},
            {'question': 'Si un círculo tiene radio 3, su perímetro y área son respectivamente:', 'options': {'A': '$6\\pi$ y $9\\pi$', 'B': '$9\\pi$ y $6\\pi$', 'C': '$3\\pi$ y $3\\pi$', 'D': '$6\\pi$ y $6\\pi$'}, 'answer': 'A', 'explanation': 'Típ: Perímetro $2 \\cdot 3 \\cdot \\pi = 6\\pi$. Área $3^2 \\cdot \\pi = 9\\pi$. ¡No las confundas!'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g13_quiz")
