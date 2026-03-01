import streamlit as st


def render_F04():
    st.title("F04: Función Exponencial y Logarítmica — El Crecimiento sin Límites")

    st.markdown(r"""
### 🛡️ 1. El Portal: Del Crecimiento Lento al Explosivo

Imagina que depositas $\$100\,000$ en una cuenta que duplica tu dinero cada año. Al cabo de $1$ año tienes $\$200\,000$; al cabo de $2$ años, $\$400\,000$; al cabo de $10$ años, ¡más de $\$100$ millones! Este crecimiento "que se dispara" se llama **crecimiento exponencial**, y la función que lo modela es:

$$f(x) = a^x \quad \text{con } a > 0 \text{ y } a \neq 1$$

Donde $a$ es la **base** y $x$ es el **exponente** (que ahora es variable, no constante como en las potencias).

---

### 🛡️ 1.1 Comportamiento de la Función Exponencial

| Condición | Comportamiento | Ejemplo |
| :---: | :--- | :--- |
| $a > 1$ | **Crecimiento exponencial**: la función crece cada vez más rápido | $f(x) = 2^x$: $1, 2, 4, 8, 16, \ldots$ |
| $0 < a < 1$ | **Decrecimiento exponencial**: la función decrece acercándose a $0$ | $f(x) = \left(\frac{1}{2}\right)^x$: $1, \frac{1}{2}, \frac{1}{4}, \ldots$ |

Propiedades fundamentales del gráfico de $f(x) = a^x$:

| Propiedad | Valor |
| :--- | :--- |
| **Dominio** | $\mathbb{R}$ (todos los reales) |
| **Recorrido** | $(0, +\infty)$ (siempre positiva, nunca vale $0$) |
| **Intercepto $y$** | $(0, 1)$ porque $a^0 = 1$ |
| **Asíntota horizontal** | El eje $x$ ($y = 0$) |

> **Tip PAES:** La función exponencial **nunca** toca el eje $x$. Se acerca infinitamente, pero jamás lo alcanza. Esto se llama **asíntota**.

---

### 🏛️ 1.2 El Logaritmo: La Función Inversa

Si la exponencial responde "¿cuánto vale $a^x$?", el **logaritmo** responde la pregunta inversa: "¿a qué exponente debo elevar $a$ para obtener un resultado dado?"

$$\log_a(b) = c \quad \Longleftrightarrow \quad a^c = b$$

Se lee "logaritmo en base $a$ de $b$". Es simplemente el **exponente** al que hay que elevar la base para obtener el argumento.

| Forma logarítmica | Forma exponencial | Valor |
| :--- | :--- | :---: |
| $\log_2(8)$ | $2^? = 8$ | $3$ |
| $\log_3(81)$ | $3^? = 81$ | $4$ |
| $\log_{10}(1000)$ | $10^? = 1000$ | $3$ |
| $\log_5(1)$ | $5^? = 1$ | $0$ |
| $\log_4\!\left(\frac{1}{4}\right)$ | $4^? = \frac{1}{4}$ | $-1$ |

---

### 🛡️ 1.3 Propiedades de los Logaritmos

Estas propiedades transforman operaciones complicadas en sumas, restas y multiplicaciones:

| Propiedad | Fórmula | Ejemplo |
| :--- | :--- | :--- |
| **Logaritmo de un producto** | $\log_a(M \cdot N) = \log_a(M) + \log_a(N)$ | $\log_2(8 \cdot 4) = \log_2(8) + \log_2(4) = 3 + 2 = 5$ |
| **Logaritmo de un cociente** | $\log_a\!\left(\frac{M}{N}\right) = \log_a(M) - \log_a(N)$ | $\log_3(27/3) = \log_3(27) - \log_3(3) = 3 - 1 = 2$ |
| **Logaritmo de una potencia** | $\log_a(M^n) = n \cdot \log_a(M)$ | $\log_2(4^3) = 3 \cdot \log_2(4) = 3 \cdot 2 = 6$ |
| **Logaritmo de la base** | $\log_a(a) = 1$ | $\log_7(7) = 1$ |
| **Logaritmo de 1** | $\log_a(1) = 0$ | $\log_5(1) = 0$ |

> **Notación especial:** $\log(x)$ sin base suele significar $\log_{10}(x)$ (logaritmo común) y $\ln(x) = \log_e(x)$ (logaritmo natural, base $e \approx 2{,}718$).

---

### 🛡️ 1.4 Ecuaciones Exponenciales Básicas

Para resolver ecuaciones exponenciales, la estrategia principal es **igualar las bases**:

$$2^{x+1} = 8 \quad \Rightarrow \quad 2^{x+1} = 2^3 \quad \Rightarrow \quad x + 1 = 3 \quad \Rightarrow \quad x = 2$$

Cuando no puedes igualar las bases, aplicas logaritmo a ambos lados:

$$3^x = 20 \quad \Rightarrow \quad x = \log_3(20) = \frac{\log(20)}{\log(3)} \approx 2{,}73$$

---

### 🏛️ 1.5 Ecuaciones Logarítmicas Básicas

Para resolver ecuaciones logarítmicas, convierte a forma exponencial:

$$\log_2(x - 1) = 4 \quad \Rightarrow \quad x - 1 = 2^4 = 16 \quad \Rightarrow \quad x = 17$$

> **Cuidado:** Siempre verifica que el argumento del logaritmo sea **positivo**. En el ejemplo: $x - 1 = 16 > 0$ ✅.

| Tipo de ecuación | Estrategia | Ejemplo |
| :--- | :--- | :--- |
| $a^{f(x)} = a^{g(x)}$ | Igualar exponentes: $f(x) = g(x)$ | $5^{2x} = 5^6 \Rightarrow 2x = 6$ |
| $a^x = k$ | Aplicar $\log_a$: $x = \log_a(k)$ | $10^x = 500$ |
| $\log_a(f(x)) = c$ | Convertir: $f(x) = a^c$ | $\log_3(x) = 2 \Rightarrow x = 9$ |

---

> "Los logaritmos, al reducir a unos pocos días el trabajo de muchos meses, duplican la vida de los astrónomos."
> — **Pierre-Simon de Laplace**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería F04", expanded=False):
        st.markdown(r"""
### E01: Evaluar una función exponencial

**Situación:** Si $f(x) = 3 \cdot 2^x$, calcula $f(0)$, $f(3)$ y $f(-2)$.

**La Carpintería:**

| $x$ | Sustitución | Cálculo | $f(x)$ |
| :---: | :--- | :--- | :---: |
| $0$ | $3 \cdot 2^0$ | $3 \cdot 1$ | $3$ |
| $3$ | $3 \cdot 2^3$ | $3 \cdot 8$ | $24$ |
| $-2$ | $3 \cdot 2^{-2}$ | $3 \cdot \frac{1}{4}$ | $\frac{3}{4}$ |

Observa: la función siempre es positiva y crece muy rápido.

---

### E02: Convertir entre forma logarítmica y exponencial

**Situación:** Escribe en forma exponencial: $\log_5(125) = 3$.

**La Carpintería:**
1. **Identificar:** Base = $5$, resultado = $125$, exponente = $3$.
2. **Forma exponencial:** $5^3 = 125$ ✅.

**Inverso:** Escribe $4^{-2} = \frac{1}{16}$ en forma logarítmica.
1. **Base** = $4$, **resultado** = $\frac{1}{16}$, **exponente** = $-2$.
2. **Forma logarítmica:** $\log_4\!\left(\frac{1}{16}\right) = -2$.

---

### E03: Aplicar propiedades de logaritmos

**Situación:** Simplifica $\log_2(32) - \log_2(4) + \log_2(8)$.

**La Carpintería:**
1. **Evaluar cada uno:** $\log_2(32) = 5$, $\log_2(4) = 2$, $\log_2(8) = 3$.
2. **Operar:** $5 - 2 + 3 = 6$.
3. **Verificar con propiedades:** $\log_2\!\left(\frac{32 \cdot 8}{4}\right) = \log_2(64) = 6$ ✅.

---

### E04: Resolver una ecuación exponencial

**Situación:** Resuelve $4^{x-1} = 64$.

**La Carpintería:**
1. **Escribir con la misma base:** $4 = 2^2$ y $64 = 2^6$.
2. **Reescribir:** $(2^2)^{x-1} = 2^6 \Rightarrow 2^{2(x-1)} = 2^6$.
3. **Igualar exponentes:** $2(x - 1) = 6 \Rightarrow 2x - 2 = 6 \Rightarrow x = 4$.
4. **Verificar:** $4^{4-1} = 4^3 = 64$ ✅.
""")

    with st.expander("❓ Cuestionario F04: Función Exponencial y Logarítmica", expanded=False):
        st.markdown(r"""
**1. El valor de $\log_2(64)$ es:**

A) $5$
B) $6$
C) $8$
D) $32$

---

**2. ¿Cuál es el recorrido de $f(x) = 5^x$?**

A) $\mathbb{R}$
B) $(0, +\infty)$
C) $[0, +\infty)$
D) $[1, +\infty)$

---

**3. Si $\log_3(x) = 4$, entonces $x$ es:**

A) $12$
B) $64$
C) $81$
D) $27$

---

**4. $\log(100) + \log(10)$ es igual a:**

A) $\log(1000)$
B) $\log(110)$
C) $1000$
D) $3$

---

**5. Si $2^x = 32$, entonces $x$ es:**

A) $4$
B) $5$
C) $6$
D) $16$

---

**6. La función $f(x) = \left(\frac{1}{3}\right)^x$ es:**

A) Creciente
B) Decreciente
C) Constante
D) No es función

---

**7. $\log_a(a^5)$ es igual a:**

A) $a$
B) $5a$
C) $5$
D) $a^5$
""")

    with st.expander("🔑 Pauta Técnica F04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | $2^6 = 64$, por lo tanto $\log_2(64) = 6$. |
| **2** | **B** | La función exponencial con base $> 1$ toma todos los valores positivos, pero nunca vale $0$ ni negativos. Recorrido: $(0, +\infty)$. |
| **3** | **C** | $\log_3(x) = 4 \Rightarrow x = 3^4 = 81$. |
| **4** | **D** | $\log(100) + \log(10) = 2 + 1 = 3$. También: $\log(100 \cdot 10) = \log(1000) = 3$. Las opciones A y D son equivalentes; la respuesta numérica es $3$. |
| **5** | **B** | $2^5 = 32$, así que $x = 5$. |
| **6** | **B** | Cuando la base está entre $0$ y $1$, la función exponencial es decreciente. |
| **7** | **C** | Por la propiedad $\log_a(a^n) = n$, el resultado es $5$. |
""")
