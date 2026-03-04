import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_A02():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("A02: Multiplicación de Expresiones — La Propiedad Distributiva")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ El concepto de "Repartir" (Distribuir)

    En aritmética, $2 \cdot (3 + 5) = 16$ porque puedes sumar primero.
    Pero en álgebra, cuando tienes $2x(x + 3)$, **no puedes sumar** lo de adentro. El factor de afuera tiene que entrar a "visitar" a cada término del paréntesis.

    * **La Regla:** $a(b + c) = ab + ac$

    ---

    ### 🛡️ Multiplicación de Monomios (El choque de partículas)

    Antes de distribuir, hay que saber qué ocurre cuando dos términos chocan:
    1. **Coeficientes:** se multiplican normal.
    2. **Variables:** si son la misma letra, **se suman los exponentes**.

    **Ejemplo:** $3x^2 \cdot 4x^3$
    * Coeficientes: $3 \cdot 4 = 12$
    * Letras: $x^2 \cdot x^3 = x^{2+3} = x^5$
    * Resultado: $\mathbf{12x^5}$

    ---

    ### 🛡️ Binomio × Binomio (Todos contra todos)

    Cuando tienes $(a + b)(c + d)$, todos los del primer grupo saludan a todos los del segundo.

    **Ejemplo Magistral:** $(x + 3)(x + 5)$
    1. $x \cdot x = x^2$
    2. $x \cdot 5 = 5x$
    3. $3 \cdot x = 3x$
    4. $3 \cdot 5 = 15$
    * Resultado: $x^2 + 5x + 3x + 15$ → $\mathbf{x^2 + 8x + 15}$

    ---

    ### 🛡️ El Peligro de los Signos

    El signo pertenece al número que viene **después**.
    * $-2x(x - 5)$:  $-2x \cdot x = -2x^2$  y  $-2x \cdot (-5) = +10x$ ¡Menos por menos da más!
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        # FIGURA
        st.markdown("#### 📊 Visualización: Distribución y Pendientes")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        x = np.linspace(-2, 4, 100)
        axes[0].plot(x, 2*x, label='$m = 2$ (Positiva pronunciada)', color='#1b5e20', lw=2.5)
        axes[0].plot(x, 0.5*x, label='$m = 0.5$ (Positiva suave)', color='#1565c0', lw=2.5)
        axes[0].plot(x, -x, label='$m = -1$ (Negativa)', color='#c0392b', lw=2.5)
        axes[0].axhline(0, color='black', lw=1)
        axes[0].axvline(0, color='black', lw=1)
        axes[0].set_title("Interpretación de la pendiente $m$", fontsize=13, fontweight='bold')
        axes[0].grid(True, alpha=0.3); axes[0].legend(fontsize=10)

        vals_x = [1, 2, 3]
        vals_y = [(v+3)*(v+5) for v in vals_x]
        table_data = [[f'$x={v}$', f'$x^2={v**2}$', f'$8x={8*v}$', f'Área$={r}$'] 
                      for v, r in zip(vals_x, vals_y)]
        axes[1].axis('off')
        tbl = axes[1].table(cellText=table_data,
                            colLabels=['Valor $x$', 'Término $x^2$', 'Término $8x$', 'Total $(x+3)(x+5)$'],
                            loc='center', cellLoc='center')
        tbl.scale(1, 2.2)
        tbl.auto_set_font_size(False); tbl.set_fontsize(11)
        axes[1].set_title("Verificación numérica: $(x+3)(x+5) = x^2+8x+15$",
                          fontsize=12, fontweight='bold', pad=15)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería A02", expanded=False):
        st.markdown(r"""
### E01: Multiplicación de monomios

| Operación | Proceso | Resultado |
| :--- | :--- | :--- |
| $4a \cdot 3a^2$ | Coef: $4\cdot3=12$; Exp: $1+2=3$ | $12a^3$ |
| $(-5m)(2n)$ | Signos distintos: $-$; $5\cdot2=10$ | $-10mn$ |
| $(3x^2)^2$ | Coef: $3^2=9$; Exp: $2\cdot2=4$ | $9x^4$ |

### E02: Distribución a un binomio

$2x(x+4) = 2x\cdot x + 2x\cdot 4 = 2x^2 + 8x$

### E03: Binomio × Binomio

$(x+2)(x+3)$:
| Primer × Segundo | Resultado |
| :--- | :--- |
| $x \cdot x$ | $x^2$ |
| $x \cdot 3$ | $3x$ |
| $2 \cdot x$ | $2x$ |
| $2 \cdot 3$ | $6$ |
| **Total** | $x^2 + 5x + 6$ |

### E04: Signo negativo fuera

$-(x - 3) = -x + 3$ — El negativo cambia el signo de TODOS los términos internos.
""")

    with st.expander("❓ Cuestionario A02: Multiplicación Algebraica", expanded=False):
        quiz = [
            {"question": r"Al multiplicar $4a \cdot 3a^2$, el resultado es:",
             "options": {"A": r"$7a^3$", "B": r"$12a^2$", "C": r"$12a^3$", "D": r"$12a$"},
             "answer": "C", "explanation": r"$4\cdot3=12$; suma exponentes: $a^{1+2}=a^3$."},
            {"question": r"¿Cuál es el resultado de $2x(x + 4)$?",
             "options": {"A": r"$2x^2 + 8x$", "B": r"$2x + 8$", "C": r"$2x^2 + 4$", "D": r"$10x^2$"},
             "answer": "A", "explanation": r"El $2x$ multiplica a $x$ y luego al $4$."},
            {"question": r"Si multiplicamos $(-5m)(2n)$, obtenemos:",
             "options": {"A": r"$-3mn$", "B": r"$10mn$", "C": r"$-10m + n$", "D": r"$-10mn$"},
             "answer": "D", "explanation": "Signos distintos dan negativo. Las letras distintas se yuxtaponen."},
            {"question": r"Resuelve $(x + 2)(x + 3)$:",
             "options": {"A": r"$x^2 + 6$", "B": r"$x^2 + 5x + 6$", "C": r"$2x + 5$", "D": r"$x^2 + 2x + 6$"},
             "answer": "B", "explanation": r"$x^2 + 3x + 2x + 6 = x^2 + 5x + 6$."},
            {"question": r"¿Qué sucede con $-(x - 3)$ al eliminar el paréntesis?",
             "options": {"A": r"$-x - 3$", "B": r"$x + 3$", "C": r"$-x + 3$", "D": r"$x - 3$"},
             "answer": "C", "explanation": "El menos de afuera cambia el signo de CADA término interior."},
            {"question": r"El área de un rectángulo de lados $(a + 2)$ y $(a + 5)$ es:",
             "options": {"A": r"$2a + 7$", "B": r"$a^2 + 7a + 10$", "C": r"$a^2 + 10$", "D": r"$a^2 + 7a + 7$"},
             "answer": "B", "explanation": r"$(a+2)(a+5) = a^2+5a+2a+10 = a^2+7a+10$."},
            {"question": r"Si el lado de un cuadrado se duplica a $2s$, el área es:",
             "options": {"A": r"$2s^2$", "B": r"$4s^2$", "C": r"$s^4$", "D": r"$2s$"},
             "answer": "B", "explanation": r"$(2s)^2 = 4s^2$. ¡El área se cuadruplica!"},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="a02_quiz")

    with st.expander("🔑 Pauta Técnica A02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $4\cdot3=12$; $a^1\cdot a^2 = a^3$. |
| **2** | **A** | $2x\cdot x = 2x^2$; $2x\cdot 4 = 8x$. |
| **3** | **D** | Signos distintos → negativo; $5\cdot2=10$; letras distintas juntas. |
| **4** | **B** | $(x+2)(x+3)$: $x^2+3x+2x+6 = x^2+5x+6$. |
| **5** | **C** | El $-$ de afuera invierte el signo de cada término. |
| **6** | **B** | $(a+2)(a+5) = a^2+7a+10$. |
| **7** | **B** | $(2s)^2 = 4s^2$. |
""")
