import streamlit as st


def render_G03():
    st.title("G03: Cuadriláteros y Polígonos — Más Allá del Triángulo")

    st.markdown(r"""
### 🛡️ 1. El Portal: Del Triángulo al Mundo de los Polígonos

Si el triángulo es el ladrillo básico de la geometría, los **cuadriláteros** y los **polígonos** son las paredes, pisos y techos que construimos con esos ladrillos. Todo polígono se puede descomponer en triángulos, y esa idea simple es la clave para entender sus propiedades.

Un **polígono** es una figura plana cerrada formada por segmentos de recta llamados **lados**. Un **cuadrilátero** es un polígono de cuatro lados.

---

### 🛡️ 1.1 Clasificación de Cuadriláteros

| Cuadrilátero | Lados paralelos | Propiedades clave |
| :--- | :--- | :--- |
| **Paralelogramo** | 2 pares de lados paralelos | Lados opuestos iguales, ángulos opuestos iguales, diagonales se bisecan |
| **Rectángulo** | 2 pares de lados paralelos | Paralelogramo con 4 ángulos rectos, diagonales iguales |
| **Rombo** | 2 pares de lados paralelos | Paralelogramo con 4 lados iguales, diagonales perpendiculares |
| **Cuadrado** | 2 pares de lados paralelos | Rectángulo + Rombo: 4 lados iguales y 4 ángulos rectos |
| **Trapecio** | 1 par de lados paralelos | Las bases son los lados paralelos |
| **Trapezoide** | 0 pares de lados paralelos | Cuadrilátero general sin paralelismo |

> **Tip PAES:** El cuadrado es simultáneamente un rectángulo, un rombo y un paralelogramo. La jerarquía es: cuadrado ⊂ rombo ⊂ paralelogramo y cuadrado ⊂ rectángulo ⊂ paralelogramo.

---

### 🛡️ 1.2 Propiedades de las Diagonales

| Cuadrilátero | Diagonales iguales | Diagonales se bisecan | Diagonales perpendiculares |
| :--- | :---: | :---: | :---: |
| **Paralelogramo** | No necesariamente | ✅ Sí | No necesariamente |
| **Rectángulo** | ✅ Sí | ✅ Sí | No necesariamente |
| **Rombo** | No necesariamente | ✅ Sí | ✅ Sí |
| **Cuadrado** | ✅ Sí | ✅ Sí | ✅ Sí |
| **Trapecio isósceles** | ✅ Sí | No | No necesariamente |

---

### 🏛️ 1.3 Suma de Ángulos Interiores de un Polígono

Todo polígono de $n$ lados se puede dividir en $(n - 2)$ triángulos trazando diagonales desde un vértice. Como cada triángulo tiene $180°$, la suma de los ángulos interiores es:

$$S_i = (n - 2) \cdot 180°$$

| Polígono | $n$ | Triángulos | Suma ángulos interiores |
| :--- | :---: | :---: | :---: |
| Triángulo | $3$ | $1$ | $180°$ |
| Cuadrilátero | $4$ | $2$ | $360°$ |
| Pentágono | $5$ | $3$ | $540°$ |
| Hexágono | $6$ | $4$ | $720°$ |
| Decágono | $10$ | $8$ | $1440°$ |

---

### 🛡️ 1.4 Polígonos Regulares

Un polígono es **regular** si todos sus lados son iguales y todos sus ángulos son iguales. En un polígono regular de $n$ lados, cada ángulo interior mide:

$$\alpha = \frac{(n - 2) \cdot 180°}{n}$$

Y cada ángulo exterior mide:

$$\beta = \frac{360°}{n}$$

> **Dato clave:** La suma de todos los ángulos **exteriores** de cualquier polígono convexo es siempre $360°$, sin importar el número de lados.

---

### 🛡️ 1.5 Número de Diagonales

El número de diagonales de un polígono de $n$ lados es:

$$d = \frac{n(n - 3)}{2}$$

| Polígono | $n$ | Diagonales |
| :--- | :---: | :---: |
| Triángulo | $3$ | $0$ |
| Cuadrilátero | $4$ | $2$ |
| Pentágono | $5$ | $5$ |
| Hexágono | $6$ | $9$ |
| Decágono | $10$ | $35$ |

---

> "La naturaleza es un libro escrito en el lenguaje de la geometría."
> — **Galileo Galilei**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G03", expanded=False):
        st.markdown(r"""
### E01: Suma de ángulos de un cuadrilátero

**Situación:** Un cuadrilátero tiene tres ángulos de $85°$, $90°$ y $110°$. ¿Cuánto mide el cuarto ángulo?

**La Carpintería:**
1. Suma de ángulos interiores de un cuadrilátero: $(4 - 2) \cdot 180° = 360°$.
2. $85° + 90° + 110° + x = 360°$.
3. $x = 360° - 285° = 75°$.

---

### E02: Ángulo interior de un polígono regular

**Situación:** ¿Cuánto mide cada ángulo interior de un octógono regular?

**La Carpintería:**
1. Fórmula: $\alpha = \dfrac{(n - 2) \cdot 180°}{n}$.
2. $\alpha = \dfrac{(8 - 2) \cdot 180°}{8} = \dfrac{6 \cdot 180°}{8} = \dfrac{1080°}{8} = 135°$.

| Paso | Cálculo | Resultado |
| :--- | :--- | :---: |
| Valor de $n$ | $n = 8$ | — |
| Numerador | $(8-2) \cdot 180° = 1080°$ | — |
| División | $1080° \div 8$ | $135°$ |

---

### E03: Diagonales de un polígono

**Situación:** ¿Cuántas diagonales tiene un heptágono ($7$ lados)?

**La Carpintería:**
1. Fórmula: $d = \dfrac{n(n - 3)}{2}$.
2. $d = \dfrac{7(7 - 3)}{2} = \dfrac{7 \cdot 4}{2} = \dfrac{28}{2} = 14$.

---

### E04: Identificar un cuadrilátero por sus diagonales

**Situación:** Un cuadrilátero tiene diagonales que se bisecan mutuamente y son perpendiculares, pero no son iguales. ¿Qué cuadrilátero es?

**La Carpintería:**
1. Se bisecan → es un **paralelogramo**.
2. Son perpendiculares → es un **rombo**.
3. No son iguales → **no es un cuadrado** (el cuadrado tiene diagonales iguales).
4. **Respuesta:** Es un **rombo** (que no es cuadrado).
""")

    with st.expander("❓ Cuestionario G03: Cuadriláteros y Polígonos", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es la suma de los ángulos interiores de un hexágono?**

A) $540°$
B) $600°$
C) $720°$
D) $1080°$

---

**2. ¿Cuántas diagonales tiene un pentágono?**

A) $3$
B) $5$
C) $7$
D) $10$

---

**3. Un paralelogramo tiene un ángulo de $70°$. ¿Cuánto miden los otros tres ángulos?**

A) $70°$, $110°$, $110°$
B) $70°$, $70°$, $150°$
C) $110°$, $110°$, $70°$
D) $70°$, $90°$, $130°$

---

**4. ¿Cuánto mide cada ángulo exterior de un polígono regular de $12$ lados?**

A) $15°$
B) $30°$
C) $36°$
D) $150°$

---

**5. ¿Cuál cuadrilátero tiene diagonales que son iguales, se bisecan mutuamente y son perpendiculares?**

A) Rectángulo
B) Rombo
C) Cuadrado
D) Trapecio

---

**6. ¿Cuántos triángulos se forman al trazar todas las diagonales desde un vértice de un decágono?**

A) $7$
B) $8$
C) $9$
D) $10$

---

**7. Un polígono regular tiene ángulos interiores de $120°$. ¿De cuántos lados es?**

A) $5$
B) $6$
C) $8$
D) $10$
""")

    with st.expander("🔑 Pauta Técnica G03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **C** | $(6 - 2) \cdot 180° = 4 \cdot 180° = 720°$. |
| **2** | **B** | $d = \frac{5(5-3)}{2} = \frac{5 \cdot 2}{2} = 5$. |
| **3** | **A** | En un paralelogramo, ángulos opuestos son iguales y consecutivos son suplementarios: $70°$, $110°$, $70°$, $110°$. Los otros tres son $70°$, $110°$, $110°$. |
| **4** | **B** | $\frac{360°}{12} = 30°$. |
| **5** | **C** | Solo el cuadrado cumple las tres propiedades: iguales, se bisecan y perpendiculares. |
| **6** | **B** | Desde un vértice de un polígono de $n$ lados se forman $n - 2$ triángulos: $10 - 2 = 8$. |
| **7** | **B** | Si $\frac{(n-2) \cdot 180°}{n} = 120°$, entonces $(n-2) \cdot 180 = 120n$, $180n - 360 = 120n$, $60n = 360$, $n = 6$. Hexágono regular. |
""")
