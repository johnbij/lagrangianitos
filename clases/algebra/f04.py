import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_F04():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("F04: Función Cuadrática y sus Gráficas")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ Forma General

    $$f(x) = ax^2 + bx + c \quad (a \neq 0)$$

    Si $a = 0$, vuelve a ser lineal. El coeficiente $a$ es el "jefe" de la parábola.

    ---

    ### 🛡️ Concavidad (El valor de $a$)

    * **Si $a > 0$:** Parábola abierta hacia **arriba** (😊 forma $\cup$). Tiene un **Mínimo**.
    * **Si $a < 0$:** Parábola abierta hacia **abajo** (😔 forma $\cap$). Tiene un **Máximo**.

    ---

    ### 🛡️ Intersección con el eje Y

    El punto de corte con el eje $Y$ es siempre $(0, c)$. El valor de $c$ da la altura inicial.

    ---

    ### 🛡️ El Vértice ($V$)

    Es el punto más alto o más bajo de la parábola.
    $$x_v = \frac{-b}{2a} \qquad y_v = f(x_v)$$

    ---

    ### 🛡️ El Eje de Simetría

    Línea vertical que divide la parábola en dos mitades iguales: $x = \dfrac{-b}{2a}$
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Concavidad, Vértice y abertura")
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        x = np.linspace(-2, 2, 200)

        # Abertura según a
        axes[0].plot(x, 4*x**2,   color='#c0392b', lw=2.5, label='$a=4$ (estrecha)')
        axes[0].plot(x, x**2,     color='black',   lw=2.5, label='$a=1$ (estándar)')
        axes[0].plot(x, 0.2*x**2, color='#1565c0', lw=2.5, label='$a=0.2$ (ancha)')
        axes[0].axhline(0, color='black', lw=1); axes[0].axvline(0, color='black', lw=1)
        axes[0].set_title("Efecto de $a$: abertura", fontsize=12, fontweight='bold')
        axes[0].set_ylim(-0.5, 5); axes[0].legend(fontsize=9); axes[0].grid(True, alpha=0.3)

        # Vértice y eje de simetría
        x2 = np.linspace(-1, 5, 200)
        y2 = x2**2 - 4*x2 + 5    # vértice (2, 1)
        axes[1].plot(x2, y2, color='#7b1fa2', lw=2.5, label=r'$x^2-4x+5$')
        axes[1].axvline(2, color='#f39c12', lw=2, linestyle='--', label='Eje de simetría $x=2$')
        axes[1].scatter([2], [1], color='black', s=140, zorder=5)
        axes[1].annotate('Vértice $(2,1)$', xy=(2, 1), xytext=(2.7, 2),
                         arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
        axes[1].axhline(0, color='black', lw=1); axes[1].axvline(0, color='black', lw=1)
        axes[1].set_title("Vértice y eje de simetría", fontsize=12, fontweight='bold')
        axes[1].legend(fontsize=9); axes[1].grid(True, alpha=0.3)

        # Parábola hacia abajo con máximo
        x3 = np.linspace(-1, 5, 200)
        y3 = -x3**2 + 4*x3 + 1
        axes[2].plot(x3, y3, color='purple', lw=2.5, label=r'$-x^2+4x+1$')
        axes[2].axvline(2, color='gray', lw=1.5, linestyle=':', label='Eje: $x=2$')
        axes[2].scatter([2], [5], color='black', s=140, zorder=5)
        axes[2].annotate('Vértice $(2,5)$\n¡Máximo!', xy=(2, 5), xytext=(3, 4.2),
                         arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
        axes[2].axhline(0, color='black', lw=1); axes[2].axvline(0, color='black', lw=1)
        axes[2].set_title("$a<0$: máximo en el vértice", fontsize=12, fontweight='bold')
        axes[2].legend(fontsize=9); axes[2].grid(True, alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería F04", expanded=False):
        st.markdown(r"""
### E01: Identificar componentes

$f(x) = 2x^2 - 4x + 5$: $a=2$ (>0, mínimo), $b=-4$, $c=5$ (corte Y en $(0,5)$)

### E02: Calcular el vértice

$f(x) = x^2 - 6x + 1$:
1. $x_v = -(-6)/(2\cdot1) = 3$
2. $y_v = f(3) = 9 - 18 + 1 = -8$
3. Vértice: $(3, -8)$

### E03: Trazar la parábola

Para $f(x) = x^2 - 3x - 4$:
| $x$ | $f(x)$ |
| :---: | :---: |
| -1 | 0 |
| 0 | -4 |
| 4 | 0 |
| 1.5 | -6.25 (vértice) |
""")

    with st.expander("❓ Cuestionario F04: Función Cuadrática", expanded=False):
        quiz = [
            {"question": r"Dada $f(x) = 2x^2 - 4x + 5$, ¿hacia dónde se abre la parábola?",
             "options": {"A": "Hacia abajo, porque el 2 es positivo.", "B": "Hacia arriba, porque el 2 es positivo.", "C": "Hacia la derecha.", "D": "Hacia la izquierda."},
             "answer": "B", "explanation": r"$a=2>0$ → concavidad hacia arriba (mínimo)."},
            {"question": r"¿En qué punto corta al eje Y la función $f(x) = x^2 + 3x - 8$?",
             "options": {"A": r"$(0, 3)$", "B": r"$(3, 0)$", "C": r"$(0, -8)$", "D": r"$(-8, 0)$"},
             "answer": "C", "explanation": r"El corte con el eje $Y$ es $(0, c) = (0, -8)$."},
            {"question": r"¿Cuál es la coordenada $x$ del vértice para $f(x) = x^2 - 6x + 1$?",
             "options": {"A": "6", "B": "-3", "C": "3", "D": "0"},
             "answer": "C", "explanation": r"$x_v = -(-6)/(2\cdot1) = 6/2 = 3$."},
            {"question": r"Si $a < 0$ en una función cuadrática, la función tiene:",
             "options": {"A": "Un punto mínimo.", "B": "Un punto máximo.", "C": "Ningún punto crítico.", "D": "Una línea recta."},
             "answer": "B", "explanation": "Parábola hacia abajo = tope = máximo."},
            {"question": r"¿Cuál es el eje de simetría de $f(x) = x^2 + 4x + 10$?",
             "options": {"A": r"$x = 2$", "B": r"$x = 4$", "C": r"$x = -2$", "D": r"$x = -4$"},
             "answer": "C", "explanation": r"$x = -4/(2\cdot1) = -2$."},
            {"question": r"¿Qué representa la coordenada $y$ del vértice?",
             "options": {"A": "El punto de corte con el eje $X$.", "B": "El valor máximo o mínimo de la función.", "C": "El coeficiente $b$.", "D": "La pendiente."},
             "answer": "B", "explanation": "La $y$ del vértice es el valor extremo (máx o mín) de la función."},
            {"question": r"En $f(x) = 5x^2 - 10$, ¿cuál es el valor de $b$?",
             "options": {"A": "5", "B": "-10", "C": "0", "D": "10"},
             "answer": "C", "explanation": r"No hay término con $x$ sola, por tanto $b=0$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="f04_quiz")

    with st.expander("🔑 Pauta Técnica F04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $a=2>0$ → abre hacia arriba. |
| **2** | **C** | Corte eje $Y$: $(0, c)=(0,-8)$. |
| **3** | **C** | $x_v=6/2=3$. |
| **4** | **B** | $a<0$ → montaña → máximo. |
| **5** | **C** | $x=-4/(2)=-2$. |
| **6** | **B** | $y_v$ = valor extremo. |
| **7** | **C** | No hay término $bx$, por tanto $b=0$. |
""")
