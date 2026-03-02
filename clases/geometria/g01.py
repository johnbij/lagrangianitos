import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G01():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G01: Plano Cartesiano, Distancia y Punto Medio")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
### 🎬 Video 056 — El Plano Cartesiano

Es el mapa de operaciones. Se compone de dos ejes perpendiculares:

* **Eje X (Abscisas):** El eje horizontal.
* **Eje Y (Ordenadas):** El eje vertical.
* **Origen:** El punto $(0,0)$, donde ambos ejes se cruzan.

Los ejes dividen el plano en 4 **cuadrantes**:

| Cuadrante | Signo de $x$ | Signo de $y$ |
| :--- | :---: | :---: |
| **I** | $+$ | $+$ |
| **II** | $-$ | $+$ |
| **III** | $-$ | $-$ |
| **IV** | $+$ | $-$ |

> **Statham Tip:** *"Seba, dile que el orden importa. En el código y en el mapa, primero caminas (X) y luego subes (Y). Si lo haces al revés, caes en una trampa."*

---

### 🎬 Video 057 — Distancia entre Dos Puntos

Para calcular la distancia entre $A(x_1, y_1)$ y $B(x_2, y_2)$, usamos el Teorema de Pitágoras aplicado al plano:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**Procedimiento:**
1. Resta las coordenadas $x$ y elévalas al cuadrado.
2. Resta las coordenadas $y$ y elévalas al cuadrado.
3. Suma ambos resultados y saca la raíz cuadrada.

> La distancia siempre es positiva. No importa si vas de $A$ a $B$ o de $B$ a $A$, el camino mide lo mismo.

---

### 🎬 Video 058 — Punto Medio

El punto medio $M$ divide al segmento en dos partes exactamente iguales. Es el promedio de las coordenadas:

$$M = \left( \frac{x_1 + x_2}{2},\ \frac{y_1 + y_2}{2} \right)$$

**Ejemplo:** Si $A(2, 4)$ y $B(8, 10)$:
* $x_M = (2 + 8) / 2 = 5$
* $y_M = (4 + 10) / 2 = 7$
* **Punto Medio:** $M(5, 7)$
""")

    # ── FIGURA: Plano Cartesiano ─────────────────────────────────────────────
    st.markdown("#### 📊 El Plano Cartesiano y sus Cuadrantes")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='black', linewidth=2)
    ax.axvline(0, color='black', linewidth=2)

    puntos = [(3, 4), (-3, 4), (-3, -4), (3, -4)]
    etiquetas = ['I (+,+)', 'II (-,+)', 'III (-,-)', 'IV (+,-)']
    colores = ['#1b5e20', '#c0392b', '#6C63FF', '#e67e22']

    for (x, y), et, col in zip(puntos, etiquetas, colores):
        ax.scatter(x, y, color=col, s=120, zorder=5)
        ax.text(x, y + 0.6, f'{et}\nP({x},{y})', ha='center', color=col, fontweight='bold', fontsize=10)
        ax.plot([x, x], [0, y], color=col, linestyle='--', alpha=0.4)
        ax.plot([0, x], [y, y], color=col, linestyle='--', alpha=0.4)

    ax.set_xlim(-6, 6); ax.set_ylim(-6, 6)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.set_xlabel("Eje X (Abscisas)", fontsize=11)
    ax.set_ylabel("Eje Y (Ordenadas)", fontsize=11)
    ax.set_title("Plano Cartesiano — Los 4 Cuadrantes", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🎬 Video 059 — Ángulos y su Clasificación

| Nombre | Medida | Visualización |
| :--- | :--- | :--- |
| **Agudo** | Menor a 90° | Cerrado, "afilado" |
| **Recto** | Exactamente 90° | Forma una 'L' perfecta |
| **Obtuso** | Entre 90° y 180° | Abierto, ancho |
| **Extendido** | Exactamente 180° | Una línea recta |

**Relaciones importantes:**
* **Complementarios:** Dos ángulos que suman 90°. Ej: 30° y 60°.
* **Suplementarios:** Dos ángulos que suman 180°. Ej: 120° y 60°.
* **Opuestos por el vértice:** Se forman cuando dos rectas se cruzan; los ángulos opuestos son **siempre iguales**.

---

### 🎬 Video 060 — Ángulos entre Paralelas

Cuando una **transversal** (una recta que cruza) corta dos rectas paralelas, se forman 8 ángulos. Solo hay **dos medidas** distintas que se repiten.

* **Ángulos Correspondientes:** Misma posición relativa → Son **iguales**.
* **Alternos Internos:** Dentro de las paralelas en lados opuestos → Son **iguales**.
* **Alternos Externos:** Fuera en lados opuestos → Son **iguales**.
* **Co-internos (Conjugados):** Interior, mismo lado → Suman **180°**.

> **Statham Tip:** *"Seba, dile que busque la letra 'Z'. Los ángulos que quedan dentro de las esquinas de la Z son alternos internos y siempre son iguales. Es el truco de reconocimiento más rápido."*
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G01", expanded=False):
        st.markdown(r"""
### E01: Identificar coordenadas y cuadrante

**Datos:** $P(-3, 5)$, $Q(4, -2)$, $R(0, 7)$

| Punto | Cuadrante | Signo de X | Signo de Y |
| :--- | :--- | :--- | :--- |
| $P(-3, 5)$ | **II** | Negativo | Positivo |
| $Q(4, -2)$ | **IV** | Positivo | Negativo |
| $R(0, 7)$ | Eje Y | — | Positivo |

---

### E02: Calcular distancia entre dos puntos

**Datos:** $A(1, 2)$ y $B(4, 6)$

$$d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

La distancia es **5 unidades**. (¡Un trío pitagórico 3-4-5!)

---

### E03: Encontrar el punto medio

**Datos:** $C(3, -1)$ y $D(7, 5)$

$$M = \left(\frac{3+7}{2},\ \frac{-1+5}{2}\right) = \left(5,\ 2\right)$$

---

### E04: Ángulos entre paralelas

Si una transversal corta dos paralelas formando un ángulo de 65°, ¿cuánto mide el ángulo co-interno?

* Los co-internos suman 180°.
* $180° - 65° = 115°$
""")

    # ── QUIZ ────────────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario G01: Plano, Distancia y Ángulos", expanded=False):
        quiz = [
            {"question": r'El punto $P(-2, 5)$ se ubica en el cuadrante:',
             "options": {"A": "I", "B": "II", "C": "III", "D": "IV"},
             "answer": "B", "explanation": r"El Cuadrante II tiene $x$ negativo e $y$ positivo."},
            {"question": r'La distancia entre $A(0, 0)$ y $B(3, 4)$ es:',
             "options": {"A": "5", "B": "7", "C": r"$\sqrt{7}$", "D": "3,5"},
             "answer": "A", "explanation": r"$d = \sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5$. Trío 3-4-5."},
            {"question": r'El punto medio entre $A(2, 6)$ y $B(8, 2)$ es:',
             "options": {"A": r"$(5, 4)$", "B": r"$(6, 8)$", "C": r"$(4, 5)$", "D": r"$(10, 8)$"},
             "answer": "A", "explanation": r"$M_x = (2+8)/2 = 5$; $M_y = (6+2)/2 = 4$."},
            {"question": "Dos ángulos son complementarios. Uno mide 38°. ¿Cuánto mide el otro?",
             "options": {"A": "142°", "B": "62°", "C": "52°", "D": "128°"},
             "answer": "C", "explanation": "Complementarios suman 90°. $90° - 38° = 52°$."},
            {"question": "Una transversal corta dos paralelas. Un ángulo mide 70°. Su alterno interno mide:",
             "options": {"A": "110°", "B": "70°", "C": "20°", "D": "140°"},
             "answer": "B", "explanation": "Los ángulos alternos internos son siempre iguales."},
            {"question": r'Una transversal corta dos paralelas. Un ángulo mide 115°. Su co-interno (conjugado) mide:',
             "options": {"A": "65°", "B": "115°", "C": "25°", "D": "75°"},
             "answer": "A", "explanation": "Los co-internos son suplementarios: $180° - 115° = 65°$."},
            {"question": r'¿En cuál cuadrante tienen ambas coordenadas signo negativo?',
             "options": {"A": "I", "B": "II", "C": "III", "D": "IV"},
             "answer": "C", "explanation": "El Cuadrante III tiene $x < 0$ e $y < 0$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g01_quiz")

    # ── PAUTA ───────────────────────────────────────────────────────────────
    with st.expander("🔑 Pauta Técnica G01", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | Cuadrante II: $x < 0$, $y > 0$. |
| **2** | **A** | Trío pitagórico 3-4-5. $\sqrt{9+16}=5$. |
| **3** | **A** | Promedio de cada coordenada: $(5, 4)$. |
| **4** | **C** | $90° - 38° = 52°$. Los complementarios suman 90°. |
| **5** | **B** | Alternos internos son iguales. |
| **6** | **A** | Co-internos son suplementarios: $180° - 115° = 65°$. |
| **7** | **C** | Cuadrante III: ambas negativas. |
""")
