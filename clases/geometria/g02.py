import streamlit as st


def render_G02():
    st.title("G02: Triángulos — La Figura Indestructible")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Por qué el Triángulo es la Figura más Importante?

De todas las figuras geométricas, el triángulo es la única que **no se deforma** al aplicar fuerza sobre sus vértices. Por eso los puentes, techos y estructuras metálicas se construyen con triángulos: es la figura **rígida** por excelencia.

Un **triángulo** es un polígono de tres lados, tres vértices y tres ángulos interiores. Es el polígono más simple y la base de toda la geometría plana.

---

### 🛡️ 1.1 Clasificación por Lados

| Tipo | Propiedad de lados | Propiedad de ángulos |
| :--- | :--- | :--- |
| **Equilátero** | Tres lados iguales | Tres ángulos iguales de $60°$ |
| **Isósceles** | Dos lados iguales | Dos ángulos basales iguales |
| **Escaleno** | Tres lados distintos | Tres ángulos distintos |

---

### 🛡️ 1.2 Clasificación por Ángulos

| Tipo | Propiedad |
| :--- | :--- |
| **Acutángulo** | Los tres ángulos son agudos ($< 90°$) |
| **Rectángulo** | Tiene un ángulo recto ($= 90°$) |
| **Obtusángulo** | Tiene un ángulo obtuso ($> 90°$) |

> **Tip PAES:** Un triángulo puede pertenecer a ambas clasificaciones al mismo tiempo. Por ejemplo, un triángulo **isósceles rectángulo** tiene dos lados iguales y un ángulo de $90°$.

---

### 🏛️ 1.3 Propiedades Fundamentales

**Suma de ángulos interiores:**

$$\alpha + \beta + \gamma = 180°$$

Esta es la propiedad más usada en la PAES. Si conoces dos ángulos, siempre puedes encontrar el tercero.

**Ángulo exterior:**

El ángulo exterior de un triángulo es igual a la **suma de los dos ángulos interiores no adyacentes**:

$$\theta_{ext} = \alpha + \beta$$

donde $\alpha$ y $\beta$ son los ángulos interiores no adyacentes al ángulo exterior $\theta_{ext}$.

**Desigualdad triangular:**

Para que tres segmentos formen un triángulo, la suma de cualesquiera dos lados debe ser **mayor** que el tercero:

$$a + b > c, \quad a + c > b, \quad b + c > a$$

> **Tip PAES:** Para verificar rápidamente, basta comprobar que la suma de los dos lados **menores** sea mayor que el lado **mayor**.

---

### 🛡️ 1.4 Congruencia de Triángulos

Dos triángulos son **congruentes** ($\cong$) si tienen exactamente la misma forma y tamaño. Los criterios son:

| Criterio | Significado | Qué necesitas saber |
| :--- | :--- | :--- |
| **LLL** | Lado-Lado-Lado | Los tres lados de uno son iguales a los tres del otro |
| **LAL** | Lado-Ángulo-Lado | Dos lados y el ángulo **comprendido** entre ellos son iguales |
| **ALA** | Ángulo-Lado-Ángulo | Dos ángulos y el lado **comprendido** entre ellos son iguales |

> **Cuidado:** El criterio **AAL** (Ángulo-Ángulo-Lado) también es válido, pero **LLA** no siempre lo es (caso ambiguo).

---

### 🛡️ 1.5 Semejanza de Triángulos

Dos triángulos son **semejantes** ($\sim$) si tienen la misma forma pero pueden diferir en tamaño. Sus lados correspondientes son **proporcionales** y sus ángulos correspondientes son **iguales**.

| Criterio | Significado |
| :--- | :--- |
| **AA** | Dos pares de ángulos iguales (el tercero queda determinado) |
| **LAL** | Dos lados proporcionales y el ángulo comprendido igual |
| **LLL** | Los tres pares de lados proporcionales |

Si los triángulos son semejantes con razón de semejanza $k$, entonces:

$$\frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c} = k$$

---

> "Un triángulo es la mitad de un paralelogramo, y eso basta para construir el mundo."
> — **Euclides**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G02", expanded=False):
        st.markdown(r"""
### E01: Encontrar un ángulo desconocido

**Situación:** Un triángulo tiene ángulos de $45°$ y $78°$. ¿Cuánto mide el tercer ángulo?

**La Carpintería:**
1. Suma de ángulos interiores: $\alpha + \beta + \gamma = 180°$.
2. $45° + 78° + \gamma = 180°$.
3. $\gamma = 180° - 45° - 78° = 57°$.

---

### E02: Ángulo exterior

**Situación:** En un triángulo, los ángulos interiores miden $50°$ y $65°$. ¿Cuánto mide el ángulo exterior adyacente al tercer ángulo?

**La Carpintería:**
1. El ángulo exterior es la suma de los dos interiores no adyacentes: $\theta_{ext} = 50° + 65° = 115°$.
2. **Verificación:** El tercer ángulo interior es $180° - 50° - 65° = 65°$. Su suplemento es $180° - 65° = 115°$ ✅.

---

### E03: Desigualdad triangular

**Situación:** ¿Pueden tres segmentos de longitudes $3$, $7$ y $12$ formar un triángulo?

**La Carpintería:**
1. Verificar: $3 + 7 = 10 > 12$? → $10 > 12$ es **falso**.
2. **No pueden** formar un triángulo.
3. La suma de los dos lados menores ($3 + 7 = 10$) no supera al lado mayor ($12$).

| Verificación | Operación | ¿Cumple? |
| :--- | :--- | :---: |
| $3 + 7 > 12$ | $10 > 12$ | ❌ No |

---

### E04: Semejanza de triángulos

**Situación:** Dos triángulos semejantes tienen lados $3$, $4$, $5$ y $6$, $x$, $10$ respectivamente. Encuentra $x$.

**La Carpintería:**
1. La razón de semejanza: $k = \dfrac{6}{3} = 2$. Verificamos: $\dfrac{10}{5} = 2$ ✅.
2. El lado desconocido: $x = 4 \cdot 2 = 8$.

| Lado original | Factor $k$ | Lado semejante |
| :--- | :---: | :--- |
| $3$ | $\times 2$ | $6$ |
| $4$ | $\times 2$ | $8$ |
| $5$ | $\times 2$ | $10$ |
""")

    with st.expander("❓ Cuestionario G02: Triángulos", expanded=False):
        st.markdown(r"""
**1. Un triángulo tiene ángulos de $60°$, $60°$ y $60°$. ¿Cómo se clasifica?**

A) Isósceles acutángulo
B) Equilátero acutángulo
C) Escaleno acutángulo
D) Equilátero rectángulo

---

**2. Si dos ángulos de un triángulo miden $35°$ y $90°$, ¿cuánto mide el tercero?**

A) $45°$
B) $55°$
C) $65°$
D) $125°$

---

**3. ¿Cuál de las siguientes ternas de longitudes NO puede formar un triángulo?**

A) $3, 4, 5$
B) $5, 5, 8$
C) $2, 3, 7$
D) $6, 7, 10$

---

**4. El ángulo exterior de un triángulo mide $130°$. Si uno de los ángulos interiores no adyacentes mide $55°$, ¿cuánto mide el otro?**

A) $50°$
B) $55°$
C) $75°$
D) $125°$

---

**5. Dos triángulos tienen dos pares de ángulos iguales ($40°$ y $80°$). ¿Qué criterio de semejanza se aplica?**

A) LLL
B) LAL
C) AA
D) ALA

---

**6. Si un triángulo isósceles tiene un ángulo de $100°$, ¿cuánto miden los ángulos basales?**

A) $40°$ cada uno
B) $50°$ cada uno
C) $80°$ cada uno
D) $30°$ cada uno

---

**7. ¿Cuál es el criterio de congruencia que utiliza dos lados y el ángulo comprendido entre ellos?**

A) LLL
B) ALA
C) LAL
D) AA
""")

    with st.expander("🔑 Pauta Técnica G02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | Tres ángulos de $60°$ implican tres lados iguales → equilátero. Todos los ángulos son agudos → acutángulo. |
| **2** | **B** | $180° - 35° - 90° = 55°$. |
| **3** | **C** | $2 + 3 = 5 < 7$. La suma de los dos menores no supera al mayor. |
| **4** | **C** | Ángulo exterior = suma de interiores no adyacentes: $130° = 55° + x \Rightarrow x = 75°$. |
| **5** | **C** | Dos pares de ángulos iguales → criterio AA de semejanza. El tercer ángulo queda determinado. |
| **6** | **A** | El ángulo de $100°$ es el ángulo desigual. Los basales: $(180° - 100°) \div 2 = 40°$. |
| **7** | **C** | LAL = Lado-Ángulo-Lado, donde el ángulo está comprendido entre los dos lados. |
""")
