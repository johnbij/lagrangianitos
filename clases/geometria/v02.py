import streamlit as st


def render_V02():
    st.title("V02: Operaciones con Vectores — Sumando Flechas")

    st.markdown(r"""
### 🛡️ 1. Suma de Vectores

Dados $\vec{u} = (u_1, u_2)$ y $\vec{v} = (v_1, v_2)$:

$$\vec{u} + \vec{v} = (u_1 + v_1,\; u_2 + v_2)$$

**Interpretación geométrica:**
- **Regla del paralelogramo:** Se colocan ambos vectores con el mismo origen; la diagonal del paralelogramo es la suma.
- **Regla del triángulo (punta-cola):** Se coloca el origen de $\vec{v}$ en la punta de $\vec{u}$; la suma va del origen de $\vec{u}$ a la punta de $\vec{v}$.

---

### 🛡️ 2. Resta de Vectores

$$\vec{u} - \vec{v} = (u_1 - v_1,\; u_2 - v_2)$$

Geométricamente, $\vec{u} - \vec{v} = \vec{u} + (-\vec{v})$, es decir, se suma $\vec{u}$ con el opuesto de $\vec{v}$.

---

### 🛡️ 3. Multiplicación por un Escalar

Dado un escalar $k \in \mathbb{R}$ y un vector $\vec{v} = (v_1, v_2)$:

$$k \cdot \vec{v} = (k \cdot v_1,\; k \cdot v_2)$$

| Escalar $k$ | Efecto sobre $\vec{v}$ |
| :--- | :--- |
| $k > 1$ | Estira el vector (mismo sentido) |
| $0 < k < 1$ | Comprime el vector (mismo sentido) |
| $k = -1$ | Invierte el sentido |
| $k < 0$ | Estira/comprime e invierte el sentido |
| $k = 0$ | Resultado: vector nulo $\vec{0}$ |

El módulo se escala: $\|k\vec{v}\| = |k| \cdot \|\vec{v}\|$.

---

### 🛡️ 4. Combinación Lineal

Una **combinación lineal** de vectores $\vec{u}$ y $\vec{v}$ es cualquier expresión de la forma:

$$\alpha \vec{u} + \beta \vec{v}$$

donde $\alpha, \beta \in \mathbb{R}$.

Cualquier vector del plano se puede escribir como combinación lineal de dos vectores no paralelos. En particular:

$$\vec{v} = v_1 \hat{i} + v_2 \hat{j}$$

---

### 🛡️ 5. Propiedades de las Operaciones

| Propiedad | Expresión |
| :--- | :--- |
| Conmutativa (suma) | $\vec{u} + \vec{v} = \vec{v} + \vec{u}$ |
| Asociativa (suma) | $(\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})$ |
| Elemento neutro | $\vec{v} + \vec{0} = \vec{v}$ |
| Elemento opuesto | $\vec{v} + (-\vec{v}) = \vec{0}$ |
| Distributiva escalar | $k(\vec{u} + \vec{v}) = k\vec{u} + k\vec{v}$ |
| Distributiva vectorial | $(k_1 + k_2)\vec{v} = k_1 \vec{v} + k_2 \vec{v}$ |
| Asociativa escalar | $k_1(k_2 \vec{v}) = (k_1 k_2)\vec{v}$ |

---

### 🛡️ 6. Vectores Paralelos

Dos vectores $\vec{u}$ y $\vec{v}$ son **paralelos** (o colineales) si uno es múltiplo escalar del otro:

$$\vec{u} \parallel \vec{v} \iff \vec{u} = k \vec{v} \text{ para algún } k \in \mathbb{R}$$

Equivalentemente: $\vec{u} = (u_1, u_2)$ y $\vec{v} = (v_1, v_2)$ son paralelos si y solo si:

$$u_1 v_2 - u_2 v_1 = 0$$

---

> *"Las matemáticas son la reina de las ciencias."*
> — **Carl Friedrich Gauss**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería V02", expanded=False):
        st.markdown(r"""
### E01: Suma y resta de vectores

**Situación:** Dados $\vec{u} = (3, -2)$ y $\vec{v} = (-1, 5)$, calcula $\vec{u} + \vec{v}$ y $\vec{u} - \vec{v}$.

**La Carpintería:**
1. $\vec{u} + \vec{v} = (3 + (-1),\; -2 + 5) = (2, 3)$.
2. $\vec{u} - \vec{v} = (3 - (-1),\; -2 - 5) = (4, -7)$.

| Operación | Resultado |
| :--- | :---: |
| $\vec{u} + \vec{v}$ | $(2, 3)$ |
| $\vec{u} - \vec{v}$ | $(4, -7)$ |

---

### E02: Multiplicación por escalar

**Situación:** Si $\vec{v} = (4, -3)$, calcula $2\vec{v}$, $-\vec{v}$ y $\frac{1}{2}\vec{v}$.

**La Carpintería:**
1. $2\vec{v} = (8, -6)$.
2. $-\vec{v} = (-4, 3)$.
3. $\frac{1}{2}\vec{v} = (2, -1{,}5)$.

| Escalar | Resultado | Módulo |
| :---: | :---: | :---: |
| $2$ | $(8, -6)$ | $10$ |
| $-1$ | $(-4, 3)$ | $5$ |
| $\frac{1}{2}$ | $(2, -1{,}5)$ | $2{,}5$ |

Módulo original: $\|\vec{v}\| = \sqrt{16+9} = 5$. Se confirma: $\|2\vec{v}\| = 2 \cdot 5 = 10$.

---

### E03: Combinación lineal

**Situación:** Expresa $\vec{w} = (7, 1)$ como combinación lineal de $\vec{u} = (2, 1)$ y $\vec{v} = (1, -1)$.

**La Carpintería:**
1. Buscamos $\alpha$ y $\beta$ tales que $\alpha(2, 1) + \beta(1, -1) = (7, 1)$.
2. Sistema: $2\alpha + \beta = 7$ y $\alpha - \beta = 1$.
3. Sumando: $3\alpha = 8 \Rightarrow \alpha = \frac{8}{3}$.
4. De la segunda: $\beta = \alpha - 1 = \frac{8}{3} - 1 = \frac{5}{3}$.
5. $\vec{w} = \frac{8}{3}\vec{u} + \frac{5}{3}\vec{v}$.

---

### E04: Verificar paralelismo

**Situación:** ¿Son paralelos $\vec{a} = (6, -4)$ y $\vec{b} = (-9, 6)$?

**La Carpintería:**
1. Comprobamos: $u_1 v_2 - u_2 v_1 = (6)(6) - (-4)(-9) = 36 - 36 = 0$.
2. Como el resultado es $0$, **sí son paralelos**.
3. Además, $\vec{b} = -\frac{3}{2}\vec{a}$ (sentidos opuestos).
""")

    with st.expander("❓ Cuestionario V02: Operaciones con Vectores", expanded=False):
        st.markdown(r"""
**1. Si $\vec{u} = (2, 5)$ y $\vec{v} = (3, -1)$, ¿cuánto es $\vec{u} + \vec{v}$?**

A) $(5, 4)$
B) $(5, 6)$
C) $(-1, 6)$
D) $(6, 4)$

---

**2. Si $\vec{w} = (-4, 7)$, ¿cuánto es $3\vec{w}$?**

A) $(-12, 21)$
B) $(-1, 10)$
C) $(12, -21)$
D) $(-12, -21)$

---

**3. Dados $\vec{a} = (1, 3)$ y $\vec{b} = (4, -2)$, ¿cuánto es $\vec{a} - \vec{b}$?**

A) $(5, 1)$
B) $(-3, 5)$
C) $(3, -5)$
D) $(-5, 1)$

---

**4. ¿Cuál de los siguientes pares de vectores son paralelos?**

A) $(2, 3)$ y $(4, 5)$
B) $(1, -2)$ y $(-3, 6)$
C) $(3, 1)$ y $(1, 3)$
D) $(5, 0)$ y $(0, 5)$

---

**5. Si $\vec{u} + \vec{v} = (6, 2)$ y $\vec{u} = (4, -1)$, entonces $\vec{v} =$**

A) $(10, 1)$
B) $(2, 3)$
C) $(-2, -3)$
D) $(2, -3)$

---

**6. ¿Cuál es el módulo de $2\vec{v}$ si $\|\vec{v}\| = 7$?**

A) $7$
B) $9$
C) $14$
D) $49$

---

**7. La combinación lineal $2(1, 0) + 3(0, 1)$ da como resultado:**

A) $(2, 3)$
B) $(3, 2)$
C) $(5, 5)$
D) $(6, 0)$
""")

    with st.expander("🔑 Pauta Técnica V02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **A** | $(2+3,\; 5+(-1)) = (5, 4)$. |
| **2** | **A** | $3(-4, 7) = (-12, 21)$. |
| **3** | **B** | $(1-4,\; 3-(-2)) = (-3, 5)$. |
| **4** | **B** | $(1)(-3) \cdot$ test: $u_1 v_2 - u_2 v_1 = (1)(6) - (-2)(-3) = 6 - 6 = 0$. Son paralelos. |
| **5** | **B** | $\vec{v} = (6,2) - (4,-1) = (2, 3)$. |
| **6** | **C** | $\|2\vec{v}\| = |2| \cdot \|\vec{v}\| = 2 \cdot 7 = 14$. |
| **7** | **A** | $2(1,0) + 3(0,1) = (2,0) + (0,3) = (2, 3)$. |
""")
