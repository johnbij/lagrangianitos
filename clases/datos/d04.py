import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_D04():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("D04: El Arte del Promedio — Medias Simples y Compuestas")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ Crónica de la Precisión: Pierre-Simon Laplace

    Laplace decía que el azar no es más que nuestra falta de conocimiento, y que al promediar muchas mediciones, los errores individuales se cancelan, dejando brillar la "verdad" de los datos.

    ---

    ### 🛡️ Tipos de Promedio

    #### A) Media Simple (Datos sueltos)
    $$\bar{x} = \frac{\sum x_i}{n}$$

    #### B) Media en Tablas de Frecuencia (Ponderada por repetición)
    Cuando los datos se repiten, multiplica el dato por su frecuencia:
    $$\bar{x} = \frac{\sum x_i \cdot f_i}{n}$$

    #### C) Media en Datos Agrupados (Intervalos)
    Usa la **Marca de Clase ($m_i$)** — punto medio del intervalo — como representante:
    $$\bar{x} = \frac{\sum m_i \cdot f_i}{n}$$

    ---

    ### 🛡️ El Promedio de Promedios (Media Ponderada)

    ⚠️ **No puedes promediar dos promedios directamente si los grupos tienen distinto tamaño.**

    **Ejemplo:**
    * Grupo A (10 personas): promedio 5,0.
    * Grupo B (30 personas): promedio 7,0.
    * **Error común:** $(5,0 + 7,0) / 2 = 6,0$ ❌

    **La Carpintería Correcta:**
    $$\bar{x}_{total} = \frac{\bar{x}_A \cdot n_A + \bar{x}_B \cdot n_B}{n_A + n_B} = \frac{5,0\cdot10 + 7,0\cdot30}{40} = \frac{260}{40} = 6,5 \checkmark$$

    ---

    ### 🛡️ Propiedades que ahorran tiempo

    1. **Suma de desviaciones:** $\sum(x_i - \bar{x}) = 0$ siempre.
    2. **Linealidad:** Si a todos los datos se les suma una constante $k$, la media sube en $k$.
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Media ponderada vs. error común")
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        grupos = ['Grupo A\n(10 pers.)', 'Grupo B\n(30 pers.)', 'Promedio\nERROR', 'Promedio\nCORRECTO']
        valores = [5.0, 7.0, 6.0, 6.5]
        colors  = ['#4285f4', '#34a853', '#ea4335', '#1b5e20']
        alphas  = [0.8, 0.8, 0.5, 1.0]
        bars = axes[0].bar(grupos, valores, color=colors, edgecolor='black', alpha=0.85, width=0.6)
        axes[0].set_ylim(4, 8)
        axes[0].set_title("Media Ponderada: la trampa del promedio de promedios", fontsize=11, fontweight='bold')
        axes[0].set_ylabel("Promedio")
        for bar, v in zip(bars, valores):
            axes[0].text(bar.get_x()+bar.get_width()/2, v+0.05, str(v),
                         ha='center', fontsize=12, fontweight='bold')
        axes[0].axhline(6.5, color='#1b5e20', lw=2, linestyle='--', label='Correcto: 6,5')
        axes[0].axhline(6.0, color='#ea4335', lw=2, linestyle=':', label='Error: 6,0')
        axes[0].legend(fontsize=10)
        axes[0].grid(True, alpha=0.3, axis='y')

        x_i = [4, 5, 6]
        f_i = [3, 2, 5]
        xf  = [x*f for x,f in zip(x_i, f_i)]
        bar_labels = [f'$x_i={x}$\n$f_i={f}$\n$x_i\cdot f_i={xf[i]}$' for i,(x,f) in enumerate(zip(x_i,f_i))]
        axes[1].bar(range(3), xf, color=['#4285f4','#ea4335','#fbbc04'], edgecolor='black', alpha=0.85)
        axes[1].set_xticks(range(3)); axes[1].set_xticklabels(bar_labels, fontsize=10)
        axes[1].set_title(f"Media en tabla: $\\bar{{x}} = 52/10 = 5,2$", fontsize=12, fontweight='bold')
        axes[1].set_ylabel(r"$x_i \cdot f_i$")
        axes[1].grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería D04", expanded=False):
        st.markdown(r"""
### E01: Media simple

5 edades: 12, 15, 15, 18, 20 → $\bar{x} = (12+15+15+18+20)/5 = 80/5 = 16$

### E02: Media en tabla de frecuencias

| $x_i$ | $f_i$ | $x_i \cdot f_i$ |
| :---: | :---: | :---: |
| 4 | 3 | 12 |
| 5 | 2 | 10 |
| 6 | 5 | 30 |
| **Total** | **10** | **52** |

$\bar{x} = 52/10 = 5,2$

### E03: Media ponderada

Grupos A (n=10, $\bar{x}=5,0$) y B (n=20, $\bar{x}=6,5$):

$\bar{x}_{total} = \dfrac{5,0\cdot10 + 6,5\cdot20}{30} = \dfrac{50+130}{30} = 6,0$
""")

    with st.expander("❓ Cuestionario D04: El Arte del Promedio", expanded=False):
        quiz = [
            {"question": r"5 amigos tienen edades: 12, 15, 15, 18, 20. ¿Cuál es la edad promedio?",
             "options": {"A": "15", "B": "16", "C": "17", "D": "18"},
             "answer": "B", "explanation": r"$(12+15+15+18+20)/5 = 80/5 = 16$."},
            {"question": r"En tabla: $x_i=4$ ($f_i=3$), $x_i=5$ ($f_i=2$), $x_i=6$ ($f_i=5$). ¿Cuál es la media?",
             "options": {"A": "5,0", "B": "5,2", "C": "5,3", "D": "5,5"},
             "answer": "B", "explanation": r"$(4\cdot3+5\cdot2+6\cdot5)/(3+2+5) = 52/10 = 5,2$."},
            {"question": r"Para calcular la media en datos agrupados en intervalos, se usa:",
             "options": {"A": "El límite inferior.", "B": "El límite superior.", "C": "La marca de clase (punto medio).", "D": "La amplitud del intervalo."},
             "answer": "C", "explanation": "La marca de clase es el representante único de cada intervalo."},
            {"question": r"El promedio de 6 números es 12. Se agrega un 7° número y el nuevo promedio es 13. ¿Cuál es el 7° número?",
             "options": {"A": "13", "B": "15", "C": "18", "D": "19"},
             "answer": "D", "explanation": r"Suma original: $6\cdot12=72$. Nueva suma: $7\cdot13=91$. Número: $91-72=19$."},
            {"question": r"Grupo A (10 pers., promedio 5,0) y Grupo B (20 pers., promedio 6,5). ¿Cuál es la media ponderada?",
             "options": {"A": "5,75", "B": "5,5", "C": "6,0", "D": "6,25"},
             "answer": "C", "explanation": r"$(5,0\cdot10 + 6,5\cdot20)/30 = 180/30 = 6,0$."},
            {"question": r"Si a todos los datos se les suma una constante $k$, ¿qué pasa con la media?",
             "options": {"A": "Se multiplica por $k$.", "B": "Aumenta en $k$.", "C": "No cambia.", "D": "Depende de $n$."},
             "answer": "B", "explanation": "Propiedad de linealidad: la media sube exactamente en $k$."},
            {"question": r"¿Cuál es el error al promediar directamente dos promedios de grupos de distinto tamaño?",
             "options": {"A": "Se ignora la moda.", "B": "Se ignora el peso (tamaño) de cada grupo.", "C": "Se usan datos incorrectos.", "D": "Se confunden media y mediana."},
             "answer": "B", "explanation": "El error clásico: no ponderar por el tamaño de cada grupo."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="d04_quiz")

    with st.expander("🔑 Pauta Técnica D04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $80/5=16$. |
| **2** | **B** | $52/10=5,2$. |
| **3** | **C** | Marca de clase = punto medio del intervalo. |
| **4** | **D** | $7\cdot13-6\cdot12=91-72=19$. |
| **5** | **C** | $(50+130)/30=6,0$. |
| **6** | **B** | Linealidad: media sube en $k$. |
| **7** | **B** | Falta ponderar por el tamaño de cada grupo. |
""")
