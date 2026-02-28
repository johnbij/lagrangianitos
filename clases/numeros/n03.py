import streamlit as st
import matplotlib.pyplot as plt


def render_N03():
    st.title("N03: Los Números Cardinales (ℕ₀) — La Conquista del Vacío")

    st.markdown(r"""
### 🛡️ 1. El Portal: El Descubrimiento de la Nada

En el capítulo anterior vimos que los Naturales servían para contar lo que "estaba ahí". Pero, ¿cómo representamos la ausencia total? Durante siglos, la humanidad le tuvo miedo al vacío. No fue hasta que civilizaciones como la India y los Mayas entendieron que el "nada" también es una cantidad, que la matemática pudo avanzar hacia el álgebra moderna.

Al añadir el **0** a nuestro conjunto de naturales, creamos los **Números Cardinales** (o Naturales Extendidos). Este pequeño cambio redefine las fronteras de lo que podemos calcular.

---

### 🛡️ 2. Definición y Notación

Se denota con la letra $\mathbb{N}_0$ (o a veces $\mathbb{N} \cup \{0\}$) y se define como:

$$\mathbb{N}_0 = \{0, 1, 2, 3, 4, 5, ...\}$$

* **Primer Elemento:** El **0** es ahora el inicio absoluto.
* **Cambio de Guardia:** En este conjunto, el **1 ya no es el límite**; ahora el 1 sí tiene un antecesor natural (el 0).
* **El Nuevo Muro:** El único número que carece de antecesor en $\mathbb{N}_0$ es el **0**.
""")

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(-1, 7)
    ax.set_ylim(0.5, 2.5)
    ax.axhline(2, xmin=0.25, xmax=0.9, color='black', lw=2, alpha=0.3)
    for x in range(1, 7):
        ax.plot(x, 2, 'ro', markersize=10)
        ax.text(x, 2.15, str(x), ha='center', fontsize=12, fontweight='bold', color='red')
    ax.vlines(1, 1.8, 2.2, color='red', lw=4)
    ax.text(-0.8, 2, "Naturales (N)", fontsize=12, fontweight='bold', va='center')
    ax.axhline(1, xmin=0.125, xmax=0.9, color='black', lw=2, alpha=0.3)
    for x in range(0, 7):
        ax.plot(x, 1, 'go', markersize=10)
        ax.text(x, 0.7, str(x), ha='center', fontsize=12, fontweight='bold', color='green')
    ax.vlines(0, 0.8, 1.2, color='green', lw=4)
    ax.text(-0.8, 1, "Cardinales (N₀)", fontsize=12, fontweight='bold', va='center')
    ax.annotate('', xy=(7, 2), xytext=(6.5, 2), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(7, 1), xytext=(6.5, 1), arrowprops=dict(arrowstyle='->', lw=2))
    circle = plt.Circle((0, 1), 0.25, color='yellow', alpha=0.3, ec='green', ls='--')
    ax.add_patch(circle)
    ax.text(0, 1.3, "¡Nuevo elemento!", color='darkgreen', fontsize=9, ha='center', fontweight='bold')
    plt.title("Comparativa de Límites: N vs N₀", fontsize=14, fontweight='bold', pad=20)
    ax.axis('off')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🛡️ 3. El Cero bajo la Lupa (Protocolo PAES)

El cero no es un número cualquiera; es un agente especial con reglas propias que debes memorizar para evitar trampas:

1. **Paridad:** El 0 es un **número PAR**. Cumple con la fórmula $2k = n$, donde si $k=0$, entonces $n=0$.
2. **Neutro Aditivo:** Es el elemento que no hace nada en la suma: $a + 0 = a$.
3. **Elemento Absorbente:** En la multiplicación, el cero es un "agujero negro": $a \cdot 0 = 0$.
4. **La Prohibición:** La división **por cero** ($\frac{a}{0}$) no existe. Es una indefinición matemática. Si ves un denominador que puede ser cero, ahí hay una trampa.

---

### 🛡️ 4. Diccionario de Supervivencia (Lenguaje Técnico)

La PAES no siempre te dirá "use los cardinales". Usará estas frases clave:

* **"Enteros positivos":** Se refiere a $\mathbb{N} = \{1, 2, 3, ...\}$ (El 0 queda FUERA).
* **"Enteros no negativos":** Se refiere a $\mathbb{N}_0 = \{0, 1, 2, 3, ...\}$ (El 0 queda DENTRO).

> **Típ:** La palabra **"no negativo"** es la forma elegante de la PAES para obligarte a incluir el cero. Si el problema dice "un número no negativo", y tú partes contando desde el 1, perdiste el ejercicio.

---

### 🛡️ 5. Propiedades de Clausura en $\mathbb{N}_0$

¿Cambia algo respecto a los naturales?

* **Adición y Multiplicación:** Siguen siendo **Cerradas**.
* **Sustracción:** Sigue **SIN ser cerrada**, pero ganamos un caso: $a - a = 0$. Ahora podemos restar números iguales, algo que en $\mathbb{N}$ era prohibido.

---

> "El cero es la mayor invención de la humanidad porque nos permite representar la nada como si fuera algo".
> — **Anónimo** (Relacionado con la invención del sistema posicional).
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería N03", expanded=False):
        st.markdown(r"""
### E01: La Vecindad del Uno en Diferentes Conjuntos

**Situación:** Determinar el antecesor del número 1 en el conjunto $\mathbb{N}$ y en el conjunto $\mathbb{N}_0$.

**La Carpintería:**
1. **Analizar en $\mathbb{N}$:** El conjunto parte en el 1. No hay nada a su izquierda. El antecesor **no existe** en $\mathbb{N}$.
2. **Analizar en $\mathbb{N}_0$:** El conjunto parte en el 0. Al restar 1 al número ($1-1$), obtenemos 0.
3. **Verificar:** El 0 pertenece a $\mathbb{N}_0$.
4. **Resultado:** En $\mathbb{N}_0$, el antecesor de 1 es el 0.

| Conjunto | Número | Antecesor ($n-1$) | ¿Existe en el conjunto? |
| :--- | :---: | :---: | :---: |
| Naturales ($\mathbb{N}$) | 1 | 0 | ❌ NO |
| Cardinales ($\mathbb{N}_0$) | 1 | 0 | ✅ SÍ |

---

### E02: El Cero y la Paridad

**Situación:** Si $x$ es un número natural, determinar si la expresión $2 \cdot (x - x)$ representa un número par.

**La Carpintería:**
1. **Resolver el paréntesis:** $x - x = 0$.
2. **Multiplicar:** $2 \cdot 0 = 0$.
3. **Aplicar definición de Par:** Un número es par si se puede escribir como $2k$ (con $k$ entero).
4. **Comprobar:** $0 = 2 \cdot 0$.
5. **Resultado:** Sí, el resultado es 0, y el 0 es un **número par**.

| Expresión | Valor | Clasificación |
| :--- | :---: | :--- |
| $x - x$ | 0 | Elemento Neutro / Cardinal |
| $2 \cdot 0$ | 0 | **Número Par** |

---

### E03: Traducción de "Enteros No Negativos"

**Situación:** Un problema PAES dice: *"Sea $n$ un entero no negativo menor que 3"*. ¿Cuáles son los posibles valores de $n$?

**La Carpintería:**
1. **Decodificar "No Negativo":** Significa que incluye al cero y a los positivos ($\mathbb{N}_0$).
2. **Decodificar "Menor que 3":** Significa que el 3 no está incluido ($n < 3$).
3. **Listar candidatos:** 0, 1, 2.
4. **Resultado:** El conjunto de valores es $\{0, 1, 2\}$.

| Frase Técnica | Traducción Matemática | Valores |
| :--- | :--- | :--- |
| "Enteros positivos" | $n \in \mathbb{N}$ | $\{1, 2, ...\}$ |
| "Enteros no negativos" | $n \in \mathbb{N}_0$ | $\{0, 1, 2, ...\}$ |

---

### E04: La Absorción y la Indefinición

**Situación:** Evaluar la expresión $\frac{10 \cdot (5 - 5)}{x}$ sabiendo que $x$ es un número cardinal sin antecesor.

**La Carpintería:**
1. **Identificar x:** El único cardinal sin antecesor es $x = 0$.
2. **Calcular numerador:** $10 \cdot (0) = 0$.
3. **Plantear la división:** $\frac{0}{0}$.
4. **Evaluar:** La división por cero es una **indefinición**. No importa que el numerador sea cero.
5. **Resultado:** La expresión no está definida.

| Parte | Operación | Resultado |
| :--- | :--- | :--- |
| Numerador | $10 \cdot 0$ | 0 |
| Denominador | Valor de $x$ | 0 |
| **Total** | **$0 / 0$** | **🚫 Indefinido** |

---

### E05: Clausura Extendida

**Situación:** ¿Se cumple la propiedad de clausura para la sustracción en $\mathbb{N}_0$ si restamos dos números iguales?

**La Carpintería:**
1. **Definir la resta:** $a - a$.
2. **Resultado:** 0.
3. **Verificar pertenencia:** ¿El 0 pertenece a $\mathbb{N}_0$? Sí.
4. **Conclusión:** A diferencia de los Naturales ($\mathbb{N}$), en los Cardinales ($\mathbb{N}_0$) la resta de números iguales **sí cumple** la clausura. (Pero la resta de un menor con un mayor sigue fallando).

| Operación | Conjunto N | Conjunto N0 |
| :--- | :---: | :---: |
| $5 - 5$ | ❌ Se sale | ✅ Clausura (0) |
| $3 - 5$ | ❌ Se sale | ❌ Se sale |
""")

    with st.expander("❓ Cuestionario N03: Números Cardinales", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el único número que pertenece al conjunto de los Cardinales ($\mathbb{N}_0$) pero NO al de los Naturales ($\mathbb{N}$)?**

A) 1  
B) 0  
C) -1  
D) No existe tal número.

---

**2. Si $n$ es un número cardinal, ¿cuál es la condición para que $n$ NO tenga un antecesor en $\mathbb{N}_0$?**

A) $n = 1$  
B) $n$ debe ser par.  
C) $n = 0$  
D) Todos los cardinales tienen antecesor.

---

**3. ¿Cuál de las siguientes frases representa al conjunto $\{0, 1, 2, 3, ...\}$?**

A) Enteros positivos.  
B) Enteros no positivos.  
C) Enteros no negativos.  
D) Naturales.

---

**4. Respecto al número 0, ¿cuál de estas afirmaciones es CORRECTA?**

A) Es un número impar.  
B) Es el neutro multiplicativo.  
C) Es un número par.  
D) Es el sucesor de 1.

---

**5. La expresión $\frac{5}{k-2}$ no está definida en los reales. ¿Cuál es el valor de $k$?**

A) 0  
B) 2  
C) 5  
D) -2

---

**6. Si $A = \{ \text{enteros no negativos menores que 2} \}$, ¿cuál es la cardinalidad (cantidad de elementos) de $A$?**

A) 1  
B) 2  
C) 3  
D) Infinita

---

**7. ¿Qué propiedad del cero se aplica en la operación $1.245 \cdot 0 = 0$?**

A) Neutro aditivo  
B) Elemento absorbente  
C) Clausura  
D) Distributividad

---

**8. En el conjunto $\mathbb{N}_0$, ¿cuál es el antecesor del sucesor de 0?**

A) 0  
B) 1  
C) 2  
D) No existe

---

**9. Si sumamos dos números cardinales cualesquiera, el resultado siempre será un número cardinal. Esto se debe a la propiedad de:**

A) Conmutatividad  
B) Asociatividad  
C) Clausura  
D) Tricotomía

---

**10. "Sea $x$ un número tal que $x \in \mathbb{N}$". De esta afirmación se deduce que:**

A) $x$ puede ser 0.  
B) $x$ es estrictamente mayor que 0.  
C) $x$ no tiene antecesor en $\mathbb{N}_0$.  
D) $x$ es un entero no positivo.
""")

    with st.expander("🔑 Pauta Técnica N03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | La definición de $\mathbb{N}_0$ es $\mathbb{N} \cup \{0\}$. El cero es el único elemento que marca la diferencia entre ambos conjuntos. |
| **2** | **C** | En los Cardinales, el 0 es el nuevo límite izquierdo. Como no hay números menores que él en este conjunto, no tiene antecesor. |
| **3** | **C** | "No negativos" significa: "todos los que no tengan signo menos", lo que incluye obligatoriamente al cero y a los positivos. |
| **4** | **C** | El 0 es par porque cumple la regla $2 \cdot k$: $2 \cdot 0 = 0$. Es un error común creer que es neutro o que no tiene paridad. |
| **5** | **B** | Para que una fracción no esté definida, su denominador debe ser 0. Si $k - 2 = 0$, entonces $k$ debe valer 2. |
| **6** | **B** | Los "no negativos menores que 2" son el $\{0, 1\}$. El conjunto tiene exactamente 2 elementos. |
| **7** | **B** | Cualquier número multiplicado por 0 resulta en 0. Esta propiedad se llama elemento absorbente (anulación). |
| **8** | **A** | El sucesor de 0 es 1 ($0+1$). El antecesor de 1 es 0 ($1-1$). Volvemos al punto de partida. |
| **9** | **C** | La clausura es la "propiedad de club": si opero dos socios ($\mathbb{N}_0$), el resultado debe ser otro socio del club. |
| **10** | **B** | Si $x \in \mathbb{N}$, entonces $x \in \{1, 2, 3, ...\}$. Todos estos valores son mayores que cero. |

---

> **Típ:** "Cuidado con la pregunta 5. En la PAES, la indefinición por división por cero es una de las formas más comunes de descartar alternativas en suficiencia de datos."
""")
