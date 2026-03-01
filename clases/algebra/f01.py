import streamlit as st


def render_F01():
    st.title("F01: Concepto de Función — El Lenguaje de las Relaciones")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Qué es una Función?

Imagina una máquina de jugos: metes una fruta y sale un jugo. Si metes una manzana, sale jugo de manzana; si metes una naranja, sale jugo de naranja. **Nunca** sale jugo de manzana y de naranja al mismo tiempo por la misma fruta. Eso es exactamente lo que ocurre con una **función**: a cada elemento de entrada le corresponde **exactamente un** elemento de salida.

Formalmente, una **función** $f$ es una regla que asigna a cada elemento $x$ de un conjunto $A$ (llamado **dominio**) un único elemento $y$ de un conjunto $B$ (llamado **codominio**). Escribimos:

$$f: A \to B \quad \text{donde} \quad y = f(x)$$

La variable $x$ se llama **variable independiente** y la variable $y$ se llama **variable dependiente**, porque su valor *depende* de qué $x$ elijamos.

---

### 🛡️ 1.1 Dominio, Codominio y Recorrido (Rango)

Estos tres conceptos son el ADN de toda función:

| Concepto | Definición | Ejemplo con $f(x) = x^2$ y $A = \{-2, -1, 0, 1, 2\}$ |
| :--- | :--- | :--- |
| **Dominio** | Conjunto de todos los valores de entrada permitidos | $\{-2, -1, 0, 1, 2\}$ |
| **Codominio** | Conjunto donde "viven" las posibles salidas | $\mathbb{R}$ (todos los reales, por ejemplo) |
| **Recorrido (Rango)** | Conjunto de salidas que **efectivamente** se obtienen | $\{0, 1, 4\}$ |

> **Tip PAES:** El recorrido siempre es un subconjunto del codominio. No son lo mismo: el codominio es "el hotel completo", el recorrido son "las habitaciones que realmente se usan".

---

### 🛡️ 1.2 Notación $f(x)$ y Evaluación

La notación $f(x)$ se lee "f de x" y representa el valor de salida cuando la entrada es $x$. No es una multiplicación; es una **instrucción**:

- Si $f(x) = 3x - 1$, entonces $f(2) = 3(2) - 1 = 5$.
- Si $g(x) = x^2 + 1$, entonces $g(-3) = (-3)^2 + 1 = 10$.

Puedes evaluar funciones con cualquier expresión, no solo números:

$$f(a + 1) = 3(a + 1) - 1 = 3a + 3 - 1 = 3a + 2$$

---

### 🏛️ 1.3 El Test de la Línea Vertical

¿Cómo saber si un gráfico en el plano cartesiano representa una función? Usa el **test de la línea vertical**:

> Si **cualquier línea vertical** que traces corta al gráfico en **a lo más un punto**, entonces el gráfico **sí** es una función.

| Gráfico | ¿Es función? | Razón |
| :--- | :---: | :--- |
| Recta no vertical | ✅ Sí | Cada vertical la corta en exactamente un punto |
| Parábola $y = x^2$ | ✅ Sí | Cada vertical corta en un solo punto |
| Circunferencia $x^2 + y^2 = r^2$ | ❌ No | Una vertical puede cortar en dos puntos |
| Recta vertical $x = 3$ | ❌ No | La vertical $x = 3$ corta en infinitos puntos |

---

### 🛡️ 1.4 Representaciones de una Función

Una función puede presentarse de varias formas equivalentes:

| Representación | Ejemplo |
| :--- | :--- |
| **Verbal** | "A cada número le asigno su doble" |
| **Algebraica (fórmula)** | $f(x) = 2x$ |
| **Tabla de valores** | $x$: $0, 1, 2, 3$ → $f(x)$: $0, 2, 4, 6$ |
| **Gráfica** | Una recta que pasa por el origen con pendiente $2$ |
| **Diagrama de flechas** | Flechas de cada $x$ a su imagen $f(x)$ |

La PAES puede presentar una función en cualquiera de estas formas y pedirte que la interpretes en otra.

---

### 🏛️ 1.5 Clasificación: Inyectiva, Sobreyectiva y Biyectiva

Estas clasificaciones describen "cómo se comporta" la función respecto a sus conjuntos:

| Tipo | Definición | Ejemplo |
| :--- | :--- | :--- |
| **Inyectiva** (uno a uno) | Elementos distintos del dominio tienen imágenes distintas: si $x_1 \neq x_2$, entonces $f(x_1) \neq f(x_2)$ | $f(x) = 2x + 1$ es inyectiva |
| **Sobreyectiva** (sobre) | Todo elemento del codominio es imagen de al menos un elemento del dominio (recorrido = codominio) | $f: \mathbb{R} \to \mathbb{R}$, $f(x) = x^3$ |
| **Biyectiva** | Es inyectiva **y** sobreyectiva a la vez. Cada elemento del codominio tiene exactamente un preimagen | $f: \mathbb{R} \to \mathbb{R}$, $f(x) = 2x + 1$ |

> **Test visual de inyectividad:** Si toda línea *horizontal* corta al gráfico en a lo más un punto, la función es inyectiva. Ejemplo: $f(x) = x^2$ **no** es inyectiva en $\mathbb{R}$ porque $f(2) = f(-2) = 4$.

---

> "Una función es la idea más importante en toda la matemática."
> — **Peter Dirichlet** (quien formalizó el concepto moderno de función)
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería F01", expanded=False):
        st.markdown(r"""
### E01: Evaluar una función en distintos valores

**Situación:** Dada $f(x) = x^2 - 4x + 3$, calcular $f(0)$, $f(1)$, $f(3)$ y $f(-2)$.

**La Carpintería:**

| $x$ | Sustitución | Cálculo | $f(x)$ |
| :---: | :--- | :--- | :---: |
| $0$ | $0^2 - 4(0) + 3$ | $0 - 0 + 3$ | $3$ |
| $1$ | $1^2 - 4(1) + 3$ | $1 - 4 + 3$ | $0$ |
| $3$ | $3^2 - 4(3) + 3$ | $9 - 12 + 3$ | $0$ |
| $-2$ | $(-2)^2 - 4(-2) + 3$ | $4 + 8 + 3$ | $15$ |

El recorrido parcial observado es $\{0, 3, 15\}$.

---

### E02: Determinar el dominio de una función

**Situación:** ¿Cuál es el dominio de $f(x) = \dfrac{1}{x - 3}$?

**La Carpintería:**
1. **Restricción:** El denominador no puede ser cero.
2. **Ecuación crítica:** $x - 3 = 0 \Rightarrow x = 3$.
3. **Dominio:** Todos los reales excepto $3$, es decir, $\text{Dom}(f) = \mathbb{R} \setminus \{3\}$.

> En la PAES suelen preguntar: "¿Para qué valor de $x$ la función no está definida?" Respuesta: $x = 3$.

---

### E03: Aplicar el test de la línea vertical

**Situación:** Determina si la relación $x^2 + y^2 = 25$ es una función.

**La Carpintería:**
1. **Despejar $y$:** $y = \pm\sqrt{25 - x^2}$.
2. **Análisis:** Para $x = 0$, obtenemos $y = 5$ o $y = -5$. Dos valores de salida para una misma entrada.
3. **Conclusión:** **No** es función porque no pasa el test de la línea vertical.

---

### E04: Clasificar funciones

**Situación:** Sea $f: \{1, 2, 3\} \to \{a, b, c, d\}$ definida por $f(1) = a$, $f(2) = c$, $f(3) = d$.

**La Carpintería:**

| Propiedad | ¿Se cumple? | Razón |
| :--- | :---: | :--- |
| ¿Inyectiva? | ✅ Sí | Cada entrada tiene imagen distinta: $a \neq c \neq d$ |
| ¿Sobreyectiva? | ❌ No | El elemento $b$ del codominio no es imagen de ningún elemento |
| ¿Biyectiva? | ❌ No | No es sobreyectiva |
""")

    with st.expander("❓ Cuestionario F01: Concepto de Función", expanded=False):
        st.markdown(r"""
**1. ¿Cuál de las siguientes relaciones es una función?**

A) $\{(1, 2), (1, 3), (2, 4)\}$
B) $\{(1, 2), (2, 3), (3, 4)\}$
C) $\{(1, 2), (2, 2), (1, 5)\}$
D) $x^2 + y^2 = 1$

---

**2. Si $f(x) = 3x - 5$, entonces $f(-2)$ es:**

A) $-11$
B) $-1$
C) $1$
D) $11$

---

**3. El dominio de $f(x) = \dfrac{x}{x + 2}$ es:**

A) $\mathbb{R}$
B) $\mathbb{R} \setminus \{2\}$
C) $\mathbb{R} \setminus \{-2\}$
D) $\mathbb{R} \setminus \{0\}$

---

**4. ¿Cuál gráfico NO representa una función?**

A) Una parábola con vértice en el origen abierta hacia arriba
B) Una recta con pendiente $2$
C) Una circunferencia de radio $3$
D) Una recta horizontal $y = 5$

---

**5. Si $f(x) = x^2$ con dominio $\mathbb{R}$, entonces $f$ es:**

A) Inyectiva y sobreyectiva
B) Solo inyectiva
C) Solo sobreyectiva
D) Ni inyectiva ni sobreyectiva (sobre $\mathbb{R}$)

---

**6. Si $f(x) = 2x + 1$ y $f(a) = 7$, entonces $a$ es:**

A) $4$
B) $3$
C) $15$
D) $6$

---

**7. ¿Cuál es el recorrido de $f(x) = |x|$ con dominio $\mathbb{R}$?**

A) $\mathbb{R}$
B) $\{x \in \mathbb{R} : x > 0\}$
C) $\{x \in \mathbb{R} : x \geq 0\}$
D) $\{0\}$
""")

    with st.expander("🔑 Pauta Técnica F01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | En A y C, el valor $x = 1$ tiene dos imágenes distintas, lo que viola la definición de función. D es una circunferencia, que no pasa el test vertical. |
| **2** | **A** | $f(-2) = 3(-2) - 5 = -6 - 5 = -11$. |
| **3** | **C** | El denominador $x + 2 = 0$ cuando $x = -2$. Ese valor se excluye del dominio. |
| **4** | **C** | La circunferencia no pasa el test de la línea vertical: una vertical puede cortarla en dos puntos. |
| **5** | **D** | No es inyectiva ($f(2) = f(-2) = 4$) y no es sobreyectiva sobre $\mathbb{R}$ (no produce valores negativos). |
| **6** | **B** | $2a + 1 = 7 \Rightarrow 2a = 6 \Rightarrow a = 3$. |
| **7** | **C** | El valor absoluto siempre es $\geq 0$, y para cada $y \geq 0$ existe $x$ tal que $|x| = y$. El recorrido es $[0, +\infty)$. |
""")
