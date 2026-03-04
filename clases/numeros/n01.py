import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def render_N01():

    # ── TÍTULO Y SECCIONES 1-3 ───────────────────────────────────────────────
    st.markdown("""
## N01: Teoría de Conjuntos - El Lenguaje Maestro

---

### 🛡️  El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás. A menudo, nos enseñan que las matemáticas son un conjunto de reglas para calcular el vuelto o aprobar un examen, pero eso es como decir que la música es solo saber apretar teclas. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.

Este eje de **Números** no se trata de hacer cuentas rápidas; se trata de aprender a clasificar el caos. Durante las próximas unidades, descubriremos que los números no están "tirados" en el espacio, sino que habitan en estructuras organizadas llamadas **Conjuntos**. Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer fronteras y a entender que todo gran sistema se basa en quién pertenece a qué y bajo qué reglas. Prepárate para una apertura de mente donde el infinito deja de ser un concepto místico y se convierte en un terreno que podemos cartografiar.

### 🛡️ Crónica del Infinito: El Legado de Georg Cantor
A finales del siglo XIX, un hombre decidió desafiar a la teología y a la ciencia de su tiempo. **Georg Cantor** se atrevió a decir que el infinito no era un muro infranqueable, sino un jardín que podía ser medido. Cantor demostró que los conjuntos nos permiten comparar tamaños de infinitos que parecen imposibles. Su valentía permitió que hoy podamos definir con precisión quirúrgica qué es un número. En la PAES, este lenguaje es tu escudo: si dominas los conjuntos, dominas las instrucciones de la prueba.

### 🛡️  El Marco de Referencia: Universo, Vacío y Subconjuntos
Para que exista el orden, debe existir un límite y una jerarquía clara:

* **El Universo ($\\mathcal{U}$):** Es el contexto total que contiene todos los elementos de un problema. Nada existe fuera del universo.
* **El Vacío ($\\emptyset$ o $\\{\\}$):** Un conjunto sin elementos. Es la representación de la nada matemática y es subconjunto de cualquier conjunto por definición.
* **Pertenencia ($\\in$):** Relación de un **elemento** hacia un conjunto. (Ej: Manzana $\\in$ Frutas).
* **Subconjunto o Inclusión ($\\subset$):** Se dice que $A$ es subconjunto de $B$ ($A \\subset B$) si **todos** los elementos de $A$ están también en $B$.

> **💡 Tip:** Si $A \\subset B$, entonces la intersección es el más pequeño ($A \\cap B = A$) y la unión es el más grande ($A \\cup B = B$).
""")

    # ── FIGURA 1: Relación de Inclusión ─────────────────────────────────────
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.add_patch(plt.Rectangle((0, 0), 10, 8, color='#f0f0f0', ec='black', lw=2))
    ax1.add_patch(plt.Circle((5, 4), 3, color='#3498db', alpha=0.3, ec='blue', lw=2))
    ax1.text(5, 6.5, "Conjunto B", fontsize=12, fontweight='bold', color='blue', ha='center')
    ax1.add_patch(plt.Circle((5, 4), 1.2, color='#2980b9', alpha=0.8, ec='navy', lw=2))
    ax1.text(5, 4, "A ⊂ B", fontsize=12, fontweight='bold', color='white', ha='center', va='center')
    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1, 9)
    ax1.axis('off')
    fig1.suptitle("Relación de Inclusión (Subconjuntos)", fontsize=15, fontweight='bold')
    st.pyplot(fig1)
    plt.close(fig1)

    # ── SECCIONES 4 y 5 ─────────────────────────────────────────────────────
    st.markdown("""
### 🛡️  Operaciones de "1000 Puntos"
Estas operaciones son las que "mueven" los elementos entre conjuntos:

| Operación | Símbolo | Significado Lógico | Carpintería Técnica |
| :--- | :---: | :--- | :--- |
| **Unión** | $\\cup$ | $x \\in A$ **o** $x \\in B$ | Agrupar todos los elementos de ambos. |
| **Intersección** | $\\cap$ | $x \\in A$ **y** $x \\in B$ | Solo los elementos que se repiten. |
| **Diferencia** | $-$ | $x \\in A$ pero $x \\notin B$ | Al primer conjunto le borras lo que sea del segundo. |
| **Complemento** | $A^c$ | $x \\in \\mathcal{U}$ pero $x \\notin A$ | Todo lo que le falta a A para ser el Universo. |

### 🛡️ Cardinalidad y Conjunto Potencia
* **Cardinalidad ($n$):** Llamamos cardinalidad al número de elementos únicos de un conjunto. Se denota como $\\#A = n$ o $n(A)$.
* **Regla de Oro de la Unión:** $\\#(A \\cup B) = \\#A + \\#B - \\#(A \\cap B)$.
* **Conjunto Potencia:** Es el conjunto formado por todos los subconjuntos posibles de $A$.
* **Total de Subconjuntos:** Si la cardinalidad de un conjunto es $n$, el total de subconjuntos que se pueden formar es:
$$2^n$$
> **💡 Tip:** El total de subconjuntos siempre incluye al **Vacío** y al **propio conjunto $A$**. Si agregas un elemento a la bolsa, el conjunto potencia crece al doble.

### 🛡️  Cartografía Visual (Diagramas de Venn-Euler)
Para dominar la PAES, debes "ver" la operación antes de calcularla. Aquí se presentan las estructuras visuales para tu análisis:
""")

    # ── FIGURA 2: Lámina de operaciones ─────────────────────────────────────
    color_a = '#e74c3c'
    color_b = '#3498db'
    color_u = '#f1c40f'

    fig2, axs = plt.subplots(2, 4, figsize=(20, 10))
    fig2.patch.set_facecolor('white')
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    # 1. Vacío
    axs[0, 0].add_patch(Rectangle((0.1, 0.1), 0.8, 0.8, color='#f9f9f9', ec='black', lw=2))
    axs[0, 0].text(0.9, 0.9, "U", fontweight='bold', ha='right')
    axs[0, 0].text(0.5, 0.5, "Ø", fontsize=40, ha='center', va='center', alpha=0.3)
    axs[0, 0].set_title("1. Conjunto Vacío", fontweight='bold')

    # 2. Intersección
    axs[0, 1].add_patch(Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.3, ec='red'))
    axs[0, 1].add_patch(Circle((0.6, 0.5), 0.25, color=color_b, alpha=0.3, ec='blue'))
    axs[0, 1].text(0.25, 0.5, "A", fontweight='bold', fontsize=12)
    axs[0, 1].text(0.75, 0.5, "B", fontweight='bold', fontsize=12)
    axs[0, 1].text(0.5, 0.5, "A∩B", ha='center', fontweight='bold', color='black')
    axs[0, 1].set_title("2. Intersección", fontweight='bold')

    # 3. Unión
    axs[0, 2].add_patch(Circle((0.4, 0.5), 0.25, color='purple', alpha=0.6))
    axs[0, 2].add_patch(Circle((0.6, 0.5), 0.25, color='purple', alpha=0.6))
    axs[0, 2].text(0.25, 0.5, "A", fontweight='bold', color='white')
    axs[0, 2].text(0.75, 0.5, "B", fontweight='bold', color='white')
    axs[0, 2].set_title("3. Unión (A ∪ B)", fontweight='bold')

    # 4. Diferencia
    axs[0, 3].add_patch(Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.8, ec='red'))
    axs[0, 3].add_patch(Circle((0.6, 0.5), 0.25, color='white', alpha=1.0))
    axs[0, 3].add_patch(Circle((0.6, 0.5), 0.25, color=color_b, alpha=0.1, ec='blue', ls='--'))
    axs[0, 3].text(0.2, 0.5, "A", fontweight='bold')
    axs[0, 3].text(0.75, 0.5, "B", fontweight='bold', alpha=0.5)
    axs[0, 3].set_title("4. Diferencia (A - B)", fontweight='bold')

    # 5. Complemento
    axs[1, 0].add_patch(Rectangle((0.1, 0.1), 0.8, 0.8, color=color_u, alpha=0.3, ec='black'))
    axs[1, 0].add_patch(Circle((0.5, 0.5), 0.25, color='white', ec='black'))
    axs[1, 0].text(0.5, 0.5, "A", ha='center', va='center', fontweight='bold')
    axs[1, 0].text(0.15, 0.8, "Aᶜ", fontsize=15, fontweight='bold')
    axs[1, 0].set_title("5. Complemento de A", fontweight='bold')

    # 6. Disjuntos
    axs[1, 1].add_patch(Circle((0.25, 0.5), 0.2, color=color_a, alpha=0.5, ec='red'))
    axs[1, 1].add_patch(Circle((0.75, 0.5), 0.2, color=color_b, alpha=0.5, ec='blue'))
    axs[1, 1].text(0.25, 0.5, "A", ha='center', fontweight='bold')
    axs[1, 1].text(0.75, 0.5, "B", ha='center', fontweight='bold')
    axs[1, 1].set_title("6. Disjuntos (A ∩ B = Ø)", fontweight='bold')

    # 7. Unión Disjunta
    axs[1, 2].add_patch(Circle((0.25, 0.5), 0.2, color='gray', alpha=0.8))
    axs[1, 2].add_patch(Circle((0.75, 0.5), 0.2, color='gray', alpha=0.8))
    axs[1, 2].text(0.25, 0.5, "A", ha='center', fontweight='bold', color='white')
    axs[1, 2].text(0.75, 0.5, "B", ha='center', fontweight='bold', color='white')
    axs[1, 2].set_title("7. Unión Disjunta", fontweight='bold')

    # 8. Subconjunto
    axs[1, 3].add_patch(Circle((0.5, 0.5), 0.35, color=color_b, alpha=0.3, ec='blue'))
    axs[1, 3].add_patch(Circle((0.5, 0.5), 0.15, color=color_a, alpha=0.8, ec='red'))
    axs[1, 3].text(0.5, 0.75, "B", color='blue', fontweight='bold')
    axs[1, 3].text(0.5, 0.5, "A", color='white', fontweight='bold', ha='center', va='center')
    axs[1, 3].set_title("8. Inclusión (A ⊂ B)", fontweight='bold')

    for ax in axs.flat:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

    fig2.suptitle("LÁMINA TÉCNICA: OPERACIONES DE CONJUNTOS", fontsize=20, fontweight='bold')
    st.pyplot(fig2)
    plt.close(fig2)

    # ── CITA FINAL ───────────────────────────────────────────────────────────
    st.markdown("""
---
> *"En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".*
>
> — **Georg Cantor**
""")
