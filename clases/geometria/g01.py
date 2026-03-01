import streamlit as st


def render_G01():
    st.title("G01: Ángulos y Rectas — La Geometría del Encuentro")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Por qué Importan los Ángulos?

Cada vez que dos calles se cruzan, que abres una puerta o que un rayo de sol entra por la ventana, se forma un **ángulo**. La geometría de los ángulos es la primera herramienta que usamos para medir y describir el espacio que nos rodea.

Un **ángulo** es la región del plano comprendida entre dos **rayos** (semirrectas) que comparten un mismo punto de origen llamado **vértice**. Se mide en **grados sexagesimales** (°).

---

### 🛡️ 1.1 Clasificación de Ángulos según su Medida

| Tipo de ángulo | Medida | Ejemplo visual |
| :--- | :--- | :--- |
| **Agudo** | $0° < \alpha < 90°$ | Un trozo de pizza delgado |
| **Recto** | $\alpha = 90°$ | La esquina de un cuaderno |
| **Obtuso** | $90° < \alpha < 180°$ | Una puerta casi abierta |
| **Llano o extendido** | $\alpha = 180°$ | Una línea recta |
| **Completo o perigonal** | $\alpha = 360°$ | Una vuelta completa |

> **Tip PAES:** Si la pregunta dice "ángulo recto", piensa inmediatamente en $90°$. Es la medida más frecuente en los ítems de geometría.

---

### 🛡️ 1.2 Pares de Ángulos Especiales

Cuando dos ángulos se relacionan entre sí, aparecen combinaciones que la PAES adora preguntar:

| Relación | Definición | Propiedad |
| :--- | :--- | :--- |
| **Complementarios** | Dos ángulos cuya suma es $90°$ | $\alpha + \beta = 90°$ |
| **Suplementarios** | Dos ángulos cuya suma es $180°$ | $\alpha + \beta = 180°$ |
| **Opuestos por el vértice (OPV)** | Ángulos formados por dos rectas que se cortan | $\alpha = \beta$ (son iguales) |

**Ejemplo rápido:** Si un ángulo mide $65°$, su complemento mide $90° - 65° = 25°$ y su suplemento mide $180° - 65° = 115°$.

---

### 🏛️ 1.3 Ángulos entre Paralelas y una Transversal

Cuando una recta (llamada **transversal** o **secante**) corta a dos rectas **paralelas**, se generan **8 ángulos** con relaciones muy precisas. Este es el tema estrella de la PAES en geometría de posición.

| Relación | Posición | Propiedad |
| :--- | :--- | :--- |
| **Correspondientes** | Mismo lado de la transversal, uno interno y otro externo | Son **iguales** |
| **Alternos internos** | Lados opuestos de la transversal, ambos entre las paralelas | Son **iguales** |
| **Alternos externos** | Lados opuestos de la transversal, ambos fuera de las paralelas | Son **iguales** |
| **Colineales (o co-interiores)** | Mismo lado de la transversal, ambos entre las paralelas | Son **suplementarios** ($\alpha + \beta = 180°$) |

> **Regla de oro:** Si las rectas son paralelas, los ángulos correspondientes y alternos son **iguales**, y los colineales suman $180°$. Si no son paralelas, ninguna de estas propiedades se cumple.

---

### 🛡️ 1.4 Ángulos en la Práctica: Bisectriz y Ángulos Adyacentes

- **Ángulos adyacentes:** Comparten un lado y el vértice, y no se superponen. Sus medidas se suman para dar el ángulo total.
- **Bisectriz:** Es el rayo que divide un ángulo en dos partes **iguales**. Si un ángulo mide $\alpha$, cada mitad mide $\dfrac{\alpha}{2}$.

---

### 🛡️ 1.5 Resumen de Fórmulas Clave

| Fórmula | Descripción |
| :--- | :--- |
| $\alpha + \beta = 90°$ | Ángulos complementarios |
| $\alpha + \beta = 180°$ | Ángulos suplementarios |
| $\alpha = \beta$ | Ángulos opuestos por el vértice |
| $\alpha = \beta$ | Ángulos correspondientes (paralelas) |
| $\alpha = \beta$ | Ángulos alternos internos (paralelas) |
| $\alpha + \beta = 180°$ | Ángulos colineales (paralelas) |

---

> "La geometría es el arte de razonar bien sobre figuras mal hechas."
> — **Henri Poincaré**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G01", expanded=False):
        st.markdown(r"""
### E01: Encontrar el complemento y el suplemento

**Situación:** Un ángulo mide $38°$. Encuentra su complemento y su suplemento.

**La Carpintería:**
1. **Complemento:** $90° - 38° = 52°$.
2. **Suplemento:** $180° - 38° = 142°$.

| Relación | Cálculo | Resultado |
| :--- | :--- | :---: |
| Complemento | $90° - 38°$ | $52°$ |
| Suplemento | $180° - 38°$ | $142°$ |

---

### E02: Ángulos opuestos por el vértice

**Situación:** Dos rectas se cortan formando un ángulo de $72°$. ¿Cuánto miden los otros tres ángulos?

**La Carpintería:**
1. El ángulo **OPV** al dado también mide $72°$.
2. Los otros dos son **suplementarios** al de $72°$: $180° - 72° = 108°$.
3. Los cuatro ángulos son: $72°$, $108°$, $72°$, $108°$.

---

### E03: Ángulos entre paralelas

**Situación:** Dos rectas paralelas son cortadas por una transversal. Uno de los ángulos mide $125°$. Encuentra los 8 ángulos.

**La Carpintería:**
1. El ángulo dado: $125°$.
2. Su **suplementario** (adyacente): $180° - 125° = 55°$.
3. En la primera intersección: $125°$, $55°$, $125°$, $55°$ (por OPV).
4. En la segunda intersección: los **correspondientes** son iguales → mismos valores.
5. Los 8 ángulos: cuatro de $125°$ y cuatro de $55°$.

| Intersección | Ángulos |
| :--- | :--- |
| Primera | $125°$, $55°$, $125°$, $55°$ |
| Segunda | $125°$, $55°$, $125°$, $55°$ |

---

### E04: Encontrar un ángulo usando colineales

**Situación:** Dos paralelas cortadas por una transversal. Un ángulo co-interior mide $3x + 10°$ y el otro mide $2x + 20°$. Encuentra $x$.

**La Carpintería:**
1. Los ángulos colineales son **suplementarios**: $(3x + 10) + (2x + 20) = 180$.
2. $5x + 30 = 180$.
3. $5x = 150$.
4. $x = 30$.
5. **Verificación:** $3(30) + 10 = 100°$ y $2(30) + 20 = 80°$ → $100° + 80° = 180°$ ✅.
""")

    with st.expander("❓ Cuestionario G01: Ángulos y Rectas", expanded=False):
        st.markdown(r"""
**1. Si un ángulo mide $47°$, ¿cuánto mide su suplemento?**

A) $43°$
B) $133°$
C) $137°$
D) $313°$

---

**2. Dos rectas se cortan y forman un ángulo de $110°$. ¿Cuánto mide el ángulo opuesto por el vértice?**

A) $70°$
B) $80°$
C) $110°$
D) $180°$

---

**3. Si dos rectas paralelas son cortadas por una transversal y un ángulo alterno interno mide $64°$, ¿cuánto mide el otro ángulo alterno interno?**

A) $26°$
B) $64°$
C) $116°$
D) $128°$

---

**4. Dos ángulos son complementarios. Si uno de ellos mide $3x°$ y el otro $2x + 15°$, ¿cuál es el valor de $x$?**

A) $15$
B) $18$
C) $25$
D) $30$

---

**5. En un par de ángulos co-interiores (colineales) entre paralelas, si uno mide $75°$, ¿cuánto mide el otro?**

A) $75°$
B) $105°$
C) $115°$
D) $285°$

---

**6. ¿Cuál de los siguientes pares de ángulos son SIEMPRE iguales cuando dos paralelas son cortadas por una transversal?**

A) Colineales
B) Suplementarios
C) Correspondientes
D) Adyacentes

---

**7. La bisectriz de un ángulo de $124°$ forma dos ángulos que miden:**

A) $60°$ y $64°$
B) $62°$ y $62°$
C) $31°$ y $93°$
D) $124°$ y $124°$
""")

    with st.expander("🔑 Pauta Técnica G01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | Suplemento = $180° - 47° = 133°$. |
| **2** | **C** | Los ángulos opuestos por el vértice son iguales: $110°$. |
| **3** | **B** | Los ángulos alternos internos entre paralelas son iguales: $64°$. |
| **4** | **A** | Complementarios suman $90°$: $3x + 2x + 15 = 90 \Rightarrow 5x = 75 \Rightarrow x = 15$. |
| **5** | **B** | Los colineales son suplementarios: $180° - 75° = 105°$. |
| **6** | **C** | Los ángulos correspondientes entre paralelas son siempre iguales. Los colineales suman $180°$, no son iguales. |
| **7** | **B** | La bisectriz divide en dos partes iguales: $124° \div 2 = 62°$ cada una. |
""")
