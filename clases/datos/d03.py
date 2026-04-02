import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_D03():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("D03: Medidas de Tendencia Central (MTC)")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ El Rigor Científico: Gauss, Laplace y el "Centro"

    Durante el siglo XVIII, la ciencia enfrentaba un problema: las mediciones astronómicas nunca eran exactas. Cada astrónomo obtenía un dato distinto. **Carl Friedrich Gauss** y **Pierre-Simon Laplace** propusieron que el valor más probable se encuentra en el "centro" donde los errores se compensan.

    ---

    ### 🛡️ Los Tres Pilares

    1. **Media Aritmética ($\bar{x}$):** El equilibrio de masas. Suma todos los valores y divide por el total.
       $$\bar{x} = \frac{\sum x_i}{n}$$

    2. **Mediana ($Me$):** El centro de posición. Al ordenar los datos, es el valor que deja el 50% a cada lado.
       * Si $n$ es impar: es el dato central.
       * Si $n$ es par: promedio de los dos datos centrales.

    3. **Moda ($Mo$):** El centro de repetición. Es el valor con mayor frecuencia absoluta.

    ---

    ### 🛡️ Simetría y Asimetría: Gauss vs. La Realidad

    **Distribución Simétrica (ideal):** Media = Mediana = Moda. Los datos forman una campana perfecta.

    **Distribución Asimétrica (real):** La media se "arrastra" hacia los extremos. Ejemplo: sueldos muy altos distorsionan la media hacia arriba, pero la mediana permanece más estable.

    > 💡 **Regla práctica:** Si hay valores extremos (como sueldos millonarios), la **Mediana** es más representativa que la Media.
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Distribución simétrica vs. asimétrica")
        try:
            from scipy import stats
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            datos_sim = [1, 2, 2, 3, 3, 3, 4, 4, 5]
            m_sim = np.mean(datos_sim); me_sim = np.median(datos_sim)
            axes[0].hist(datos_sim, bins=np.arange(0.5, 6.5, 1), color='#4285f4', edgecolor='black', alpha=0.7)
            axes[0].axvline(m_sim,  color='red',   lw=2.5, linestyle='--', label=f'Media = {m_sim:.1f}')
            axes[0].axvline(me_sim, color='green', lw=2.5, linestyle=':', label=f'Mediana = {me_sim:.1f}')
            axes[0].set_title("Distribución Simétrica\n(Media ≈ Mediana)", fontsize=12, fontweight='bold')
            axes[0].legend(fontsize=10); axes[0].grid(True, alpha=0.3)

            datos_asim = [1, 1, 2, 2, 2, 3, 3, 10, 20, 50]
            m_asim = np.mean(datos_asim); me_asim = np.median(datos_asim)
            axes[1].hist(datos_asim, bins=10, color='#ea4335', edgecolor='black', alpha=0.7)
            axes[1].axvline(m_asim,  color='red',   lw=2.5, linestyle='--', label=f'Media = {m_asim:.1f}')
            axes[1].axvline(me_asim, color='green', lw=2.5, linestyle=':', label=f'Mediana = {me_asim:.1f}')
            axes[1].set_title("Distribución Asimétrica\n(Media arrastrada por extremos)", fontsize=12, fontweight='bold')
            axes[1].legend(fontsize=10); axes[1].grid(True, alpha=0.3)

            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        except ImportError:
            st.info("Instala scipy para ver la distribución.")


    with st.expander("🚀 Guía de Ejemplos: Carpintería D03", expanded=False):
        st.markdown(r"""
### E01: Calcular Media, Mediana y Moda

**Datos:** $\{3, 5, 7, 7, 9, 11\}$ ($n=6$ par)

* **Media:** $(3+5+7+7+9+11)/6 = 42/6 = 7$
* **Mediana:** Promedio de 3° y 4° dato: $(7+7)/2 = 7$
* **Moda:** 7 (aparece 2 veces)

### E02: Media en tabla de frecuencias

| $x_i$ | $f_i$ | $x_i \cdot f_i$ |
| :---: | :---: | :---: |
| 4 | 3 | 12 |
| 5 | 2 | 10 |
| 6 | 5 | 30 |
| **Total** | **10** | **52** |

$\bar{x} = 52/10 = 5,2$

### E03: Elegir la medida correcta

En sueldos muy desiguales (mayoría gana poco, pocos ganan muchísimo), la **Mediana** es más representativa que la Media.
""")

    with st.expander("❓ Cuestionario D03: Medidas de Tendencia Central", expanded=False):
        quiz = [
            {"question": r"Si todos los valores de un conjunto aumentan en 5 unidades, ¿qué sucede con la media?",
             "options": {"A": "Se mantiene igual.", "B": "Aumenta en 5 unidades.", "C": r"Aumenta en $5 \times n$.", "D": "No se puede determinar."},
             "answer": "B", "explanation": "La media es una medida de posición; si todos se mueven, el centro se mueve igual."},
            {"question": r"En una distribución de sueldos donde la mayoría gana el mínimo y pocos ganan millones, ¿cuál es la medida más representativa?",
             "options": {"A": "La Media.", "B": "La Mediana.", "C": "La Moda.", "D": "El Rango."},
             "answer": "B", "explanation": "La Mediana ignora los extremos, siendo más 'honesta' en distribuciones asimétricas."},
            {"question": r"Si el conjunto es $\{2, 3, 3, 5, 8, 10\}$, ¿cuál es la Mediana?",
             "options": {"A": "3", "B": "4", "C": "5", "D": "4,5"},
             "answer": "B", "explanation": r"$n=6$ (par): promedio de 3° y 4° dato = $(3+5)/2 = 4$."},
            {"question": r"¿Cómo se llama la distribución donde Media, Mediana y Moda coinciden?",
             "options": {"A": "Asimétrica.", "B": "Bimodal.", "C": "Simétrica.", "D": "Amodal."},
             "answer": "C", "explanation": "Es el caso ideal de la campana de Gauss."},
            {"question": r"La suma de las desviaciones de cada dato respecto a su media $(\sum(x_i - \bar{x}))$ es siempre:",
             "options": {"A": "Un número positivo.", "B": "Un número negativo.", "C": "Cero.", "D": "La varianza."},
             "answer": "C", "explanation": "La media es el punto de equilibrio exacto: las desviaciones se cancelan."},
            {"question": r"Para hallar la Mediana en un conjunto de $n=8$ datos ordenados, el promedio es entre el:",
             "options": {"A": "4° y 5° dato.", "B": "3° y 6° dato.", "C": "1° y 8° dato.", "D": "Dato del centro."},
             "answer": "A", "explanation": r"Para $n$ par: promedio del $n/2$-ésimo y $(n/2+1)$-ésimo dato."},
            {"question": r"En una tabla, el dato '5' aparece con $f_i = 4$. ¿Cuál es la moda si ningún otro dato tiene esa frecuencia?",
             "options": {"A": "4.", "B": "20.", "C": "5.", "D": "No hay moda."},
             "answer": "C", "explanation": "La moda es el valor con mayor frecuencia, en este caso: 5."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="d03_quiz")
