import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G03():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G03: Círculo, Cuerpos en 3D y Transformaciones")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
### 🎬 Video 066 — Círculo y Circunferencia

**Conceptos clave:**
* **Radio ($r$):** Distancia del centro a cualquier punto del borde.
* **Diámetro ($d = 2r$):** Cruza de lado a lado por el centro.
* **Pi ($\pi \approx 3{,}14$):** La constante que relaciona el perímetro con el diámetro.

| Medida | Fórmula | Concepto |
| :--- | :---: | :--- |
| **Perímetro** | $2\pi r$ | La longitud del borde (la cuerda del cerco). |
| **Área** | $\pi r^2$ | El espacio interior del círculo. |

> **Statham Tip:** *"Seba, dile al alumno que no confunda $r^2$ con $2r$. Un error ahí y el área se convierte en perímetro. Fatal."*

---

### 🎬 Video 067 — Partes del Círculo (Arco y Sector)

**Arco de Circunferencia:** Es un trozo del borde. Depende del ángulo central $\alpha$:

$$L_{arco} = \frac{2\pi r \cdot \alpha}{360°}$$

**Sector Circular:** La "rebanada de pizza". Su área:

$$A_{sector} = \frac{\pi r^2 \cdot \alpha}{360°}$$

**Clave:** Tanto el arco como el sector son proporcionales al ángulo. Si $\alpha = 180°$, obtienes exactamente la **mitad**.

---

### 🎬 Video 068 — Prismas y Cubos

**Volumen de un Prisma Recto:**
$$V = \text{Área de la base} \times \text{Altura}$$

**El Cubo (Hexaedro Regular):** Las 6 caras son cuadrados iguales de lado $a$.

| Medida | Fórmula |
| :--- | :---: |
| Volumen | $a^3$ |
| Área Total | $6a^2$ |

---

### 🎬 Video 069 — El Cilindro

Un cilindro tiene dos **bases circulares** y una **cara lateral curva** (como una lata de bebida).

| Medida | Fórmula | Intuición |
| :--- | :---: | :--- |
| **Volumen** | $\pi r^2 h$ | Base circular × altura |
| **Área Lateral** | $2\pi r h$ | Un rectángulo "enrollado" |
| **Área Total** | $2\pi r h + 2\pi r^2$ | Lateral + 2 tapas |
""")

    # ── FIGURA: Cono vs Cilindro ─────────────────────────────────────────────
    st.markdown("#### 📊 Relación entre el Cono y el Cilindro")
    fig, ax = plt.subplots(figsize=(6, 5))

    # Cilindro (contorno azul)
    ax.add_patch(plt.Rectangle((-2, 0), 4, 5, edgecolor='#1a5276', facecolor='none', lw=2.5, linestyle='--'))
    ax.text(2.3, 2.5, "Cilindro\n$V = \\pi r^2 h$", color='#1a5276', fontsize=11)

    # Cono inscrito
    ax.fill([-2, 2, 0], [0, 0, 5], color='#f39c12', alpha=0.5)
    ax.plot([-2, 2, 0, -2], [0, 0, 5, 0], 'k-', lw=2)
    ax.text(0, 2, "Cono\n$V=\\frac{1}{3}\\pi r^2 h$", ha='center', va='center',
            fontweight='bold', fontsize=12)

    ax.text(0, -0.6, r"El cono = $\frac{1}{3}$ del cilindro con misma base y altura",
            ha='center', fontsize=11, color='#922b21', fontweight='bold')

    ax.set_xlim(-3.5, 5); ax.set_ylim(-1, 6)
    ax.axis('off')
    ax.set_title("Volúmenes: Cilindro y Cono Inscrito", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🎬 Video 070 — Transformaciones Isométricas: Introducción

Una **isometría** es un movimiento que **conserva la forma y el tamaño** de la figura. La figura original y su imagen son **congruentes**.

Los tres tipos de isometrías son:
1. **Traslación:** Se desplaza la figura. No cambia orientación.
2. **Reflexión (Simetría):** Se "voltea" la figura. Produce imagen espejo.
3. **Rotación:** Se gira la figura alrededor de un punto.

> **Statham Tip:** *"Isométrico significa 'igual medida'. Si la figura se achica o se agranda, ya no es isometría. No dejes que te engañen."*

**Diferencia clave:** La **Homotecia** (próxima clase) también mueve la figura, pero cambia su tamaño → **NO es isometría**.
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G03", expanded=False):
        st.markdown(r"""
### E01: Área y perímetro del círculo

Una rueda tiene radio $r = 7$ cm. Calcular perímetro y área.

* $P = 2 \pi r = 2 \times 3{,}14 \times 7 = 43{,}96$ cm
* $A = \pi r^2 = 3{,}14 \times 49 = 153{,}86$ cm²

---

### E02: Sector circular (rebanada de pizza)

Sector con $r = 6$ y ángulo $\alpha = 90°$.

* $L_{arco} = \dfrac{2\pi \times 6 \times 90}{360} = \dfrac{1080\pi}{360} = 3\pi \approx 9{,}42$
* $A_{sector} = \dfrac{\pi \times 36 \times 90}{360} = 9\pi \approx 28{,}27$

---

### E03: Volumen del cubo

Un cubo de arista $a = 4$ cm.

* $V = 4^3 = 64$ cm³
* $A_T = 6 \times 4^2 = 6 \times 16 = 96$ cm²

---

### E04: Volumen del cilindro

Cilindro con $r = 3$ cm y $h = 10$ cm.

$$V = \pi r^2 h = \pi \times 9 \times 10 = 90\pi \approx 282{,}7 \text{ cm}^3$$

---

### E05: ¿Isometría o no?

| Transformación | ¿Isometría? |
| :--- | :---: |
| Traslación de 5 unidades | ✅ Sí |
| Ampliar la figura al doble | ❌ No (cambia el tamaño) |
| Reflexión respecto al eje X | ✅ Sí |
| Homotecia con $k = 3$ | ❌ No |
""")

    # ── QUIZ ────────────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario G03: Círculo, 3D e Isometrías", expanded=False):
        quiz = [
            {"question": r'Un círculo tiene radio $r = 5$. Su área es:',
             "options": {"A": r"$10\pi$", "B": r"$25\pi$", "C": r"$5\pi$", "D": r"$50\pi$"},
             "answer": "B", "explanation": r"$A = \pi r^2 = \pi \times 25 = 25\pi$."},
            {"question": r'El perímetro de un círculo con diámetro 10 es:',
             "options": {"A": r"$5\pi$", "B": r"$20\pi$", "C": r"$10\pi$", "D": r"$100\pi$"},
             "answer": "C", "explanation": r"$d = 10 \Rightarrow r = 5$. $P = 2\pi r = 10\pi$."},
            {"question": r'Un sector circular tiene $r = 6$ y ángulo de 180°. Su área es:',
             "options": {"A": r"$36\pi$", "B": r"$18\pi$", "C": r"$12\pi$", "D": r"$6\pi$"},
             "answer": "B", "explanation": r"$A = \frac{\pi \times 36 \times 180}{360} = 18\pi$. Es la mitad del círculo."},
            {"question": r'Un cubo tiene arista 3 cm. Su volumen es:',
             "options": {"A": "9 cm³", "B": "54 cm³", "C": "27 cm³", "D": "18 cm³"},
             "answer": "C", "explanation": r"$V = 3^3 = 27$ cm³."},
            {"question": r'Un cubo tiene arista 3 cm. Su área total (todas las caras) es:',
             "options": {"A": "54 cm²", "B": "18 cm²", "C": "27 cm²", "D": "36 cm²"},
             "answer": "A", "explanation": r"$A_T = 6 \times 3^2 = 6 \times 9 = 54$ cm²."},
            {"question": "¿Cuál de estas transformaciones NO es una isometría?",
             "options": {"A": "Traslación", "B": "Reflexión", "C": "Homotecia", "D": "Rotación"},
             "answer": "C", "explanation": "La homotecia cambia el tamaño de la figura. Las isometrías conservan forma Y tamaño."},
            {"question": r'Un cilindro tiene $r=2$ y $h=5$. Su volumen es:',
             "options": {"A": r"$40\pi$", "B": r"$20\pi$", "C": r"$10\pi$", "D": r"$4\pi$"},
             "answer": "B", "explanation": r"$V = \pi r^2 h = \pi \times 4 \times 5 = 20\pi$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g03_quiz")

    # ── PAUTA ───────────────────────────────────────────────────────────────
    with st.expander("🔑 Pauta Técnica G03", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $A = \pi r^2 = 25\pi$. No confundir con $2\pi r$. |
| **2** | **C** | $r = d/2 = 5$. $P = 2\pi \times 5 = 10\pi$. |
| **3** | **B** | 180° = mitad del círculo → $\frac{36\pi}{2} = 18\pi$. |
| **4** | **C** | $V = 3^3 = 27$ cm³. |
| **5** | **A** | $A_T = 6 \times 9 = 54$ cm². El cubo tiene 6 caras. |
| **6** | **C** | La homotecia escala la figura. Las isometrías no cambian el tamaño. |
| **7** | **B** | $V = \pi \times 4 \times 5 = 20\pi$. |
""")
