import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G05():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G05: Ángulos entre Paralelas y una Transversal")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
# 🎬 Clase G05: Ángulos entre Paralelas y una Transversal
**Eje:** Geometría | **Nivel:** Alcance del Objetivo

---

### 🛡️ 1. El Escenario
Cuando dos rectas paralelas ($L_1 \parallel L_2$) son cortadas por una recta transversal (o secante), se forman 8 ángulos que guardan relaciones matemáticas específicas entre sí.

### ⚖️ 2. Tipos de Ángulos y sus Propiedades
* **Ángulos Correspondientes:** Están en la misma posición relativa. Son **Iguales**.
* **Ángulos Alternos Internos:** Estás "dentro" de las paralelas, en lados opuestos de la secante. Son **Iguales**.
* **Ángulos Alternos Externos:** Están "fuera" de las paralelas, en lados opuestos de la secante. Son **Iguales**.
* **Ángulos Colaterales (Internos o Externos):** Están al mismo lado de la secante. Son **Suplementarios** (suman 180°).

> **Newton Tip:** "Típ: Si las rectas son paralelas, solo existen dos medidas de ángulos en todo el dibujo. O son iguales, o suman 180°. ¡No hay más ciencia!"
""")

    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🛠️ Ejercitación Técnica G05 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G05 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Si un ángulo obtuso mide 130°, ¿cuánto mide su correspondiente? | 1. Por propiedad de paralelas, los correspondientes son iguales. | **130°** |
| **E02** | Hallar el alterno interno de un ángulo de 50° | 1. Los ángulos alternos internos entre paralelas miden lo mismo. | **50°** |
| **E03** | Ángulos colaterales internos: uno mide $x$ y el otro 70°. | 1. Suman 180°. <br>2. $180 - 70 = 110$. | **$x = 110°$** |
| **E04** | ¿Cómo son los ángulos opuestos por el vértice? | 1. Siempre son iguales, sin importar si hay paralelas o no. | **Iguales** |
| **E05** | Si los ángulos alternos externos no son iguales... | 1. Entonces las rectas **no** son paralelas. | **No son paralelas** |
""")

    with st.expander("❓ Cuestionario G05", expanded=False):
        quiz = [
            {'question': 'Los ángulos correspondientes entre rectas paralelas son:', 'options': {'A': 'Suplementarios', 'B': 'Complementarios', 'C': 'Iguales (Congruentes)', 'D': 'Opuestos'}, 'answer': 'C', 'explanation': 'Imagina que deslizas una paralela sobre la otra; los correspondientes calzan perfecto. Son iguales.'},
            {'question': 'Si un ángulo alterno interno mide 65°, su pareja mide:', 'options': {'A': '25°', 'B': '65°', 'C': '115°', 'D': '180°'}, 'answer': 'B', 'explanation': "La 'Z' de alternos internos nunca falla: los ángulos en las esquinas de la Z son iguales."},
            {'question': 'Dos ángulos colaterales internos entre paralelas siempre suman:', 'options': {'A': '90°', 'B': '180°', 'C': '270°', 'D': '360°'}, 'answer': 'B', 'explanation': "Colaterales viene de 'al mismo lado'. Al estar al mismo lado, se 'aplastan' formando un ángulo llano de 180°."},
            {'question': 'Los ángulos que están fuera de las paralelas y en lados opuestos de la transversal son:', 'options': {'A': 'Alternos internos', 'B': 'Alternos externos', 'C': 'Correspondientes', 'D': 'Colaterales externos'}, 'answer': 'B', 'explanation': 'Externos porque están afuera, alternos porque saltan la barda (la transversal).'},
            {'question': 'Si un ángulo mide 40°, ¿cuánto mide su suplemento colateral?', 'options': {'A': '40°', 'B': '50°', 'C': '140°', 'D': '160°'}, 'answer': 'C', 'explanation': 'Típ: $180 - 40 = 140$. No te compliques la vida.'},
            {'question': '¿Qué relación tienen los ángulos opuestos por el vértice en este sistema?', 'options': {'A': 'Son suplementarios', 'B': 'Suman 90°\n) Son iguales\nD) Son siempre rectos\n\n**7. Si las rectas L1 y L2 no son paralelas, los ángulos correspondientes:**\nA) Siguen siendo iguales\nB) No son iguales', 'C': 'Suman 180°', 'D': 'Son nulos'}, 'answer': 'C', 'explanation': 'Propiedad básica: cualquier par de rectas que se crucen forman ángulos opuestos iguales.'},
            {'question': 'En el sistema de paralelas, si un ángulo mide 90°, todos los demás miden:', 'options': {'A': '0° o 90°', 'B': '45° o 90°', 'C': '90°', 'D': '180°'}, 'answer': 'C', 'explanation': 'Si uno es recto, la transversal es perpendicular a ambas. Todos los ángulos resultantes serán de 90°.'},
            {'question': 'Los ángulos adyacentes que forman una línea recta son:', 'options': {'A': 'Complementarios', 'B': 'Suplementarios', 'C': 'Correspondientes', 'D': 'Alternos'}, 'answer': 'B', 'explanation': 'Adyacentes sobre una recta siempre suman 180°. Son suplementarios por definición.'},
            {'question': 'Si el ángulo "a" es alterno externo con "b", y $a = 125°$, entonces $b$ es:', 'options': {'A': '55°', 'B': '125°', 'C': '180°', 'D': '90°'}, 'answer': 'B', 'explanation': 'Alternos externos entre paralelas son iguales. Marca 125° y sigue con la siguiente.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g05_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G05)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **C** | **Galileo Tip:** "Imagina que deslizas una paralela sobre la otra; los correspondientes calzan perfecto. Son iguales." |
| **2** | **B** | **Newton Tip:** "La 'Z' de alternos internos nunca falla: los ángulos en las esquinas de la Z son iguales." |
| **3** | **B** | **Hawking Tip:** "Colaterales viene de 'al mismo lado'. Al estar al mismo lado, se 'aplastan' formando un ángulo llano de 180°." |
| **4** | **B** | **Curie Tip:** "Externos porque están afuera, alternos porque saltan la barda (la transversal)." |
| **5** | **C** | **Statham Tip:** "Típ: $180 - 40 = 140$. No te compliques la vida." |
| **6** | **C** | **Newton Tip:** "Propiedad básica: cualquier par de rectas que se crucen forman ángulos opuestos iguales." |
| **7** | **B** | **Galileo Tip:** "La igualdad de estos ángulos es la prueba de fuego de que las rectas son paralelas." |
| **8** | **C** | **Hawking Tip:** "Si uno es recto, la transversal es perpendicular a ambas. Todos los ángulos resultantes serán de 90°." |
| **9** | **B** | **Curie Tip:** "Adyacentes sobre una recta siempre suman 180°. Son suplementarios por definición." |
| **10** | **B** | **Statham Tip:** "Alternos externos entre paralelas son iguales. Marca 125° y sigue con la siguiente." |
""")
