import streamlit as st


def render_A02():
    st.title("A02: Productos Notables — Los Atajos del Álgebra")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Para Qué Memorizar Fórmulas?

Imagínate que cada vez que quieres ir de tu casa al colegio tuvieras que recorrer todas las calles una por una. Los **Productos Notables** son los atajos: caminos directos que ya fueron descubiertos y verificados, y que te ahorran una enorme cantidad de trabajo algebraico.

No se trata de memorizar por memorizar. Se trata de **reconocer patrones** que aparecen una y otra vez, tanto en la PAES como en la vida universitaria. Quien domina estos atajos, domina el álgebra.

---

### 🛡️ 2.1 Cuadrado de un Binomio (Suma)

$$\boxed{(a + b)^2 = a^2 + 2ab + b^2}$$

**¿De dónde sale?** Es simplemente multiplicar el binomio por sí mismo:

$$(a + b)(a + b) = a \cdot a + a \cdot b + b \cdot a + b \cdot b = a^2 + 2ab + b^2$$

> **Regla verbal:** "El cuadrado del primero, más el doble producto, más el cuadrado del segundo."

**Ejemplo:** $(x + 3)^2 = x^2 + 2(x)(3) + 3^2 = x^2 + 6x + 9$

---

### 🛡️ 2.2 Cuadrado de un Binomio (Resta)

$$\boxed{(a - b)^2 = a^2 - 2ab + b^2}$$

La única diferencia con el anterior es el signo del **doble producto**, que ahora es negativo.

> **Error clásico PAES:** Creer que $(a - b)^2 = a^2 - b^2$. ¡NO! Eso sería la diferencia de cuadrados, que es otra fórmula completamente distinta.

**Ejemplo:** $(2x - 5)^2 = (2x)^2 - 2(2x)(5) + 5^2 = 4x^2 - 20x + 25$

---

### 🛡️ 2.3 Suma por Diferencia (Diferencia de Cuadrados)

$$\boxed{(a + b)(a - b) = a^2 - b^2}$$

Cuando multiplicas una suma por su diferencia, los términos cruzados ($+ab$ y $-ab$) se cancelan y queda solo la **diferencia de los cuadrados**.

**Ejemplo:** $(3x + 7)(3x - 7) = (3x)^2 - 7^2 = 9x^2 - 49$

| Producto Notable | Fórmula | Resultado del Ejemplo |
| :--- | :--- | :--- |
| $(a + b)^2$ | $a^2 + 2ab + b^2$ | $(x + 3)^2 = x^2 + 6x + 9$ |
| $(a - b)^2$ | $a^2 - 2ab + b^2$ | $(2x - 5)^2 = 4x^2 - 20x + 25$ |
| $(a + b)(a - b)$ | $a^2 - b^2$ | $(3x + 7)(3x - 7) = 9x^2 - 49$ |

---

### 🏛️ 2.4 Cubo de un Binomio

Para la PAES M1, estos son menos frecuentes pero conviene conocerlos:

$$\boxed{(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3}$$

$$\boxed{(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3}$$

> **Regla verbal para $(a + b)^3$:** "Cubo del primero, más tres veces el cuadrado del primero por el segundo, más tres veces el primero por el cuadrado del segundo, más el cubo del segundo."

**Ejemplo:** $(x + 2)^3 = x^3 + 3x^2(2) + 3x(4) + 8 = x^3 + 6x^2 + 12x + 8$

---

### 🛡️ 2.5 Producto de Binomios con Término Común

$$(x + a)(x + b) = x^2 + (a + b)x + ab$$

Este patrón aparece constantemente en factorización de trinomios:

**Ejemplo:** $(x + 5)(x - 3) = x^2 + (5 + (-3))x + (5)(-3) = x^2 + 2x - 15$

---

> "Las matemáticas son el lenguaje con el que Dios escribió el universo."
> — **Galileo Galilei**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería A02", expanded=False):
        st.markdown(r"""
### E01: Cuadrado de binomio (suma)

**Situación:** Desarrollar $(3x + 4y)^2$.

**La Carpintería:**
1. **Identificar:** $a = 3x$, $b = 4y$.
2. **Aplicar fórmula:** $a^2 + 2ab + b^2$.
3. **Calcular cada parte:**
   - $a^2 = (3x)^2 = 9x^2$
   - $2ab = 2(3x)(4y) = 24xy$
   - $b^2 = (4y)^2 = 16y^2$
4. **Resultado:** $9x^2 + 24xy + 16y^2$.

| Componente | Cálculo | Resultado |
| :--- | :--- | :---: |
| $a^2$ | $(3x)^2$ | $9x^2$ |
| $2ab$ | $2(3x)(4y)$ | $24xy$ |
| $b^2$ | $(4y)^2$ | $16y^2$ |

---

### E02: Cuadrado de binomio (resta)

**Situación:** Desarrollar $(5a - 2b)^2$.

**La Carpintería:**
1. **Identificar:** $a = 5a$, $b = 2b$.
2. **Aplicar fórmula:** $a^2 - 2ab + b^2$.
3. **Resultado:** $(5a)^2 - 2(5a)(2b) + (2b)^2 = 25a^2 - 20ab + 4b^2$.

---

### E03: Suma por diferencia

**Situación:** Calcular $(x^2 + 3)(x^2 - 3)$.

**La Carpintería:**
1. **Reconocer patrón:** Es $(a + b)(a - b)$ con $a = x^2$ y $b = 3$.
2. **Aplicar fórmula:** $a^2 - b^2$.
3. **Resultado:** $(x^2)^2 - 3^2 = x^4 - 9$.

---

### E04: Cubo de binomio

**Situación:** Desarrollar $(x - 1)^3$.

**La Carpintería:**
1. **Identificar:** $a = x$, $b = 1$.
2. **Aplicar fórmula:** $a^3 - 3a^2b + 3ab^2 - b^3$.
3. **Calcular:**
   - $x^3 - 3x^2(1) + 3x(1)^2 - 1^3$
   - $x^3 - 3x^2 + 3x - 1$

| Componente | Cálculo | Resultado |
| :--- | :--- | :---: |
| $a^3$ | $x^3$ | $x^3$ |
| $3a^2b$ | $3x^2(1)$ | $3x^2$ |
| $3ab^2$ | $3x(1)$ | $3x$ |
| $b^3$ | $1$ | $1$ |

---

### E05: Producto con término común

**Situación:** Desarrollar $(x + 7)(x - 4)$.

**La Carpintería:**
1. **Identificar:** Término común $x$, con $a = 7$ y $b = -4$.
2. **Aplicar:** $x^2 + (7 + (-4))x + (7)(-4)$.
3. **Resultado:** $x^2 + 3x - 28$.
""")

    with st.expander("❓ Cuestionario A02: Productos Notables", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el desarrollo de $(x + 5)^2$?**

A) $x^2 + 25$
B) $x^2 + 5x + 25$
C) $x^2 + 10x + 25$
D) $2x + 10$

---

**2. El resultado de $(4a - 3b)^2$ es:**

A) $16a^2 - 9b^2$
B) $16a^2 - 24ab + 9b^2$
C) $16a^2 + 24ab + 9b^2$
D) $16a^2 - 12ab + 9b^2$

---

**3. ¿Cuál es el resultado de $(x + 6)(x - 6)$?**

A) $x^2 + 36$
B) $x^2 - 36$
C) $x^2 - 12x + 36$
D) $x^2 + 12x + 36$

---

**4. El desarrollo de $(2x + 1)^3$ es:**

A) $8x^3 + 1$
B) $8x^3 + 12x^2 + 6x + 1$
C) $8x^3 + 6x^2 + 3x + 1$
D) $4x^2 + 4x + 1$

---

**5. El producto $(x + 3)(x - 5)$ es igual a:**

A) $x^2 - 2x - 15$
B) $x^2 + 2x - 15$
C) $x^2 - 8x + 15$
D) $x^2 - 15$

---

**6. Si $(a + b)^2 = 49$ y $a^2 + b^2 = 25$, entonces $2ab$ vale:**

A) $12$
B) $24$
C) $74$
D) $7$

---

**7. ¿Cuál de las siguientes expresiones es un trinomio cuadrado perfecto?**

A) $x^2 + 6x + 8$
B) $x^2 + 6x + 9$
C) $x^2 + 5x + 9$
D) $x^2 - 6x - 9$
""")

    with st.expander("🔑 Pauta Técnica A02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **C** | $(x+5)^2 = x^2 + 2(x)(5) + 25 = x^2 + 10x + 25$. El error clásico es olvidar el doble producto. |
| **2** | **B** | $(4a-3b)^2 = 16a^2 - 2(4a)(3b) + 9b^2 = 16a^2 - 24ab + 9b^2$. El doble producto es negativo. |
| **3** | **B** | Es suma por diferencia: $(x+6)(x-6) = x^2 - 36$. Los términos cruzados se cancelan. |
| **4** | **B** | $(2x+1)^3 = (2x)^3 + 3(2x)^2(1) + 3(2x)(1)^2 + 1^3 = 8x^3 + 12x^2 + 6x + 1$. |
| **5** | **A** | $(x+3)(x-5) = x^2 + (3-5)x + (3)(-5) = x^2 - 2x - 15$. |
| **6** | **B** | $(a+b)^2 = a^2 + 2ab + b^2$, así $49 = 25 + 2ab$, luego $2ab = 24$. |
| **7** | **B** | Para ser TCP: el doble producto debe coincidir. $2 \cdot x \cdot 3 = 6x$ ✅. En los demás no cuadra. |
""")
