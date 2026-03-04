import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G10():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G10: Elementos Secundarios II — Simetrales y Transversales")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase G10: Elementos Secundarios II - Simetrales y Transversales
    **Eje:** Geometría | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. La Simetral (Mediatriz)
    Es la recta **perpendicular** a un lado del triángulo que pasa, exactamente, por su **punto medio**.
    * **Punto de intersección:** Las tres simetrales se cortan en el **Circuncentro**.
    * **Propiedad:** El circuncentro es el centro de la circunferencia **circunscrita** (la que pasa por los tres vértices).
    * **Dato clave:** No necesariamente pasa por el vértice opuesto (solo en el isósceles y equilátero).

    ### ⚖️ 2. La Transversal de Gravedad ($t$)
    Es el segmento que une un vértice con el **punto medio** del lado opuesto.
    * **Punto de intersección:** Las tres transversales se cortan en el **Baricentro** (o Centro de Gravedad).
    * **Propiedad 2:1:** El baricentro divide a cada transversal en dos segmentos que están en razón $2:1$ (la parte que va al vértice es el doble que la que va al lado).

    > **Newton Tip:** "Seba, dile a tu alumno que el Baricentro es el punto de equilibrio. Si recortas el triángulo en cartón y pones el dedo ahí, no se cae. ¡Es física pura aplicada al papel!"
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G10 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G10 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Una transversal mide 9 cm. ¿A qué distancia del vértice está el baricentro? | 1. Dividir el total por 3: $9 / 3 = 3$.<br>2. La parte del vértice es el doble: $3 \times 2 = 6$. | **6 cm** |
| **E02** | ¿Dónde se ubica el circuncentro en un triángulo rectángulo? | 1. Por propiedad, el circuncentro de un triángulo rectángulo está siempre en el medio de la hipotenusa. | **Punto medio hipotenusa** |
| **E03** | La simetral corta al lado en un ángulo de... | 1. Por definición, la simetral es perpendicular al segmento. | **90°** |
| **E04** | El segmento baricentro-lado mide 5. ¿Cuánto mide la transversal completa? | 1. El segmento al vértice es el doble: 10.<br>2. Sumar ambas partes: $10 + 5 = 15$. | **15 unidades** |
| **E05** | ¿Qué elemento secundario NO pasa obligatoriamente por un vértice? | 1. La simetral solo necesita el punto medio y los 90°. | **La Simetral** |
""")

    with st.expander("❓ Cuestionario G10", expanded=False):
        quiz = [
            {'question': 'El punto de intersección de las transversales de gravedad se llama:', 'options': {'A': 'Incentro', 'B': 'Circuncentro', 'C': 'Baricentro', 'D': 'Ortocentro'}, 'answer': 'C', 'explanation': 'Baricentro = Gravedad. Es el punto donde el peso del triángulo se equilibra.'},
            {'question': 'La simetral es una recta que cumple dos condiciones sobre un lado:', 'options': {'A': 'Es paralela y pasa por el punto medio', 'B': 'Es perpendicular y pasa por el punto medio', 'C': 'Es perpendicular y pasa por el vértice', 'D': 'Divide el ángulo en dos partes iguales'}, 'answer': 'B', 'explanation': 'Simetral = Simetría. Divide el lado justo a la mitad y en ángulo recto.'},
            {'question': 'El circuncentro es el centro de la circunferencia que:', 'options': {'A': 'Está inscrita en el triángulo', 'B': 'Pasa por los tres vértices del triángulo', 'C': 'Toca solo un lado del triángulo', 'D': 'Es tangente a las alturas'}, 'answer': 'B', 'explanation': "Circuncentro viene de 'Circunscribir'. Envuelve al triángulo tocando sus esquinas."},
            {'question': 'Si una transversal de gravedad mide 12 cm, la distancia del baricentro al lado es:', 'options': {'A': '4 cm', 'B': '6 cm', 'C': '8 cm', 'D': '2 cm'}, 'answer': 'A', 'explanation': 'Divide 12 en tres partes iguales ($12/3 = 4$). La parte pequeña (al lado) es 4.'},
            {'question': 'El baricentro divide a la transversal de gravedad en la razón:', 'options': {'A': '$1:1$', 'B': '$2:1$', 'C': '$3:1$', 'D': '$4:1$'}, 'answer': 'B', 'explanation': 'Típ: El camino al vértice es siempre el doble de largo que el camino al lado. $2:1$.'},
            {'question': '¿Cuál de estos puntos es el "centro de masa" del triángulo?', 'options': {'A': 'Ortocentro', 'B': 'Incentro', 'C': 'Baricentro', 'D': 'Circuncentro'}, 'answer': 'C', 'explanation': 'Si pudieras colgar el triángulo de un hilo, lo harías desde el baricentro.'},
            {'question': 'En un triángulo equilátero, el baricentro, ortocentro, incentro y circuncentro:', 'options': {'A': 'Están en los vértices', 'B': 'Son el mismo punto', 'C': 'Están fuera del triángulo', 'D': 'No existen'}, 'answer': 'B', 'explanation': 'En la perfección del equilátero, todos los centros colapsan en un solo punto mágico.'},
            {'question': 'La recta que es perpendicular al punto medio de un segmento se llama:', 'options': {'A': 'Bisectriz', 'B': 'Simetral', 'C': 'Altura', 'D': 'Transversal'}, 'answer': 'B', 'explanation': 'Simetral y Mediatriz son dos nombres para la misma línea. Grábatelos.'},
            {'question': 'Si el baricentro está a 10 cm del vértice, ¿cuánto mide el segmento que falta para llegar al lado?', 'options': {'A': '20 cm', 'B': '10 cm', 'C': '5 cm\n) 2.5 cm\n\n**10. El circuncentro de un triángulo obtusángulo se encuentra:**\nA) En el interior\nB) En el exterior\nC) En el punto medio del lado mayor', 'D': 'En un vértice'}, 'answer': 'C', 'explanation': 'Si la parte grande es 10, la parte chica tiene que ser la mitad. O sea, 5.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g10_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G10)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **C** | **Newton Tip:** "Baricentro = Gravedad. Es el punto donde el peso del triángulo se equilibra." |
| **2** | **B** | **Galileo Tip:** "Simetral = Simetría. Divide el lado justo a la mitad y en ángulo recto." |
| **3** | **B** | **Hawking Tip:** "Circuncentro viene de 'Circunscribir'. Envuelve al triángulo tocando sus esquinas." |
| **4** | **A** | **Curie Tip:** "Divide 12 en tres partes iguales ($12/3 = 4$). La parte pequeña (al lado) es 4." |
| **5** | **B** | **Statham Tip:** "Típ: El camino al vértice es siempre el doble de largo que el camino al lado. $2:1$." |
| **6** | **C** | **Newton Tip:** "Si pudieras colgar el triángulo de un hilo, lo harías desde el baricentro." |
| **7** | **B** | **Galileo Tip:** "En la perfección del equilátero, todos los centros colapsan en un solo punto mágico." |
| **8** | **B** | **Hawking Tip:** "Simetral y Mediatriz son dos nombres para la misma línea. Grábatelos." |
| **9** | **C** | **Curie Tip:** "Si la parte grande es 10, la parte chica tiene que ser la mitad. O sea, 5." |
| **10** | **B** | **Statham Tip:** "Típ: Al igual que el ortocentro, el circuncentro se 'sale' del triángulo cuando este es muy abierto (obtuso)." |
""")
