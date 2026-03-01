import streamlit as st


def render_A04():
    st.title("A04: Ecuaciones de Primer Grado — Encontrar lo Desconocido")

    st.markdown(r"""
### 🛡️ 1. El Portal: La Balanza de la Justicia

Una ecuación es como una **balanza en equilibrio**: lo que hay a la izquierda pesa lo mismo que lo que hay a la derecha. Si agregas o quitas algo de un lado, debes hacer exactamente lo mismo del otro para que la balanza no se desequilibre.

Resolver una ecuación es encontrar el valor de la incógnita que hace que esa igualdad sea **verdadera**. Ese valor se llama **solución** o **raíz** de la ecuación.

---

### 🛡️ 4.1 Anatomía de una Ecuación

| Concepto | Definición | Ejemplo en $3x + 5 = 14$ |
| :--- | :--- | :--- |
| **Ecuación** | Igualdad con al menos una incógnita | $3x + 5 = 14$ |
| **Incógnita** | La variable cuyo valor buscamos | $x$ |
| **Primer miembro** | Todo lo que está a la izquierda del $=$ | $3x + 5$ |
| **Segundo miembro** | Todo lo que está a la derecha del $=$ | $14$ |
| **Solución (raíz)** | Valor que satisface la igualdad | $x = 3$ |

> **Verificación:** Siempre puedes comprobar reemplazando: $3(3) + 5 = 9 + 5 = 14$ ✅.

---

### 🛡️ 4.2 Ecuaciones Lineales: Método de Resolución

Una ecuación de primer grado tiene la forma $ax + b = c$. El objetivo es **despejar $x$**:

$$3x + 5 = 14$$
$$3x = 14 - 5 \quad \text{(restar 5 a ambos lados)}$$
$$3x = 9$$
$$x = \frac{9}{3} = 3 \quad \text{(dividir por 3 a ambos lados)}$$

**Regla de oro:** Lo que está sumando pasa restando. Lo que está multiplicando pasa dividiendo. Pero técnicamente estás aplicando la **operación inversa** a ambos miembros.

---

### 🛡️ 4.3 Ecuaciones con Paréntesis y Términos Semejantes

Cuando la ecuación tiene paréntesis, primero se aplica la propiedad distributiva:

$$2(x + 3) - 5 = 3(x - 1)$$
$$2x + 6 - 5 = 3x - 3$$
$$2x + 1 = 3x - 3$$
$$1 + 3 = 3x - 2x$$
$$4 = x$$

---

### 🏛️ 4.4 Ecuaciones con Fracciones

La estrategia es **multiplicar toda la ecuación** por el MCM de los denominadores para eliminar las fracciones:

$$\frac{x}{2} + \frac{x}{3} = 5$$

MCM de $2$ y $3$ es $6$. Multiplicamos todo por $6$:

$$6 \cdot \frac{x}{2} + 6 \cdot \frac{x}{3} = 6 \cdot 5$$
$$3x + 2x = 30$$
$$5x = 30$$
$$x = 6$$

---

### 🛡️ 4.5 Ecuaciones Literales (Despeje de Variables)

A veces no resuelves para $x$, sino que despejas una variable en función de las demás. Esto es muy común en fórmulas de física y geometría:

**Ejemplo:** Despejar $h$ de la fórmula del área del triángulo $A = \frac{b \cdot h}{2}$.

$$A = \frac{bh}{2}$$
$$2A = bh$$
$$h = \frac{2A}{b}$$

| Fórmula original | Variable a despejar | Resultado |
| :--- | :---: | :--- |
| $v = d/t$ | $d$ | $d = v \cdot t$ |
| $A = \pi r^2$ | $r$ | $r = \sqrt{A/\pi}$ |
| $F = ma$ | $a$ | $a = F/m$ |
| $P = 2l + 2a$ | $l$ | $l = (P - 2a)/2$ |

---

### 🛡️ 4.6 Problemas de Planteo (La Joya de la PAES)

Estos problemas te dan un enunciado en español y tú debes:
1. **Definir la variable** ($x$ = lo que buscas).
2. **Traducir** el enunciado a una ecuación.
3. **Resolver** la ecuación.
4. **Verificar** que la respuesta tenga sentido.

> **Ejemplo:** "Si al triple de un número le resto 7, obtengo el mismo resultado que al sumarle 11."

Sea $x$ el número: $3x - 7 = x + 11 \Rightarrow 2x = 18 \Rightarrow x = 9$.

**Verificación:** $3(9) - 7 = 20$ y $9 + 11 = 20$ ✅.

---

> "Las ecuaciones son más importantes para mí, porque la política es para el presente, pero una ecuación es algo para la eternidad."
> — **Albert Einstein**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería A04", expanded=False):
        st.markdown(r"""
### E01: Ecuación lineal básica

**Situación:** Resolver $5x - 8 = 2x + 7$.

**La Carpintería:**
1. **Agrupar las $x$ a un lado:** $5x - 2x = 7 + 8$.
2. **Reducir:** $3x = 15$.
3. **Despejar:** $x = 5$.
4. **Verificar:** $5(5) - 8 = 17$ y $2(5) + 7 = 17$ ✅.

| Paso | Operación | Resultado |
| :--- | :--- | :---: |
| Agrupar | $5x - 2x = 7 + 8$ | $3x = 15$ |
| Despejar | $15 \div 3$ | $x = 5$ |
| Verificar | $25 - 8 = 10 + 7$ | $17 = 17$ ✅ |

---

### E02: Ecuación con paréntesis

**Situación:** Resolver $4(x - 2) + 3 = 2(x + 5) - 1$.

**La Carpintería:**
1. **Distribuir:** $4x - 8 + 3 = 2x + 10 - 1$.
2. **Reducir cada lado:** $4x - 5 = 2x + 9$.
3. **Agrupar:** $4x - 2x = 9 + 5$.
4. **Resolver:** $2x = 14 \Rightarrow x = 7$.
5. **Verificar:** $4(5) + 3 = 23$ y $2(12) - 1 = 23$ ✅.

---

### E03: Ecuación con fracciones

**Situación:** Resolver $\dfrac{2x + 1}{3} - \dfrac{x}{4} = 2$.

**La Carpintería:**
1. **MCM de 3 y 4:** $12$.
2. **Multiplicar todo por 12:** $4(2x + 1) - 3x = 24$.
3. **Distribuir:** $8x + 4 - 3x = 24$.
4. **Reducir:** $5x + 4 = 24$.
5. **Resolver:** $5x = 20 \Rightarrow x = 4$.
6. **Verificar:** $\frac{9}{3} - \frac{4}{4} = 3 - 1 = 2$ ✅.

| Paso | Operación | Resultado |
| :--- | :--- | :---: |
| Eliminar fracciones | $\times 12$ | $4(2x+1) - 3x = 24$ |
| Distribuir | $8x + 4 - 3x$ | $5x + 4 = 24$ |
| Resolver | $5x = 20$ | $x = 4$ |

---

### E04: Problema de planteo

**Situación:** La edad de María es el doble de la de Juan. Dentro de 5 años, la suma de sus edades será 40. ¿Cuántos años tiene cada uno?

**La Carpintería:**
1. **Variable:** Sea $x$ = edad de Juan. Entonces María tiene $2x$ años.
2. **Dentro de 5 años:** Juan tendrá $x + 5$ y María tendrá $2x + 5$.
3. **Ecuación:** $(x + 5) + (2x + 5) = 40$.
4. **Resolver:** $3x + 10 = 40 \Rightarrow 3x = 30 \Rightarrow x = 10$.
5. **Respuesta:** Juan tiene $10$ años y María tiene $20$ años.
6. **Verificar:** Dentro de 5 años: $15 + 25 = 40$ ✅.
""")

    with st.expander("❓ Cuestionario A04: Ecuaciones de Primer Grado", expanded=False):
        st.markdown(r"""
**1. La solución de la ecuación $4x + 3 = 19$ es:**

A) $x = 4$
B) $x = 3$
C) $x = 5,5$
D) $x = 16$

---

**2. Al resolver $3(x - 2) = 2(x + 1)$, se obtiene:**

A) $x = 8$
B) $x = 4$
C) $x = -4$
D) $x = 1$

---

**3. La ecuación $\dfrac{x}{3} + \dfrac{x}{6} = 5$ tiene como solución:**

A) $x = 10$
B) $x = 15$
C) $x = 6$
D) $x = 30$

---

**4. Si al despejar $t$ de la fórmula $d = v \cdot t + d_0$, se obtiene:**

A) $t = d - d_0 - v$
B) $t = \dfrac{d - d_0}{v}$
C) $t = \dfrac{d + d_0}{v}$
D) $t = v(d - d_0)$

---

**5. "Tres números consecutivos suman 42." ¿Cuál es el mayor de ellos?**

A) $13$
B) $14$
C) $15$
D) $16$

---

**6. ¿Cuál es el conjunto solución de $2x + 5 = 2x + 5$?**

A) $x = 0$
B) $x = 5$
C) No tiene solución
D) Todo número real es solución

---

**7. La ecuación $\dfrac{3x - 1}{2} = \dfrac{x + 5}{4}$ tiene como solución:**

A) $x = \dfrac{7}{5}$
B) $x = \dfrac{12}{5}$
C) $x = \dfrac{7}{10}$
D) $x = 3$
""")

    with st.expander("🔑 Pauta Técnica A04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **A** | $4x = 19 - 3 = 16$, luego $x = 16/4 = 4$. |
| **2** | **A** | $3x - 6 = 2x + 2 \Rightarrow x = 8$. Verificar: $3(6) = 18$ y $2(9) = 18$ ✅. |
| **3** | **A** | MCM = 6: $2x + x = 30 \Rightarrow 3x = 30 \Rightarrow x = 10$. |
| **4** | **B** | $d - d_0 = vt \Rightarrow t = (d - d_0)/v$. Se resta $d_0$ y se divide por $v$. |
| **5** | **C** | Sea $x$, $x+1$, $x+2$: $3x + 3 = 42 \Rightarrow x = 13$. El mayor es $13 + 2 = 15$. |
| **6** | **D** | La ecuación es una identidad: se cumple para todo valor de $x$. Es una ecuación con infinitas soluciones. |
| **7** | **A** | Multiplicar por 4: $2(3x-1) = x+5 \Rightarrow 6x - 2 = x + 5 \Rightarrow 5x = 7 \Rightarrow x = 7/5$. |
""")
