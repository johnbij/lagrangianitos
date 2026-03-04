import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G09():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G09: Elementos Secundarios I — Alturas y Bisectrices")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase G09: Elementos Secundarios I - Alturas y Bisectrices
    **Eje:** Geometría | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. La Altura ($h$)
    Es el segmento perpendicular que va desde un vértice al lado opuesto (o a su prolongación).
    * **Punto de intersección:** Las tres alturas se cortan en el **Ortocentro**.
    * **Dato clave:** En un triángulo obtusángulo, el ortocentro queda fuera del triángulo.

    ### ⚖️ 2. La Bisectriz ($b$)
    Es el rayo que divide a un ángulo interior en dos ángulos de igual medida (congruentes).
    * **Punto de intersección:** Las tres bisectrices se cortan en el **Incentro**.
    * **Propiedad:** El incentro es el centro de la circunferencia **inscrita** (la que toca los lados por dentro).

    > **Statham Tip:** *"Acuérdate: Altura = Perpendicular (90°). Bisectriz = Bisectar (partir el ángulo en dos). No las confundas o te vas a marear en los ejercicios de ángulos."*
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G09 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G09 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | En un triángulo, una bisectriz divide un ángulo de 80°. | 1. Por definición, la bisectriz divide en partes iguales.<br>2. $80 / 2 = 40$. | **Dos ángulos de 40°** |
| **E02** | ¿Dónde se ubica la altura en un triángulo rectángulo? | 1. Los catetos son perpendiculares entre sí.<br>2. Por lo tanto, un cateto es la altura del otro. | **En los catetos** |
| **E03** | Si el incentro está a 5 cm de un lado, ¿a cuánto está de los otros? | 1. El incentro equidista de todos los lados.<br>2. Es el radio de la circunferencia inscrita. | **5 cm** |
| **E04** | Ángulo entre una altura y la base. | 1. La altura es, por definición, perpendicular al lado opuesto. | **90°** |
| **E05** | Hallar ángulo $x$ si una bisectriz parte un ángulo de $2x + 10$ en 30°. | 1. $30 = (2x + 10) / 2$.<br>2. $60 = 2x + 10 \implies 50 = 2x$. | **$x = 25$** |
""")

    with st.expander("❓ Cuestionario G09", expanded=False):
        quiz = [
            {'question': 'El punto donde se cruzan las tres alturas de un triángulo se llama:', 'options': {'A': 'Incentro', 'B': 'Ortocentro', 'C': 'Baricentro', 'D': 'Circuncentro'}, 'answer': 'B', 'explanation': 'A-O: Altura con Ortocentro. Aprende la sigla y no se te olvida más.'},
            {'question': 'La bisectriz es el segmento que divide a un:', 'options': {'A': 'Lado en dos partes iguales', 'B': 'Ángulo en dos partes iguales', 'C': 'Triángulo en dos áreas iguales', 'D': 'Lado en forma perpendicular'}, 'answer': 'B', 'explanation': 'Bisectriz = Bi (dos) - Sectriz (corte). Corta el ángulo en dos iguales.'},
            {'question': 'El incentro es el centro de la circunferencia:', 'options': {'A': 'Circunscrita (por fuera)', 'B': 'Inscrita (por dentro)', 'C': 'Tangente externa', 'D': 'De Euler'}, 'answer': 'B', 'explanation': "Incentro viene de 'In' (dentro). Es el centro de lo que está adentro."},
            {'question': 'En un triángulo rectángulo, el ortocentro se encuentra en:', 'options': {'A': 'El centro de la hipotenusa', 'B': 'El vértice del ángulo recto', 'C': 'Fuera del triángulo', 'D': 'En el incentro'}, 'answer': 'B', 'explanation': 'Como las alturas son los mismos catetos, el único punto donde se pueden juntar es el rincón del ángulo recto.'},
            {'question': 'Si una bisectriz genera dos ángulos de 35°, ¿cuánto medía el ángulo original?', 'options': {'A': '35°', 'B': '70°', 'C': '90°', 'D': '145°'}, 'answer': 'B', 'explanation': 'Típ: $35 \\times 2 = 70$. No hay más vuelta que darle.'},
            {'question': '¿Cuál elemento secundario SIEMPRE forma un ángulo de 90° con el lado opuesto?', 'options': {'A': 'Bisectriz', 'B': 'Altura', 'C': 'Transversal de gravedad', 'D': 'Simetral'}, 'answer': 'B', 'explanation': 'Altura es sinónimo de perpendicularidad respecto a una base.'},
            {'question': 'El ortocentro de un triángulo obtusángulo se ubica:', 'options': {'A': 'En un vértice', 'B': 'En el interior', 'C': 'En el exterior', 'D': 'Sobre el lado más largo'}, 'answer': 'C', 'explanation': 'Es el único caso donde el punto de encuentro se arranca del dibujo.'},
            {'question': 'Las bisectrices de un triángulo equilátero miden:', 'options': {'A': 'Lo mismo que las alturas', 'B': 'Más que las alturas', 'C': 'Menos que las alturas', 'D': 'Cero'}, 'answer': 'A', 'explanation': 'En el equilátero (la perfección), todos los elementos secundarios coinciden en el mismo segmento.'},
            {'question': 'La distancia desde el incentro hacia cualquier lado del triángulo es:', 'options': {'A': 'Variable', 'B': 'Siempre la misma (el radio)', 'C': 'Igual a la altura', 'D': 'El doble de la bisectriz'}, 'answer': 'B', 'explanation': "Esa es la gracia del incentro: 'toca' a todos los lados a la misma distancia."},
            {'question': 'Si en un triángulo una altura coincide con una bisectriz, el triángulo es al menos:', 'options': {'A': 'Escaleno', 'B': 'Isósceles', 'C': 'Obtusángulo', 'D': 'Rectángulo escaleno'}, 'answer': 'B', 'explanation': 'Típ: Esa simetría solo ocurre cuando hay lados iguales que mandan la figura.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g09_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G09)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **B** | **Newton Tip:** "A-O: Altura con Ortocentro. Aprende la sigla y no se te olvida más." |
| **2** | **B** | **Galileo Tip:** "Bisectriz = Bi (dos) - Sectriz (corte). Corta el ángulo en dos iguales." |
| **3** | **B** | **Hawking Tip:** "Incentro viene de 'In' (dentro). Es el centro de lo que está adentro." |
| **4** | **B** | **Curie Tip:** "Como las alturas son los mismos catetos, el único punto donde se pueden juntar es el rincón del ángulo recto." |
| **5** | **B** | **Statham Tip:** "Típ: $35 \times 2 = 70$. No hay más vuelta que darle." |
| **6** | **B** | **Newton Tip:** "Altura es sinónimo de perpendicularidad respecto a una base." |
| **7** | **C** | **Galileo Tip:** "Es el único caso donde el punto de encuentro se arranca del dibujo." |
| **8** | **A** | **Hawking Tip:** "En el equilátero (la perfección), todos los elementos secundarios coinciden en el mismo segmento." |
| **9** | **B** | **Curie Tip:** "Esa es la gracia del incentro: 'toca' a todos los lados a la misma distancia." |
| **10** | **B** | **Statham Tip:** "Típ: Esa simetría solo ocurre cuando hay lados iguales que mandan la figura." |
""")
