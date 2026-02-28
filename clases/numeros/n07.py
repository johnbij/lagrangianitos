import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def render_N07():
    st.title("N07: Los Números Reales (ℝ) — La Recta Numérica Completa")

    # ── PORTAL ──────────────────────────────────────────────────────────────
    st.header("🛡️ 1. El Portal: El Mapa del Tesoro Completo")
    st.markdown(r"""
Imagínate que hasta ahora estábamos explorando el mapa de una isla, pero solo veíamos los
árboles (Naturales) o los senderos (Racionales). Los **Números Reales** son la isla completa,
con cada grano de arena y cada gota de agua.

Históricamente, la matemática pasó siglos intentando "tapar los hoyos" de la recta numérica.
Cuando por fin unimos a los Racionales con los Irracionales, logramos la **Continuidad**.
Si tiras un dardo a la recta numérica, no importa dónde caiga, **SIEMPRE** vas a clavar un
Número Real. No hay vacíos.
""")

    # ── FIGURA: DIAGRAMA DE CONJUNTOS ────────────────────────────────────────
    st.subheader("📊 La Jerarquía de los Conjuntos Numéricos")
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')

    conjuntos = [
        (5, 3.5, 4.5, 3.0, '#1565C0', 'ℝ  Reales', 0.3),
        (4.2, 3.5, 3.2, 2.2, '#2E7D32', 'ℚ  Racionales', 0.3),
        (3.7, 3.5, 2.0, 1.4, '#F57F17', 'ℤ  Enteros', 0.3),
        (3.5, 3.5, 1.2, 0.85, '#c0392b', 'ℕ₀', 0.25),
        (3.5, 3.5, 0.6, 0.42, '#7b1fa2', 'ℕ', 0.2),
    ]

    for cx, cy, w, h, color, label, alpha in conjuntos:
        ellipse = mpatches.Ellipse((cx, cy), w*2, h*2,
                                    edgecolor=color, facecolor=color,
                                    alpha=alpha, linewidth=2.5)
        ax.add_patch(ellipse)

    # Etiquetas
    ax.text(8.5, 6.2, "ℝ", fontsize=16, color='#1565C0', fontweight='bold')
    ax.text(7.0, 5.5, "ℚ", fontsize=14, color='#2E7D32', fontweight='bold')
    ax.text(6.0, 4.5, "ℤ", fontsize=13, color='#F57F17', fontweight='bold')
    ax.text(4.9, 3.9, "ℕ₀", fontsize=11, color='#c0392b', fontweight='bold')
    ax.text(3.5, 3.5, "ℕ", fontsize=10, color='#7b1fa2', fontweight='bold', ha='center', va='center')

    # Irracionales fuera del círculo de ℚ
    ax.text(1.0, 5.8, "ℐ  Irracionales", fontsize=11, color='#880E4F', fontweight='bold')
    ax.text(1.0, 5.3, "π, e, φ, √2...", fontsize=9, color='#880E4F')
    ax.annotate('', xy=(2.0, 4.8), xytext=(1.8, 5.2),
                arrowprops=dict(arrowstyle='->', color='#880E4F', lw=1.5))

    ax.axis('off')
    plt.title("Jerarquía: ℕ ⊂ ℕ₀ ⊂ ℤ ⊂ ℚ ⊂ ℝ  y  ℐ ⊂ ℝ", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # ── ESTRUCTURA ──────────────────────────────────────────────────────────
    st.header("🛡️ 7.1 La Recta Numérica Continua")
    st.markdown(r"""
$$\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$$

- **Unión final:** Racionales + Irracionales = Reales.
- **Disjuntos:** Un número no puede estar en crisis de identidad. O es $\mathbb{Q}$ o es $\mathbb{I}$.
  La intersección es vacía: $\mathbb{Q} \cap \mathbb{I} = \emptyset$.
""")

    # ── ZONAS DE PELIGRO ────────────────────────────────────────────────────
    st.header("🛡️ 7.2 ¿Qué NO es un Real? (Zonas de Peligro PAES)")
    st.markdown(r"""
| Expresión | Tipo | Razón |
|:---|:---:|:---|
| $\sqrt{-4}$ | ❌ No Real | Raíz par de base negativa → número **Imaginario** |
| $k / 0$ | ❌ No Real | División por cero → **Indefinición** |
""")
    st.error("🚨 **Trampa clásica PAES:** $\\sqrt{-9}$, $5/0$, $\\sqrt{-1}$ no son números reales.")

    # ── AXIOMAS ─────────────────────────────────────────────────────────────
    st.header("🛡️ 7.3 El Rigor Técnico: Axiomas y Cuerpo")
    st.markdown(r"""
- **Axioma:** Verdad absoluta que no requiere demostración. Regla de oro aceptada para construir todo lo demás.
- **Cuerpo:** Estructura matemática donde suma y multiplicación se portan "bien" (mientras no dividas por cero).
""")
    st.info("💡 **Tip:** Los axiomas son como las leyes de la física en un videojuego. No preguntas por qué funciona la gravedad, simplemente saltas. En la PAES, cuando despejas una ecuación, usas estos axiomas sin darte cuenta.")

    # ── TABLA DE AXIOMAS ────────────────────────────────────────────────────
    st.header("🛡️ 7.4 Los Axiomas de Cuerpo de los Reales")
    st.markdown(r"""
Para cualquier $a, b, c \in \mathbb{R}$:

| Propiedad | Suma (+) | Multiplicación (×) |
|:---|:---|:---|
| **Clausura** | $a + b \in \mathbb{R}$ | $a \cdot b \in \mathbb{R}$ |
| **Conmutatividad** | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| **Asociatividad** | $a + (b+c) = (a+b) + c$ | $a(bc) = (ab)c$ |
| **Neutro** | $a + 0 = a$ | $a \cdot 1 = a$ |
| **Inverso** | $a + (-a) = 0$ | $a \cdot \frac{1}{a} = 1\;(a \neq 0)$ |
| **Distributividad** | \multicolumn{2}{|c|} $a(b+c) = ab + ac$ |
""")

    st.markdown("""
---
> *"Las leyes de la matemática no son meras invenciones humanas, son la descripción de la estructura misma de la realidad."*
> — **Roger Penrose**
""")

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Carpintería de Ejemplos N07", expanded=False):
        st.markdown(r"""
### E02: El Filtro de la Realidad
Clasificar: $\sqrt{25}$, $\sqrt{-25}$, $0/7$, $7/0$

| Número | Resultado | ¿Es Real? | Razón |
|:---|:---:|:---:|:---|
| $\sqrt{25}$ | 5 | ✅ SÍ | Raíz de base positiva |
| $\sqrt{-25}$ | $5i$ | ❌ NO | Raíz par de base negativa |
| $0/7$ | 0 | ✅ SÍ | El cero es real |
| $7/0$ | $\nexists$ | ❌ NO | Indefinición |

---
### E03: Inversos
- **Inverso aditivo de -3:** es $3$ porque $-3 + 3 = 0$
- **Inverso multiplicativo de 2/5:** es $5/2$ porque $\frac{2}{5} \cdot \frac{5}{2} = 1$

---
### E04: Identificar Axioma
$3(x + 4) = 3x + 12$ → **Distributividad**

---
### E05: Neutros en acción
$\pi \cdot 1 + (5 + (-5))$

| Paso | Operación | Axioma |
|:---|:---:|:---|
| 1 | $\pi \cdot 1 = \pi$ | Neutro multiplicativo |
| 2 | $5 + (-5) = 0$ | Inverso aditivo |
| 3 | $\pi + 0 = \pi$ | Neutro aditivo |

**Resultado: $\pi$**

---
### E06: Clasificación Específica de -4

| Conjunto | ¿Pertenece? | Razón |
|:---|:---:|:---|
| $\mathbb{N}$ | ❌ No | Es negativo |
| $\mathbb{Z}$ | ✅ Sí | Valor exacto sin decimales |
| $\mathbb{Q}$ | ✅ Sí | Se escribe como $-4/1$ |
| $\mathbb{R}$ | ✅ Sí | Está en la recta numérica |
""")

    # ── CUESTIONARIO ────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario N07", expanded=False):
        st.markdown(r"""
**1.** ¿Cuál NO pertenece a ℝ?
- A) $\sqrt{2}$ · B) **$\sqrt{-9}$** · C) $0/\pi$ · D) $-10{,}5$

**2.** El axioma que garantiza $a + 0 = a$ se llama:
- A) Clausura · B) **Neutro Aditivo** · C) Inverso Aditivo · D) Conmutatividad

**3.** ¿Cuál es el inverso multiplicativo de $-0{,}75$?
- A) 0,75 · B) 4/3 · C) **-4/3** · D) -3/4

**4.** $a(b + c) = ab + ac$ representa el axioma de:
- A) Asociatividad · B) Conmutatividad · C) **Distributividad** · D) Inverso

**5.** ¿Cuál es CORRECTA sobre subconjuntos de ℝ?
- A) Todo real es racional · B) ℐ ⊂ ℚ · C) **ℝ = ℚ ∪ ℐ** · D) 0 es racional e irracional

**6.** ¿Qué ocurre con $5/(4-4)$?
- A) Es 0 · B) Es 5 · C) **Es indefinición** · D) Es irracional

**7.** Conmutatividad en multiplicación significa:
- A) **El orden de los factores no altera el producto** · B) Todo número × 1 es el mismo · C) Se pueden reagrupar · D) Todo × 0 es 0

**8.** Si $x$ es irracional, ¿cuál es SIEMPRE real?
- A) **$x + 5$** · B) $x^2$ · C) $x/0$ · D) $\sqrt{-x}$ (con $x > 0$)

**9.** Inverso aditivo de $\sqrt{2}$:
- A) $1/\sqrt{2}$ · B) 2 · C) **$-\sqrt{2}$** · D) 0

**10.** Racionales + los que no pueden escribirse como $a/b$ forman:
- A) ℤ · B) Imaginarios · C) **ℝ** · D) ℕ
""")

    with st.expander("🔑 Pauta N07", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería |
|:---:|:---:|:---|
| 1 | **B** | Raíces de índice par con base negativa son imaginarias, no reales. |
| 2 | **B** | El neutro es el que "no altera". En suma es el 0. |
| 3 | **C** | $-0{,}75 = -3/4$. Inverso: dar vuelta la fracción conservando el signo → $-4/3$. |
| 4 | **C** | Distribuir el factor exterior a cada sumando del paréntesis. |
| 5 | **C** | Definición estructural de ℝ: $\mathbb{Q} \cup \mathbb{I}$. |
| 6 | **C** | $4 - 4 = 0$. División por cero → indefinición. |
| 7 | **A** | $a \cdot b = b \cdot a$. El intercambio de posición no afecta el resultado. |
| 8 | **A** | Por clausura: irracional + racional = real siempre. |
| 9 | **C** | Inverso aditivo = mismo número con signo contrario para que la suma dé 0. |
| 10 | **C** | Racionales + Irracionales = ℝ. El universo completo. |
""")
