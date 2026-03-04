import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_D01():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("D01: Epistemología — Historia y la Necesidad de Medir")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ Contexto Histórico: El Control del Caos

    La estadística no nació en un laboratorio, nació en los palacios y en las morgues por una necesidad puramente práctica.

    * **La Necesidad de Estado:** Desde el Antiguo Egipto hasta el Imperio Romano, la estadística era "Censo". De ahí su nombre: *Statisticum* (relativo al Estado).
    * **La Peste y el Nacimiento de la Tendencia:** En el Londres del siglo XVII, **John Graunt** fue el primero en notar que, aunque la muerte de una persona parece azarosa, la de miles sigue un **patrón predecible**.
    * **La Ingeniería y la Calidad:** Con la Revolución Industrial, la estadística pasó de "contar gente" a "asegurar procesos", controlando la variabilidad inevitable de materiales y naturaleza.

    ---

    ### 🛡️ El Concepto de Incertidumbre

    En la ciencia existen dos tipos de fenómenos:
    1. **Deterministas:** Si sueltas una piedra, cae. El resultado es único y predecible.
    2. **Aleatorios:** Si lanzas un dado o mides una pieza fabricada, el resultado varía. Aquí entra la Estadística: el estudio científico de la **variabilidad**.

    ---

    ### 🛡️ Población, Muestra y el "Salto" Inferencial

    * **Población ($N$):** El universo completo. Su medida se llama **Parámetro** (la verdad absoluta, muchas veces inalcanzable).
    * **Muestra ($n$):** La parte que realmente medimos. Su medida se llama **Estadístico**.

    **Regla mnemotécnica: PP-EM → Parámetro para la Población, Estadístico para la Muestra.**

    La inferencia estadística es el "salto" desde lo que vemos en la muestra hacia lo que concluimos de la población.
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Variables y tipos de datos")
        fig, axes = plt.subplots(1, 2, figsize=(13, 5))

        categorias = ['Matemática', 'Lenguaje', 'Historia', 'Cs. Naturales', 'Ed. Física']
        puntajes   = [450, 520, 410, 480, 390]
        colors     = ['#4285f4','#ea4335','#fbbc04','#34a853','#9b59b6']
        axes[0].bar(categorias, puntajes, color=colors, edgecolor='black', alpha=0.85)
        axes[0].set_title("Ejemplo: Puntaje promedio por ramo", fontsize=12, fontweight='bold')
        axes[0].set_ylabel("Puntaje"); axes[0].set_ylim(300, 600)
        axes[0].grid(True, alpha=0.3, axis='y')
        for i, v in enumerate(puntajes):
            axes[0].text(i, v+3, str(v), ha='center', fontsize=10, fontweight='bold')

        tipos  = ['Cuantitativa\nContinua', 'Cuantitativa\nDiscreta', 'Cualitativa\nOrdinal', 'Cualitativa\nNominal']
        ejems  = ['Temperatura\nAltura\nPeso', 'Nº de hijos\nNº de fallas\nPuntaje', 'Nivel de\nEducación\nGrado', 'Color\nNacionalidad\nSexo']
        y_pos  = [3, 2, 1, 0]
        axes[1].axis('off')
        for y, t, e in zip(y_pos, tipos, ejems):
            axes[1].text(0.05, y/3+0.08, t, fontsize=11, fontweight='bold',
                         bbox=dict(boxstyle='round', facecolor='#e3f2fd', alpha=0.7))
            axes[1].text(0.55, y/3+0.08, e, fontsize=9, color='#333', va='center')
        axes[1].set_xlim(0, 1); axes[1].set_ylim(-0.1, 1.3)
        axes[1].set_title("Clasificación de variables", fontsize=12, fontweight='bold')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería D01", expanded=False):
        st.markdown(r"""
### E01: Identificar Población vs. Muestra

**Situación:** Un investigador encuesta a 500 universitarios para saber cuántas horas estudian.

| Concepto | En este caso |
| :--- | :--- |
| Población | Todos los universitarios del país |
| Muestra | Los 500 encuestados |
| Parámetro | La media real de horas de toda la población |
| Estadístico | La media calculada con los 500 encuestados |

### E02: Clasificar variables

| Variable | Tipo |
| :--- | :--- |
| Temperatura corporal | Cuantitativa continua |
| Número de hermanos | Cuantitativa discreta |
| Nivel de satisfacción (bajo/medio/alto) | Cualitativa ordinal |
| Color de ojos | Cualitativa nominal |
""")

    with st.expander("❓ Cuestionario D01: Fundamentos e Historia", expanded=False):
        quiz = [
            {"question": r'¿Qué motivó el análisis de las "Tablas de Mortalidad" por John Graunt?',
             "options": {"A": "Inventar los seguros de vida modernos.", "B": "Encontrar patrones de salud pública ante las pestes.", "C": "Inventariar las riquezas del reino.", "D": "El estudio de juegos de azar."},
             "answer": "B", "explanation": "Graunt buscaba predecir tendencias de mortalidad cuando las epidemias parecían sin regla."},
            {"question": r"Si un equipo analiza 50 vigas de un lote de 5.000, ¿cómo se llaman esas 50 vigas?",
             "options": {"A": "Población.", "B": "Parámetro.", "C": "Muestra.", "D": "Estadístico."},
             "answer": "C", "explanation": "La muestra es el subconjunto representativo que se extrae para ser estudiado."},
            {"question": r"La medida calculada a partir de una muestra se llama:",
             "options": {"A": "Parámetro.", "B": "Estadístico.", "C": "Coeficiente.", "D": "Inferencia."},
             "answer": "B", "explanation": "PP-EM: Estadístico para la Muestra."},
            {"question": r"¿Cuál de las siguientes es una variable cuantitativa continua?",
             "options": {"A": "Número de hermanos.", "B": "Estadístico.", "C": "Temperatura corporal.", "D": "Nivel de educación."},
             "answer": "C", "explanation": "Continua: puede tomar cualquier valor (decimales) en un rango."},
            {"question": r"La inferencia estadística consiste en:",
             "options": {"A": "Calcular promedios de datos exactos.", "B": "Extrapolar conclusiones de la muestra hacia la población.", "C": "Contar datos en una tabla.", "D": "Construir gráficos de barras."},
             "answer": "B", "explanation": "Inferir es 'saltar' de lo observado en la muestra hacia la población."},
            {"question": r"El nivel de satisfacción 'bajo/medio/alto' es una variable:",
             "options": {"A": "Cuantitativa discreta.", "B": "Cuantitativa continua.", "C": "Cualitativa ordinal.", "D": "Cualitativa nominal."},
             "answer": "C", "explanation": "Hay jerarquía (uno es 'mayor' que otro) pero no son números."},
            {"question": r"¿Por qué la estadística es esencial en ingeniería?",
             "options": {"A": "Para calcular exactamente cada pieza.", "B": "Para diseñar gráficos bonitos.", "C": "Para controlar y predecir la variabilidad inevitable.", "D": "Para evitar usar matemáticas."},
             "answer": "C", "explanation": "La estadística controla la variabilidad en los procesos industriales."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="d01_quiz")

    with st.expander("🔑 Pauta Técnica D01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | Graunt buscaba patrones en las epidemias. |
| **2** | **C** | Subconjunto representativo = muestra. |
| **3** | **B** | PP-EM: **E**stadístico para la **M**uestra. |
| **4** | **C** | Temperatura = continua (decimales posibles). |
| **5** | **B** | Inferencia = saltar de muestra a población. |
| **6** | **C** | Con jerarquía y no numérica = ordinal. |
| **7** | **C** | Estadística controla la variabilidad. |
""")
