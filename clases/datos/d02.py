import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """<style>.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }</style>"""

def render_D02():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("D02: Organización y Visualización de Datos")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ El Surgimiento del Orden

    Hacia 1880, el censo de EE.UU. tardaba 7 años en tabularse a mano. **Herman Hollerith** diseñó una máquina de tarjetas perforadas que lo procesó en meses. Esa capacidad de **tabular** permitió el nacimiento de la computación moderna.

    En ingeniería, el dato crudo no sirve. Necesitamos estructuras que revelen patrones ocultos.

    ---

    ### 🛡️ El Lenguaje de los Subíndices

    Cuando veas letras con subíndices (como $f_i$), piensa en una **dirección de celda**. El índice $i$ es el número de fila.

    | Índice ($i$) | Categoría ($x_i$) | Frecuencia ($f_i$) |
    | :---: | :--- | :---: |
    | **1** | Perros | **12** → $f_1 = 12$ |
    | **2** | Gatos | **8** → $f_2 = 8$ |
    | **3** | Peces | **5** → $f_3 = 5$ |
    | | **TOTAL ($n$)** | **25** |

    ---

    ### 🛡️ Anatomía de la Tabla Técnica

    Una tabla profesional tiene:
    1. **$i$:** Índice o número de fila.
    2. **$f_i$:** Frecuencia Absoluta (conteo). Suma total = $n$.
    3. **$F_i$:** Frecuencia Acumulada. El último valor = $n$.
    4. **$h_i$:** Frecuencia Relativa ($f_i / n$). Suma total = 1 (o 100%).
    5. **$m_c$:** Marca de Clase (punto medio de un intervalo).

    ---

    ### 🛡️ Tipos de Gráficos

    * **Barras:** Para frecuencias de categorías separadas.
    * **Circular (Sectores):** Para mostrar proporciones del total.
    * **Histograma:** Para datos continuos agrupados en intervalos. Las barras se **tocan** (no hay espacio entre ellas).
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("#### 📊 Visualización: Tabla de frecuencias y gráficos")
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        cats = ['X', 'Y', 'Z']
        fi   = [25, 40, 35]
        Fi   = [25, 65, 100]
        colors = ['#4285f4', '#ea4335', '#fbbc04']

        # Tabla
        axes[0].axis('off')
        table_data = [[cats[i], fi[i], Fi[i], f'{fi[i]}%'] for i in range(3)]
        table_data.append(['Total', 100, '-', '100%'])
        tbl = axes[0].table(cellText=table_data,
                            colLabels=['$x_i$', '$f_i$', '$F_i$', '$h_i$'],
                            loc='center', cellLoc='center')
        tbl.scale(1, 2.5); tbl.auto_set_font_size(False); tbl.set_fontsize(12)
        axes[0].set_title("Tabla de Frecuencias", fontsize=12, fontweight='bold', pad=20)

        axes[1].bar(cats, fi, color=colors, edgecolor='black', alpha=0.85)
        axes[1].set_title("Gráfico de Barras", fontsize=12, fontweight='bold')
        axes[1].set_ylabel("Frecuencia Absoluta")
        for i, v in enumerate(fi):
            axes[1].text(i, v+0.5, str(v), ha='center', fontsize=11, fontweight='bold')
        axes[1].grid(True, alpha=0.3, axis='y')

        axes[2].pie(fi, labels=[f'{c}\n({v}%)' for c,v in zip(cats,fi)],
                    autopct='%1.1f%%', startangle=90, colors=colors,
                    wedgeprops=dict(edgecolor='black', lw=1.2))
        axes[2].set_title("Gráfico Circular (Sectores)", fontsize=12, fontweight='bold')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()


    with st.expander("🚀 Guía de Ejemplos: Carpintería D02", expanded=False):
        st.markdown(r"""
### E01: Construir tabla de frecuencias

**Datos:** 10 páginas web con links rotos: `3, 1, 0, 3, 1, 1, 0, 2, 3, 1`

| $i$ | $x_i$ | $f_i$ | $F_i$ | $h_i$ |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 2 | 2 | 0,2 |
| 2 | 1 | 4 | 6 | 0,4 |
| 3 | 2 | 1 | 7 | 0,1 |
| 4 | 3 | 3 | 10 | 0,3 |
| | **Total** | **10** | | **1,0** |

### E02: Calcular ángulo del sector circular

Si $f_i = 25$ y $n = 100$: ángulo $= (25/100) \times 360° = 90°$

### E03: Marca de clase

Para el intervalo $[20, 30[$: $m_c = (20+30)/2 = 25$
""")

    with st.expander("❓ Cuestionario D02: Organización y Representación", expanded=False):
        quiz = [
            {"question": r"Si la tabla de categorías X, Y, Z tiene $f_i = [25, 40, 35]$, ¿cuál es el tamaño de la muestra $n$?",
             "options": {"A": "25", "B": "60", "C": "100", "D": "40"},
             "answer": "C", "explanation": r"$n = \sum f_i = 25+40+35 = 100$."},
            {"question": r"¿Cuál es la frecuencia relativa acumulada ($H_i$) hasta la segunda categoría (Y)?",
             "options": {"A": "0,25", "B": "0,65", "C": "0,40", "D": "1,00"},
             "answer": "B", "explanation": r"$F_2=65$; $H_2=65/100=0,65$."},
            {"question": r"Si un sector del gráfico circular tiene un ángulo de 72° y la muestra es de 200 personas, ¿cuántas personas representa?",
             "options": {"A": "20", "B": "40", "C": "72", "D": "14"},
             "answer": "B", "explanation": r"$(72/360) \times 200 = 0,2 \times 200 = 40$."},
            {"question": r"¿Quién fue el pionero de la visualización de datos moderna (gráficos de barras y torta)?",
             "options": {"A": "Herman Hollerith", "B": "John Graunt", "C": "William Playfair", "D": "Carl Gauss"},
             "answer": "C", "explanation": "Playfair fue el pionero de la visualización de datos moderna."},
            {"question": r"En un histograma, ¿qué representa la 'Marca de Clase'?",
             "options": {"A": "El límite inferior del intervalo.", "B": "El límite superior del intervalo.", "C": "El punto medio del intervalo.", "D": "El total de datos del intervalo."},
             "answer": "C", "explanation": "La marca de clase es el punto medio que 'da la cara' por el intervalo."},
            {"question": r"¿Cuál es la diferencia clave entre un gráfico de barras y un histograma?",
             "options": {"A": "El histograma es para categorías; las barras para datos continuos.", "B": "En el histograma las barras se tocan (datos continuos); en el de barras no.", "C": "No hay diferencia.", "D": "El histograma usa colores y el de barras no."},
             "answer": "B", "explanation": "Las barras del histograma se tocan porque los intervalos son contiguos (datos continuos)."},
            {"question": r"Si $h_i = 0,15$ en una muestra de 100 personas, ¿cuántas personas corresponden?",
             "options": {"A": "1,5", "B": "85", "C": "15", "D": "150"},
             "answer": "C", "explanation": r"$0,15 \times 100 = 15$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="d02_quiz")
