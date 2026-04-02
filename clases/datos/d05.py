import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_D05():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("D05: Medidas de Posición — Cuartiles, Percentiles y Boxplot")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ Sir Francis Galton y la Clasificación

    A finales del siglo XIX, **Galton** se dio cuenta de que el "promedio" no era suficiente para entender una población. Necesitaba saber quiénes estaban en el 10% más alto o el 25% más bajo. Así inventó los **Percentiles**.

    ---

    ### 🛡️ Cuartiles y Percentiles

    Las medidas de posición dividen los datos **ordenados** en partes iguales:

    1. **Cuartiles ($Q_k$):** Dividen en **4 partes** iguales (cada 25%).
       * $Q_1$: supera al 25% de los datos.
       * $Q_2$: supera al 50% (≡ **Mediana**).
       * $Q_3$: supera al 75% de los datos.

    2. **Percentiles ($P_k$):** Dividen en **100 partes** iguales.
       * $P_{80}$ significa que el 80% de los datos es igual o menor a ese valor.

    ---

    ### 🛡️ Rango Intercuartil (RIC)

    Mide la dispersión del 50% central de los datos:
    $$RIC = Q_3 - Q_1$$

    ---

    ### 🛡️ El Diagrama de Cajón (Boxplot)

    Visualiza los 5 números resumen de los datos:
    * **Mínimo** | **$Q_1$** | **Mediana ($Q_2$)** | **$Q_3$** | **Máximo**

    El ancho de la **caja** es el RIC. Los **bigotes** se extienden al mínimo y máximo (o hasta 1,5 RIC en versiones con outliers).
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Boxplot anotado y comparación de distribuciones")
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        datos = [5, 20, 22, 24, 25, 26, 27, 28, 40, 42, 65]
        bp = axes[0].boxplot(datos, vert=False, patch_artist=True, whis=np.inf,
                             boxprops=dict(facecolor='#4285f4', color='black', alpha=0.7),
                             medianprops=dict(color='red', linewidth=3))
        q1, q2, q3 = np.percentile(datos, [25, 50, 75])
        min_v, max_v = min(datos), max(datos)
        for val, lbl in [(min_v,'Mín'), (q1,'Q₁'), (q2,'Mediana'), (q3,'Q₃'), (max_v,'Máx')]:
            axes[0].axvline(val, color='gray', lw=1, linestyle=':')
            axes[0].text(val, 1.18, f'{lbl}\n{val}', ha='center', fontsize=9, fontweight='bold')
        axes[0].set_title("Boxplot: 5 números resumen", fontsize=12, fontweight='bold')
        axes[0].set_yticks([]); axes[0].grid(True, alpha=0.3, axis='x')

        d1 = [10, 11, 12, 13, 14, 15, 30, 50, 80, 120]
        d2 = [20, 25, 28, 30, 31, 32, 33, 35, 38, 40]
        axes[1].boxplot([d1, d2], vert=False, patch_artist=True, whis=np.inf,
                        boxprops=dict(facecolor='#fbbc04', alpha=0.7),
                        medianprops=dict(color='red', linewidth=2.5))
        axes[1].set_yticklabels(['Asimétrica\n(cola derecha)', 'Simétrica\n(concentrada)'], fontsize=10)
        axes[1].set_title("Comparación: asimétrica vs. simétrica", fontsize=12, fontweight='bold')
        axes[1].grid(True, alpha=0.3, axis='x')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería D05", expanded=False):
        st.markdown(r"""
### E01: Calcular Cuartiles

**Datos ordenados (n=12):** 2, 4, 5, 6, 8, 9, 10, 11, 14, 15, 18, 20

Posición $Q_1 = (25\cdot12)/100 = 3$ → 3er dato = **5**
Posición $Q_2 = (50\cdot12)/100 = 6$ → 6to dato = **9** (Mediana)
Posición $Q_3 = (75\cdot12)/100 = 9$ → 9no dato = **14**

$RIC = 14 - 5 = 9$

### E02: Percentil en tabla

Muestra de $n=80$. Posición $P_{50} = (50\cdot80)/100 = 40$.
Si $F_2 = 35$ y $F_3 = 55$, el dato 40 cae en la fila 3 → $P_{50}$ pertenece al intervalo de la 3ª fila.

### E03: Interpretar un Boxplot

* **Caja larga → alta dispersión** en el 50% central.
* **Bigote muy largo a la derecha → asimetría positiva** (datos extremos altos).
* **Mediana cerca del Q₁ → concentración en la parte baja** de los datos.
""")

    with st.expander("❓ Cuestionario D05: Medidas de Posición", expanded=False):
        quiz = [
            {"question": r"Un estudiante está en el percentil 85. Esto significa que:",
             "options": {"A": "Obtuvo 85% de correctas.", "B": "El 85% de sus compañeros obtuvo igual o mayor.", "C": "Superó o igualó al 85% de los estudiantes.", "D": "Le falta 15% para el promedio."},
             "answer": "C", "explanation": "El percentil $k$ indica que el $k$% de los datos son iguales o menores."},
            {"question": r"¿A qué medida de tendencia central equivale siempre el segundo cuartil ($Q_2$)?",
             "options": {"A": "La Media.", "B": "La Moda.", "C": "La Mediana.", "D": "El Rango."},
             "answer": "C", "explanation": r"$Q_2$ divide la muestra al 50%, igual que la Mediana."},
            {"question": r"Si la muestra tiene $n=120$, ¿en qué posición se encuentra el $Q_1$?",
             "options": {"A": "Posición 25.", "B": "Posición 30.", "C": "Posición 40.", "D": "Posición 60."},
             "answer": "B", "explanation": r"$Q_1 = (25\cdot120)/100 = 30$."},
            {"question": r"¿Qué mide el Rango Intercuartil (RIC)?",
             "options": {"A": "La diferencia entre el máximo y el mínimo.", "B": "La dispersión del 50% central de los datos.", "C": "La distancia entre la media y la mediana.", "D": "El total de datos."},
             "answer": "B", "explanation": r"$RIC = Q_3 - Q_1$ captura la dispersión del corazón de los datos."},
            {"question": r"En un Boxplot, ¿qué representa la línea dentro de la caja?",
             "options": {"A": r"La Media.", "B": r"El $Q_1$.", "C": r"La Mediana ($Q_2$).", "D": "El Rango."},
             "answer": "C", "explanation": "La línea interior de la caja es siempre la Mediana."},
            {"question": r"¿Cuántos datos representa el $Q_3$ en una muestra de 100 personas?",
             "options": {"A": "3 personas.", "B": "25 personas.", "C": "75 personas.", "D": "3% de las personas."},
             "answer": "C", "explanation": r"$Q_3$ supera al 75% de los datos = 75 personas."},
            {"question": r"Si en un Boxplot el bigote derecho es mucho más largo que el izquierdo, la distribución es:",
             "options": {"A": "Simétrica.", "B": "Asimétrica negativa (cola izquierda).", "C": "Asimétrica positiva (cola derecha).", "D": "Bimodal."},
             "answer": "C", "explanation": "Bigote largo a la derecha = cola hacia la derecha = asimetría positiva."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="d05_quiz")
