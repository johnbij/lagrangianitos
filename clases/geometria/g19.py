import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G19():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G19: Transformaciones Isométricas — Movimiento sin Deformación")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
# 🎬 Clase G19: Transformaciones Isométricas - Movimiento sin Deformación
**Eje:** Geometría | **Nivel:** Alcance del Objetivo

---

### 🛡️ 1. Definición de Isometría
Del griego *iso* (igual) y *metría* (medida). Son transformaciones que cambian la posición o el sentido de una figura pero **mantienen su forma y su tamaño** (congruencia).

### ⚖️ 2. Los Tres Tipos Fundamentales
* **Traslación:** Desplazar cada punto de la figura según un **vector de traslación** $\vec{v}(a, b)$. Se suma $a$ a las $x$ y $b$ a las $y$.
* **Rotación:** Girar la figura respecto a un **centro de rotación** y un **ángulo $\alpha$**.
    * El sentido positivo es antihorario (contrario al reloj).
* **Simetría (Reflexión):**
    * **Axial:** Respecto a una recta (eje). Actúa como un espejo.
    * **Central:** Respecto a un punto (equivalente a una rotación de 180°).

### 📐 3. Puntos Clave en el Plano (Centro $O(0,0)$)
Si rotamos un punto $(x, y)$ en sentido antihorario:
* **90°:** $(-y, x)$
* **180°:** $(-x, -y)$
* **270°:** $(y, -x)$

> **Newton Tip:** "Seba, dile a tu alumno: en las isometrías, el área y el perímetro son SAGRADOS, no cambian. Si en un ejercicio te dicen que el área cambió, ¡no es isometría!"
""")

    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🛠️ Ejercitación Técnica G19 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G19 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Trasladar el punto $A(3, -2)$ según el vector $\vec{v}(-1, 5)$. | 1. Sumar coordenadas: $(3 + (-1), -2 + 5)$. | **$A'(2, 3)$** |
| **E02** | Rotar el punto $B(4, 1)$ en 90° respecto al origen. | 1. Aplicar regla $(-y, x)$. <br>2. El 1 pasa a ser $-1$ y el 4 queda igual. | **$B'(-1, 4)$** |
| **E03** | Simetría axial de $C(2, 5)$ respecto al eje $X$. | 1. En eje $X$, el signo de $y$ cambia, $x$ se mantiene. | **$C'(2, -5)$** |
| **E04** | Simetría axial de $D(2, 5)$ respecto al eje $Y$. | 1. En eje $Y$, el signo de $x$ cambia, $y$ se mantiene. | **$D'(-2, 5)$** |
| **E05** | ¿Qué vector traslada $P(1, 1)$ a $P'(4, -2)$? | 1. Restar: Final - Inicial. <br>2. $(4-1, -2-1)$. | **$\vec{v}(3, -3)$** |
""")

    with st.expander("❓ Cuestionario G19", expanded=False):
        quiz = [
            {'question': 'Una transformación isométrica se caracteriza por mantener siempre:', 'options': {'A': 'La posición original', 'B': 'El área y el tamaño', 'C': 'La orientación de la figura', 'D': 'El centro de gravedad'}, 'answer': 'B', 'explanation': "Isometría significa 'misma medida'. Los lados y ángulos no sufren estrés, solo se mueven."},
            {'question': 'Si trasladamos un punto $(x, y)$ con el vector $\\vec{v}(a, b)$, el nuevo punto es:', 'options': {'A': '$(x \\cdot a, y \\cdot b)$', 'B': '$(x - a, y - b)$', 'C': '$(x + a, y + b)$', 'D': '$(a, b)$'}, 'answer': 'C', 'explanation': 'La traslación es una simple suma vectorial. Desplazamiento puro.'},
            {'question': 'La rotación de un punto $(3, 2)$ en 180° respecto al origen resulta en:', 'options': {'A': '$(-3, -2)$', 'B': '$(-2, 3)$', 'C': '$(2, -3)$', 'D': '$(3, -2)$'}, 'answer': 'A', 'explanation': "180° es el 'opuesto' total. Ambos signos cambian de bando."},
            {'question': 'La simetría respecto a un punto es equivalente a una rotación de:', 'options': {'A': '90°', 'B': '180°', 'C': '270°', 'D': '360°'}, 'answer': 'B', 'explanation': 'La simetría central y el giro de media vuelta son hermanos gemelos.'},
            {'question': 'Al reflejar el punto $(-4, 7)$ respecto al eje $Y$, obtenemos:', 'options': {'A': '$(-4, -7)$', 'B': '$(4, 7)$', 'C': '$(4, -7)$', 'D': '$(7, -4)$'}, 'answer': 'B', 'explanation': 'Típ: Si el espejo es el eje $Y$, el punto cruza de izquierda a derecha, pero mantiene su altura.'},
            {'question': '¿Cuál de las siguientes NO es una transformación isométrica?', 'options': {'A': 'Traslación', 'B': 'Rotación', 'C': 'Homotecia ($k=2$)', 'D': 'Simetría Axial'}, 'answer': 'C', 'explanation': "La homotecia cambia el tamaño, por eso es una transformación 'isomórfica' (misma forma) pero NO isométrica."},
            {'question': 'En una rotación de 270° (antihorario), el punto $(x, y)$ se convierte en:', 'options': {'A': '$(-y, x)$', 'B': '$(-x, -y)$', 'C': '$(y, -x)$', 'D': '$(y, x)$'}, 'answer': 'C', 'explanation': '270° es como girar 90° en sentido horario. Intercambias y cambias el signo de la nueva $y$.'},
            {'question': 'Si aplicamos dos simetrías axiales respecto a ejes paralelos, el resultado es una:', 'options': {'A': 'Rotación', 'B': 'Traslación', 'C': 'Nueva simetría axial', 'D': 'Homotecia'}, 'answer': 'B', 'explanation': 'Dos reflexiones seguidas en espejos paralelos equivalen a empujar la figura (trasladarla).'},
            {'question': 'El vector que deja a una figura en su posición original es:', 'options': {'A': '$\\vec{v}(1, 1)$', 'B': '$\\vec{v}(0, 0)$', 'C': '$\\vec{v}(-1, -1)$', 'D': '$\\vec{v}(\\infty, \\infty)$'}, 'answer': 'B', 'explanation': "Se llama vector nulo. Es el 'no te muevas'."},
            {'question': 'Una figura tiene simetría central si al rotarla en _____ grados queda igual:', 'options': {'A': '45°', 'B': '90°', 'C': '180°', 'D': '360°'}, 'answer': 'C', 'explanation': "Típ: Piensa en la letra 'S' o en el número '8'. Si los giras 180°, se ven exactamente igual."}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g19_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G19)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **B** | **Galileo Tip:** "Isometría significa 'misma medida'. Los lados y ángulos no sufren estrés, solo se mueven." |
| **2** | **C** | **Newton Tip:** "La traslación es una simple suma vectorial. Desplazamiento puro." |
| **3** | **A** | **Hawking Tip:** "180° es el 'opuesto' total. Ambos signos cambian de bando." |
| **4** | **B** | **Curie Tip:** "La simetría central y el giro de media vuelta son hermanos gemelos." |
| **5** | **B** | **Statham Tip:** "Típ: Si el espejo es el eje $Y$, el punto cruza de izquierda a derecha, pero mantiene su altura." |
| **6** | **C** | **Newton Tip:** "La homotecia cambia el tamaño, por eso es una transformación 'isomórfica' (misma forma) pero NO isométrica." |
| **7** | **C** | **Galileo Tip:** "270° es como girar 90° en sentido horario. Intercambias y cambias el signo de la nueva $y$." |
| **8** | **B** | **Hawking Tip:** "Dos reflexiones seguidas en espejos paralelos equivalen a empujar la figura (trasladarla)." |
| **9** | **B** | **Curie Tip:** "Se llama vector nulo. Es el 'no te muevas'." |
| **10** | **C** | **Statham Tip:** "Típ: Piensa en la letra 'S' o en el número '8'. Si los giras 180°, se ven exactamente igual." |
""")
