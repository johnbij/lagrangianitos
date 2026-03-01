import streamlit as st


def render_V04():
    st.title("V04: La Ecuación de la Recta en Forma Vectorial — Rectas con Flechas")

    st.markdown(r"""
### 🛡️ 1. Ecuación Vectorial de la Recta

Una recta en el plano queda determinada por un **punto** $P_0(x_0, y_0)$ que pertenece a ella y un **vector director** $\vec{d} = (d_1, d_2)$ que indica su dirección.

La **ecuación vectorial** de la recta es:

$$(x, y) = (x_0, y_0) + t(d_1, d_2), \quad t \in \mathbb{R}$$

Cada valor de $t$ genera un punto distinto de la recta.

---

### 🛡️ 2. Ecuaciones Paramétricas

Al separar componentes, obtenemos las **ecuaciones paramétricas**:

$$\begin{cases} x = x_0 + t \cdot d_1 \\ y = y_0 + t \cdot d_2 \end{cases}$$

El parámetro $t$ recorre todos los reales y genera todos los puntos de la recta.

---

### 🛡️ 3. De la Forma Vectorial a la Cartesiana

Para eliminar el parámetro $t$:

1. De la primera ecuación: $t = \frac{x - x_0}{d_1}$ (si $d_1 \neq 0$).
2. De la segunda: $t = \frac{y - y_0}{d_2}$ (si $d_2 \neq 0$).
3. Igualando: $\frac{x - x_0}{d_1} = \frac{y - y_0}{d_2}$.
4. Desarrollando: $d_2(x - x_0) = d_1(y - y_0)$.
5. Reordenando: $d_2 x - d_1 y + (d_1 y_0 - d_2 x_0) = 0$.

La forma cartesiana general es: $ax + by + c = 0$.

---

### 🛡️ 4. Vector Director y Vector Normal

| Concepto | Definición | Relación |
| :--- | :--- | :--- |
| **Vector director** $\vec{d}$ | Paralelo a la recta | Indica la dirección de la recta |
| **Vector normal** $\vec{n}$ | Perpendicular a la recta | $\vec{n} \perp \vec{d}$ |

Si la recta es $ax + by + c = 0$:
- **Vector normal:** $\vec{n} = (a, b)$.
- **Vector director:** $\vec{d} = (-b, a)$ o $(b, -a)$.

> **Tip PAES:** Los coeficientes de $x$ e $y$ en la ecuación cartesiana forman directamente el vector normal.

---

### 🛡️ 5. Paralelismo y Perpendicularidad de Rectas

| Relación | Condición con vectores directores | Condición con vectores normales |
| :--- | :--- | :--- |
| **Paralelas** | $\vec{d}_1 \parallel \vec{d}_2$ (proporcionales) | $\vec{n}_1 \parallel \vec{n}_2$ |
| **Perpendiculares** | $\vec{d}_1 \cdot \vec{d}_2 = 0$ | $\vec{n}_1 \cdot \vec{n}_2 = 0$ |
| **Secantes** | Ni paralelas ni perpendiculares | — |

Dadas $\ell_1: a_1 x + b_1 y + c_1 = 0$ y $\ell_2: a_2 x + b_2 y + c_2 = 0$:

- **Paralelas:** $\frac{a_1}{a_2} = \frac{b_1}{b_2}$ (proporcionales).
- **Perpendiculares:** $a_1 a_2 + b_1 b_2 = 0$.

---

### 🛡️ 6. Resumen de Formas de la Recta

| Forma | Ecuación | Datos necesarios |
| :--- | :--- | :--- |
| Vectorial | $(x,y) = (x_0, y_0) + t(d_1, d_2)$ | Punto + vector director |
| Paramétrica | $x = x_0 + td_1$, $y = y_0 + td_2$ | Punto + vector director |
| Cartesiana | $ax + by + c = 0$ | Coeficientes |
| Pendiente-intercepto | $y = mx + n$ | Pendiente + intercepto |

---

> *"La línea recta es el camino más corto entre dos puntos."*
> — **Arquímedes**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería V04", expanded=False):
        st.markdown(r"""
### E01: Ecuación vectorial a partir de punto y vector director

**Situación:** Encuentra la ecuación vectorial de la recta que pasa por $P(2, 3)$ con vector director $\vec{d} = (1, -4)$.

**La Carpintería:**
1. $(x, y) = (2, 3) + t(1, -4)$, con $t \in \mathbb{R}$.
2. Paramétricas: $x = 2 + t$, $y = 3 - 4t$.

| $t$ | $x$ | $y$ | Punto |
| :---: | :---: | :---: | :--- |
| $0$ | $2$ | $3$ | $P(2,3)$ |
| $1$ | $3$ | $-1$ | $(3, -1)$ |
| $-1$ | $1$ | $7$ | $(1, 7)$ |

---

### E02: De vectorial a cartesiana

**Situación:** Lleva la recta $(x, y) = (1, 2) + t(3, -1)$ a forma cartesiana.

**La Carpintería:**
1. $\vec{d} = (3, -1)$, así que $\vec{n} = (1, 3)$ (perpendicular).
2. La ecuación cartesiana es: $1(x - 1) + 3(y - 2) = 0$.
3. $x - 1 + 3y - 6 = 0$.
4. $x + 3y - 7 = 0$.

**Verificación:** El punto $(1, 2)$: $1 + 6 - 7 = 0$ ✅.

---

### E03: Determinar paralelismo y perpendicularidad

**Situación:** Dadas las rectas $\ell_1: 2x - 3y + 5 = 0$ y $\ell_2: 4x - 6y + 1 = 0$, ¿son paralelas, perpendiculares o secantes?

**La Carpintería:**
1. $\vec{n}_1 = (2, -3)$ y $\vec{n}_2 = (4, -6)$.
2. ¿Proporcionales? $\frac{2}{4} = \frac{-3}{-6} = \frac{1}{2}$. ✅
3. Los vectores normales son proporcionales, así que las rectas son **paralelas**.

---

### E04: Recta por dos puntos

**Situación:** Encuentra la ecuación vectorial de la recta que pasa por $A(1, 5)$ y $B(4, -1)$.

**La Carpintería:**
1. Vector director: $\vec{AB} = (4-1,\; -1-5) = (3, -6)$.
2. Ecuación vectorial: $(x, y) = (1, 5) + t(3, -6)$.
3. Simplificamos $\vec{d}$: podemos usar $\vec{d} = (1, -2)$ (dividiendo por $3$).
4. $(x, y) = (1, 5) + t(1, -2)$.
""")

    with st.expander("❓ Cuestionario V04: La Recta en Forma Vectorial", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es la ecuación vectorial de la recta que pasa por $(3, -1)$ con vector director $(2, 5)$?**

A) $(x, y) = (2, 5) + t(3, -1)$
B) $(x, y) = (3, -1) + t(2, 5)$
C) $(x, y) = (3, -1) + t(5, 2)$
D) $(x, y) = (5, 4) + t(2, 5)$

---

**2. Si la recta tiene ecuación $3x - 2y + 7 = 0$, ¿cuál es su vector normal?**

A) $(3, 7)$
B) $(3, -2)$
C) $(-2, 3)$
D) $(2, 3)$

---

**3. ¿Cuál es un vector director de la recta $5x + y - 3 = 0$?**

A) $(5, 1)$
B) $(1, -5)$
C) $(-1, 5)$
D) B y C son correctas

---

**4. Las rectas $x - 2y + 3 = 0$ y $2x - 4y + 1 = 0$ son:**

A) Perpendiculares
B) Paralelas
C) Coincidentes
D) Secantes

---

**5. Las rectas $3x + y = 0$ y $x - 3y + 2 = 0$ son:**

A) Paralelas
B) Perpendiculares
C) Secantes (no perpendiculares)
D) Coincidentes

---

**6. Si $(x, y) = (0, 1) + t(4, -2)$, ¿qué punto corresponde a $t = 3$?**

A) $(4, -2)$
B) $(12, -5)$
C) $(12, -6)$
D) $(3, -5)$

---

**7. ¿Cuál es la ecuación cartesiana de la recta $(x, y) = (2, 1) + t(1, 3)$?**

A) $x - 3y + 1 = 0$
B) $3x - y - 5 = 0$
C) $x + 3y - 5 = 0$
D) $3x + y - 7 = 0$
""")

    with st.expander("🔑 Pauta Técnica V04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | Formato: punto + $t$ · (vector director). Punto = $(3,-1)$, $\vec{d} = (2,5)$. |
| **2** | **B** | En $ax + by + c = 0$, el vector normal es $(a, b) = (3, -2)$. |
| **3** | **D** | Si $\vec{n} = (5, 1)$, los directores son $(-1, 5)$ o $(1, -5)$. Ambos son válidos. |
| **4** | **B** | $\frac{1}{2} = \frac{-2}{-4} = \frac{1}{2}$. Los coeficientes son proporcionales → paralelas. |
| **5** | **B** | $\vec{n}_1 \cdot \vec{n}_2 = (3)(1) + (1)(-3) = 0$. Producto punto cero → perpendiculares. |
| **6** | **B** | $x = 0 + 4(3) = 12$, $y = 1 + (-2)(3) = -5$. El punto es $(12, -5)$. |
| **7** | **B** | $\vec{d} = (1,3)$, $\vec{n} = (3, -1)$. Ecuación: $3(x-2) - 1(y-1) = 0 \Rightarrow 3x - y - 5 = 0$. |
""")
