import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_V04():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("V04: Vectores e Isometrías — El Motor del Movimiento")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase V04: Vectores e Isometrías - El Motor del Movimiento
    **Eje:** Vectores | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. Traslación: La Suma Vectorial
    La traslación es la aplicación más directa de los vectores. Trasladar un punto $P$ según un vector $\vec{v}$ es, simplemente, realizar una suma de componentes.
    * **Fórmula:** $P' = P + \vec{v}$
    * Si tienes una figura, aplicas el mismo vector a cada uno de sus vértices.

    ### ⚖️ 2. Composición de Traslaciones
    Si aplicas una traslación $\vec{u}$ y luego otra $\vec{v}$, el resultado es una única traslación equivalente a la **suma de ambos vectores**.
    $$\vec{v}_{final} = \vec{u} + \vec{v}$$

    ### 📐 3. Vectores en Rotaciones y Simetrías
    Aunque las rotaciones y simetrías cambian la orientación, podemos usar vectores para describir la posición de los puntos respecto al centro de giro o al eje:
    * **Rotación 180°:** Equivale a multiplicar el vector posición por el escalar $k = -1$.
    * **Simetría Central:** Es exactamente lo mismo que una ponderación por $-1$ desde el centro de simetría.

    > **Newton Tip:** "Seba, dile a tu alumno: si en la prueba te piden aplicar tres traslaciones seguidas, ¡no muevas la figura tres veces! Suma los tres vectores primero y mueve la figura una sola vez con el resultado. Ahorrarás tiempo valioso."
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica V04 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica V04 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Trasladar el punto $A(2, 5)$ según el vector $\vec{v}(3, -1)$. | 1. Sumar coordenadas: $(2+3, 5-1)$. | **$A'(5, 4)$** |
| **E02** | Aplicar $\vec{u}(1, 2)$ y luego $\vec{v}(-4, 5)$ al origen. | 1. Sumar vectores: $(1-4, 2+5) = (-3, 7)$.<br>2. Aplicar al $(0,0)$. | **$(-3, 7)$** |
| **E03** | ¿Qué vector traslada $P(1, 1)$ a $P'(5, 5)$? | 1. Restar Final - Inicial: $(5-1, 5-1)$. | **$\vec{v}(4, 4)$** |
| **E04** | Una figura se traslada por $\vec{v}(2, 2)$ tres veces. | 1. Multiplicar vector por 3: $3 \cdot (2, 2)$. | **$\vec{v}_{total}(6, 6)$** |
| **E05** | Si $A(3, 4)$ se refleja simétricamente respecto al origen. | 1. Equivale a ponderar por $-1$: $(-1 \cdot 3, -1 \cdot 4)$. | **$A'(-3, -4)$** |
""")

    with st.expander("❓ Cuestionario V04", expanded=False):
        quiz = [
            {'question': 'La traslación de un punto $P$ mediante un vector $\\vec{v}$ se calcula como:', 'options': {'A': '$P \\cdot \\vec{v}$', 'B': '$P - \\vec{v}$', 'C': '$P + \\vec{v}$', 'D': '$\\vec{v} / P$'}, 'answer': 'C', 'explanation': 'La traslación es la forma geométrica de ver la suma de vectores. Punto + Desplazamiento.'},
            {'question': 'Si aplicamos el vector $\\vec{v}(4, -2)$ al punto $(-1, 5)$, el nuevo punto es:', 'options': {'A': '$(3, 3)$', 'B': '$(5, 3)$', 'C': '$(3, 7)$', 'D': '$(5, 7)$'}, 'answer': 'A', 'explanation': 'Suma componente a componente: $-1 + 4 = 3$ y $5 - 2 = 3$.'},
            {'question': 'Dos traslaciones sucesivas $\\vec{u}(1, 1)$ y $\\vec{v}(2, 2)$ equivalen a:', 'options': {'A': '$\\vec{w}(1, 1)$', 'B': '$\\vec{w}(2, 2)$', 'C': '$\\vec{w}(3, 3)$', 'D': '$\\vec{w}(0, 0)$'}, 'answer': 'C', 'explanation': 'Las traslaciones son aditivas. Simplemente suma los vectores para obtener el efecto total.'},
            {'question': 'Si al trasladar el punto $(2, 2)$ obtenemos $(0, 0)$, el vector utilizado fue:', 'options': {'A': '$(2, 2)$', 'B': '$(-2, -2)$', 'C': '$(0, 0)$', 'D': '$(2, -2)$'}, 'answer': 'B', 'explanation': 'Para ir de 2 a 0, debes restar 2. Por eso el vector es negativo en ambas partes.'},
            {'question': 'El vector que representa una traslación nula (la figura no se mueve) es:', 'options': {'A': '$(1, 1)$', 'B': '$(0, 0)$', 'C': '$(-1, -1)$', 'D': '$(1, 0)$'}, 'answer': 'B', 'explanation': 'Típ: El vector $(0,0)$ es el elemento neutro de la traslación.'},
            {'question': 'Si una figura se traslada por $\\vec{v}$ y luego por $-\\vec{v}$, la figura:', 'options': {'A': 'Se mueve al doble de distancia', 'B': 'Cambia de tamaño', 'C': 'Vuelve a su posición original', 'D': 'Se invierte'}, 'answer': 'C', 'explanation': 'Sumar un vector y luego su opuesto da como resultado el vector nulo. No hubo movimiento neto.'},
            {'question': 'En una traslación, el vector aplicado a cada punto de la figura debe ser:', 'options': {'A': 'Diferente para cada punto', 'B': 'El mismo para todos los puntos', 'C': 'Proporcional a la distancia al origen', 'D': 'Nulo'}, 'answer': 'B', 'explanation': 'Si aplicaras vectores distintos a cada punto, la figura se deformaría o se rompería.'},
            {'question': "Si el punto $A(1, 4)$ llega al punto $A'(5, 2)$ tras una traslación, el vector es:", 'options': {'A': '$(4, -2)$', 'B': '$(-4, 2)$', 'C': '$(6, 6)$', 'D': '$(4, 2)$'}, 'answer': 'A', 'explanation': 'Resta Final ($5, 2$) menos Inicial ($1, 4$). $5-1=4$ y $2-4=-2$.'},
            {'question': 'Una rotación de 180° respecto al origen es equivalente a una ponderación de vector posición por:', 'options': {'A': '$k = 1$', 'B': '$k = 0$', 'C': '$k = -1$', 'D': '$k = 2$'}, 'answer': 'C', 'explanation': 'Girar 180° es enviar cada punto al lado opuesto del origen, que es lo que hace el escalar $-1$.'},
            {'question': 'Si sumamos los vectores de traslación de un triángulo que volvió a su sitio original, la suma es:', 'options': {'A': 'El área del triángulo', 'B': 'El vector nulo $(0, 0)$', 'C': 'El perímetro', 'D': 'El vector $(1, 1)$'}, 'answer': 'B', 'explanation': 'Típ: Si el desplazamiento total es cero, la suma de todos los vectores intermedios debe ser cero.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="v04_quiz")
