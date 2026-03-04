import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G14():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G14: Ángulos en la Circunferencia")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
# 🎬 Clase G14: Ángulos en la Circunferencia
**Eje:** Geometría | **Nivel:** Alcance del Objetivo

---

### 🛡️ 1. Ángulo del Centro
Es aquel cuyo vértice es el centro de la circunferencia y sus lados son radios.
* **Propiedad:** La medida del ángulo del centro es igual a la medida del arco que subtiende.

### ⚖️ 2. Ángulo Inscrito
Es aquel cuyo vértice está sobre la circunferencia y sus lados son cuerdas.
* **Propiedad Maestra:** El ángulo inscrito mide siempre la **mitad** del ángulo del centro que subtiende el mismo arco.
* **Corolario:** Todos los ángulos inscritos que subtienden el mismo arco son iguales.

### 📐 3. Casos Especiales
* **Ángulo Semi-inscrito:** Formado por una cuerda y una tangente. Mide la mitad del arco que subtiende.
* **Ángulo en la Semicircunferencia:** Todo ángulo inscrito que subtiende un diámetro es siempre un **ángulo recto (90°)**.

> **Newton Tip:** "Seba, dile a tu alumno: si ves un triángulo dibujado dentro de un círculo y un lado es el diámetro, ¡automáticamente ese triángulo es rectángulo! Es el truco más rápido de la prueba."
""")

    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🛠️ Ejercitación Técnica G14 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G14 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Si el arco $AB$ mide 80°, ¿cuánto mide el ángulo del centro? | 1. Por definición, miden lo mismo. | **80°** |
| **E02** | Si el arco $AB$ mide 80°, ¿cuánto mide el ángulo inscrito? | 1. El ángulo inscrito es la mitad del arco.<br>2. $80 / 2 = 40$. | **40°** |
| **E03** | Un ángulo inscrito mide 30°. ¿Cuánto mide el ángulo del centro asociado? | 1. El del centro es el doble del inscrito.<br>2. $30 \cdot 2 = 60$. | **60°** |
| **E04** | Hallar ángulo $x$ inscrito que subtiende un diámetro. | 1. Por teorema, todo ángulo sobre el diámetro es recto. | **90°** |
| **E05** | Dos ángulos inscritos subtienden el mismo arco. Si uno mide 25°, ¿el otro? | 1. Ángulos que comparten el mismo arco son iguales. | **25°** |
""")

    with st.expander("❓ Cuestionario G14", expanded=False):
        quiz = [
            {'question': 'El ángulo cuyo vértice es el centro de la circunferencia se llama:', 'options': {'A': 'Inscrito', 'B': 'Del centro', 'C': 'Semi-inscrito', 'D': 'Interior'}, 'answer': 'B', 'explanation': 'Su nombre lo dice todo: nace en el centro, usa los radios como brazos.'},
            {'question': 'Si un ángulo del centro mide 100°, el ángulo inscrito que subtiende el mismo arco mide:', 'options': {'A': '100°', 'B': '200°', 'C': '50°', 'D': '25°'}, 'answer': 'C', 'explanation': "Regla de oro: El inscrito es siempre el más 'flaco', exactamente la mitad."},
            {'question': 'Todo ángulo inscrito en una semicircunferencia (que subtiende el diámetro) mide:', 'options': {'A': '45°', 'B': '90°', 'C': '180°', 'D': '60°'}, 'answer': 'B', 'explanation': 'Es un clásico. Un ángulo que mira a la mitad del círculo (180°) tiene que medir 90°.'},
            {'question': 'Si un arco mide 70°, el ángulo inscrito correspondiente mide:', 'options': {'A': '35°', 'B': '70°', 'C': '140°', 'D': '10°'}, 'answer': 'A', 'explanation': 'Ángulo inscrito = Arco / 2. Entonces $70 / 2 = 35$.'},
            {'question': 'El ángulo formado por una cuerda y una recta tangente se llama:', 'options': {'A': 'Inscrito', 'B': 'Semi-inscrito', 'C': 'Exterior', 'D': 'Central'}, 'answer': 'B', 'explanation': "Típ: Es como un inscrito 'al borde'. Se calcula igual: mitad del arco."},
            {'question': 'Dos ángulos inscritos que subtienden el mismo arco son siempre:', 'options': {'A': 'Suplementarios', 'B': 'Complementarios', 'C': 'Iguales', 'D': 'Diferentes'}, 'answer': 'C', 'explanation': 'No importa dónde pongas el vértice en el borde, si miran al mismo arco, valen lo mismo.'},
            {'question': 'Si el ángulo inscrito mide 45°, el arco que subtiende mide:', 'options': {'A': '22.5°', 'B': '45°', 'C': '90°', 'D': '180°'}, 'answer': 'C', 'explanation': 'Si el ángulo es 45, el arco es el doble: 90. Es un cuarto de circunferencia.'},
            {'question': 'En una circunferencia, la medida total de los arcos es:', 'options': {'A': '180°', 'B': '270°', 'C': '360°', 'D': '100°'}, 'answer': 'C', 'explanation': 'Al igual que un ángulo completo, la vuelta total de arcos suma 360°.'},
            {'question': 'Si un ángulo central mide $x$, el ángulo inscrito que subtiende el mismo arco mide:', 'options': {'A': '$2x$', 'B': '$x$', 'C': '$x/2$', 'D': '$x+10$'}, 'answer': 'C', 'explanation': 'Relación fundamental: Centro es el total, Inscrito es la mitad.'},
            {'question': 'Un cuadrilátero está inscrito en una circunferencia. Sus ángulos opuestos deben ser:', 'options': {'A': 'Iguales', 'B': 'Suplementarios (suman 180°)', 'C': 'Complementarios', 'D': 'Rectos'}, 'answer': 'B', 'explanation': 'Típ: Se llama cuadrilátero cíclico. Propiedad avanzada que salva vidas en la prueba.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g14_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G14)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **B** | **Galileo Tip:** "Su nombre lo dice todo: nace en el centro, usa los radios como brazos." |
| **2** | **C** | **Newton Tip:** "Regla de oro: El inscrito es siempre el más 'flaco', exactamente la mitad." |
| **3** | **B** | **Hawking Tip:** "Es un clásico. Un ángulo que mira a la mitad del círculo (180°) tiene que medir 90°." |
| **4** | **A** | **Curie Tip:** "Ángulo inscrito = Arco / 2. Entonces $70 / 2 = 35$." |
| **5** | **B** | **Statham Tip:** "Típ: Es como un inscrito 'al borde'. Se calcula igual: mitad del arco." |
| **6** | **C** | **Newton Tip:** "No importa dónde pongas el vértice en el borde, si miran al mismo arco, valen lo mismo." |
| **7** | **C** | **Galileo Tip:** "Si el ángulo es 45, el arco es el doble: 90. Es un cuarto de circunferencia." |
| **8** | **C** | **Hawking Tip:** "Al igual que un ángulo completo, la vuelta total de arcos suma 360°." |
| **9** | **C** | **Curie Tip:** "Relación fundamental: Centro es el total, Inscrito es la mitad." |
| **10** | **B** | **Statham Tip:** "Típ: Se llama cuadrilátero cíclico. Propiedad avanzada que salva vidas en la prueba." |
""")
