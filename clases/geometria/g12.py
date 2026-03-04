import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G12():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G12: Áreas y Perímetros I — Triángulos y Cuadriláteros")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # 🎬 Clase G12: Áreas y Perímetros I - Triángulos y Cuadriláteros
    **Eje:** Geometría | **Nivel:** Alcance del Objetivo

    ---

    ### 🛡️ 1. Conceptos Base
    * **Perímetro ($P$):** Es la suma de todos los lados de una figura. Representa el contorno (medida lineal).
    * **Área ($A$):** Es la medida de la superficie encerrada por la figura (medida cuadrada).

    ### ⚖️ 2. Fórmulas de Triángulos
    * **Cualquier Triángulo:** $A = \frac{\text{base} \cdot \text{altura}}{2}$
    * **Triángulo Rectángulo:** $A = \frac{\text{cateto}_1 \cdot \text{cateto}_2}{2}$
    * **Triángulo Equilátero:** $A = \frac{a^2\sqrt{3}}{4}$ (donde $a$ es el lado).

    ### 📐 3. Fórmulas de Cuadriláteros
    * **Cuadrado:** $P = 4a$ | $A = a^2$ o $A = \frac{d^2}{2}$ (con la diagonal).
    * **Rectángulo:** $P = 2(a + b)$ | $A = \text{base} \cdot \text{altura}$.
    * **Rombo:** $A = \frac{D \cdot d}{2}$ (producto de diagonales dividido por 2).
    * **Trapecio:** $A = \frac{(B + b) \cdot h}{2}$ (promedio de las bases por la altura).

    > **Newton Tip:** "Seba, dile a tu alumno: el área es cuántas baldosas caben dentro, el perímetro es cuánta cinta necesito para rodearlo. ¡Que no mezclen peras con manzanas!"
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G12 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G12 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Área de un triángulo de base 10 y altura 6. | 1. Aplicar formula: $(10 \cdot 6) / 2$.<br>2. $60 / 2 = 30$. | **30 u²** |
| **E02** | Perímetro de un cuadrado de área 64. | 1. Calcular lado: $\sqrt{64} = 8$.<br>2. Multiplicar por 4: $8 \cdot 4 = 32$. | **32 u** |
| **E03** | Área de un rombo con diagonales de 8 y 10. | 1. Multiplicar diagonales: $8 \cdot 10 = 80$.<br>2. Dividir por 2: $80 / 2 = 40$. | **40 u²** |
| **E04** | Área de un trapecio: bases 6 y 4, altura 5. | 1. Sumar bases: $6 + 4 = 10$.<br>2. Multiplicar por altura y dividir por 2: $(10 \cdot 5) / 2$. | **25 u²** |
| **E05** | Perímetro de un rectángulo de área 50 si un lado es 5. | 1. Hallar otro lado: $50 / 5 = 10$.<br>2. Sumar lados: $2 \cdot (5 + 10) = 30$. | **30 u** |
""")

    with st.expander("❓ Cuestionario G12", expanded=False):
        quiz = [
            {'question': 'Si el lado de un cuadrado se duplica, su área se:', 'options': {'A': 'Duplica', 'B': 'Triplica', 'C': 'Cuadruplica', 'D': 'Mantiene igual'}, 'answer': 'C', 'explanation': 'Recuerda que el área es $L^2$. Si el lado es $2L$, el área es $(2L)^2 = 4L^2$. ¡Cuidado con esa trampa!'},
            {'question': 'El área de un triángulo rectángulo de catetos 3 y 4 es:', 'options': {'A': '6', 'B': '12', 'C': '7', 'D': '5'}, 'answer': 'A', 'explanation': 'En el triángulo rectángulo, los catetos actúan como base y altura. $(3 \\cdot 4) / 2 = 6$.'},
            {'question': 'El perímetro de un rectángulo de 10 cm de base y 5 cm de altura es:', 'options': {'A': '15 cm', 'B': '30 cm', 'C': '50 cm', 'D': '25 cm'}, 'answer': 'B', 'explanation': 'Suma todos los bordes: $10 + 5 + 10 + 5 = 30$.'},
            {'question': 'Si las diagonales de un rombo miden 12 y 16, su área es:', 'options': {'A': '192', 'B': '96', 'C': '56', 'D': '28'}, 'answer': 'B', 'explanation': 'Fórmula del rombo: $(12 \\cdot 16) / 2 = 96$. No olvides dividir por dos.'},
            {'question': 'El área de un cuadrado cuya diagonal mide $4\\sqrt{2}$ es:', 'options': {'A': '8', 'B': '16', 'C': '32', 'D': '64'}, 'answer': 'B', 'explanation': 'Típ: Si la diagonal es $4\\sqrt{2}$, el lado es 4. El área es $4^2 = 16$.'},
            {'question': '¿Cuál es el área de un triángulo equilátero de lado 2?', 'options': {'A': '$\\sqrt{3}$', 'B': '$2\\sqrt{3}$', 'C': '4', 'D': '1'}, 'answer': 'A', 'explanation': 'Aplica la fórmula: $(2^2 \\cdot \\sqrt{3}) / 4 = 4\\sqrt{3} / 4 = \\sqrt{3}$.'},
            {'question': 'Un trapecio tiene bases de 12 y 8 cm. Si su altura es 10 cm, el área es:', 'options': {'A': '200 cm²', 'B': '100 cm²', 'C': '96 cm²', 'D': '80 cm²'}, 'answer': 'B', 'explanation': 'Promedio de bases: $(12+8)/2 = 10$. Luego $10 \\cdot 10 = 100$.'},
            {'question': 'Si el perímetro de un cuadrado es 20, su área es:', 'options': {'A': '20', 'B': '25', 'C': '400', 'D': '100'}, 'answer': 'B', 'explanation': 'Lado = $20 / 4 = 5$. Área = $5^2 = 25$.'},
            {'question': 'El área de un rectángulo es 48. Si su base es 8, su perímetro es:', 'options': {'A': '6', 'B': '14', 'C': '28', 'D': '32'}, 'answer': 'C', 'explanation': 'Altura = $48 / 8 = 6$. Perímetro = $2 \\cdot (8 + 6) = 2 \\cdot 14 = 28$.'},
            {'question': 'La suma de los lados de cualquier polígono se llama:', 'options': {'A': 'Área', 'B': 'Diagonal', 'C': 'Perímetro', 'D': 'Volumen'}, 'answer': 'C', 'explanation': 'Típ: El perímetro es el camino por la orilla. Concepto fundamental.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g12_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G12)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **C** | **Galileo Tip:** "Recuerda que el área es $L^2$. Si el lado es $2L$, el área es $(2L)^2 = 4L^2$. ¡Cuidado con esa trampa!" |
| **2** | **A** | **Newton Tip:** "En el triángulo rectángulo, los catetos actúan como base y altura. $(3 \cdot 4) / 2 = 6$." |
| **3** | **B** | **Hawking Tip:** "Suma todos los bordes: $10 + 5 + 10 + 5 = 30$." |
| **4** | **B** | **Curie Tip:** "Fórmula del rombo: $(12 \cdot 16) / 2 = 96$. No olvides dividir por dos." |
| **5** | **B** | **Statham Tip:** "Típ: Si la diagonal es $4\sqrt{2}$, el lado es 4. El área es $4^2 = 16$." |
| **6** | **A** | **Newton Tip:** "Aplica la fórmula: $(2^2 \cdot \sqrt{3}) / 4 = 4\sqrt{3} / 4 = \sqrt{3}$." |
| **7** | **B** | **Galileo Tip:** "Promedio de bases: $(12+8)/2 = 10$. Luego $10 \cdot 10 = 100$." |
| **8** | **B** | **Hawking Tip:** "Lado = $20 / 4 = 5$. Área = $5^2 = 25$." |
| **9** | **C** | **Curie Tip:** "Altura = $48 / 8 = 6$. Perímetro = $2 \cdot (8 + 6) = 2 \cdot 14 = 28$." |
| **10** | **C** | **Statham Tip:** "Típ: El perímetro es el camino por la orilla. Concepto fundamental." |
""")
