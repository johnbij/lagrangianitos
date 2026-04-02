import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_A05():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("A05: Trinomio Cuadrado Perfecto y Completación de Cuadrados")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ El Trinomio Cuadrado Perfecto (TCP)

    Un trinomio es "Perfecto" cuando proviene directamente de un Cuadrado de Binomio.

    **¿Cómo reconocerlo?**
    1. El primer término es cuadrado perfecto (ej: $x^2$).
    2. El último término es cuadrado perfecto (ej: $25$).
    3. **La prueba de fuego:** el término del medio = $2 \cdot \sqrt{\text{primero}} \cdot \sqrt{\text{último}}$

    **Ejemplo:** $x^2 + 10x + 25$ → $\sqrt{x^2}=x$, $\sqrt{25}=5$, doble producto: $2\cdot x\cdot 5=10x$ ✅

    * **Factorización:** $x^2 + 10x + 25 = (x + 5)^2$

    ---

    ### 🛡️ Completación de Cuadrados: "El truco del cero"

    A veces la PAES te da un trinomio que **no es perfecto**. Por ejemplo: $x^2 + 6x + 5$.
    Si fuera perfecto, el último número debería ser $(6/2)^2 = 9$. Pero tenemos 5.

    **Un programador hackea la expresión sumando y restando lo que le falta:**

    1. Toma el coeficiente de $x$ (el 6).
    2. Divídelo por 2 (da 3).
    3. Elévalo al cuadrado (da 9).
    4. **Suma y resta ese 9** (sin alterar el valor).

    **Paso a paso:**
    * $x^2 + 6x + 5$
    * $(x^2 + 6x + 9) - 9 + 5$
    * $(x + 3)^2 - 4$

    > **¿Para qué sirve?** Para encontrar el vértice de parábolas, resolver ecuaciones cuadráticas complejas y transformar círculos en geometría.

    ---

    ### 🛡️ Resumen: Condición para ser TCP

    $$c = \left(\frac{b}{2}\right)^2$$

    Si no se cumple, completamos cuadrados para forzarlo.
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: TCP vs. No-TCP y Vértice por completación")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        x = np.linspace(-7, 3, 300)
        axes[0].plot(x, x**2 + 10*x + 25, color='#1b5e20', lw=2.5, label=r'TCP: $x^2+10x+25=(x+5)^2$')
        axes[0].plot(x, x**2 + 10*x + 20, color='#c0392b', lw=2, linestyle='--', label=r'No TCP: $x^2+10x+20$')
        axes[0].scatter([-5], [0], color='#1b5e20', s=100, zorder=5)
        axes[0].axhline(0, color='black', lw=1); axes[0].axvline(0, color='black', lw=1)
        axes[0].set_ylim(-10, 30)
        axes[0].set_title("TCP toca en un punto; No-TCP tiene dos raíces", fontsize=12, fontweight='bold')
        axes[0].legend(fontsize=9); axes[0].grid(True, alpha=0.3)

        x2 = np.linspace(-1, 7, 300)
        y = x2**2 + 6*x2 + 5    # (x+3)^2 - 4 → vértice (-3, -4)
        axes[1].plot(x2 - 8, y, color='#7b1fa2', lw=2.5, label=r'$f(x)=x^2+6x+5=(x+3)^2-4$')
        axes[1].scatter([-3], [-4], color='#f39c12', s=120, zorder=5, label='Vértice $(-3,-4)$')
        axes[1].axhline(0, color='black', lw=1); axes[1].axvline(0, color='black', lw=1)
        axes[1].axvline(-3, color='gray', lw=1.2, linestyle=':', label='Eje de simetría $x=-3$')
        axes[1].set_xlim(-7, 1); axes[1].set_ylim(-6, 10)
        axes[1].set_title("Completación: vértice visible", fontsize=12, fontweight='bold')
        axes[1].legend(fontsize=9); axes[1].grid(True, alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería A05", expanded=False):
        st.markdown(r"""
### E01: Reconocer TCP

| Trinomio | Prueba del medio | ¿Es TCP? |
| :--- | :--- | :---: |
| $x^2 + 6x + 9$ | $2\cdot x\cdot3=6x$ ✅ | **Sí** → $(x+3)^2$ |
| $x^2 + 4x + 2$ | necesitaría $2^2=4$, pero tiene 2 ✖ | **No** |
| $4x^2 + 12x + 9$ | $2\cdot2x\cdot3=12x$ ✅ | **Sí** → $(2x+3)^2$ |

### E02: Completar cuadrado

$x^2 + 8x + 3$:
1. Mitad de 8 = 4; $4^2=16$
2. $(x^2+8x+16) - 16 + 3 = (x+4)^2 - 13$
3. Vértice: $(-4, -13)$

### E03: Encontrar $c$ para que sea TCP

Si $x^2 + 12x + c$ debe ser TCP: $c = (12/2)^2 = 36$
""")

    with st.expander("❓ Cuestionario A05: Perfección y Hackeo Algebraico", expanded=False):
        quiz = [
            {"question": r"¿Cuál de los siguientes trinomios es un TCP?",
             "options": {"A": r"$x^2 + 4x + 2$", "B": r"$x^2 + 6x + 9$", "C": r"$x^2 + 5x + 25$", "D": r"$x^2 + 10x + 100$"},
             "answer": "B", "explanation": r"Mitad de 6 es 3; $3^2=9$. Calza perfecto."},
            {"question": r"Si $x^2 + 12x + c$ debe ser TCP, ¿cuál es $c$?",
             "options": {"A": "6", "B": "12", "C": "36", "D": "144"},
             "answer": "C", "explanation": r"Mitad de 12 es 6; $6^2=36$."},
            {"question": r"Al factorizar $x^2 - 14x + 49$, obtenemos:",
             "options": {"A": r"$(x-7)(x+7)$", "B": r"$(x+7)^2$", "C": r"$(x-7)^2$", "D": r"$(x-49)^2$"},
             "answer": "C", "explanation": r"Signo del medio es $-$, por lo que el binomio resta: $(x-7)^2$."},
            {"question": r"Para completar cuadrados en $x^2 + 8x$, ¿qué número se suma y resta?",
             "options": {"A": "4", "B": "8", "C": "16", "D": "64"},
             "answer": "C", "explanation": r"Mitad de 8 es 4; $4^2=16$."},
            {"question": r"$x^2 + 2x + 5$ escrito como cuadrado completado es:",
             "options": {"A": r"$(x+1)^2 + 4$", "B": r"$(x+1)^2 + 5$", "C": r"$(x+2)^2 + 1$", "D": r"$(x+1)^2 - 4$"},
             "answer": "A", "explanation": r"Mitad de 2 es 1; $1^2=1$. $(x^2+2x+1)-1+5=(x+1)^2+4$."},
            {"question": r"Si $x^2 + bx + 16$ es TCP con $b > 0$, ¿cuál es $b$?",
             "options": {"A": "4", "B": "8", "C": "16", "D": "32"},
             "answer": "B", "explanation": r"$\sqrt{16}=4$; doble producto: $2\cdot1\cdot4=8$."},
            {"question": r"Al completar cuadrados en $x^2 - 10x + 20$, obtenemos $(x-5)^2 + k$. ¿Cuál es $k$?",
             "options": {"A": "5", "B": "-5", "C": "20", "D": "-25"},
             "answer": "B", "explanation": r"$(x^2-10x+25)-25+20 = (x-5)^2 - 5$. Por tanto $k=-5$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="a05_quiz")
