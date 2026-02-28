import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def render_N03():
    st.title("N03: Los Números Cardinales (ℕ₀) — La Conquista del Vacío")

    # ── PORTAL ──────────────────────────────────────────────────────────────
    st.header("🛡️ 1. El Portal: El Descubrimiento de la Nada")
    st.markdown("""
En el capítulo anterior vimos que los Naturales servían para contar lo que "estaba ahí".
Pero, ¿cómo representamos la ausencia total? Durante siglos, la humanidad le tuvo miedo al vacío.
No fue hasta que civilizaciones como la India y los Mayas entendieron que la "nada" también
es una cantidad, que la matemática pudo avanzar hacia el álgebra moderna.

Al añadir el **0** a nuestro conjunto de naturales, creamos los **Números Cardinales**
(o Naturales Extendidos). Este pequeño cambio redefine las fronteras de lo que podemos calcular.
""")

    # ── DEFINICIÓN ──────────────────────────────────────────────────────────
    st.header("🛡️ 2. Definición y Notación")
    st.markdown(r"""
Se denota con la letra $\mathbb{N}_0$ y se define como:

$$\mathbb{N}_0 = \{0, 1, 2, 3, 4, 5, ...\}$$

- **Primer Elemento:** El **0** es ahora el inicio absoluto.
- **Cambio de Guardia:** El **1 ya no es el límite**; ahora el 1 sí tiene un antecesor natural (el 0).
- **El Nuevo Muro:** El único número que carece de antecesor en $\mathbb{N}_0$ es el **0**.
""")

    # ── FIGURA ──────────────────────────────────────────────────────────────
    st.subheader("📊 Comparativa: ℕ vs ℕ₀")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(-1, 7)
    ax.set_ylim(0.3, 2.7)

    # Naturales
    ax.axhline(2, xmin=0.2, xmax=0.9, color='black', lw=2, alpha=0.3)
    for x in range(1, 7):
        ax.plot(x, 2, 'ro', markersize=12)
        ax.text(x, 2.2, str(x), ha='center', fontsize=12, fontweight='bold', color='red')
    ax.vlines(1, 1.8, 2.2, color='red', lw=4)
    ax.text(-0.7, 2, "ℕ", fontsize=14, fontweight='bold', va='center', color='red')

    # Cardinales
    ax.axhline(1, xmin=0.1, xmax=0.9, color='black', lw=2, alpha=0.3)
    for x in range(0, 7):
        ax.plot(x, 1, 'go', markersize=12)
        ax.text(x, 0.7, str(x), ha='center', fontsize=12, fontweight='bold', color='green')
    ax.vlines(0, 0.8, 1.2, color='green', lw=4)
    ax.text(-0.7, 1, "ℕ₀", fontsize=14, fontweight='bold', va='center', color='green')

    # Flechas infinitud
    ax.annotate('', xy=(7, 2), xytext=(6.5, 2), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(7, 1), xytext=(6.5, 1), arrowprops=dict(arrowstyle='->', lw=2))

    # Resaltar el 0
    circle = plt.Circle((0, 1), 0.28, color='yellow', alpha=0.4, ec='green', ls='--', lw=2)
    ax.add_patch(circle)
    ax.text(0, 1.35, "¡Nuevo!", color='darkgreen', fontsize=9, ha='center', fontweight='bold')

    plt.title("Comparativa de Límites: ℕ vs ℕ₀", fontsize=13, fontweight='bold', pad=15)
    ax.axis('off')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # ── EL CERO ─────────────────────────────────────────────────────────────
    st.header("🛡️ 3. El Cero bajo la Lupa (Protocolo PAES)")
    st.markdown(r"""
El cero no es un número cualquiera; es un **agente especial** con reglas propias:

1. **Paridad:** El 0 es un **número PAR**. Cumple $2k = n$ con $k=0$.
2. **Neutro Aditivo:** Es el elemento que no hace nada en la suma: $a + 0 = a$.
3. **Elemento Absorbente:** En la multiplicación es un agujero negro: $a \cdot 0 = 0$.
4. **La Prohibición:** La división **por cero** ($\frac{a}{0}$) **no existe**. Es una indefinición matemática.
""")

    st.info("💡 **Tip PAES:** Si ves un denominador que puede ser cero, ahí hay una trampa.")

    # ── DICCIONARIO ─────────────────────────────────────────────────────────
    st.header("🛡️ 4. Diccionario de Supervivencia")
    st.markdown(r"""
La PAES no siempre dirá "use los cardinales". Usará estas frases clave:

| Frase PAES | Traducción | El cero... |
|:---|:---|:---:|
| **"Enteros positivos"** | $\mathbb{N} = \{1, 2, 3, ...\}$ | ❌ Fuera |
| **"Enteros no negativos"** | $\mathbb{N}_0 = \{0, 1, 2, ...\}$ | ✅ Dentro |
""")

    st.warning("⚠️ **La palabra \"no negativo\"** es la forma elegante de la PAES para obligarte a incluir el cero.")

    # ── CLAUSURA ────────────────────────────────────────────────────────────
    st.header("🛡️ 5. Propiedades de Clausura en ℕ₀")
    st.markdown(r"""
| Operación | Cerrada en ℕ₀ | Observación |
|:---|:---:|:---|
| **Adición (+)** | ✅ SÍ | Siempre da un cardinal |
| **Multiplicación (×)** | ✅ SÍ | Siempre da un cardinal |
| **Sustracción (−)** | ⚠️ CASI | Solo si $a \geq b$. Nuevo caso: $a - a = 0$ ya es válido |
""")

    st.markdown("""
---
> *"El cero es la mayor invención de la humanidad porque nos permite representar la nada como si fuera algo."*
""")

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Carpintería de Ejemplos N03", expanded=False):
        st.markdown(r"""
### E01: La Vecindad del Uno en Diferentes Conjuntos
**Situación:** Determinar el antecesor del número 1 en $\mathbb{N}$ y en $\mathbb{N}_0$.

| Conjunto | Número | Antecesor | ¿Existe? |
|:---|:---:|:---:|:---:|
| $\mathbb{N}$ | 1 | 0 | ❌ NO |
| $\mathbb{N}_0$ | 1 | 0 | ✅ SÍ |

---
### E02: El Cero y la Paridad
**Situación:** ¿Es la expresión $2 \cdot (x - x)$ un número par?

1. $x - x = 0$
2. $2 \cdot 0 = 0$
3. $0 = 2 \cdot 0$ → cumple definición de par ✅

---
### E03: Traducción de "Enteros No Negativos"
*"Sea $n$ un entero no negativo menor que 3"* → $n \in \{0, 1, 2\}$

---
### E04: La Absorción y la Indefinición
**Expresión:** $\frac{10 \cdot (5-5)}{x}$ con $x$ = cardinal sin antecesor → $x = 0$

Resultado: $\frac{0}{0}$ → **🚫 Indefinido**

---
### E05: Clausura Extendida

| Operación | En ℕ | En ℕ₀ |
|:---|:---:|:---:|
| $5 - 5$ | ❌ Se sale | ✅ Clausura (0) |
| $3 - 5$ | ❌ Se sale | ❌ Se sale |
""")

    # ── CUESTIONARIO ────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario N03", expanded=False):
        st.markdown(r"""
**1.** ¿Cuál es el único número que pertenece a $\mathbb{N}_0$ pero NO a $\mathbb{N}$?
- A) 1 · B) **0** · C) -1 · D) No existe

**2.** ¿Cuál es la condición para que $n \in \mathbb{N}_0$ NO tenga antecesor?
- A) $n = 1$ · B) $n > 0$ · C) **$n = 0$** · D) $n$ es par

**3.** La expresión $3 \cdot 0$ es igual a:
- A) 3 · B) 1/3 · C) **0** · D) Indefinida

**4.** "Enteros no negativos menores que 4" corresponde al conjunto:
- A) $\{1,2,3\}$ · B) $\{1,2,3,4\}$ · C) **$\{0,1,2,3\}$** · D) $\{0,1,2,3,4\}$

**5.** ¿Es el 0 un número par?
- A) No, no es par ni impar · B) No, es neutro · C) **Sí, porque $0 = 2 \cdot 0$** · D) Depende del contexto
""")

    with st.expander("🔑 Pauta N03", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería |
|:---:|:---:|:---|
| 1 | **B** | El único nuevo elemento al pasar de ℕ a ℕ₀ es el 0. |
| 2 | **C** | En ℕ₀, el 0 es el inicio; no hay nada a su izquierda. |
| 3 | **C** | Propiedad absorbente del cero. |
| 4 | **C** | "No negativo" incluye el cero. Menor que 4 excluye el 4. |
| 5 | **C** | Definición: $n$ es par si $n = 2k$ con $k$ entero. Para $k=0$, $n=0$. |
""")
