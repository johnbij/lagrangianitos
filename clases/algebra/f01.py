import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_F01():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("F01: Conceptos Fundamentales de Funciones")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ Definición de Función

    Una función es una relación entre dos conjuntos donde a cada elemento del conjunto de entrada (**Dominio**) le corresponde **exactamente uno** del conjunto de llegada (**Codominio**).

    * **Input ($x$):** Preimagen.
    * **Output ($f(x)$ o $y$):** Imagen.

    ---

    ### 🛡️ Conceptos Clave

    * **Dominio (Dom f):** El conjunto de todos los valores que $x$ puede tomar (inputs permitidos).
    * **Codominio:** El conjunto de todos los posibles valores de llegada.
    * **Recorrido / Rango (Rec f):** Los valores que la función entrega efectivamente (las imágenes reales).
    * **Composición ($f \circ g$):** Aplicar una función dentro de otra. $f(g(x))$: primero $g$, luego $f$.

    ---

    ### 🛡️ Evaluación de una Función

    Evaluar = reemplazar $x$ por un valor específico.
    > Si $f(x) = 2x + 3$, entonces $f(5) = 2(5) + 3 = 13$.
    > Aquí **5** es la preimagen y **13** es la imagen.
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Diagrama sagital y función afín")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        # Diagrama sagital
        ax = axes[0]
        circle1 = plt.Circle((0.2, 0.5), 0.18, color='#1565c0', fill=False, lw=2.5)
        circle2 = plt.Circle((0.8, 0.5), 0.18, color='#c0392b', fill=False, lw=2.5)
        ax.add_patch(circle1); ax.add_patch(circle2)
        preimages = [0.35, 0.50, 0.65]
        images    = [0.35, 0.50, 0.65]
        for pi, im in zip(preimages, images):
            ax.annotate("", xy=(0.62, im), xytext=(0.38, pi),
                        arrowprops=dict(arrowstyle="->", color="black", lw=1.5))
        for i, (pi, im) in enumerate(zip(preimages, images)):
            ax.text(0.20, pi, f'$x_{i+1}$', ha='center', fontsize=12, color='#1565c0', fontweight='bold')
            ax.text(0.80, im, f'$f(x_{i+1})$', ha='center', fontsize=11, color='#c0392b', fontweight='bold')
        ax.text(0.20, 0.10, 'Dominio', ha='center', fontsize=11, color='#1565c0')
        ax.text(0.80, 0.10, 'Codominio', ha='center', fontsize=11, color='#c0392b')
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
        ax.set_title("Diagrama Sagital: cada $x$ → un solo $f(x)$", fontsize=12, fontweight='bold')

        # Función afín
        x = np.linspace(-4, 4, 100)
        y = 2*x + 3
        axes[1].plot(x, y, color='#1b5e20', lw=2.5, label='$f(x) = 2x + 3$')
        axes[1].scatter([5], [13], color='#c0392b', s=120, zorder=5, label='$f(5)=13$')
        axes[1].axhline(0, color='black', lw=1); axes[1].axvline(0, color='black', lw=1)
        axes[1].set_title("Evaluación: $f(5) = 2(5)+3 = 13$", fontsize=12, fontweight='bold')
        axes[1].legend(fontsize=11); axes[1].grid(True, alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería F01", expanded=False):
        st.markdown(r"""
### E01: Evaluación directa

Si $f(x) = 3x - 5$:
* $f(4) = 3(4) - 5 = 12 - 5 = 7$ → imagen de 4 es 7
* $f(-1) = 3(-1) - 5 = -8$ → imagen de $-1$ es $-8$

### E02: Composición de funciones

Si $f(x) = x^2$ y $g(x) = x + 1$, hallar $(f \circ g)(3)$:
1. Primero $g$: $g(3) = 3 + 1 = 4$
2. Luego $f$: $f(4) = 4^2 = 16$
3. Resultado: $(f \circ g)(3) = 16$

### E03: Identificar preimagen e imagen

Si $f(2) = 10$:
* **2** es la preimagen (input, pertenece al Dominio)
* **10** es la imagen (output, pertenece al Recorrido)
""")

    with st.expander("❓ Cuestionario F01: Conceptos de Funciones", expanded=False):
        quiz = [
            {"question": r"Si $f(x) = 3x - 5$, ¿cuál es la imagen de 4?",
             "options": {"A": "7", "B": "4", "C": "-5", "D": "17"},
             "answer": "A", "explanation": r"$f(4) = 3(4)-5 = 12-5 = 7$."},
            {"question": r"¿Cómo se llama el conjunto de todos los valores de entrada para los que $f$ está definida?",
             "options": {"A": "Recorrido", "B": "Codominio", "C": "Dominio", "D": "Rango"},
             "answer": "C", "explanation": "El Dominio es el set de datos de entrada permitidos."},
            {"question": r"Si $f(2) = 10$, ¿cuál es correcta?",
             "options": {"A": "10 es la preimagen de 2.", "B": "2 es la imagen de 10.", "C": "10 es la imagen de 2.", "D": "2 es el codominio."},
             "answer": "C", "explanation": "El resultado (10) es la imagen del valor de entrada (2)."},
            {"question": r"Si $f(x) = x^2$ y $g(x) = x+1$, ¿cuál es $(f \circ g)(3)$?",
             "options": {"A": "10", "B": "16", "C": "12", "D": "9"},
             "answer": "B", "explanation": r"Primero $g(3)=4$. Luego $f(4)=16$."},
            {"question": r"El conjunto de los valores que la función efectivamente produce se llama:",
             "options": {"A": "Dominio", "B": "Preimagen", "C": "Recorrido", "D": "Conjunto de partida"},
             "answer": "C", "explanation": "El Recorrido (o Rango) son los outputs reales."},
            {"question": r"¿Por qué $f(x) = 1/x$ no está definida en $x=0$?",
             "options": {"A": "Porque 1 no se puede dividir.", "B": "Porque el dominio es solo positivo.", "C": "Porque dividir por cero es indefinido.", "D": "Porque $f(0) = 0$."},
             "answer": "C", "explanation": "No se puede dividir por cero; 0 no pertenece al dominio."},
            {"question": r"¿Cuál de las siguientes relaciones NO es una función?",
             "options": {"A": r"$(1,2), (3,4), (5,6)$", "B": r"$(1,2), (1,3), (2,4)$", "C": r"$(0,0), (1,1), (2,4)$", "D": r"$(-1,1), (0,0), (1,1)$"},
             "answer": "B", "explanation": r"El input $x=1$ tiene dos imágenes (2 y 3). No es función."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="f01_quiz")
