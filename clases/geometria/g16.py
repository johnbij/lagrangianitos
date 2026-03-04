import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G16():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G16: Teorema de Tales — Proporcionalidad entre Paralelas")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
# 🎬 Clase G16: Teorema de Tales - Proporcionalidad Entre Paralelas
**Eje:** Geometría | **Nivel:** Alcance del Objetivo

---

### 🛡️ 1. El Teorema Fundamental
Si tres o más rectas paralelas ($L_1 \parallel L_2 \parallel L_3$) son cortadas por dos rectas transversales ($S_1$ y $S_2$), los segmentos determinados en una de las transversales son **proporcionales** a los segmentos correspondientes en la otra.

### ⚖️ 2. Tipos de Configuraciones
* **Configuración Simple (Escalera):** Segmentos laterales proporcionales.
  $$\frac{a}{b} = \frac{c}{d}$$
* **Configuración en Triángulo:** Si una recta es paralela a un lado del triángulo, se forman segmentos proporcionales y triángulos semejantes.
* **Configuración en "X" (Reloj de Arena):** Dos paralelas unidas por transversales que se cruzan. Los lados opuestos mantienen la razón.

### 📐 3. La Regla de Oro
Lo más importante en Tales es el **orden**. Si empiezas de arriba hacia abajo en una transversal, debes hacer lo mismo en la otra. Si comparas "segmento corto" con "segmento total", debes repetir esa lógica en todo el ejercicio.

> **Newton Tip:** "Seba, dile a tu alumno que Tales es como una fotocopiadora: mantiene la forma y las proporciones, solo cambia el tamaño. ¡Si aprenden a armar la fracción, el ejercicio está resuelto!"
""")

    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🛠️ Ejercitación Técnica G16 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G16 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | En paralelas, los segmentos en $S_1$ son 2 y 4. En $S_2$ son 3 y $x$. | 1. Armar proporción: $2 / 4 = 3 / x$.<br>2. Multiplicar cruzado: $2x = 12$. | **$x = 6$** |
| **E02** | En un triángulo, una paralela divide un lado en 5 y 10. Si el otro lado total mide 18. | 1. Razón es $5:15$ (parte/total).<br>2. $5 / 15 = x / 18 \implies 1/3 = x / 18$. | **$x = 6$** |
| **E03** | Configuración en "X": paralela superior 4, inferior 8. Lado superior 3. | 1. La razón es $4:8$ ($1:2$).<br>2. El lado inferior debe ser el doble: $3 \cdot 2$. | **6** |
| **E04** | Segmentos en $S_1$ son $x$ y $x+2$. En $S_2$ son 2 y 4. | 1. $x / (x+2) = 2 / 4 \implies x / (x+2) = 1/2$.<br>2. $2x = x + 2$. | **$x = 2$** |
| **E05** | ¿Qué condición debe cumplirse para aplicar Tales? | 1. Siempre debe haber al menos un par de rectas paralelas. | **Paralelismo** |
""")

    with st.expander("❓ Cuestionario G16", expanded=False):
        quiz = [
            {'question': 'El Teorema de Tales se fundamenta en la existencia de rectas:', 'options': {'A': 'Perpendiculares', 'B': 'Paralelas', 'C': 'Secantes que no se cortan', 'D': 'Coincidentes'}, 'answer': 'B', 'explanation': 'Sin paralelas no hay Tales. Es la condición necesaria y suficiente.'},
            {'question': 'Si en una transversal los segmentos miden 5 y 10, y en la otra un segmento mide 4, su pareja mide:', 'options': {'A': '2', 'B': '4', 'C': '8', 'D': '12'}, 'answer': 'C', 'explanation': 'Como 10 es el doble de 5, el resultado debe ser el doble de 4. O sea, 8.'},
            {'question': 'En el Teorema de Tales, la relación entre los segmentos correspondientes es de:', 'options': {'A': 'Igualdad', 'B': 'Diferencia constante', 'C': 'Proporcionalidad', 'D': 'Suma constante'}, 'answer': 'C', 'explanation': 'Las medidas cambian, pero la división (razón) entre ellas se mantiene constante.'},
            {'question': 'Si una recta paralela a la base de un triángulo corta los otros dos lados, los segmentos determinados son:', 'options': {'A': 'Iguales a la base', 'B': 'Proporcionales', 'C': 'Siempre la mitad de los lados', 'D': 'Perpendiculares'}, 'answer': 'B', 'explanation': 'Es la aplicación más común en los exámenes de ingreso a la universidad.'},
            {'question': 'En la proporción $a/b = c/d$, si $a=2, b=6$ y $c=3$, entonces $d$ vale:', 'options': {'A': '1', 'B': '9', 'C': '12', 'D': '18'}, 'answer': 'B', 'explanation': 'Típ: $2/6 = 1/3$. Entonces $3/d = 1/3$, lo que nos da $d = 9$.'},
            {'question': 'La configuración de Tales en "triángulo" genera dos triángulos que son:', 'options': {'A': 'Congruentes', 'B': 'Semejantes', 'C': 'Equiláteros', 'D': 'Rectángulos'}, 'answer': 'B', 'explanation': 'Semejantes significa que tienen la misma forma pero distinto tamaño.'},
            {'question': 'Si los segmentos de una transversal están en razón $1:3$, en la otra transversal estarán en razón:', 'options': {'A': '$1:3$', 'B': '$3:1$', 'C': '$1:9$', 'D': 'Depende de la inclinación'}, 'answer': 'A', 'explanation': 'La inclinación de las transversales no afecta la proporción de los segmentos.'},
            {'question': 'En una "X" de Tales, si la base menor es 5 y la mayor 15, la razón de semejanza es:', 'options': {'A': '$1:2$', 'B': '$1:3$', 'C': '$1:4$', 'D': '$1:5$'}, 'answer': 'B', 'explanation': 'Simplemente divides $5/15 = 1/3$.'},
            {'question': '¿Se puede aplicar Tales si las rectas transversales son paralelas entre sí?', 'options': {'A': 'No, nunca', 'B': 'Sí, y los segmentos serán iguales', 'C': 'Solo si son perpendiculares', 'D': 'Solo en el vacío'}, 'answer': 'B', 'explanation': 'Sí, en ese caso se forma un paralelogramo y los segmentos enfrentados son iguales ($1:1$).'},
            {'question': 'Si $L_1 \\parallel L_2$ y se cortan por transversales, el segmento $x$ en $2/x = 4/10$ es:', 'options': {'A': '5', 'B': '20', 'C': '8', 'D': '4'}, 'answer': 'A', 'explanation': 'Típ: Simplifica $4/10$ a $2/5$. Entonces $2/x = 2/5$, por lo tanto $x = 5$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g16_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G16)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **B** | **Galileo Tip:** "Sin paralelas no hay Tales. Es la condición necesaria y suficiente." |
| **2** | **C** | **Newton Tip:** "Como 10 es el doble de 5, el resultado debe ser el doble de 4. O sea, 8." |
| **3** | **C** | **Hawking Tip:** "Las medidas cambian, pero la división (razón) entre ellas se mantiene constante." |
| **4** | **B** | **Curie Tip:** "Es la aplicación más común en los exámenes de ingreso a la universidad." |
| **5** | **B** | **Statham Tip:** "Típ: $2/6 = 1/3$. Entonces $3/d = 1/3$, lo que nos da $d = 9$." |
| **6** | **B** | **Newton Tip:** "Semejantes significa que tienen la misma forma pero distinto tamaño." |
| **7** | **A** | **Galileo Tip:** "La inclinación de las transversales no afecta la proporción de los segmentos." |
| **8** | **B** | **Hawking Tip:** "Simplemente divides $5/15 = 1/3$." |
| **9** | **B** | **Curie Tip:** "Sí, en ese caso se forma un paralelogramo y los segmentos enfrentados son iguales ($1:1$)." |
| **10** | **A** | **Statham Tip:** "Típ: Simplifica $4/10$ a $2/5$. Entonces $2/x = 2/5$, por lo tanto $x = 5$." |
""")
