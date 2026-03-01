import streamlit as st


def render_P03():
    st.title("P03: El Teorema de Pitágoras — La Joya de la Geometría")

    st.markdown(r"""
### 🛡️ 1. El Teorema más Famoso de la Matemática

En todo **triángulo rectángulo**, el cuadrado de la **hipotenusa** (el lado opuesto al ángulo recto) es igual a la suma de los cuadrados de los **catetos**:

$$a^2 + b^2 = c^2$$

donde $c$ es la hipotenusa y $a$, $b$ son los catetos.

> **Tip PAES:** La hipotenusa siempre es el lado **más largo** del triángulo rectángulo y está frente al ángulo de $90°$.

---

### 🛡️ 2. Demostración Visual

Imagina tres cuadrados construidos sobre cada lado del triángulo rectángulo:
- Cuadrado sobre el cateto $a$: área $= a^2$.
- Cuadrado sobre el cateto $b$: área $= b^2$.
- Cuadrado sobre la hipotenusa $c$: área $= c^2$.

El teorema dice que: **el área del cuadrado grande es igual a la suma de las áreas de los dos cuadrados pequeños**.

$$\boxed{a^2 + b^2 = c^2}$$

---

### 🛡️ 3. Aplicaciones Fundamentales

| Problema | Fórmula a usar |
| :--- | :--- |
| Hallar la hipotenusa | $c = \sqrt{a^2 + b^2}$ |
| Hallar un cateto | $a = \sqrt{c^2 - b^2}$ |
| Verificar si es rectángulo | Comprobar si $a^2 + b^2 = c^2$ |

---

### 🛡️ 4. Ternas Pitagóricas

Una **terna pitagórica** es un conjunto de tres números enteros positivos $(a, b, c)$ que satisfacen $a^2 + b^2 = c^2$.

| Terna | Verificación |
| :--- | :--- |
| $(3, 4, 5)$ | $9 + 16 = 25$ ✅ |
| $(5, 12, 13)$ | $25 + 144 = 169$ ✅ |
| $(8, 15, 17)$ | $64 + 225 = 289$ ✅ |
| $(7, 24, 25)$ | $49 + 576 = 625$ ✅ |

> **Tip PAES:** Los múltiplos de una terna también son ternas. Por ejemplo, $(6, 8, 10) = 2 \times (3, 4, 5)$.

---

### 🛡️ 5. Distancia entre Dos Puntos

El teorema de Pitágoras permite calcular la **distancia** entre dos puntos $A(x_1, y_1)$ y $B(x_2, y_2)$ en el plano cartesiano:

$$d(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Esta fórmula es simplemente Pitágoras aplicado al triángulo rectángulo formado por las diferencias de coordenadas.

---

### 🛡️ 6. Recíproco del Teorema de Pitágoras

El **recíproco** dice: si en un triángulo de lados $a$, $b$ y $c$ (con $c$ el mayor) se cumple que $a^2 + b^2 = c^2$, entonces el triángulo **es rectángulo**.

Además:
- Si $a^2 + b^2 > c^2$: el triángulo es **acutángulo** (todos los ángulos agudos).
- Si $a^2 + b^2 < c^2$: el triángulo es **obtusángulo** (tiene un ángulo obtuso).

---

> *"No hay camino real hacia la geometría."*
> — **Euclides**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería P03", expanded=False):
        st.markdown(r"""
### E01: Calcular la hipotenusa

**Situación:** Un triángulo rectángulo tiene catetos de $6$ cm y $8$ cm. ¿Cuánto mide la hipotenusa?

**La Carpintería:**
1. **Fórmula:** $c = \sqrt{a^2 + b^2} = \sqrt{6^2 + 8^2}$.
2. $c = \sqrt{36 + 64} = \sqrt{100} = 10$ cm.
3. **Verificación:** $(6, 8, 10)$ es múltiplo de la terna $(3, 4, 5)$ ✅.

| Dato | Valor |
| :--- | :---: |
| Cateto $a$ | $6$ cm |
| Cateto $b$ | $8$ cm |
| **Hipotenusa** | **$10$ cm** |

---

### E02: Calcular un cateto

**Situación:** Una escalera de $13$ m de largo se apoya contra una pared. El pie de la escalera está a $5$ m de la base de la pared. ¿A qué altura llega la escalera?

**La Carpintería:**
1. La escalera es la hipotenusa: $c = 13$ m.
2. La distancia al muro es un cateto: $b = 5$ m.
3. La altura es el otro cateto: $a = \sqrt{c^2 - b^2} = \sqrt{169 - 25} = \sqrt{144} = 12$ m.

---

### E03: Distancia entre dos puntos

**Situación:** Calcula la distancia entre $A(1, 2)$ y $B(4, 6)$.

**La Carpintería:**
1. $\Delta x = 4 - 1 = 3$ y $\Delta y = 6 - 2 = 4$.
2. $d = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
3. La distancia es **5 unidades**.

| Componente | Valor |
| :--- | :---: |
| $\Delta x$ | $3$ |
| $\Delta y$ | $4$ |
| **Distancia** | **$5$** |

---

### E04: Clasificar un triángulo

**Situación:** ¿Un triángulo con lados $7$, $10$ y $12$ es rectángulo, acutángulo u obtusángulo?

**La Carpintería:**
1. El lado mayor es $c = 12$.
2. Comparamos: $a^2 + b^2 = 7^2 + 10^2 = 49 + 100 = 149$.
3. $c^2 = 12^2 = 144$.
4. Como $149 > 144$, es decir $a^2 + b^2 > c^2$, el triángulo es **acutángulo**.
""")

    with st.expander("❓ Cuestionario P03: Teorema de Pitágoras", expanded=False):
        st.markdown(r"""
**1. Un triángulo rectángulo tiene catetos de $5$ cm y $12$ cm. ¿Cuánto mide la hipotenusa?**

A) $7$ cm
B) $13$ cm
C) $17$ cm
D) $60$ cm

---

**2. La diagonal de un rectángulo de $9$ m × $12$ m mide:**

A) $3$ m
B) $15$ m
C) $21$ m
D) $108$ m

---

**3. ¿Cuál de las siguientes ternas NO es pitagórica?**

A) $(3, 4, 5)$
B) $(5, 12, 13)$
C) $(6, 8, 11)$
D) $(8, 15, 17)$

---

**4. La distancia entre los puntos $A(2, 3)$ y $B(5, 7)$ es:**

A) $3$
B) $4$
C) $5$
D) $7$

---

**5. Un triángulo tiene lados $5$, $7$ y $9$. Este triángulo es:**

A) Rectángulo
B) Acutángulo
C) Obtusángulo
D) No existe

---

**6. Si la hipotenusa de un triángulo rectángulo mide $10$ cm y un cateto mide $6$ cm, ¿cuánto mide el otro cateto?**

A) $4$ cm
B) $6$ cm
C) $8$ cm
D) $16$ cm

---

**7. Un cuadrado tiene diagonal de $10$ cm. ¿Cuánto mide su lado?**

A) $5$ cm
B) $\frac{10}{\sqrt{2}}$ cm
C) $5\sqrt{2}$ cm
D) B y C son equivalentes
""")

    with st.expander("🔑 Pauta Técnica P03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $c = \sqrt{25 + 144} = \sqrt{169} = 13$ cm. |
| **2** | **B** | $d = \sqrt{81 + 144} = \sqrt{225} = 15$ m. |
| **3** | **C** | $6^2 + 8^2 = 100 \neq 121 = 11^2$. No cumple $a^2 + b^2 = c^2$. |
| **4** | **C** | $d = \sqrt{(5-2)^2 + (7-3)^2} = \sqrt{9 + 16} = 5$. |
| **5** | **C** | $5^2 + 7^2 = 74 < 81 = 9^2$. Como $a^2+b^2 < c^2$, es obtusángulo. |
| **6** | **C** | $a = \sqrt{100 - 36} = \sqrt{64} = 8$ cm. |
| **7** | **D** | $\ell = \frac{10}{\sqrt{2}} = \frac{10\sqrt{2}}{2} = 5\sqrt{2}$ cm. Ambas expresiones son equivalentes. |
""")
