import streamlit as st


def render_F03():
    st.title("F03: Función Cuadrática — La Parábola que Describe el Mundo")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Por qué la Parábola?

Cuando lanzas una pelota, el camino que dibuja en el aire no es una línea recta: es una **parábola**. Los espejos de los telescopios, las antenas satelitales y hasta el chorro de una fuente de agua siguen esta curva. La **función cuadrática** es la herramienta matemática que la describe:

$$f(x) = ax^2 + bx + c \quad \text{con } a \neq 0$$

Los coeficientes $a$, $b$ y $c$ controlan todo el comportamiento de la parábola. Aprende a leerlos y dominarás una parte importante de la PAES.

---

### 🛡️ 1.1 Los Tres Coeficientes y su Rol

| Coeficiente | Rol | Efecto visual |
| :---: | :--- | :--- |
| $a$ | **Concavidad y amplitud** | $a > 0$: parábola abierta hacia arriba ("sonrisa") · $a < 0$: abierta hacia abajo ("tristeza") |
| $b$ | Junto con $a$, determina la **posición horizontal** del vértice | Desplaza lateralmente la parábola |
| $c$ | **Intercepto con el eje $y$**: $f(0) = c$ | Es el punto donde la parábola corta el eje $y$ |

> **Tip PAES:** Si te preguntan "¿qué pasa si cambiamos el signo de $a$?", la respuesta es: la parábola se voltea (se refleja respecto al eje $x$).

---

### 🛡️ 1.2 El Vértice: El Punto Clave

El **vértice** es el punto más alto (si $a < 0$) o más bajo (si $a > 0$) de la parábola. Sus coordenadas son:

$$x_v = -\frac{b}{2a} \qquad y_v = f(x_v) = f\!\left(-\frac{b}{2a}\right)$$

El vértice también determina:
- El **valor máximo** de $f$ (si $a < 0$) o el **valor mínimo** (si $a > 0$).
- El **eje de simetría**: la recta vertical $x = -\dfrac{b}{2a}$ que divide la parábola en dos mitades espejo.

| Si $a > 0$ | Si $a < 0$ |
| :--- | :--- |
| Parábola abierta hacia arriba | Parábola abierta hacia abajo |
| El vértice es un **mínimo** | El vértice es un **máximo** |
| El recorrido es $[y_v, +\infty)$ | El recorrido es $(-\infty, y_v]$ |

---

### 🏛️ 1.3 El Discriminante $\Delta$ y las Raíces

Las **raíces** (o ceros) de la función cuadrática son los valores de $x$ donde $f(x) = 0$. Se obtienen con la fórmula general:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

El **discriminante** $\Delta = b^2 - 4ac$ te dice cuántas soluciones reales hay:

| Valor de $\Delta$ | Número de raíces reales | Interpretación geométrica |
| :---: | :---: | :--- |
| $\Delta > 0$ | Dos raíces distintas | La parábola corta al eje $x$ en **dos** puntos |
| $\Delta = 0$ | Una raíz doble (repetida) | La parábola **toca** al eje $x$ en un punto (el vértice) |
| $\Delta < 0$ | Ninguna raíz real | La parábola **no toca** el eje $x$ |

> **Tip PAES:** No siempre necesitas calcular las raíces. A veces basta con calcular $\Delta$ para responder la pregunta.

---

### 🛡️ 1.4 Intersecciones con los Ejes

| Eje | Cómo se encuentra | Resultado |
| :--- | :--- | :--- |
| **Eje $y$** | Evaluar $f(0) = c$ | Punto $(0, c)$ |
| **Eje $x$** | Resolver $ax^2 + bx + c = 0$ | Depende de $\Delta$ |

Para graficar una parábola necesitas al menos tres puntos estratégicos: el **vértice**, el **intercepto $y$** y, si existen, las **raíces**.

---

### 🏛️ 1.5 Forma Canónica (Vértice)

La función cuadrática también puede escribirse en **forma de vértice**:

$$f(x) = a(x - h)^2 + k$$

donde $(h, k)$ es el vértice. Esta forma es muy práctica porque puedes leer el vértice directamente:

| Forma estándar | Forma de vértice | Vértice |
| :--- | :--- | :---: |
| $f(x) = 2x^2 - 8x + 6$ | $f(x) = 2(x - 2)^2 - 2$ | $(2, -2)$ |
| $f(x) = -x^2 + 6x - 5$ | $f(x) = -(x - 3)^2 + 4$ | $(3, 4)$ |

---

> "La naturaleza habla en parábolas, y quien entiende la cuadrática, entiende el movimiento del universo."
> — **Galileo Galilei**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería F03", expanded=False):
        st.markdown(r"""
### E01: Encontrar el vértice de una parábola

**Situación:** Dada $f(x) = x^2 - 6x + 8$, encuentra el vértice.

**La Carpintería:**
1. **Identificar coeficientes:** $a = 1$, $b = -6$, $c = 8$.
2. **Coordenada $x$ del vértice:** $x_v = -\dfrac{-6}{2(1)} = \dfrac{6}{2} = 3$.
3. **Coordenada $y$ del vértice:** $y_v = f(3) = 3^2 - 6(3) + 8 = 9 - 18 + 8 = -1$.
4. **Vértice:** $(3, -1)$.
5. **Es un mínimo** porque $a = 1 > 0$.

---

### E02: Usar el discriminante

**Situación:** ¿Cuántas raíces reales tiene $f(x) = 2x^2 + 3x + 5$?

**La Carpintería:**
1. **Coeficientes:** $a = 2$, $b = 3$, $c = 5$.
2. **Discriminante:** $\Delta = 3^2 - 4(2)(5) = 9 - 40 = -31$.
3. **Conclusión:** Como $\Delta < 0$, la función **no tiene raíces reales**. La parábola no corta el eje $x$.

---

### E03: Calcular las raíces de una cuadrática

**Situación:** Encuentra las raíces de $f(x) = x^2 - 5x + 6$.

**La Carpintería:**
1. **Discriminante:** $\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1 > 0$.
2. **Raíces:**
   - $x_1 = \dfrac{5 + \sqrt{1}}{2} = \dfrac{5 + 1}{2} = 3$
   - $x_2 = \dfrac{5 - \sqrt{1}}{2} = \dfrac{5 - 1}{2} = 2$
3. **Verificación:** $f(3) = 9 - 15 + 6 = 0$ ✅ y $f(2) = 4 - 10 + 6 = 0$ ✅

| Dato | Valor |
| :--- | :---: |
| Vértice $x_v$ | $\frac{5}{2} = 2.5$ |
| Vértice $y_v$ | $f(2.5) = 6.25 - 12.5 + 6 = -0.25$ |
| Raíces | $x = 2$ y $x = 3$ |
| Intercepto $y$ | $(0, 6)$ |

---

### E04: De forma estándar a forma de vértice

**Situación:** Escribe $f(x) = x^2 + 4x + 1$ en forma de vértice.

**La Carpintería (completar el cuadrado):**
1. **Agrupar:** $f(x) = (x^2 + 4x) + 1$.
2. **Completar:** La mitad de $4$ es $2$, y $2^2 = 4$. Sumar y restar $4$:
   $f(x) = (x^2 + 4x + 4) - 4 + 1 = (x + 2)^2 - 3$.
3. **Resultado:** $f(x) = (x + 2)^2 - 3$ con vértice $(-2, -3)$.
""")

    with st.expander("❓ Cuestionario F03: Función Cuadrática", expanded=False):
        st.markdown(r"""
**1. El vértice de $f(x) = x^2 - 4x + 7$ es:**

A) $(2, 3)$
B) $(-2, 3)$
C) $(4, 7)$
D) $(2, 7)$

---

**2. Si $a < 0$ en $f(x) = ax^2 + bx + c$, la parábola:**

A) Se abre hacia arriba
B) Se abre hacia abajo
C) Es una línea recta
D) No tiene vértice

---

**3. El discriminante de $f(x) = x^2 - 4x + 4$ es:**

A) $0$
B) $4$
C) $-4$
D) $8$

---

**4. ¿Cuál es el intercepto con el eje $y$ de $f(x) = 3x^2 - 2x + 5$?**

A) $3$
B) $-2$
C) $5$
D) $0$

---

**5. Si $\Delta > 0$, la parábola corta al eje $x$ en:**

A) Ningún punto
B) Un punto
C) Dos puntos
D) Tres puntos

---

**6. El eje de simetría de $f(x) = -2x^2 + 12x - 1$ es:**

A) $x = -3$
B) $x = 3$
C) $x = 6$
D) $x = -6$

---

**7. La función $f(x) = -(x - 1)^2 + 9$ tiene un valor:**

A) Mínimo igual a $9$
B) Máximo igual a $9$
C) Mínimo igual a $1$
D) Máximo igual a $1$
""")

    with st.expander("🔑 Pauta Técnica F03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **A** | $x_v = -\frac{-4}{2(1)} = 2$. $y_v = 2^2 - 4(2) + 7 = 4 - 8 + 7 = 3$. Vértice $(2, 3)$. |
| **2** | **B** | Cuando $a < 0$, la parábola se abre hacia abajo (forma de "U" invertida). |
| **3** | **A** | $\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0$. Raíz doble en $x = 2$. |
| **4** | **C** | El intercepto $y$ es $f(0) = c = 5$. |
| **5** | **C** | $\Delta > 0$ significa dos raíces reales distintas, es decir, la parábola cruza el eje $x$ en dos puntos. |
| **6** | **B** | Eje de simetría: $x = -\frac{12}{2(-2)} = -\frac{12}{-4} = 3$. |
| **7** | **B** | Como $a = -1 < 0$, la parábola se abre hacia abajo. El vértice $(1, 9)$ es un máximo, con valor $9$. |
""")
