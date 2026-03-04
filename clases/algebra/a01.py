import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_A01():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("A01: Lenguaje Algebraico — El Código de la Realidad")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)
        st.markdown(r"""
    ### 🛡️ De la Palabra al Símbolo

    Si el álgebra es un lenguaje, necesitamos un diccionario. Traducir del "español" al "matemático" es el primer paso para programar cualquier solución.

    * **El Sujeto:** Casi siempre es "un número", bautizado como $x$, $n$ o $a$.
    * **La Acción:** Son las operaciones.
        * "Aumentar" → sumar ($+$). "Diferencia" → restar ($-$).
        * "Factor/Producto" → multiplicar ($\cdot$). "Cociente/Razón" → dividir ($/$).

    ---

    ### 🛡️ El Orden de los Factores (La importancia de la precisión)

    En álgebra el orden de las palabras **cambia el resultado**.

    1. **El doble del sucesor** de $x$: primero sucesor $(x+1)$, luego duplicar → $2(x+1)$
    2. **El sucesor del doble** de $x$: primero duplicar $2x$, luego sumar uno → $2x+1$

    ---

    ### 🛡️ Las Relaciones de "Poder" (Potencias)

    * **El Cuadrado:** área, $x^2$.  **El Cubo:** volumen, $x^3$.

    > **Lección Magistral:** "La suma de los cuadrados" ($x^2 + y^2$) NO es lo mismo que "El cuadrado de la suma" $(x+y)^2$.
    > Con $x=3, y=4$:  $9+16=25$ vs $(7)^2=49$.  **¡Los paréntesis cambian todo!**

    ---

    ### 🛡️ Términos Semejantes: La Identidad

    Solo puedes fusionar términos que comparten **letra Y exponente**.
    * $3a + 2a = 5a$ ✅  |  $3a + 2b$ ✖ (letras distintas)  |  $3a + 2a^2$ ✖ (exponente distinto)
    """)
        st.markdown('</div>', unsafe_allow_html=True)

        # ── FIGURA ──────────────────────────────────────────────────────────────
        st.markdown("#### 📊 Visualización: Orden importa — Suma vs. Cuadrado de la suma")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

        xv = np.array([1, 2, 3, 4, 5])
        axes[0].plot(xv, 2*(xv+1), 'o-', color='#1b5e20', lw=2.5, markersize=7, label=r'$2(x+1)$ — Doble del sucesor')
        axes[0].plot(xv, 2*xv+1,   's--', color='#c0392b', lw=2.5, markersize=7, label=r'$2x+1$ — Sucesor del doble')
        axes[0].set_title("El orden cambia el resultado", fontsize=13, fontweight='bold')
        axes[0].set_xlabel("$x$"); axes[0].set_ylabel("Valor")
        axes[0].legend(fontsize=11); axes[0].grid(True, alpha=0.3)
        axes[0].axhline(0, color='black', lw=0.8)

        cats = [r'$a+b$', r'$(a+b)^2$', r'$a^2+b^2$']
        vals = [7, 49, 25]
        colors = ['#6C63FF', '#e74c3c', '#27ae60']
        bars = axes[1].bar(cats, vals, color=colors, edgecolor='black', alpha=0.85, width=0.5)
        axes[1].set_title(r"$a=3,\ b=4$: Suma vs. Cuadrado de la suma", fontsize=13, fontweight='bold')
        axes[1].set_ylabel("Resultado numérico")
        for bar, v in zip(bars, vals):
            axes[1].text(bar.get_x()+bar.get_width()/2, v+0.8, str(v),
                         ha='center', fontsize=14, fontweight='bold')
        axes[1].grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        # ── EJEMPLOS ────────────────────────────────────────────────────────────

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería A01", expanded=False):
        st.markdown(r"""
### E01: Diccionario algebraico básico

| Expresión verbal | Código algebraico | Notas |
| :--- | :---: | :--- |
| El triple de un número, aumentado en 8 | $3x + 8$ | La coma indica: primero multiplica, luego suma |
| El cuadrado de la diferencia entre $a$ y $b$ | $(a-b)^2$ | "De la diferencia" → paréntesis PRIMERO |
| La cuarta parte de $n$ | $n/4$ | Cuarta parte = dividir entre 4 |
| El producto de dos números consecutivos | $x(x+1)$ | Si el primero es $x$, el siguiente es $x+1$ |
| El exceso de $x$ sobre 100 | $x - 100$ | Exceso = cuánto más tiene $x$ que 100 |

---

### E02: Reducción de términos semejantes

**Situación:** Simplificar $4m - 2n + m + 5n$

1. Identificar familias: $4m$ y $m$ son semejantes; $-2n$ y $5n$ también.
2. Agrupar y operar: $(4m + m) + (-2n + 5n) = 5m + 3n$

---

### E03: El orden cambia el resultado

Si $x = 5$:

| Expresión | Cálculo | Resultado |
| :--- | :--- | :---: |
| $2(x+1)$ — Doble del sucesor | $2(5+1) = 2 \cdot 6$ | $12$ |
| $2x+1$ — Sucesor del doble | $2(5) + 1 = 11$ | $11$ |

**Son distintas** aunque suenen parecidas en español.
""")

    # ── QUIZ ────────────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario A01: Codificación de Enunciados", expanded=False):
        quiz = [
            {"question": r'¿Cómo se traduce "el triple de un número, aumentado en 8"?',
             "options": {"A": r"$3(x + 8)$", "B": r"$x^3 + 8$", "C": r"$3x + 8$", "D": r"$3x \cdot 8$"},
             "answer": "C", "explanation": r"La coma indica: primero multiplica por 3, luego suma 8."},
            {"question": r'¿Cuál es la expresión para "el cuadrado de la diferencia entre $a$ y $b$"?',
             "options": {"A": r"$a^2 - b^2$", "B": r"$(a - b)^2$", "C": r"$2(a - b)$", "D": r"$a - b^2$"},
             "answer": "B", "explanation": r'"De la diferencia" → el paréntesis encierra la resta antes de elevar.'},
            {"question": r'"La cuarta parte de un número $n$". ¿Cómo se escribe?',
             "options": {"A": r"$n - 4$", "B": r"$4n$", "C": r"$n^4$", "D": r"$n/4$"},
             "answer": "D", "explanation": "La cuarta parte es dividir en 4 partes iguales."},
            {"question": r'Si $x$ es un entero, ¿cómo representamos su "antecesor"?',
             "options": {"A": r"$x + 1$", "B": r"$x - 1$", "C": r"$2x$", "D": r"$x/2$"},
             "answer": "B", "explanation": "El antecesor es uno menos que $x$."},
            {"question": r'¿Qué representa $2x + 2$?',
             "options": {"A": "El doble de un número aumentado en 2.", "B": "El doble del sucesor de un número.", "C": r"El cuadrado de $x$ más 2.", "D": "La mitad más 2."},
             "answer": "A", "explanation": r"Multiplicas $x$ por 2 y sumas 2."},
            {"question": r'"El producto de dos números consecutivos". Forma algebraica:',
             "options": {"A": r"$x \cdot y$", "B": r"$x + (x+1)$", "C": r"$x(x+1)$", "D": r"$2x \cdot 2x$"},
             "answer": "C", "explanation": r"El punto representa el producto; el siguiente de $x$ es $x+1$."},
            {"question": r'Al simplificar $4m - 2n + m + 5n$, el resultado es:',
             "options": {"A": r"$5m + 3n$", "B": r"$3m + 3n$", "C": r"$5m + 7n$", "D": r"$8mn$"},
             "answer": "A", "explanation": r"$4m + m = 5m$; $-2n + 5n = 3n$."},
        ]
        render_multiple_choice_quiz(quiz, key_prefix="a01_quiz")

    # ── PAUTA ───────────────────────────────────────────────────────────────
    with st.expander("🔑 Pauta Técnica A01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | La coma indica: primero multiplica por 3, luego suma 8. |
| **2** | **B** | "De la diferencia" → el paréntesis envuelve la resta antes de elevar. |
| **3** | **D** | Cuarta parte = dividir entre 4. |
| **4** | **B** | Antecesor = uno menos. |
| **5** | **A** | $2x + 2$: doble de $x$, aumentado en 2. |
| **6** | **C** | Producto de $x$ por su consecutivo $(x+1)$. |
| **7** | **A** | Semejantes: $4m+m=5m$; $-2n+5n=3n$. |
""")
