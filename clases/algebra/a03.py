import streamlit as st


def render_A03():
    st.title("A03: Factorización — Desarmar para Entender")

    st.markdown(r"""
### 🛡️ 1. El Portal: El Arte de Desarmar

Si los Productos Notables eran atajos para **multiplicar**, la Factorización es el camino inverso: **desarmar** una expresión en sus piezas más simples. Es como desarmar un motor para entender cómo funciona cada pieza.

Factorizar es escribir una expresión como un **producto de factores** más sencillos. Esta habilidad es fundamental para simplificar fracciones algebraicas, resolver ecuaciones cuadráticas y trabajar con funciones.

---

### 🛡️ 3.1 Factor Común

Es el método más básico: buscar qué tienen **en común** todos los términos y "sacarlo" afuera con un paréntesis.

$$6x^3 + 9x^2 - 3x = 3x(2x^2 + 3x - 1)$$

**Proceso:**
1. Buscar el **MCD** de los coeficientes: $\text{MCD}(6, 9, 3) = 3$.
2. Buscar la **menor potencia** de cada variable común: $x^1$.
3. Dividir cada término por el factor común.

---

### 🛡️ 3.2 Factor Común por Agrupación

Cuando la expresión tiene **4 términos** y no hay factor común global, se agrupan de a pares:

$$ax + ay + bx + by = a(x + y) + b(x + y) = (x + y)(a + b)$$

**La clave:** Después de agrupar, debe aparecer un **binomio común** que se pueda extraer.

---

### 🛡️ 3.3 Diferencia de Cuadrados

Es el inverso de la suma por diferencia:

$$\boxed{a^2 - b^2 = (a + b)(a - b)}$$

**Ejemplo:** $25x^2 - 49 = (5x)^2 - 7^2 = (5x + 7)(5x - 7)$

> **Tip PAES:** Para usar esta fórmula, ambos términos deben ser **cuadrados perfectos** y estar separados por una **resta**.

---

### 🏛️ 3.4 Trinomio Cuadrado Perfecto (TCP)

Es el inverso del cuadrado de un binomio:

$$\boxed{a^2 + 2ab + b^2 = (a + b)^2}$$
$$\boxed{a^2 - 2ab + b^2 = (a - b)^2}$$

**¿Cómo verificar si un trinomio es TCP?**
1. El primer y tercer término deben ser **cuadrados perfectos**.
2. El término del medio debe ser $\pm 2 \cdot \sqrt{\text{primero}} \cdot \sqrt{\text{tercero}}$.

**Ejemplo:** $x^2 - 10x + 25$
- $\sqrt{x^2} = x$ ✅, $\sqrt{25} = 5$ ✅
- $2(x)(5) = 10x$ ✅ (coincide con el término del medio)
- **Resultado:** $(x - 5)^2$

---

### 🛡️ 3.5 Trinomio de la Forma $x^2 + bx + c$

Buscamos dos números $p$ y $q$ tales que:
- $p + q = b$ (suman el coeficiente del término lineal)
- $p \cdot q = c$ (su producto es el término independiente)

$$x^2 + bx + c = (x + p)(x + q)$$

**Ejemplo:** $x^2 + 7x + 12$
- Buscamos dos números que sumen $7$ y multipliquen $12$.
- $3 + 4 = 7$ ✅ y $3 \times 4 = 12$ ✅
- **Resultado:** $(x + 3)(x + 4)$

| Trinomio | $p + q$ | $p \cdot q$ | $p$ | $q$ | Factorización |
| :--- | :---: | :---: | :---: | :---: | :--- |
| $x^2 + 7x + 12$ | $7$ | $12$ | $3$ | $4$ | $(x+3)(x+4)$ |
| $x^2 - 5x + 6$ | $-5$ | $6$ | $-2$ | $-3$ | $(x-2)(x-3)$ |
| $x^2 + x - 12$ | $1$ | $-12$ | $4$ | $-3$ | $(x+4)(x-3)$ |
| $x^2 - x - 6$ | $-1$ | $-6$ | $-3$ | $2$ | $(x-3)(x+2)$ |

---

### 🛡️ 3.6 Completar el Cuadrado

Es una técnica para transformar una expresión en un TCP más una constante:

$$x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$$

**Ejemplo:** $x^2 + 6x + 2$
1. Tomar la mitad del coeficiente de $x$: $6/2 = 3$.
2. Sumar y restar su cuadrado: $x^2 + 6x + 9 - 9 + 2$.
3. Agrupar: $(x + 3)^2 - 7$.

> Esta técnica es esencial para deducir la fórmula general de la ecuación cuadrática y para encontrar el vértice de una parábola.

---

> "La factorización es el microscopio del álgebra: te muestra la estructura interna de las expresiones."
> — **Leonhard Euler**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería A03", expanded=False):
        st.markdown(r"""
### E01: Factor común simple

**Situación:** Factorizar $12x^4 - 8x^3 + 4x^2$.

**La Carpintería:**
1. **MCD de coeficientes:** $\text{MCD}(12, 8, 4) = 4$.
2. **Menor potencia de $x$:** $x^2$.
3. **Factor común:** $4x^2$.
4. **Dividir cada término:** $12x^4 \div 4x^2 = 3x^2$; $8x^3 \div 4x^2 = 2x$; $4x^2 \div 4x^2 = 1$.
5. **Resultado:** $4x^2(3x^2 - 2x + 1)$.

| Término | $\div 4x^2$ | Resultado |
| :--- | :---: | :---: |
| $12x^4$ | $12x^4 / 4x^2$ | $3x^2$ |
| $-8x^3$ | $-8x^3 / 4x^2$ | $-2x$ |
| $4x^2$ | $4x^2 / 4x^2$ | $1$ |

---

### E02: Diferencia de cuadrados

**Situación:** Factorizar $81a^2 - 16b^2$.

**La Carpintería:**
1. **¿Son cuadrados perfectos?** $81a^2 = (9a)^2$ ✅ y $16b^2 = (4b)^2$ ✅.
2. **¿Es una resta?** Sí ✅.
3. **Aplicar fórmula:** $(9a + 4b)(9a - 4b)$.

---

### E03: Trinomio de la forma $x^2 + bx + c$

**Situación:** Factorizar $x^2 - 3x - 18$.

**La Carpintería:**
1. **Identificar:** $b = -3$, $c = -18$.
2. **Buscar $p$ y $q$:** Deben sumar $-3$ y multiplicar $-18$.
3. **Probar:** $-6 + 3 = -3$ ✅ y $(-6)(3) = -18$ ✅.
4. **Resultado:** $(x - 6)(x + 3)$.

| Intento | Suma | Producto | ¿Funciona? |
| :--- | :---: | :---: | :---: |
| $-9$ y $2$ | $-7$ | $-18$ | ❌ |
| $-6$ y $3$ | $-3$ | $-18$ | ✅ |

---

### E04: Completar el cuadrado

**Situación:** Escribir $x^2 - 8x + 10$ en la forma $(x - h)^2 + k$.

**La Carpintería:**
1. **Mitad del coeficiente de $x$:** $-8/2 = -4$.
2. **Su cuadrado:** $(-4)^2 = 16$.
3. **Sumar y restar $16$:** $x^2 - 8x + 16 - 16 + 10$.
4. **Agrupar:** $(x - 4)^2 - 6$.
5. **Verificación:** $(x-4)^2 - 6 = x^2 - 8x + 16 - 6 = x^2 - 8x + 10$ ✅.
""")

    with st.expander("❓ Cuestionario A03: Factorización", expanded=False):
        st.markdown(r"""
**1. Al factorizar $15x^3 - 10x^2 + 5x$, el factor común es:**

A) $5$
B) $5x$
C) $5x^2$
D) $15x$

---

**2. La factorización de $x^2 - 64$ es:**

A) $(x - 8)^2$
B) $(x + 8)^2$
C) $(x + 8)(x - 8)$
D) $(x - 32)(x + 2)$

---

**3. ¿Cuál es la factorización de $x^2 + 10x + 25$?**

A) $(x + 5)^2$
B) $(x - 5)^2$
C) $(x + 25)(x + 1)$
D) $(x + 5)(x - 5)$

---

**4. Al factorizar $x^2 + 5x + 6$, se obtiene:**

A) $(x + 1)(x + 6)$
B) $(x + 2)(x + 3)$
C) $(x - 2)(x - 3)$
D) $(x + 6)(x - 1)$

---

**5. La factorización de $4x^2 - 12x + 9$ es:**

A) $(2x - 3)^2$
B) $(2x + 3)^2$
C) $(4x - 3)(x - 3)$
D) $(2x - 9)(2x - 1)$

---

**6. Al completar el cuadrado en $x^2 + 4x - 5$, se obtiene:**

A) $(x + 2)^2 - 9$
B) $(x + 2)^2 + 9$
C) $(x + 4)^2 - 5$
D) $(x - 2)^2 - 9$

---

**7. La factorización de $x^2 - x - 20$ es:**

A) $(x - 5)(x + 4)$
B) $(x + 5)(x - 4)$
C) $(x - 10)(x + 2)$
D) $(x - 20)(x + 1)$
""")

    with st.expander("🔑 Pauta Técnica A03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | $\text{MCD}(15, 10, 5) = 5$ y la menor potencia de $x$ es $x^1$. Factor común: $5x$. |
| **2** | **C** | Diferencia de cuadrados: $x^2 - 8^2 = (x+8)(x-8)$. No es un TCP porque no tiene término lineal. |
| **3** | **A** | TCP: $\sqrt{x^2}=x$, $\sqrt{25}=5$, $2(x)(5)=10x$ ✅. Resultado: $(x+5)^2$. |
| **4** | **B** | Buscamos $p+q=5$ y $pq=6$. Los números $2$ y $3$ cumplen: $2+3=5$, $2 \cdot 3=6$. |
| **5** | **A** | TCP: $(2x)^2=4x^2$, $3^2=9$, $2(2x)(3)=12x$ ✅. El signo negativo da $(2x-3)^2$. |
| **6** | **A** | Mitad de $4$ es $2$; $2^2=4$. $x^2+4x+4-4-5=(x+2)^2-9$. |
| **7** | **A** | Buscamos $p+q=-1$ y $pq=-20$. Los números $-5$ y $4$: $-5+4=-1$, $(-5)(4)=-20$. |
""")
