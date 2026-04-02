import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_F02():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("F02: Función Lineal y Función Afín")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ La Función Lineal

    Forma: $f(x) = mx$
    * Siempre pasa por el origen $(0,0)$.
    * $m$ es la **pendiente**: describe la inclinación.
    * Representa proporcionalidad directa: si $x=0$, entonces $y=0$.

    ---

    ### 🛡️ La Función Afín

    Forma: $f(x) = mx + n$
    * $m$: Pendiente.
    * $n$: **Coeficiente de posición** — donde la recta corta al eje $Y$ → punto $(0, n)$.
    * No pasa por el origen (a menos que $n=0$). Representa un valor inicial o cargo fijo.

    ---

    ### 🛡️ La Pendiente ($m$)

    Es la razón de cambio entre $y$ e $x$:
    $$m = \frac{y_2 - y_1}{x_2 - x_1}$$

    * $m > 0$: función **creciente** (sube).
    * $m < 0$: función **decreciente** (baja).
    * $m = 0$: función **constante** (línea horizontal).

    ---

    ### 🛡️ Modelamiento Afín

    Ejemplo: una empresa cobra $\$1.000$ de cargo fijo más $\$500$ por kilómetro.
    * Función: $C(x) = 500x + 1000$
    * $m = 500$ (costo por km), $n = 1000$ (cargo fijo).
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Lineal vs. Afín y Costo modelado")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        x = np.linspace(-3, 5, 100)
        axes[0].plot(x, 2*x, color='#1b5e20', lw=2.5, label=r'Lineal: $f(x)=2x$')
        axes[0].plot(x, 2*x + 3, color='#c0392b', lw=2.5, linestyle='--', label=r'Afín: $f(x)=2x+3$')
        axes[0].scatter([0], [0], color='#1b5e20', s=100, zorder=5)
        axes[0].scatter([0], [3], color='#c0392b', s=100, zorder=5)
        axes[0].axhline(0, color='black', lw=1); axes[0].axvline(0, color='black', lw=1)
        axes[0].set_title("Lineal pasa por origen; Afín tiene coef. de posición", fontsize=11, fontweight='bold')
        axes[0].legend(fontsize=10); axes[0].grid(True, alpha=0.3)

        km = np.linspace(0, 10, 100)
        costo = 1000 + 500*km
        axes[1].plot(km, costo, color='#1565c0', lw=2.5, label='$C(x) = 500x + 1000$')
        axes[1].scatter([0], [1000], color='#c0392b', s=100, zorder=5)
        axes[1].annotate('Cargo Fijo ($1.000)', xy=(0, 1000), xytext=(1.5, 1800),
                         arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
        axes[1].set_title("Modelamiento: costo fijo + variable", fontsize=11, fontweight='bold')
        axes[1].set_xlabel("Kilómetros"); axes[1].set_ylabel("Costo ($)")
        axes[1].legend(fontsize=10); axes[1].grid(True, alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería F02", expanded=False):
        st.markdown(r"""
### E01: Calcular pendiente

Puntos $(1, 2)$ y $(3, 10)$:
$$m = \frac{10-2}{3-1} = \frac{8}{2} = 4$$

### E02: Identificar componentes

$f(x) = -3x + 7$: $m = -3$ (decreciente), $n = 7$ (corte con eje $Y$).

### E03: Modelamiento

Una plataforma cobra $\$2.000$ fijos más $\$500$ por unidad:
$C(x) = 500x + 2000$ → en $x=0$: costo = $2.000$.
""")

    with st.expander("❓ Cuestionario F02: Funciones Lineal y Afín", expanded=False):
        quiz = [
            {"question": r"¿Cuál de las siguientes funciones es una función lineal?",
             "options": {"A": r"$f(x) = 2x + 1$", "B": r"$f(x) = x^2$", "C": r"$f(x) = -5x$", "D": r"$f(x) = 3$"},
             "answer": "C", "explanation": r"La lineal tiene forma $mx$ sin constante sumada ($n=0$)."},
            {"question": r"En $f(x) = -3x + 7$, ¿cuál es el coeficiente de posición?",
             "options": {"A": "-3", "B": "7", "C": "0", "D": "3"},
             "answer": "B", "explanation": "El coeficiente de posición es el número 'solo' sin acompañar a $x$."},
            {"question": r"Si una función tiene $m > 0$, su gráfica:",
             "options": {"A": "Es horizontal.", "B": "Baja de izquierda a derecha.", "C": "Sube de izquierda a derecha.", "D": "Es vertical."},
             "answer": "C", "explanation": "Pendiente positiva = crecimiento de izquierda a derecha."},
            {"question": r"¿Cuál es la pendiente de la recta que pasa por $(1,2)$ y $(3,10)$?",
             "options": {"A": "4", "B": "8", "C": "2", "D": "5"},
             "answer": "A", "explanation": r"$m = (10-2)/(3-1) = 8/2 = 4$."},
            {"question": r"Una empresa cobra $\$2.000$ fijos más $\$500$ por unidad. ¿Cuál es la función?",
             "options": {"A": r"$C(x) = 2000x + 500$", "B": r"$C(x) = 500 + 2000x$", "C": r"$C(x) = 500x + 2000$", "D": r"$C(x) = 2500x$"},
             "answer": "C", "explanation": r"Cargo fijo = $n = 2000$. Variable por unidad = $m = 500$."},
            {"question": r"¿Por qué la función lineal $f(x)=3x$ siempre pasa por el origen?",
             "options": {"A": "Porque $m=3$.", "B": "Porque tiene pendiente positiva.", "C": "Porque cuando $x=0$, $f(0)=0$.", "D": "Por definición de pendiente."},
             "answer": "C", "explanation": r"Cuando $x=0$: $f(0) = 3(0) = 0$. El punto $(0,0)$ siempre pertenece."},
            {"question": r"El punto de corte con el eje $Y$ de $f(x) = -2x + 5$ es:",
             "options": {"A": r"$(5, 0)$", "B": r"$(0, -2)$", "C": r"$(0, 5)$", "D": r"$(-2, 5)$"},
             "answer": "C", "explanation": r"El corte con el eje $Y$ es siempre $(0, n) = (0, 5)$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="f02_quiz")
