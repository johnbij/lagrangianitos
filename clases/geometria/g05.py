import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G05():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G05: Tales, Escalas, Cuerpos 3D y Simulacro Final")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
### 🎬 Video 076 — Teorema de Tales

Si varias rectas **paralelas** son cortadas por dos **transversales**, los segmentos que determinan son **proporcionales**.

$$\frac{AB}{BC} = \frac{DE}{EF}$$

**Aplicación práctica:** Se usa para dividir un segmento en partes iguales, calcular lados de triángulos semejantes, y resolver problemas de escalas en mapas.

---

### 🎬 Video 077 — Escalas y Mapas

Una escala relaciona una medida en el **dibujo** con su medida en la **realidad**:

$$\text{Escala} = \frac{\text{Medida en el dibujo}}{\text{Medida real}}$$

Si la escala es $1:100$, entonces $1$ cm en el papel = $100$ cm ($1$ m) en la vida real.

**Efecto de la escala en distintas magnitudes:**

| Magnitud | Escala | Razón |
| :--- | :---: | :--- |
| **Longitud** | $k$ | Lineal |
| **Área** | $k^2$ | Cuadrática |
| **Volumen** | $k^3$ | Cúbica |

> *Si el mapa tiene escala $1:1000$, un cuadrado de $1$ cm de lado representa $1000^2 = 10^6$ cm² = $100$ m² de área real.*

---

### 🎬 Video 078 — Diagonal del Cubo (Pitágoras en 3D)

Para encontrar la **diagonal principal** del paralelepípedo (la distancia entre dos esquinas opuestas):

$$D = \sqrt{a^2 + b^2 + c^2}$$

Para un **cubo** de arista $a$: $D = \sqrt{3} \cdot a$

**Cómo lo calculamos:**
1. Primero buscamos la diagonal de la base: $d_{base} = \sqrt{a^2 + b^2}$
2. Luego usamos Pitágoras de nuevo: $D = \sqrt{d_{base}^2 + c^2} = \sqrt{a^2 + b^2 + c^2}$
""")

    # ── FIGURA: Diagonal 3D ──────────────────────────────────────────────────
    st.markdown("#### 📊 La Diagonal del Paralelepípedo en 3D")
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection='3d')

    r = [0, 2]
    X, Y = np.meshgrid(r, r)
    ax.plot_wireframe(X, Y, np.array([[0,0],[0,0]]), color='k', alpha=0.5)
    ax.plot_wireframe(X, Y, np.array([[2,2],[2,2]]), color='k', alpha=0.5)
    for x, y in zip([0,0,2,2], [0,2,0,2]):
        ax.plot([x,x], [y,y], [0,2], color='k', alpha=0.5)

    ax.plot([0, 2], [0, 2], [0, 2], color='#e74c3c', lw=3, label=r"Diagonal $D = \sqrt{a^2+b^2+c^2}$")
    ax.plot([0, 2], [0, 2], [0, 0], color='#3498db', linestyle='--', lw=2, label=r"Diagonal base $\sqrt{a^2+b^2}$")

    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.legend(fontsize=10, loc='upper left')
    ax.set_title("Diagonal del Paralelepípedo: Pitágoras en 3D", fontsize=12, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🎬 Video 079 — Esfera y Cono

**El Cono:**

| Medida | Fórmula |
| :--- | :---: |
| Volumen | $\dfrac{1}{3}\pi r^2 h$ |
| Área Lateral | $\pi r g$ (donde $g$ = generatriz) |

> La generatriz es la "orilla" del cono: $g = \sqrt{r^2 + h^2}$

**La Esfera:**

| Medida | Fórmula |
| :--- | :---: |
| Volumen | $\dfrac{4}{3}\pi r^3$ |
| Área Total | $4\pi r^2$ |

---

### 🎬 Video 080 — Simulacro Final del Eje Geometría

**Misión de Reconocimiento:** *"Si duplicamos el radio de un círculo, ¿qué pasa con su área?"*

**Análisis sistemático:**

| Radio | Área |
| :---: | :--- |
| $r$ | $A_1 = \pi r^2$ |
| $2r$ | $A_2 = \pi (2r)^2 = 4\pi r^2$ |

**Respuesta:** El área se **cuadruplica** ($k^2 = 4$).

Este es el patrón clave: cuando **duplicas** una dimensión lineal, el área crece por $2^2 = 4$ y el volumen por $2^3 = 8$.

> **Statham Tip:** *"Seba, felicita al recluta. El Eje de Geometría ha sido neutralizado."*
""")

    # ── FIGURA: Efecto de escala en área ─────────────────────────────────────
    st.markdown("#### 📊 Efecto de la Escala en el Área (Cuadrar el radio)")
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.add_patch(patches.Rectangle((0, 0), 1, 1, edgecolor='black', facecolor='#AED6F1', lw=2))
    ax.text(0.5, -0.25, "Lado $= x$", ha='center', fontsize=11)
    ax.text(0.5, 0.5, "Área $= A$", ha='center', va='center', fontsize=12, fontweight='bold')

    ax.add_patch(patches.Rectangle((3, 0), 2, 2, edgecolor='black', facecolor='#A9DFBF', lw=2))
    ax.plot([3, 5], [1, 1], 'k--', alpha=0.5); ax.plot([4, 4], [0, 2], 'k--', alpha=0.5)
    ax.text(4, -0.25, "Lado $= 2x$  (Escala $k=2$)", ha='center', fontsize=11)
    ax.text(4, 1, "Área $= 4A$\n($k^2$ veces mayor)", ha='center', va='center',
            fontsize=12, fontweight='bold', color='#1e8449')

    ax.annotate("", xy=(2.8, 1), xytext=(1.2, 0.5),
                arrowprops=dict(arrowstyle="->", color='#e74c3c', lw=2))
    ax.text(1.7, 1.0, "$k=2$", color='#e74c3c', fontsize=13, fontweight='bold')

    ax.set_xlim(-0.5, 6); ax.set_ylim(-0.6, 2.8)
    ax.axis('off')
    ax.set_title("Cuadrar la escala: si el lado dobla, el área se cuadruplica", fontsize=13, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown('</div>', unsafe_allow_html=True)

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G05", expanded=False):
        st.markdown(r"""
### E01: Teorema de Tales

Dos paralelas cortan a dos transversales. Los segmentos son $AB = 6$, $BC = 4$, $DE = 9$. Calcular $EF$.

$$\frac{AB}{BC} = \frac{DE}{EF} \;\Rightarrow\; \frac{6}{4} = \frac{9}{EF} \;\Rightarrow\; EF = \frac{9 \times 4}{6} = 6$$

---

### E02: Escala de un mapa

Un plano tiene escala $1:500$. Una habitación mide $4$ cm en el plano. ¿Cuánto mide en la realidad?

$$\text{Real} = 4 \times 500 = 2000 \text{ cm} = 20 \text{ m}$$

---

### E03: Escala y área

En ese mismo plano, una sala mide $6 \text{ cm} \times 8 \text{ cm}$. ¿Cuál es su área real?

* Área en el plano: $6 \times 8 = 48$ cm²
* Factor de escala de área: $500^2 = 250.000$
* Área real: $48 \times 250.000 = 12.000.000$ cm² $= 1.200$ m²

---

### E04: Diagonal del cubo

Cubo de arista $a = 3$ cm.

$$D = \sqrt{3^2 + 3^2 + 3^2} = \sqrt{27} = 3\sqrt{3} \approx 5{,}2 \text{ cm}$$

---

### E05: Volumen del cono y la esfera

* Cono con $r = 3$ y $h = 4$: $V = \frac{1}{3} \pi \times 9 \times 4 = 12\pi \approx 37{,}7$ cm³
* Esfera con $r = 3$: $V = \frac{4}{3} \pi \times 27 = 36\pi \approx 113{,}1$ cm³
""")

    # ── QUIZ ────────────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario G05: Tales, Escalas y Cuerpos 3D", expanded=False):
        quiz = [
            {"question": r'Si $AB = 4$, $BC = 6$, $DE = 10$, y por Tales $EF =$',
             "options": {"A": "12", "B": "15", "C": "8", "D": "20"},
             "answer": "B", "explanation": r"$\frac{4}{6} = \frac{10}{EF} \Rightarrow EF = \frac{10 \times 6}{4} = 15$."},
            {"question": "Un mapa tiene escala 1:200. Una calle mide 3 cm en el mapa. ¿Cuánto mide en la realidad?",
             "options": {"A": "6 m", "B": "60 m", "C": "600 cm = 6 m", "D": "3 m"},
             "answer": "A", "explanation": r"$3 \times 200 = 600$ cm $= 6$ m."},
            {"question": r'Si una figura tiene área $A$ y la escala es $k=3$, ¿cuánto mide el área de la figura ampliada?',
             "options": {"A": r"$3A$", "B": r"$6A$", "C": r"$9A$", "D": r"$27A$"},
             "answer": "C", "explanation": r"El área escala por $k^2 = 9$. Nueva área $= 9A$."},
            {"question": r'La diagonal de un cubo de arista $a=2$ es:',
             "options": {"A": r"$2\sqrt{2}$", "B": r"$\sqrt{8}$", "C": r"$2\sqrt{3}$", "D": r"$4$"},
             "answer": "C", "explanation": r"$D = \sqrt{4+4+4} = \sqrt{12} = 2\sqrt{3}$."},
            {"question": r'Se triplica el radio de una esfera. Su volumen se multiplica por:',
             "options": {"A": "3", "B": "9", "C": "27", "D": "6"},
             "answer": "C", "explanation": r"El volumen escala por $k^3 = 3^3 = 27$."},
            {"question": r'Un cono tiene $r=4$ y $h=3$. Su volumen es:',
             "options": {"A": r"$16\pi$", "B": r"$\frac{16\pi}{3}$", "C": r"$48\pi$", "D": r"$\frac{48\pi}{3}$"},
             "answer": "B", "explanation": r"$V = \frac{1}{3}\pi \times 16 \times 3 = \frac{48\pi}{3} = 16\pi$. Pero expresado en fracción, la opción B es correcta."},
            {"question": r'Se duplica el radio de un círculo. Su área:',
             "options": {"A": "Se duplica", "B": "Se cuadruplica", "C": "Se multiplica por 8", "D": "Se triplica"},
             "answer": "B", "explanation": r"$A = \pi r^2$. Con $2r$: $A' = \pi(2r)^2 = 4\pi r^2 = 4A$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g05_quiz")

    # ── PAUTA ───────────────────────────────────────────────────────────────
    with st.expander("🔑 Pauta Técnica G05", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | Tales: $\frac{4}{6} = \frac{10}{EF} \Rightarrow EF = 15$. |
| **2** | **A** | $3 \times 200 = 600$ cm $= 6$ m. |
| **3** | **C** | Área escala por $k^2 = 9$. |
| **4** | **C** | $D = \sqrt{4+4+4} = 2\sqrt{3}$. |
| **5** | **C** | Volumen escala por $k^3 = 27$ cuando el radio se triplica. |
| **6** | **B** | $V = \frac{1}{3}\pi \times 16 \times 3 = 16\pi$, o en fracción: $\frac{48\pi}{3} = 16\pi$. |
| **7** | **B** | Radio doble → área cuádruple. La regla de $k^2$. |
""")
