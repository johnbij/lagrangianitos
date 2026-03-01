import streamlit as st


def render_A05():
    st.title("A05: Inecuaciones y Sistemas de Ecuaciones Lineales — Rangos y Cruces")

    st.markdown(r"""
### 🛡️ 1. El Portal: Más Allá de la Igualdad

No todo en la vida es exacto. A veces necesitas saber que tu nota debe ser **mayor que** 4,0 para aprobar, o que tu presupuesto debe ser **menor o igual a** cierta cantidad. Las **inecuaciones** manejan esa realidad: trabajan con desigualdades en vez de igualdades.

Y cuando tienes **dos condiciones** que deben cumplirse al mismo tiempo (como "tengo $x$ billetes de mil y $y$ monedas de quinientos y el total es..."), entras al mundo de los **sistemas de ecuaciones**.

---

### 🛡️ 5.1 Inecuaciones Lineales

Una inecuación es una desigualdad que contiene una incógnita. Se resuelve igual que una ecuación, con una **regla de oro crucial**:

$$\boxed{\text{Al multiplicar o dividir por un número NEGATIVO, se INVIERTE el sentido de la desigualdad.}}$$

**Ejemplo:** Resolver $-3x + 6 > 0$.

$$-3x > -6$$
$$x < 2 \quad \text{(se invierte el } > \text{ a } < \text{ al dividir por } -3\text{)}$$

**Solución:** $x \in (-\infty, 2)$ o equivalentemente $\{x \in \mathbb{R} : x < 2\}$.

| Símbolo | Significado | Intervalo | Representación |
| :---: | :--- | :--- | :--- |
| $<$ | Menor que (estricto) | $(a, b)$ | Círculo abierto ○ |
| $\leq$ | Menor o igual que | $[a, b]$ | Círculo cerrado ● |
| $>$ | Mayor que (estricto) | $(a, b)$ | Círculo abierto ○ |
| $\geq$ | Mayor o igual que | $[a, b]$ | Círculo cerrado ● |

---

### 🛡️ 5.2 Inecuaciones con Paréntesis y Fracciones

**Ejemplo:** Resolver $\dfrac{2x - 1}{3} \leq \dfrac{x + 2}{2}$.

1. **MCM de 3 y 2:** $6$.
2. **Multiplicar por 6:** $2(2x - 1) \leq 3(x + 2)$.
3. **Distribuir:** $4x - 2 \leq 3x + 6$.
4. **Agrupar:** $4x - 3x \leq 6 + 2$.
5. **Resultado:** $x \leq 8$.
6. **Solución:** $x \in (-\infty, 8]$.

> **Tip PAES:** Como multiplicamos por $6$ (positivo), el sentido de la desigualdad **no cambia**.

---

### 🏛️ 5.3 Sistemas de Ecuaciones Lineales 2×2

Un sistema de dos ecuaciones con dos incógnitas busca el par $(x, y)$ que satisface **ambas** ecuaciones simultáneamente.

$$\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$$

Geométricamente, cada ecuación es una **recta** en el plano. La solución es el **punto de intersección** de ambas rectas.

| Caso | Geométricamente | Algebraicamente | Soluciones |
| :--- | :--- | :--- | :---: |
| **Compatible determinado** | Las rectas se cortan | Solución única | $1$ |
| **Compatible indeterminado** | Las rectas coinciden | Infinitas soluciones | $\infty$ |
| **Incompatible** | Las rectas son paralelas | Sin solución | $0$ |

---

### 🛡️ 5.4 Método de Sustitución

**Idea:** Despejar una variable de una ecuación y reemplazarla en la otra.

$$\begin{cases} x + 2y = 8 \quad \text{...(1)} \\ 3x - y = 1 \quad \text{...(2)} \end{cases}$$

1. **De (1):** $x = 8 - 2y$.
2. **Sustituir en (2):** $3(8 - 2y) - y = 1$.
3. **Resolver:** $24 - 6y - y = 1 \Rightarrow -7y = -23 \Rightarrow y = \dfrac{23}{7}$.
4. **Encontrar $x$:** $x = 8 - 2 \cdot \dfrac{23}{7} = \dfrac{56 - 46}{7} = \dfrac{10}{7}$.

---

### 🛡️ 5.5 Método de Reducción (Eliminación)

**Idea:** Multiplicar las ecuaciones por constantes para que al sumarlas se **elimine** una variable.

$$\begin{cases} 2x + 3y = 12 \quad \text{...(1)} \\ 4x - 3y = 6 \quad \text{...(2)} \end{cases}$$

1. **Observar:** Los coeficientes de $y$ ya son opuestos ($+3y$ y $-3y$).
2. **Sumar (1) + (2):** $6x = 18 \Rightarrow x = 3$.
3. **Reemplazar en (1):** $6 + 3y = 12 \Rightarrow y = 2$.
4. **Solución:** $(3, 2)$.

---

### 🛡️ 5.6 Método de Igualación

**Idea:** Despejar la **misma variable** de ambas ecuaciones e igualar las expresiones obtenidas.

$$\begin{cases} y = 2x + 1 \quad \text{...(1)} \\ y = -x + 7 \quad \text{...(2)} \end{cases}$$

1. **Igualar:** $2x + 1 = -x + 7$.
2. **Resolver:** $3x = 6 \Rightarrow x = 2$.
3. **Encontrar $y$:** $y = 2(2) + 1 = 5$.
4. **Solución:** $(2, 5)$.

---

> "La esencia de las matemáticas reside en su libertad."
> — **Georg Cantor**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería A05", expanded=False):
        st.markdown(r"""
### E01: Inecuación con cambio de signo

**Situación:** Resolver $-2x + 4 \geq 10$.

**La Carpintería:**
1. **Restar 4:** $-2x \geq 6$.
2. **Dividir por $-2$** (¡invertir!): $x \leq -3$.
3. **Solución:** $x \in (-\infty, -3]$.

| Paso | Operación | Desigualdad |
| :--- | :--- | :--- |
| Restar 4 | $-2x \geq 10 - 4$ | $-2x \geq 6$ |
| Dividir por $-2$ | Se invierte $\geq$ a $\leq$ | $x \leq -3$ |

> **Clave:** Al dividir por $-2$ (negativo), el $\geq$ se convierte en $\leq$.

---

### E02: Sistema por sustitución

**Situación:** Resolver $\begin{cases} x + y = 10 \\ 2x - y = 5 \end{cases}$

**La Carpintería:**
1. **De la primera:** $y = 10 - x$.
2. **Sustituir en la segunda:** $2x - (10 - x) = 5$.
3. **Resolver:** $2x - 10 + x = 5 \Rightarrow 3x = 15 \Rightarrow x = 5$.
4. **Encontrar $y$:** $y = 10 - 5 = 5$.
5. **Solución:** $(5, 5)$.
6. **Verificar:** $5 + 5 = 10$ ✅ y $10 - 5 = 5$ ✅.

---

### E03: Sistema por reducción

**Situación:** Resolver $\begin{cases} 3x + 2y = 16 \\ 2x + 2y = 12 \end{cases}$

**La Carpintería:**
1. **Restar (2) de (1):** $(3x + 2y) - (2x + 2y) = 16 - 12$.
2. **Simplificar:** $x = 4$.
3. **Reemplazar en (2):** $8 + 2y = 12 \Rightarrow 2y = 4 \Rightarrow y = 2$.
4. **Solución:** $(4, 2)$.
5. **Verificar:** $12 + 4 = 16$ ✅ y $8 + 4 = 12$ ✅.

| Ecuación | $x = 4$ | $y = 2$ | Verificación |
| :--- | :---: | :---: | :--- |
| $3(4) + 2(2) = 16$ | $12$ | $4$ | $16 = 16$ ✅ |
| $2(4) + 2(2) = 12$ | $8$ | $4$ | $12 = 12$ ✅ |

---

### E04: Problema de planteo con sistema

**Situación:** En una granja hay gallinas y conejos. En total hay 20 animales y 56 patas. ¿Cuántas gallinas y cuántos conejos hay?

**La Carpintería:**
1. **Variables:** $g$ = gallinas, $c$ = conejos.
2. **Ecuación de animales:** $g + c = 20$.
3. **Ecuación de patas:** $2g + 4c = 56$.
4. **De (1):** $g = 20 - c$.
5. **Sustituir en (2):** $2(20 - c) + 4c = 56 \Rightarrow 40 - 2c + 4c = 56 \Rightarrow 2c = 16 \Rightarrow c = 8$.
6. **Encontrar $g$:** $g = 20 - 8 = 12$.
7. **Respuesta:** Hay $12$ gallinas y $8$ conejos.
8. **Verificar:** $12 + 8 = 20$ ✅ y $24 + 32 = 56$ ✅.
""")

    with st.expander("❓ Cuestionario A05: Inecuaciones y Sistemas", expanded=False):
        st.markdown(r"""
**1. La solución de la inecuación $-4x > 12$ es:**

A) $x > -3$
B) $x < -3$
C) $x > 3$
D) $x < 3$

---

**2. El conjunto solución de $2x - 5 \leq 3$ es:**

A) $x \leq 4$
B) $x \geq 4$
C) $x \leq -1$
D) $x \leq 1$

---

**3. Si $\begin{cases} x + y = 7 \\ x - y = 3 \end{cases}$, entonces $x$ vale:**

A) $2$
B) $5$
C) $3$
D) $10$

---

**4. ¿Cuál es la solución del sistema $\begin{cases} y = 3x \\ 2x + y = 10 \end{cases}$?**

A) $(2, 6)$
B) $(3, 9)$
C) $(1, 3)$
D) $(5, 15)$

---

**5. Si un sistema de dos ecuaciones lineales no tiene solución, geométricamente las rectas son:**

A) Coincidentes
B) Perpendiculares
C) Paralelas
D) Secantes

---

**6. Al resolver $\dfrac{x+1}{2} > 3$, se obtiene:**

A) $x > 5$
B) $x > 7$
C) $x > 2,5$
D) $x > 4$

---

**7. El sistema $\begin{cases} 2x + 3y = 1 \\ 4x + 6y = 2 \end{cases}$ es:**

A) Incompatible (sin solución)
B) Compatible determinado (una solución)
C) Compatible indeterminado (infinitas soluciones)
D) Ninguna de las anteriores
""")

    with st.expander("🔑 Pauta Técnica A05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | $-4x > 12 \Rightarrow x < -3$. Al dividir por $-4$, se invierte el signo de $>$ a $<$. |
| **2** | **A** | $2x \leq 8 \Rightarrow x \leq 4$. Dividimos por $2$ (positivo), el signo no cambia. |
| **3** | **B** | Sumando ambas: $2x = 10 \Rightarrow x = 5$. Método de reducción directo. |
| **4** | **A** | Sustituir $y = 3x$ en la segunda: $2x + 3x = 10 \Rightarrow x = 2$, $y = 6$. |
| **5** | **C** | Rectas paralelas tienen la misma pendiente pero distinto intercepto, por lo que nunca se cruzan. |
| **6** | **A** | $x + 1 > 6 \Rightarrow x > 5$. Multiplicar por $2$ (positivo) no cambia el sentido. |
| **7** | **C** | La segunda ecuación es el doble de la primera ($\times 2$). Son la misma recta, infinitas soluciones. |
""")
