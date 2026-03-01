import streamlit as st


def render_A01():
    st.title("A01: Expresiones Algebraicas y Lenguaje Algebraico — Del Español a las Matemáticas")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Por qué Letras en Matemáticas?

Imagínate que estás armando una receta de cocina, pero no sabes cuántas personas vendrán a cenar. En vez de escribir una cantidad fija, dices "para **$n$** personas necesito **$2n$** huevos". Esa letra **$n$** es una **variable**: un símbolo que representa un número que aún no conocemos, pero que puede tomar distintos valores.

El álgebra nació precisamente de esa necesidad: expresar ideas matemáticas de forma **general**, sin atarnos a un número concreto. Es el idioma universal que conecta los problemas del mundo real con las operaciones numéricas.

---

### 🛡️ 1.1 Vocabulario Fundamental

Antes de operar, necesitas conocer las piezas del rompecabezas algebraico:

| Concepto | Definición | Ejemplo |
| :--- | :--- | :--- |
| **Variable** | Letra que representa un valor desconocido | $x$, $y$, $n$ |
| **Constante** | Número fijo que no cambia | $3$, $-7$, $\pi$ |
| **Coeficiente** | Número que multiplica a la variable | En $5x$, el coeficiente es $5$ |
| **Término** | Producto de un coeficiente y una o más variables | $3x^2$, $-7y$, $4$ |
| **Expresión algebraica** | Suma o resta de uno o más términos | $3x^2 - 7y + 4$ |

> **Tip PAES:** Cuando no ves un coeficiente escrito, el coeficiente es **1**. Es decir, $x = 1 \cdot x$.

---

### 🛡️ 1.2 Términos Semejantes

Dos términos son **semejantes** cuando tienen exactamente la misma parte literal (mismas variables con los mismos exponentes). Solo los términos semejantes se pueden sumar o restar entre sí.

| Términos | ¿Son semejantes? | Razón |
| :--- | :---: | :--- |
| $3x^2$ y $-5x^2$ | ✅ Sí | Misma variable ($x$) y mismo exponente ($2$) |
| $4xy$ y $-2xy$ | ✅ Sí | Mismas variables ($x$, $y$) con mismos exponentes |
| $3x^2$ y $3x^3$ | ❌ No | Los exponentes son distintos ($2 \neq 3$) |
| $7x$ y $7y$ | ❌ No | Las variables son distintas |

---

### 🛡️ 1.3 Reducción de Términos Semejantes

Reducir es **sumar los coeficientes** de los términos que comparten la misma parte literal:

$$5x + 3x - 2x = (5 + 3 - 2)x = 6x$$

$$4a^2b - 7a^2b + a^2b = (4 - 7 + 1)a^2b = -2a^2b$$

La clave: se operan los coeficientes y la parte literal queda igual, como si fuera una "etiqueta" que no se toca.

---

### 🏛️ 1.4 Traducción del Lenguaje Verbal al Algebraico

Este es el **superpoder** que más evalúa la PAES: convertir un enunciado en español a una expresión matemática.

| Frase en español | Expresión algebraica |
| :--- | :--- |
| "El doble de un número" | $2x$ |
| "Un número aumentado en 5" | $x + 5$ |
| "La mitad de un número" | $\dfrac{x}{2}$ |
| "El cuadrado de un número disminuido en 3" | $x^2 - 3$ |
| "La suma de dos números consecutivos" | $x + (x + 1) = 2x + 1$ |
| "El triple de un número menos su cuarta parte" | $3x - \dfrac{x}{4}$ |
| "El producto de dos números consecutivos pares" | $x(x + 2)$ |

> **Estrategia:** Identifica primero el **verbo** (suma, resta, multiplica, divide) y luego los **actores** (los números o variables involucrados).

---

### 🛡️ 1.5 Evaluación de Expresiones Algebraicas

Evaluar significa **reemplazar** la variable por un valor numérico y calcular:

Si $f(x) = 3x^2 - 2x + 1$, entonces para $x = -2$:

$$f(-2) = 3(-2)^2 - 2(-2) + 1 = 3(4) + 4 + 1 = 12 + 4 + 1 = 17$$

> **Cuidado con los signos:** Al reemplazar un valor negativo, siempre usa paréntesis para no perder el signo.

---

> "El álgebra es generosa: te ayuda con lo que no sabes."
> — **Al-Juarismi** (padre del álgebra)
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería A01", expanded=False):
        st.markdown(r"""
### E01: Identificar los componentes de una expresión

**Situación:** Dada la expresión $-4x^3 + 7x - 9$, identificar sus componentes.

**La Carpintería:**
1. **Términos:** Son tres: $-4x^3$, $7x$ y $-9$.
2. **Coeficientes:** $-4$, $7$ y $-9$ (el término independiente también es un coeficiente).
3. **Variables:** Solo aparece $x$.
4. **Grado de cada término:** $3$, $1$ y $0$ respectivamente.
5. **Grado de la expresión:** El mayor, que es $3$.

| Término | Coeficiente | Parte Literal | Grado |
| :--- | :---: | :---: | :---: |
| $-4x^3$ | $-4$ | $x^3$ | $3$ |
| $7x$ | $7$ | $x$ | $1$ |
| $-9$ | $-9$ | — | $0$ |

---

### E02: Reducción de términos semejantes

**Situación:** Simplificar $8a^2 - 3a + 5a^2 + a - 7$.

**La Carpintería:**
1. **Agrupar semejantes:** $(8a^2 + 5a^2) + (-3a + a) + (-7)$.
2. **Sumar coeficientes:** $13a^2 + (-2a) + (-7)$.
3. **Resultado:** $13a^2 - 2a - 7$.

| Grupo de Semejantes | Operación | Resultado |
| :--- | :--- | :--- |
| $8a^2 + 5a^2$ | $8 + 5 = 13$ | $13a^2$ |
| $-3a + a$ | $-3 + 1 = -2$ | $-2a$ |
| $-7$ | (sin semejante) | $-7$ |

---

### E03: Traducción del español al álgebra

**Situación:** "El triple de la edad de Pedro, disminuido en 4 años, es igual al doble de su edad aumentada en 10."

**La Carpintería:**
1. **Variable:** Sea $x$ = la edad de Pedro.
2. **"El triple de la edad de Pedro":** $3x$.
3. **"disminuido en 4 años":** $3x - 4$.
4. **"el doble de su edad":** $2x$.
5. **"aumentada en 10":** $2x + 10$.
6. **Ecuación:** $3x - 4 = 2x + 10$.

---

### E04: Evaluación de una expresión

**Situación:** Si $E = 2a^2 - 3ab + b^2$, evaluar para $a = 3$ y $b = -1$.

**La Carpintería:**
1. **Reemplazar:** $E = 2(3)^2 - 3(3)(-1) + (-1)^2$.
2. **Calcular potencias:** $E = 2(9) - 3(3)(-1) + 1$.
3. **Multiplicar:** $E = 18 + 9 + 1$.
4. **Resultado:** $E = 28$.

| Paso | Operación | Valor |
| :--- | :--- | :---: |
| Reemplazo | $2(3)^2 - 3(3)(-1) + (-1)^2$ | — |
| Potencias | $2(9) - 3(3)(-1) + 1$ | — |
| Productos | $18 + 9 + 1$ | — |
| Resultado | — | $28$ |
""")

    with st.expander("❓ Cuestionario A01: Expresiones Algebraicas", expanded=False):
        st.markdown(r"""
**1. En la expresión $-7x^2y$, ¿cuál es el coeficiente?**

A) $x^2y$
B) $7$
C) $-7$
D) $-7x^2$

---

**2. ¿Cuáles de los siguientes pares son términos semejantes?**

A) $3x^2$ y $3x^3$
B) $5ab$ y $-2ba$
C) $4x$ y $4y$
D) $x^2y$ y $xy^2$

---

**3. Al reducir $6m - 2m + 3m - m$, se obtiene:**

A) $6m$
B) $8m$
C) $4m$
D) $12m$

---

**4. La traducción algebraica de "el cuadrado de la suma de dos números" es:**

A) $x^2 + y^2$
B) $(x + y)^2$
C) $x^2 + y$
D) $2(x + y)$

---

**5. Si $x = -3$, el valor de $x^2 - 2x + 1$ es:**

A) $4$
B) $16$
C) $-2$
D) $14$

---

**6. La expresión "un número disminuido en su tercera parte" se traduce como:**

A) $x - 3$
B) $x - \dfrac{x}{3}$
C) $\dfrac{x}{3} - x$
D) $3 - x$

---

**7. ¿Cuántos términos tiene la expresión $5x^3 - 2x^2 + x - 8$?**

A) $3$
B) $4$
C) $5$
D) $2$
""")

    with st.expander("🔑 Pauta Técnica A01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **C** | El coeficiente incluye el signo. En $-7x^2y$, el coeficiente es $-7$. |
| **2** | **B** | $5ab$ y $-2ba$ son semejantes porque $ab = ba$ (conmutatividad). Mismas variables, mismos exponentes. |
| **3** | **A** | $6 - 2 + 3 - 1 = 6$. Se suman los coeficientes: $(6 - 2 + 3 - 1)m = 6m$. |
| **4** | **B** | "El cuadrado DE la suma" = $(x + y)^2$. No es lo mismo que $x^2 + y^2$ (ojo con la PAES). |
| **5** | **B** | $(-3)^2 - 2(-3) + 1 = 9 + 6 + 1 = 16$. Cuidado: $(-3)^2 = 9$, no $-9$. |
| **6** | **B** | "Disminuido en su tercera parte" = $x - \frac{x}{3}$. El pronombre "su" se refiere al mismo número. |
| **7** | **B** | Los términos son $5x^3$, $-2x^2$, $x$ y $-8$. Son 4 términos separados por sumas o restas. |
""")
