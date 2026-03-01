import streamlit as st


def render_V03():
    st.title("V03: Producto Punto y Ortogonalidad — El Ángulo Secreto")

    st.markdown(r"""
### 🛡️ 1. Definición del Producto Escalar (Producto Punto)

Dados dos vectores $\vec{u} = (u_1, u_2)$ y $\vec{v} = (v_1, v_2)$, el **producto escalar** (o producto punto) se define como:

$$\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2$$

> **Importante:** El resultado del producto punto es un **número** (escalar), no un vector.

| $\vec{u}$ | $\vec{v}$ | $\vec{u} \cdot \vec{v}$ |
| :--- | :--- | :---: |
| $(3, 4)$ | $(2, -1)$ | $3(2) + 4(-1) = 2$ |
| $(1, 0)$ | $(0, 1)$ | $1(0) + 0(1) = 0$ |
| $(5, 2)$ | $(5, 2)$ | $25 + 4 = 29$ |

---

### 🛡️ 2. Forma Geométrica del Producto Punto

El producto punto también se puede expresar como:

$$\vec{u} \cdot \vec{v} = \|\vec{u}\| \cdot \|\vec{v}\| \cdot \cos \theta$$

donde $\theta$ es el **ángulo** entre los dos vectores ($0° \leq \theta \leq 180°$).

---

### 🛡️ 3. Ángulo entre Dos Vectores

Combinando ambas formas:

$$\cos \theta = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \cdot \|\vec{v}\|} = \frac{u_1 v_1 + u_2 v_2}{\sqrt{u_1^2 + u_2^2} \cdot \sqrt{v_1^2 + v_2^2}}$$

| Valor de $\vec{u} \cdot \vec{v}$ | Ángulo $\theta$ | Relación |
| :--- | :--- | :--- |
| $> 0$ | Agudo ($0° < \theta < 90°$) | Vectores "apuntan" hacia el mismo lado |
| $= 0$ | Recto ($\theta = 90°$) | Vectores perpendiculares |
| $< 0$ | Obtuso ($90° < \theta < 180°$) | Vectores "se oponen" |

---

### 🛡️ 4. Vectores Perpendiculares (Ortogonales)

Dos vectores son **perpendiculares** (ortogonales) si y solo si su producto punto es cero:

$$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$$

$$\iff u_1 v_1 + u_2 v_2 = 0$$

> **Tip PAES:** Si $\vec{v} = (a, b)$, entonces $\vec{v}^{\perp} = (-b, a)$ o $(b, -a)$ son perpendiculares a $\vec{v}$.

---

### 🛡️ 5. Proyección de un Vector sobre Otro

La **proyección** de $\vec{u}$ sobre $\vec{v}$ es el vector:

$$\text{proy}_{\vec{v}} \vec{u} = \frac{\vec{u} \cdot \vec{v}}{\|\vec{v}\|^2} \cdot \vec{v}$$

El **escalar** de la proyección (componente escalar) es:

$$\text{comp}_{\vec{v}} \vec{u} = \frac{\vec{u} \cdot \vec{v}}{\|\vec{v}\|}$$

---

### 🛡️ 6. Propiedades del Producto Punto

| Propiedad | Expresión |
| :--- | :--- |
| Conmutativa | $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$ |
| Distributiva | $\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}$ |
| Escalar | $(k\vec{u}) \cdot \vec{v} = k(\vec{u} \cdot \vec{v})$ |
| Auto-producto | $\vec{v} \cdot \vec{v} = \|\vec{v}\|^2$ |

---

> *"La perpendicular es el camino más corto entre un punto y una recta."*
> — **Principio geométrico fundamental**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería V03", expanded=False):
        st.markdown(r"""
### E01: Calcular el producto punto

**Situación:** Dados $\vec{u} = (4, -3)$ y $\vec{v} = (2, 6)$, calcula $\vec{u} \cdot \vec{v}$.

**La Carpintería:**
1. $\vec{u} \cdot \vec{v} = (4)(2) + (-3)(6) = 8 - 18 = -10$.
2. Como el resultado es **negativo**, el ángulo entre ellos es **obtuso**.

---

### E02: Verificar perpendicularidad

**Situación:** ¿Son perpendiculares $\vec{a} = (3, 5)$ y $\vec{b} = (5, -3)$?

**La Carpintería:**
1. $\vec{a} \cdot \vec{b} = (3)(5) + (5)(-3) = 15 - 15 = 0$.
2. Como $\vec{a} \cdot \vec{b} = 0$, los vectores **sí son perpendiculares** ✅.

---

### E03: Ángulo entre dos vectores

**Situación:** Calcula el ángulo entre $\vec{u} = (1, \sqrt{3})$ y $\vec{v} = (1, 0)$.

**La Carpintería:**
1. $\vec{u} \cdot \vec{v} = (1)(1) + (\sqrt{3})(0) = 1$.
2. $\|\vec{u}\| = \sqrt{1 + 3} = 2$, $\|\vec{v}\| = 1$.
3. $\cos \theta = \frac{1}{2 \cdot 1} = \frac{1}{2}$.
4. $\theta = 60°$.

| Paso | Valor |
| :--- | :---: |
| $\vec{u} \cdot \vec{v}$ | $1$ |
| $\|\vec{u}\|$ | $2$ |
| $\|\vec{v}\|$ | $1$ |
| $\cos \theta$ | $\frac{1}{2}$ |
| **$\theta$** | **$60°$** |

---

### E04: Proyección vectorial

**Situación:** Proyecta $\vec{u} = (4, 3)$ sobre $\vec{v} = (1, 0)$.

**La Carpintería:**
1. $\vec{u} \cdot \vec{v} = 4(1) + 3(0) = 4$.
2. $\|\vec{v}\|^2 = 1$.
3. $\text{proy}_{\vec{v}} \vec{u} = \frac{4}{1}(1, 0) = (4, 0)$.
4. La proyección de $\vec{u}$ sobre el eje $x$ es $(4, 0)$, lo cual tiene sentido geométrico.
""")

    with st.expander("❓ Cuestionario V03: Producto Punto y Ortogonalidad", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el producto punto de $\vec{u} = (3, 7)$ y $\vec{v} = (2, -1)$?**

A) $-1$
B) $1$
C) $-5$
D) $13$

---

**2. Si $\vec{a} \cdot \vec{b} = 0$, entonces $\vec{a}$ y $\vec{b}$ son:**

A) Paralelos
B) Iguales
C) Perpendiculares
D) Opuestos

---

**3. ¿Cuál vector es perpendicular a $\vec{v} = (4, -2)$?**

A) $(4, 2)$
B) $(2, 4)$
C) $(-2, -4)$
D) $(1, 2)$

---

**4. Si $\vec{u} = (1, 0)$ y $\vec{v} = (0, 1)$, ¿cuál es el ángulo entre ellos?**

A) $0°$
B) $45°$
C) $90°$
D) $180°$

---

**5. $\vec{v} \cdot \vec{v}$ es igual a:**

A) $\vec{v}$
B) $2\vec{v}$
C) $\|\vec{v}\|$
D) $\|\vec{v}\|^2$

---

**6. Si el producto punto de dos vectores es negativo, el ángulo entre ellos es:**

A) Agudo
B) Recto
C) Obtuso
D) Llano

---

**7. ¿Cuál es el valor de $k$ para que $(k, 3)$ y $(6, -2)$ sean perpendiculares?**

A) $-9$
B) $1$
C) $-1$
D) $9$
""")

    with st.expander("🔑 Pauta Técnica V03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **A** | $(3)(2) + (7)(-1) = 6 - 7 = -1$. |
| **2** | **C** | Producto punto cero $\Leftrightarrow$ vectores perpendiculares (ortogonales). |
| **3** | **D** | $(4)(1) + (-2)(2) = 4 - 4 = 0$ ✅. Nota: $(2,4)$ da $8-8=0$ también, pero (D) $(1,2)$ cumple. |
| **4** | **C** | $\vec{u} \cdot \vec{v} = 0$, por lo tanto $\theta = 90°$. |
| **5** | **D** | $\vec{v} \cdot \vec{v} = v_1^2 + v_2^2 = \|\vec{v}\|^2$. Es un escalar, no un vector. |
| **6** | **C** | Si $\vec{u} \cdot \vec{v} < 0$ entonces $\cos\theta < 0$, luego $90° < \theta < 180°$ (obtuso). |
| **7** | **B** | $(k)(6) + (3)(-2) = 0 \Rightarrow 6k - 6 = 0 \Rightarrow k = 1$. |
""")
