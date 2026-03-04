import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_A04():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("A04: Factorización — El Arte de Desarmar")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ ¿Qué es Factorizar?

    Si multiplicar es armar un objeto, factorizar es **desarmarlo** para ver sus piezas originales.
    * **Multiplicar:** $(x + 2)(x + 3) \rightarrow x^2 + 5x + 6$
    * **Factorizar:** $x^2 + 5x + 6 \rightarrow (x + 2)(x + 3)$

    ---

    ### 🛡️ Factor Común (El Filtro) — Siempre primero

    Busca qué tienen en común TODOS los términos y sácalo fuera del paréntesis.
    * **Ejemplo:** $5x^2 + 10x = 5x(x + 2)$

    ---

    ### 🛡️ Diferencia de Cuadrados

    Si ves dos cuadrados restándose: $a^2 - b^2 = (a + b)(a - b)$
    * **Ejemplo:** $x^2 - 16 = (x + 4)(x - 4)$

    ---

    ### 🛡️ Suma y Diferencia de Cubos (Regla SOPA)

    * **Suma:** $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$
    * **Diferencia:** $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$

    Mnemotecnia **SOPA** para los signos del trinomio:
    **S**ame (igual al original) | **O**pposite (contrario) | **P**ositive **A**lways (siempre +)

    ---

    ### 🛡️ Trinomio $x^2 + bx + c$

    Busca dos números que **sumados** den $b$ y **multiplicados** den $c$.
    * **Ejemplo:** $x^2 + 7x + 12$ → ¿Qué suma 7 y multiplica 12? → 3 y 4 → $(x + 3)(x + 4)$
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Factorización = camino de vuelta")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        x = np.linspace(-6, 5, 300)
        y1 = x**2 + 5*x + 6    # (x+2)(x+3)
        y2 = x**2 - 9           # (x+3)(x-3)

        axes[0].plot(x, y1, color='#1b5e20', lw=2.5, label=r'$x^2+5x+6 = (x+2)(x+3)$')
        axes[0].scatter([-2, -3], [0, 0], color='#c0392b', s=100, zorder=5, label='Raíces: $x=-2,\\ x=-3$')
        axes[0].axhline(0, color='black', lw=1)
        axes[0].axvline(0, color='black', lw=1)
        axes[0].set_title("Trinomio → Raíces visibles", fontsize=12, fontweight='bold')
        axes[0].set_ylim(-5, 15); axes[0].legend(fontsize=9); axes[0].grid(True, alpha=0.3)

        axes[1].plot(x, y2, color='#7b1fa2', lw=2.5, label=r'$x^2-9 = (x+3)(x-3)$')
        axes[1].scatter([3, -3], [0, 0], color='#f39c12', s=100, zorder=5, label='Raíces: $x=\pm3$')
        axes[1].axhline(0, color='black', lw=1)
        axes[1].axvline(0, color='black', lw=1)
        axes[1].set_title("Diferencia de cuadrados", fontsize=12, fontweight='bold')
        axes[1].set_ylim(-12, 20); axes[1].legend(fontsize=9); axes[1].grid(True, alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería A04", expanded=False):
        st.markdown(r"""
### E01: Factor Común

$6x^3 - 12x^2$ → Factor común: $6x^2$ → $6x^2(x - 2)$

### E02: Diferencia de Cuadrados

$x^2 - 49 = (x+7)(x-7)$  |  $4a^2 - 25 = (2a+5)(2a-5)$

### E03: Trinomio

$x^2 - 5x + 6$: busco números que sumen $-5$ y multipliquen $6$ → $-2$ y $-3$ → $(x-2)(x-3)$

### E04: Cubos (SOPA)

$x^3 + 8 = (x+2)(x^2 - 2x + 4)$ — Igual (+), Opuesto (-), Positivo (+)
""")

    with st.expander("❓ Cuestionario A04: Desafío de Factorización", expanded=False):
        quiz = [
            {"question": r"¿Cuál es el factor común en $6x^3 - 12x^2$?",
             "options": {"A": r"$6x$", "B": r"$x^2$", "C": r"$6x^2$", "D": r"$12x$"},
             "answer": "C", "explanation": r"El 6 divide al 12 y la potencia mínima de $x$ es $x^2$."},
            {"question": r"Al factorizar $x^2 - 49$, obtenemos:",
             "options": {"A": r"$(x-7)^2$", "B": r"$(x+7)(x-7)$", "C": r"$(x+49)(x-1)$", "D": r"$x(x-49)$"},
             "answer": "B", "explanation": r"Diferencia de cuadrados: $x^2 - 7^2$."},
            {"question": r"¿Cuál es la factorización de $x^3 + 8$?",
             "options": {"A": r"$(x+2)(x^2 - 2x + 4)$", "B": r"$(x+2)^3$", "C": r"$(x+2)(x^2+2x+4)$", "D": r"$(x-2)(x^2+2x+4)$"},
             "answer": "A", "explanation": r"Suma de cubos con SOPA: $(x+2)$ luego $x^2 \mathbf{-}2x\mathbf{+}4$."},
            {"question": r"Para $x^2 - 5x + 6$, los números buscados son:",
             "options": {"A": r"$-5$ y $1$", "B": r"$-2$ y $-3$", "C": r"$2$ y $3$", "D": r"$-6$ y $1$"},
             "answer": "B", "explanation": r"$(-2)+(-3)=-5$ y $(-2)\cdot(-3)=6$."},
            {"question": r"¿Qué técnica usarías PRIMERO para factorizar $2x^2 - 18$?",
             "options": {"A": "Diferencia de cuadrados.", "B": "Factor común.", "C": "Trinomio.", "D": "Cubos."},
             "answer": "B", "explanation": r"Siempre factor común primero: $2(x^2 - 9)$, luego diferencia."},
            {"question": r"Factoriza completamente: $3x^2 + 3x - 18$",
             "options": {"A": r"$3(x+3)(x-2)$", "B": r"$(3x+9)(x-2)$", "C": r"$3(x-3)(x+2)$", "D": r"$3(x+6)(x-1)$"},
             "answer": "A", "explanation": r"Factor común 3: $3(x^2+x-6)$. Busco números: $3$ y $-2$ → $3(x+3)(x-2)$."},
            {"question": r"Al factorizar $x^2 + 10x + 25$ se obtiene:",
             "options": {"A": r"$(x+10)(x+25)$", "B": r"$(x+5)(x-5)$", "C": r"$(x+5)^2$", "D": r"$x(x+10)+25$"},
             "answer": "C", "explanation": r"TCP: $5+5=10$ y $5\cdot5=25$. Es $(x+5)^2$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="a04_quiz")

    with st.expander("🔑 Pauta Técnica A04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $6$ divide a $12$; potencia mínima $x^2$. |
| **2** | **B** | $x^2-7^2 = (x+7)(x-7)$. |
| **3** | **A** | Suma de cubos SOPA: $+, -, +$. |
| **4** | **B** | $(-2)+(-3)=-5$; $(-2)(-3)=+6$. |
| **5** | **B** | Factor común siempre primero. |
| **6** | **A** | $3(x^2+x-6) = 3(x+3)(x-2)$. |
| **7** | **C** | TCP: $(x+5)^2$. |
""")
