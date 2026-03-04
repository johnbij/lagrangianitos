import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_F03():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("F03: Análisis y Comparación de Funciones")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ Modelamiento de Situaciones Reales

    Para llevar un problema a una función, identifica:
    * **Valor Fijo ($n$):** Lo que se paga sí o sí (cargo fijo, base, cuota inicial).
    * **Valor Variable ($m$):** Lo que depende de la cantidad (precio por minuto, km, unidad).

    ---

    ### 🛡️ Comparación de Funciones (Intersección)

    Cuando comparamos dos planes (Plan A y Plan B), buscamos el punto donde ambos cobran lo mismo. Técnica: **igualar las funciones**:
    $$f(x) = g(x)$$

    ---

    ### 🛡️ Interpretación de la Gráfica

    * **Punto de intersección:** momento en que ambos planes cuestan lo mismo.
    * **Antes del punto:** conviene el plan con la línea más baja.
    * **Después del punto:** conviene el otro.

    ---

    ### 🛡️ Desplazamientos y Cambios

    * Aumenta el **cargo fijo ($n$)** → la recta sube paralelamente.
    * Aumenta el **costo variable ($m$)** → la recta se vuelve más empinada.
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Comparación de planes — Punto de equilibrio")
        fig, axes = plt.subplots(1, 2, figsize=(13, 5))

        x = np.linspace(0, 80, 200)
        plan_a = 100*x + 5000
        plan_b = 200*x

        axes[0].plot(x, plan_a, color='#1565c0', lw=2.5, label='Plan A: $100x + 5000$')
        axes[0].plot(x, plan_b, color='#c0392b', lw=2.5, label='Plan B: $200x$')
        axes[0].scatter([50], [10000], color='black', s=120, zorder=5)
        axes[0].annotate('Cruce: $x = 50$ min\n$\\$10.000$', xy=(50, 10000), xytext=(35, 11500),
                         arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
        axes[0].fill_between(x, plan_a, plan_b, where=(x < 50), alpha=0.10, color='#c0392b',
                             label='B más barato')
        axes[0].fill_between(x, plan_a, plan_b, where=(x > 50), alpha=0.10, color='#1565c0',
                             label='A más barato')
        axes[0].set_title("Plan A vs Plan B: ¿cuándo conviene cada uno?", fontsize=12, fontweight='bold')
        axes[0].set_xlabel("Minutos"); axes[0].set_ylabel("Costo ($)")
        axes[0].legend(fontsize=9); axes[0].grid(True, alpha=0.3)

        km = np.linspace(0, 10, 100)
        base  = 1000 + 500*km
        alto  = 1800 + 500*km
        steep = 1000 + 800*km
        axes[1].plot(km, base,  color='#1b5e20', lw=2.5, label='Original: $500x+1000$')
        axes[1].plot(km, alto,  color='#f39c12', lw=2,   linestyle='--', label='Mayor $n$: $500x+1800$')
        axes[1].plot(km, steep, color='#c0392b', lw=2,   linestyle=':', label='Mayor $m$: $800x+1000$')
        axes[1].set_title("Efecto de cambiar $m$ o $n$", fontsize=12, fontweight='bold')
        axes[1].set_xlabel("Kilómetros"); axes[1].set_ylabel("Costo ($)")
        axes[1].legend(fontsize=9); axes[1].grid(True, alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería F03", expanded=False):
        st.markdown(r"""
### E01: Modelar un plan

Plan A: $\$5.000$ base + $\$100$/min → $f(x) = 100x + 5000$
Plan B: sin base, $\$200$/min → $g(x) = 200x$

### E02: Encontrar el punto de cruce

$100x + 5000 = 200x$
$5000 = 100x$
$x = 50$ minutos

### E03: Interpretar la comparación

| Uso | Plan más barato |
| :--- | :--- |
| Menos de 50 min | Plan B (sin cargo fijo) |
| Exactamente 50 min | Iguales |
| Más de 50 min | Plan A (pendiente menor) |
""")

    with st.expander("❓ Cuestionario F03: Funciones en Contexto", expanded=False):
        quiz = [
            {"question": r"El Plan A cobra $\$5.000$ base + $\$100$/min. ¿Cuál es su función?",
             "options": {"A": r"$f(x) = 5000x + 100$", "B": r"$f(x) = 100x + 5000$", "C": r"$f(x) = 5100x$", "D": r"$f(x) = 100x$"},
             "answer": "B", "explanation": r"Cargo fijo $n=5000$; costo variable $m=100$."},
            {"question": r"El Plan B cobra $\$200$/min sin base. ¿A cuántos minutos ambos planes cobran igual?",
             "options": {"A": "50 min", "B": "100 min", "C": "25 min", "D": "500 min"},
             "answer": "A", "explanation": r"$100x+5000=200x$ → $x=50$."},
            {"question": r"En $C(x) = 300x + 1500$, ¿qué representa el 1500?",
             "options": {"A": "Costo por unidad.", "B": "Unidades vendidas.", "C": "Costo fijo.", "D": "La pendiente."},
             "answer": "C", "explanation": "El valor que no depende de $x$ es el costo fijo."},
            {"question": r"Si dos funciones tienen el mismo $m$ pero distinto $n$, sus gráficas son:",
             "options": {"A": "Rectas que se cortan en el origen.", "B": "Perpendiculares.", "C": "Paralelas.", "D": "La misma recta."},
             "answer": "C", "explanation": "Misma inclinación, distinto punto de partida → paralelas."},
            {"question": r"Una cuenta de agua: $\$3.000$ fijo + $\$800$/m³. ¿Cuántos m³ si pagó $\$15.000$?",
             "options": {"A": "15", "B": "18.75", "C": "12", "D": "15"},
             "answer": "D", "explanation": r"$800x+3000=15000$ → $800x=12000$ → $x=15$."},
            {"question": r"Si una recta comienza en $(0,0)$, podemos afirmar que:",
             "options": {"A": "No hay costos variables.", "B": "El cargo fijo es cero (función lineal).", "C": "El costo es constante.", "D": "La pendiente es cero."},
             "answer": "B", "explanation": "Parte del origen → no hay cargo fijo → función lineal pura."},
            {"question": r"$E(x) = 500x + 2000$ (envío de paquetes). ¿Cuánto aumenta el costo por cada kg extra?",
             "options": {"A": "$2.000$", "B": "$2.500$", "C": "$500$", "D": "$1.000$"},
             "answer": "C", "explanation": r"La pendiente $m=500$ es el costo adicional por unidad."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="f03_quiz")

    with st.expander("🔑 Pauta Técnica F03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $n=5000$ (fijo); $m=100$ (variable). |
| **2** | **A** | $100x+5000=200x$ → $x=50$. |
| **3** | **C** | Valor independiente de $x$ = costo fijo. |
| **4** | **C** | Misma pendiente, distinto origen → paralelas. |
| **5** | **D** | $800x=12000$ → $x=15$. |
| **6** | **B** | Origen = sin cargo fijo = función lineal. |
| **7** | **C** | $m=500$ → costo extra por kg. |
""")
