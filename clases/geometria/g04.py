import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G04():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G04: Traslación, Reflexión, Rotación, Homotecia y Semejanza")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
### 🎬 Video 071 — Traslación

Mover una figura mediante un **vector $\vec{v}(a, b)$** es simplemente **sumar** ese vector a cada punto:

$$P(x, y) \;\longrightarrow\; P'(x+a,\; y+b)$$

* $a$: Movimiento horizontal (positivo = derecha).
* $b$: Movimiento vertical (positivo = arriba).

La figura resultante es **idéntica** a la original (misma forma, mismo tamaño, misma orientación).
""")

    # ── FIGURA: Traslación ───────────────────────────────────────────────────
    st.markdown("#### 📊 Traslación con vector $\\vec{v}(4, 2)$")
    fig, ax = plt.subplots(figsize=(8, 4.5))

    T_orig = np.array([[1, 1], [3, 1], [2, 3], [1, 1]])
    vector = np.array([4, 2])
    T_tras = T_orig + vector

    ax.plot(T_orig[:,0], T_orig[:,1], 'b-', linewidth=2.5, label='Original')
    ax.fill(T_orig[:-1,0], T_orig[:-1,1], color='#AED6F1', alpha=0.5)
    ax.plot(T_tras[:,0], T_tras[:,1], 'r-', linewidth=2.5, label="Trasladado P'")
    ax.fill(T_tras[:-1,0], T_tras[:-1,1], color='#FADBD8', alpha=0.5)
    ax.annotate("", xy=T_tras[2], xytext=T_orig[2],
                arrowprops=dict(arrowstyle="->", color="#1e8449", lw=2.5))
    ax.text(3.8, 4.2, r"$\vec{v}(4, 2)$", fontsize=13, fontweight='bold', color='#1e8449')

    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    ax.set_xlim(0, 8); ax.set_ylim(0, 6.5)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=11)
    ax.set_title("Traslación Isométrica", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🎬 Video 072 — Reflexión (Efecto Espejo)

La reflexión "voltea" la figura respecto a un **eje de simetría**.

**Reglas fundamentales:**

| Eje de Reflexión | Transformación del punto |
| :--- | :---: |
| Eje X (horizontal) | $(x,\; y) \;\to\; (x,\; -y)$ |
| Eje Y (vertical) | $(x,\; y) \;\to\; (-x,\; y)$ |

* La distancia de cada punto al eje de simetría se **conserva**.
* La figura se "invierte" como en un espejo.
""")

    # ── FIGURA: Reflexión ────────────────────────────────────────────────────
    st.markdown("#### 📊 Reflexión respecto al Eje Y")
    fig, ax = plt.subplots(figsize=(7, 4.5))

    T_orig = np.array([[2, 1], [4, 1], [3, 4], [2, 1]])
    T_refl = np.array([[-x, y] for x, y in T_orig])

    ax.plot(T_orig[:,0], T_orig[:,1], 'b-', linewidth=2.5, label='Original')
    ax.fill(T_orig[:-1,0], T_orig[:-1,1], color='#AED6F1', alpha=0.5)
    ax.plot(T_refl[:,0], T_refl[:,1], 'g-', linewidth=2.5, label='Reflejado')
    ax.fill(T_refl[:-1,0], T_refl[:-1,1], color='#D5F5E3', alpha=0.5)

    for i in range(3):
        ax.plot([T_orig[i,0], T_refl[i,0]], [T_orig[i,1], T_refl[i,1]], 'k--', alpha=0.3)

    ax.axvline(0, color='#e74c3c', linewidth=2.5, label='Eje de Simetría (Y)')
    ax.axhline(0, color='black', lw=0.8)
    ax.set_xlim(-5, 5); ax.set_ylim(0, 5.5)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=11)
    ax.set_title("Reflexión respecto al Eje Y", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🎬 Video 073 — Rotación (Giro)

Girar una figura un ángulo $\theta$ alrededor del **origen $(0,0)$**, en sentido antihorario:

| Ángulo | Punto Original | Punto Rotado |
| :---: | :---: | :---: |
| **90°** | $(x,\; y)$ | $(-y,\; x)$ |
| **180°** | $(x,\; y)$ | $(-x,\; -y)$ |
| **270°** | $(x,\; y)$ | $(y,\; -x)$ |

**Truco mental:** Para 90° antihorario, simplemente **intercambia** las coordenadas y cambia el signo a la primera.

---

### 🎬 Video 074 — Homotecia (Cambio de Escala)

La homotecia multiplica todas las distancias desde un centro por una **razón $k$**. **Cambia el tamaño** de la figura.

* Si $|k| > 1$: La figura se **amplía**.
* Si $0 < |k| < 1$: La figura se **reduce**.
* Si $k < 0$: La figura se **invierte** respecto al centro.

**Fórmula:** $P'(x, y) \to P'(k \cdot x,\; k \cdot y)$ (cuando el centro es el origen).

**Efecto en las medidas:**

| Magnitud | Escala | Factor |
| :--- | :---: | :---: |
| Longitudes | $k$ | Lineal |
| Áreas | $k^2$ | Cuadrático |
| Volúmenes | $k^3$ | Cúbico |

---

### 🎬 Video 075 — Semejanza

Dos figuras son **semejantes** ($\sim$) si:
1. Sus **ángulos** correspondientes son iguales.
2. Sus **lados homólogos** son proporcionales (tienen la misma razón $k$).

La homotecia produce figuras semejantes. Las isometrías producen figuras **congruentes** (caso especial de semejanza con $k=1$).

> **Statham Tip:** *"Semejante es como ver la misma foto en una pantalla más grande. Todo encaja, solo cambia el zoom."*
""")

    # ── FIGURA: Semejanza ────────────────────────────────────────────────────
    st.markdown("#### 📊 Semejanza y Escala ($k = 2$)")
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot([0, 2, 0, 0], [0, 0, 3, 0], 'r-', lw=2.5)
    ax.fill([0, 2, 0], [0, 0, 3], color='#FADBD8', alpha=0.5)
    ax.text(1, -0.4, "2", color='#922b21', fontsize=13, ha='center', fontweight='bold')
    ax.text(-0.35, 1.5, "3", color='#922b21', fontsize=13, va='center', fontweight='bold')
    ax.text(1, 1.2, "Área = 3", color='#922b21', ha='center', fontsize=11)

    ax.plot([4, 8, 4, 4], [0, 0, 6, 0], 'b-', lw=2.5)
    ax.fill([4, 8, 4], [0, 0, 6], color='#AED6F1', alpha=0.5)
    ax.text(6, -0.4, "4", color='#1a5276', fontsize=13, ha='center', fontweight='bold')
    ax.text(3.5, 3, "6", color='#1a5276', fontsize=13, va='center', fontweight='bold')
    ax.text(5.7, 3, "Área = 12\n($k^2 = 4$ veces)", color='#1a5276', ha='center', fontsize=11)

    ax.annotate("", xy=(3.8, 2), xytext=(2.2, 1),
                arrowprops=dict(arrowstyle="->", color='#1e8449', lw=2))
    ax.text(2.7, 1.8, "$k=2$", color='#1e8449', fontsize=12, fontweight='bold')

    ax.set_xlim(-1, 9); ax.set_ylim(-1, 7)
    ax.axis('off')
    ax.set_title("Semejanza: Los lados escalan por $k$, las áreas por $k^2$", fontsize=13, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown('</div>', unsafe_allow_html=True)

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G04", expanded=False):
        st.markdown(r"""
### E01: Traslación de un punto

$P(3, -1)$ trasladado por $\vec{v}(2, 5)$:

$$P' = (3+2,\; -1+5) = P'(5, 4)$$

---

### E02: Reflexión respecto al Eje X

$Q(4, -3)$ reflejado respecto al Eje X:

$$Q' = (4,\; -(-3)) = Q'(4, 3)$$

El signo de $y$ cambia; $x$ queda igual.

---

### E03: Rotación de 90° antihoraria

$R(5, 2)$ rotado 90° antihorario:

$$R' = (-2,\; 5)$$

Regla: $(x, y) \to (-y, x)$.

---

### E04: Homotecia con $k = 3$

El triángulo original tiene lados de 2, 3 y 4 cm, y área $= 6$ cm².

Con $k = 3$:
* Lados nuevos: $6, 9, 12$ cm (multiplicados por $k$).
* Área nueva: $6 \times 3^2 = 6 \times 9 = 54$ cm² (multiplicada por $k^2$).

---

### E05: Triángulos semejantes

Dos triángulos tienen lados $3, 4, 5$ y $6, 8, 10$. ¿Son semejantes?

Razón: $6/3 = 8/4 = 10/5 = 2$. La razón es constante ($k=2$). **Sí son semejantes.**
""")

    # ── QUIZ ────────────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario G04: Transformaciones y Semejanza", expanded=False):
        quiz = [
            {"question": r'El punto $P(3, 5)$ se traslada con $\vec{v}(-2, 4)$. Las nuevas coordenadas son:',
             "options": {"A": r"$(1, 9)$", "B": r"$(5, 1)$", "C": r"$(1, 1)$", "D": r"$(-6, 20)$"},
             "answer": "A", "explanation": r"$P' = (3-2,\; 5+4) = (1, 9)$."},
            {"question": r'El punto $Q(-4, 3)$ se refleja respecto al Eje X. Las nuevas coordenadas son:',
             "options": {"A": r"$(4, 3)$", "B": r"$(-4, -3)$", "C": r"$(4, -3)$", "D": r"$(-4, 3)$"},
             "answer": "B", "explanation": r"Reflexión en Eje X: $(x, y) \to (x, -y)$. $Q'(-4, -3)$."},
            {"question": r'El punto $R(2, -5)$ se refleja respecto al Eje Y. Las nuevas coordenadas son:',
             "options": {"A": r"$(2, 5)$", "B": r"$(-2, -5)$", "C": r"$(-2, 5)$", "D": r"$(2, -5)$"},
             "answer": "B", "explanation": r"Reflexión en Eje Y: $(x, y) \to (-x, y)$. $R'(-2, -5)$."},
            {"question": r'El punto $P(4, 1)$ se rota 90° antihorario. Las nuevas coordenadas son:',
             "options": {"A": r"$(1, 4)$", "B": r"$(-1, 4)$", "C": r"$(4, -1)$", "D": r"$(-4, -1)$"},
             "answer": "B", "explanation": r"Rotación 90°: $(x, y) \to (-y, x) = (-1, 4)$."},
            {"question": r'Una figura tiene área 8 cm². Se aplica homotecia con $k = 4$. El área de la imagen es:',
             "options": {"A": r"$32\ \text{cm}^2$", "B": r"$128\ \text{cm}^2$", "C": r"$64\ \text{cm}^2$", "D": r"$16\ \text{cm}^2$"},
             "answer": "B", "explanation": r"El área escala por $k^2 = 16$. $8 \times 16 = 128$ cm²."},
            {"question": r'Dos triángulos tienen lados $5, 6, 7$ y $10, 12, 15$. ¿Son semejantes?',
             "options": {"A": "Sí, con $k=2$", "B": "No, las razones no son iguales", "C": "Sí, con $k=3$", "D": "No hay suficiente información"},
             "answer": "B", "explanation": r"$10/5=2$, $12/6=2$, pero $15/7 \neq 2$. Las razones no son consistentes."},
            {"question": r'Una figura se rota 180° alrededor del origen. El punto $P(3, -2)$ queda en:',
             "options": {"A": r"$(2, 3)$", "B": r"$(-3, 2)$", "C": r"$(3, 2)$", "D": r"$(-2, -3)$"},
             "answer": "B", "explanation": r"Rotación 180°: $(x, y) \to (-x, -y) = (-3, 2)$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g04_quiz")

    # ── PAUTA ───────────────────────────────────────────────────────────────
    with st.expander("🔑 Pauta Técnica G04", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **A** | $P' = (3+(-2),\; 5+4) = (1, 9)$. |
| **2** | **B** | Eje X: solo cambia el signo de $y$. $(-4, -3)$. |
| **3** | **B** | Eje Y: solo cambia el signo de $x$. $(-2, -5)$. |
| **4** | **B** | 90° antihorario: $(x,y) \to (-y, x) = (-1, 4)$. |
| **5** | **B** | Área escala por $k^2 = 16$. $8 \times 16 = 128$ cm². |
| **6** | **B** | $10/5=2$, $12/6=2$, $15/7 \approx 2{,}14$. Las razones no son iguales. |
| **7** | **B** | 180°: $(x, y) \to (-x, -y) = (-3, 2)$. |
""")
