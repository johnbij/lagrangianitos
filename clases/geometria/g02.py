import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G02():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G02: Triángulos, Pitágoras, Perímetro y Área")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
### 🎬 Video 061 — Triángulos: Fundamentos

**Propiedad de oro:** En cualquier triángulo del universo, la suma de sus ángulos interiores es **siempre 180°**.

**Clasificación según los Lados:**

| Tipo | Descripción |
| :--- | :--- |
| **Equilátero** | 3 lados iguales → 3 ángulos de 60° |
| **Isósceles** | 2 lados iguales → 2 ángulos iguales en la base |
| **Escaleno** | Todos los lados y ángulos distintos |

---

### 🎬 Video 062 — Clasificación por Ángulos y Desigualdad Triangular

**Tipos según sus ángulos:**
* **Acutángulo:** Los 3 ángulos son agudos (menores de 90°).
* **Rectángulo:** Tiene exactamente un ángulo de 90°.
* **Obtusángulo:** Tiene un ángulo obtuso (mayor de 90°).

**Desigualdad Triangular:** Para que un triángulo exista, la suma de **cualquiera de sus dos lados** debe ser **mayor** que el tercer lado.

> *Si tienes palitos de 2 cm, 2 cm y 10 cm, nunca podrás cerrar el triángulo. La línea recta es el camino más corto — si los otros dos lados no suman más que el tercero, nunca se van a tocar.*

---

### 🎬 Video 063 — Teorema de Pitágoras

Se aplica **solo** cuando hay un ángulo de 90°:

* **Catetos ($a, b$):** Los dos lados que forman la 'L'.
* **Hipotenusa ($c$):** El lado más largo, siempre frente al ángulo recto.

$$a^2 + b^2 = c^2$$

**Tríos Pitagóricos (ahorra tiempo en la prueba):**

| Trío | Verificación |
| :---: | :--- |
| $(3, 4, 5)$ | $9 + 16 = 25$ ✅ |
| $(5, 12, 13)$ | $25 + 144 = 169$ ✅ |
| $(8, 15, 17)$ | $64 + 225 = 289$ ✅ |
""")

    # ── FIGURA: Pitágoras ────────────────────────────────────────────────────
    st.markdown("#### 📊 Visualización: Teorema de Pitágoras — Trío 3-4-5")
    fig, ax = plt.subplots(figsize=(7, 4.5))

    # Triángulo rectángulo 3-4-5
    ax.plot([0, 4, 0, 0], [0, 0, 3, 0], 'b-', lw=3)
    ax.plot([0.3, 0.3, 0], [0, 0.3, 0.3], 'k-', lw=1.5)  # Cuadrito 90°
    ax.fill([0, 4, 0], [0, 0, 3], color='#AED6F1', alpha=0.4)

    ax.text(2, -0.4, "Cateto $a = 4$", ha='center', fontsize=12, color='#1a5276')
    ax.text(-0.9, 1.5, "Cateto\n$b = 3$", va='center', fontsize=12, color='#1a5276')
    ax.text(2.3, 1.9, "Hipotenusa $c = 5$", rotation=-36.8, fontsize=12,
            fontweight='bold', color='#922b21')
    ax.text(2, 3.5, r"$a^2 + b^2 = c^2$  →  $16 + 9 = 25$ ✅",
            ha='center', fontsize=13, fontweight='bold')

    ax.set_xlim(-2, 5.5); ax.set_ylim(-1, 4.5)
    ax.axis('off')
    ax.set_title("Teorema de Pitágoras: $3^2 + 4^2 = 5^2$", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🎬 Video 064 — Perímetro: El Cerco de Seguridad

Es la suma de **todos los lados** de una figura. Mide la longitud total del borde.

| Figura | Fórmula del Perímetro |
| :--- | :--- |
| **Cuadrado** | $P = 4 \cdot L$ |
| **Rectángulo** | $P = 2(L + A)$ |
| **Triángulo Equilátero** | $P = 3 \cdot L$ |
| **Polígono Irregular** | $P = $ suma de todos sus lados |
| **Circunferencia** | $P = 2\pi r$ |

---

### 🎬 Video 065 — Área: Control del Territorio

El área mide el **espacio interior** de una figura (en unidades cuadradas).

| Figura | Fórmula del Área |
| :--- | :--- |
| **Cuadrado** | $A = L^2$ |
| **Rectángulo** | $A = B \cdot h$ |
| **Triángulo** | $A = \dfrac{B \cdot h}{2}$ |
| **Trapecio** | $A = \dfrac{(B_1 + B_2) \cdot h}{2}$ |
| **Círculo** | $A = \pi r^2$ |

> **Statham Tip:** *"Seba, dile que no se olvide de dividir por 2 en el triángulo. Un triángulo es la mitad de un rectángulo; si no divide, está calculando el doble del territorio."*
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G02", expanded=False):
        st.markdown(r"""
### E01: Identificar tipo de triángulo

Un triángulo tiene ángulos de 90°, 40° y 50°.
* Suma: $90° + 40° + 50° = 180°$ ✅
* Tipo: **Rectángulo** (tiene un ángulo de 90°) y **Escaleno** (todos los ángulos y lados distintos).

---

### E02: Aplicar Pitágoras

En un triángulo rectángulo con catetos $a = 5$ y $b = 12$. ¿Cuánto mide la hipotenusa?

$$c = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$$

¡Es el trío $(5, 12, 13)$!

---

### E03: Calcular el perímetro de un rectángulo

Un rectángulo mide 8 cm de largo y 5 cm de ancho.

$$P = 2(8 + 5) = 2 \cdot 13 = 26 \text{ cm}$$

---

### E04: Calcular el área de un trapecio

Bases de 10 cm y 6 cm, altura de 4 cm.

$$A = \frac{(10 + 6) \cdot 4}{2} = \frac{16 \cdot 4}{2} = \frac{64}{2} = 32 \text{ cm}^2$$

---

### E05: Verificar desigualdad triangular

¿Pueden ser lados de un triángulo: 3, 5 y 9?

* $3 + 5 = 8 < 9$ ❌

**No** pueden formar un triángulo.
""")

    # ── QUIZ ────────────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario G02: Triángulos y Medidas", expanded=False):
        quiz = [
            {"question": "Un triángulo tiene ángulos de 60°, 60° y 60°. Es:",
             "options": {"A": "Isósceles y acutángulo", "B": "Equilátero y acutángulo", "C": "Escaleno y obtusángulo", "D": "Rectángulo e isósceles"},
             "answer": "B", "explanation": "3 ángulos iguales de 60° → equilátero. Los 3 son agudos → acutángulo."},
            {"question": r'En un triángulo rectángulo, los catetos miden 6 y 8. La hipotenusa mide:',
             "options": {"A": "10", "B": "14", "C": r"$\sqrt{28}$", "D": "100"},
             "answer": "A", "explanation": r"$\sqrt{6^2 + 8^2} = \sqrt{36+64} = \sqrt{100} = 10$. Trío 6-8-10 (múltiplo de 3-4-5)."},
            {"question": "¿Pueden ser lados de un triángulo: 4, 4 y 9?",
             "options": {"A": "Sí, forma un isósceles", "B": "No, viola la desigualdad triangular", "C": "Sí, forma un escaleno", "D": "No hay suficiente información"},
             "answer": "B", "explanation": "$4 + 4 = 8 < 9$. Los dos lados no superan al tercero."},
            {"question": "El perímetro de un cuadrado con lado 7 cm es:",
             "options": {"A": "14 cm", "B": "28 cm", "C": "49 cm", "D": "21 cm"},
             "answer": "B", "explanation": "$P = 4 \\times 7 = 28$ cm."},
            {"question": r'El área de un triángulo con base 10 m y altura 6 m es:',
             "options": {r"A": r"$60\ m^2$", "B": r"$30\ m^2$", "C": r"$15\ m^2$", "D": r"$120\ m^2$"},
             "answer": "B", "explanation": r"$A = \frac{10 \times 6}{2} = 30\ m^2$. No olvidar el divisor 2."},
            {"question": "Un rectángulo tiene largo 12 y ancho 4. Su perímetro es:",
             "options": {"A": "48", "B": "32", "C": "16", "D": "64"},
             "answer": "B", "explanation": r"$P = 2(12+4) = 2 \times 16 = 32$."},
            {"question": r'La hipotenusa de un triángulo rectángulo es 13. Un cateto es 5. El otro cateto mide:',
             "options": {"A": "8", "B": "12", "C": r"$\sqrt{8}$", "D": "18"},
             "answer": "B", "explanation": r"$b = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12$. Trío 5-12-13."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g02_quiz")

    # ── PAUTA ───────────────────────────────────────────────────────────────
    with st.expander("🔑 Pauta Técnica G02", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | 3 ángulos de 60° → equilátero. Todos agudos → acutángulo. |
| **2** | **A** | $\sqrt{36+64} = 10$. Múltiplo del trío 3-4-5. |
| **3** | **B** | $4+4=8 < 9$. No se cumple la desigualdad triangular. |
| **4** | **B** | $4 \times 7 = 28$ cm. |
| **5** | **B** | $\frac{10 \times 6}{2} = 30$. El triángulo es mitad del rectángulo. |
| **6** | **B** | $2(12+4) = 32$. |
| **7** | **B** | $\sqrt{169-25} = \sqrt{144} = 12$. Trío 5-12-13. |
""")
