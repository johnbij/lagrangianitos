import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_F05():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("F05: El Discriminante y los Puntos de Corte con el Eje X")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ ¿Qué son los ceros de la función?

    Los puntos donde la parábola corta al eje $X$ se llaman **raíces**, **ceros** o **soluciones**. En esos puntos, $f(x) = 0$.

    ---

    ### 🛡️ El Discriminante ($\Delta$) — El Semáforo

    Es la parte dentro de la raíz cuadrada de la fórmula general:
    $$\Delta = b^2 - 4ac$$

    | Caso | Semáforo | Significado |
    | :--- | :---: | :--- |
    | $\Delta > 0$ | 🟢 | Parábola corta al eje $X$ en **dos puntos** distintos |
    | $\Delta = 0$ | 🟡 | Parábola toca al eje $X$ en **un punto** (vértice sobre el eje) |
    | $\Delta < 0$ | 🔴 | Parábola **no toca** el eje $X$ (flota arriba o abajo) |

    ---

    ### 🛡️ Relación con la Fórmula General

    Para encontrar los cortes exactos:
    $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

    ### 🛡️ Análisis Visual

    * $a > 0$ y $\Delta < 0$ → parábola siempre **por sobre** el eje $X$.
    * $a < 0$ y $\Delta < 0$ → parábola siempre **por debajo** del eje $X$.
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Los tres casos del Discriminante")
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        x = np.linspace(-2.5, 2.5, 300)
        for ax, y_func, title, color, caso in [
            (axes[0], x**2 - 1,   r"$\Delta > 0$: 2 soluciones",    '#1b5e20', ">0"),
            (axes[1], x**2,       r"$\Delta = 0$: 1 solución",       '#f39c12', "=0"),
            (axes[2], x**2 + 0.8, r"$\Delta < 0$: 0 soluciones",    '#c0392b', "<0"),
        ]:
            ax.plot(x, y_func, color=color, lw=2.5)
            ax.axhline(0, color='black', lw=1.5)
            ax.axvline(0, color='black', lw=0.8)
            ax.set_title(title, fontsize=12, fontweight='bold')
            ax.grid(True, alpha=0.3); ax.set_ylim(-2, 4)
            if caso == ">0":
                ax.scatter([-1, 1], [0, 0], color=color, s=100, zorder=5)
            elif caso == "=0":
                ax.scatter([0], [0], color=color, s=120, zorder=5)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería F05", expanded=False):
        st.markdown(r"""
### E01: Calcular el Discriminante

$f(x) = x^2 - 6x + 9$:
$\Delta = (-6)^2 - 4(1)(9) = 36 - 36 = 0$ → Un punto de tangencia (TCP).

$f(x) = x^2 + 2x + 5$:
$\Delta = 4 - 20 = -16 < 0$ → No corta el eje $X$.

### E02: Usar la fórmula general

$f(x) = x^2 - 5x + 6$, $\Delta = 25 - 24 = 1 > 0$:
$$x = \frac{5 \pm 1}{2} \Rightarrow x_1 = 3, \quad x_2 = 2$$

### E03: Análisis sin calcular

¿Cuántas raíces tiene $f(x) = -2x^2 + 3x - 10$?
$\Delta = 9 - 4(-2)(-10) = 9 - 80 = -71 < 0$ → Ninguna raíz real.
""")

    with st.expander("❓ Cuestionario F05: El Discriminante", expanded=False):
        quiz = [
            {"question": r"En $f(x) = x^2 - 6x + 9$, ¿cuál es el valor del discriminante?",
             "options": {"A": "72", "B": "0", "C": "36", "D": "-36"},
             "answer": "B", "explanation": r"$(-6)^2 - 4(1)(9) = 36 - 36 = 0$."},
            {"question": r"Si $\Delta = -25$, ¿cuántas veces corta la parábola al eje X?",
             "options": {"A": "Dos veces.", "B": "Una vez.", "C": "Ninguna vez.", "D": "Depende de $c$."},
             "answer": "C", "explanation": r"$\Delta < 0$ → raíz imaginaria → no hay corte real."},
            {"question": r"Para que la parábola toque el eje X en un solo punto, $b^2 - 4ac$ debe ser:",
             "options": {"A": "Mayor a cero.", "B": "Menor a cero.", "C": "Igual a cero.", "D": "Imaginario."},
             "answer": "C", "explanation": r"$\Delta = 0$: el vértice está exactamente sobre el eje."},
            {"question": r"¿Cuál es el discriminante de $f(x) = x^2 + 2x + 5$?",
             "options": {"A": "-16", "B": "16", "C": "24", "D": "0"},
             "answer": "A", "explanation": r"$2^2 - 4(1)(5) = 4 - 20 = -16$."},
            {"question": r"Si una parábola tiene $a < 0$ y $\Delta > 0$, podemos asegurar que:",
             "options": {"A": "No toca el eje X.", "B": "Corta al eje X en dos puntos y se abre hacia abajo.", "C": "Tiene un mínimo.", "D": "Es una función lineal."},
             "answer": "B", "explanation": r"$a<0$ → hacia abajo; $\Delta>0$ → dos cortes."},
            {"question": r"Si $b^2 > 4ac$, entonces el discriminante es:",
             "options": {"A": "Negativo.", "B": "Cero.", "C": "Positivo.", "D": "Indefinido."},
             "answer": "C", "explanation": r"$b^2 - 4ac > 0$ cuando $b^2$ es mayor que $4ac$."},
            {"question": r"La función $f(x) = x^2 - 4$ tiene raíces en:",
             "options": {"A": r"$x = \pm 2$", "B": r"$x = \pm 4$", "C": r"$x = 2$", "D": r"$x = \pm \sqrt{2}$"},
             "answer": "A", "explanation": r"$x^2-4=0 \Rightarrow x^2=4 \Rightarrow x=\pm2$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="f05_quiz")

    with st.expander("🔑 Pauta Técnica F05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $36-36=0$. TCP, toca en un punto. |
| **2** | **C** | $\Delta<0$ → no hay corte real. |
| **3** | **C** | $\Delta=0$ → un solo punto de tangencia. |
| **4** | **A** | $4-20=-16$. |
| **5** | **B** | $a<0$ (↓) y $\Delta>0$ (dos cortes). |
| **6** | **C** | $b^2>4ac$ → resta positiva → $\Delta>0$. |
| **7** | **A** | $x^2=4$ → $x=\pm2$. |
""")
