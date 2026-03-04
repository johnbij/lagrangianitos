import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_A03():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("A03: Productos Notables — Atajos en el Código")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ ¿Para qué sirven?

    Hacer $(x+5)(x+5)$ multiplicando término a término es lento. Los productos notables son **patrones memorizados** que permiten saltarse el proceso manual, como funciones de acceso directo en un IDE.

    ---

    ### 🛡️ El Cuadrado del Binomio

    $(a \pm b)^2 = a^2 \pm 2ab + b^2$

    * "El primero al cuadrado, ± el doble del primero por el segundo, + el segundo al cuadrado."

    > ⚠️ **Error crítico:** Muchos creen que $(a+b)^2 = a^2 + b^2$. ¡Falso! Falta el término central $2ab$.

    ---

    ### 🛡️ Suma por su Diferencia (El exterminador)

    $(a + b)(a - b) = a^2 - b^2$

    Los términos centrales se cancelan entre sí. Es el más rápido de todos.
    * Ejemplo: $(x+3)(x-3) = x^2 - 9$

    ---

    ### 🛡️ Binomio con Término Común

    $(x + a)(x + b) = x^2 + (a+b)x + (a \cdot b)$

    1. El primero al cuadrado: $x^2$
    2. **Suma** de los números multiplicada por $x$: $(a+b)x$
    3. **Producto** de los números: $a \cdot b$

    Ejemplo: $(x+5)(x+2) = x^2 + 7x + 10$
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Los tres patrones")
        fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

        x = np.linspace(-1, 5, 200)
        axes[0].plot(x, x**2 + 8*x + 16, color='#1b5e20', lw=2.5, label=r'$(x+4)^2 = x^2+8x+16$')
        axes[0].axhline(0, color='black', lw=0.8)
        axes[0].set_title("Cuadrado del Binomio\n$(a+b)^2$", fontsize=12, fontweight='bold')
        axes[0].set_xlabel("$x$"); axes[0].legend(fontsize=9); axes[0].grid(True, alpha=0.3)
        axes[0].set_ylim(-5, 40)

        axes[1].plot(x, x**2 - 9, color='#c0392b', lw=2.5, label=r'$(x+3)(x-3) = x^2-9$')
        axes[1].axhline(0, color='black', lw=0.8)
        axes[1].scatter([3, -3], [0, 0], color='#c0392b', s=80, zorder=5)
        axes[1].set_title("Suma × Diferencia\n$a^2-b^2$", fontsize=12, fontweight='bold')
        axes[1].set_xlabel("$x$"); axes[1].legend(fontsize=9); axes[1].grid(True, alpha=0.3)
        axes[1].set_ylim(-15, 20)

        axes[2].plot(x, x**2 + 7*x + 10, color='#7b1fa2', lw=2.5, label=r'$(x+5)(x+2)$')
        axes[2].axhline(0, color='black', lw=0.8)
        axes[2].scatter([-5, -2], [0, 0], color='#7b1fa2', s=80, zorder=5)
        axes[2].set_title("Binomio c/ término común\n$(x+a)(x+b)$", fontsize=12, fontweight='bold')
        axes[2].set_xlabel("$x$"); axes[2].legend(fontsize=9); axes[2].grid(True, alpha=0.3)
        axes[2].set_ylim(-5, 30)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería A03", expanded=False):
        st.markdown(r"""
### E01: Cuadrado del Binomio

| Expresión | Desarrollo | Resultado |
| :--- | :--- | :--- |
| $(x+4)^2$ | $x^2 + 2(x)(4) + 16$ | $x^2 + 8x + 16$ |
| $(x-3)^2$ | $x^2 - 2(x)(3) + 9$ | $x^2 - 6x + 9$ |
| $(2a+3b)^2$ | $4a^2 + 2(2a)(3b) + 9b^2$ | $4a^2 + 12ab + 9b^2$ |

### E02: Suma × Diferencia

| Expresión | Resultado |
| :--- | :--- |
| $(x+7)(x-7)$ | $x^2 - 49$ |
| $(m-5)(m+5)$ | $m^2 - 25$ |

### E03: Binomio con término común

$(x+7)(x+3)$: suma=$7+3=10$, producto=$7\cdot3=21$ → $x^2+10x+21$

$(x-2)(x+5)$: suma=$-2+5=3$, producto=$-2\cdot5=-10$ → $x^2+3x-10$
""")

    with st.expander("❓ Cuestionario A03: Reconociendo Patrones", expanded=False):
        quiz = [
            {"question": r"Al desarrollar $(x + 4)^2$, el resultado correcto es:",
             "options": {"A": r"$x^2 + 16$", "B": r"$x^2 + 4x + 16$", "C": r"$x^2 + 8x + 16$", "D": r"$2x + 8$"},
             "answer": "C", "explanation": r"Término central: $2\cdot x \cdot 4 = 8x$."},
            {"question": r"¿Cuál es el resultado de $(m - 5)(m + 5)$?",
             "options": {"A": r"$m^2 - 10$", "B": r"$m^2 - 25$", "C": r"$m^2 + 25$", "D": r"$m^2 - 10m + 25$"},
             "answer": "B", "explanation": r"Suma por diferencia: $a^2-b^2 = m^2-25$."},
            {"question": r"En $(2a + 3b)^2$, ¿cuál es el término central?",
             "options": {"A": r"$6ab$", "B": r"$12ab$", "C": r"$5ab$", "D": r"$10ab$"},
             "answer": "B", "explanation": r"$2\cdot(2a)\cdot(3b) = 12ab$."},
            {"question": r"El producto $(x + 7)(x + 3)$ da:",
             "options": {"A": r"$x^2 + 10x + 21$", "B": r"$x^2 + 21x + 10$", "C": r"$x^2 + 10$", "D": r"$x^2 + 21$"},
             "answer": "A", "explanation": r"Suma: $7+3=10$; producto: $7\cdot3=21$."},
            {"question": r"¿Qué producto notable representa $a^2 - 81$?",
             "options": {"A": r"$(a - 9)^2$", "B": r"$(a + 9)^2$", "C": r"$(a + 9)(a - 9)$", "D": r"$a(a - 81)$"},
             "answer": "C", "explanation": r"Diferencia de cuadrados: $a^2 - 9^2$."},
            {"question": r"En $(x - 1)^2$, ¿cuál es el signo del término central?",
             "options": {"A": "Positivo", "B": "Negativo", "C": "Neutro", "D": "No tiene"},
             "answer": "B", "explanation": "El signo del binomio define el del término central."},
            {"question": r"¿Cuál es el desarrollo de $(3x + 1)^2$?",
             "options": {"A": r"$9x^2 + 1$", "B": r"$3x^2 + 6x + 1$", "C": r"$9x^2 + 6x + 1$", "D": r"$9x^2 + 3x + 1$"},
             "answer": "C", "explanation": r"$(3x)^2=9x^2$; $2\cdot3x\cdot1=6x$; $1^2=1$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="a03_quiz")

    with st.expander("🔑 Pauta Técnica A03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $2\cdot x\cdot4 = 8x$. |
| **2** | **B** | $m^2 - 5^2 = m^2 - 25$. |
| **3** | **B** | $2\cdot(2a)\cdot(3b) = 12ab$. |
| **4** | **A** | Suma $7+3=10$; producto $7\cdot3=21$. |
| **5** | **C** | $a^2 - 9^2$: diferencia de cuadrados. |
| **6** | **B** | El signo del binomio pasa al término central. |
| **7** | **C** | $(3x)^2=9x^2$; $2\cdot3x\cdot1=6x$. |
""")
