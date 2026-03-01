import streamlit as st


def render_PB05():
    st.title("PB05: Variable Aleatoria y Distribuciones de Probabilidad — Cuando el Azar Tiene Estructura")

    st.markdown(r"""
### 🛡️ 1. El Portal: Asignar Números al Azar

Hasta ahora, hablamos de eventos como "sacar cara" o "obtener un número par". Pero a menudo queremos trabajar con **números**: ¿cuántas caras salen al lanzar $3$ monedas? ¿Cuánto gano en un juego de azar? Una **variable aleatoria** es una función que asigna un valor numérico a cada resultado del espacio muestral.

---

### 🛡️ 2. Variable Aleatoria Discreta

Una variable aleatoria $X$ es **discreta** cuando toma un número **finito** o **contable** de valores.

**Ejemplo:** $X$ = "número de caras al lanzar $3$ monedas". Los valores posibles son $X \in \{0, 1, 2, 3\}$.

---

### 🛡️ 3. Tabla de Distribución de Probabilidad

Resume todos los valores posibles de $X$ y su probabilidad:

| $x_i$ | $P(X = x_i)$ |
| :---: | :---: |
| $0$ | $\frac{1}{8}$ |
| $1$ | $\frac{3}{8}$ |
| $2$ | $\frac{3}{8}$ |
| $3$ | $\frac{1}{8}$ |
| **Total** | $1$ |

**Propiedades:**
1. $P(X = x_i) \geq 0$ para todo $i$.
2. $\sum P(X = x_i) = 1$.

---

### 🛡️ 4. Esperanza Matemática ($E(X)$)

La esperanza (o valor esperado) es el **promedio ponderado** de los valores de $X$:

$$E(X) = \sum_{i} x_i \cdot P(X = x_i)$$

**Ejemplo (3 monedas):**

$$E(X) = 0 \cdot \frac{1}{8} + 1 \cdot \frac{3}{8} + 2 \cdot \frac{3}{8} + 3 \cdot \frac{1}{8} = \frac{0 + 3 + 6 + 3}{8} = \frac{12}{8} = 1{,}5$$

**Interpretación:** Si repitieras el experimento muchas veces, en promedio obtendrías $1{,}5$ caras por lanzamiento.

> **Tip PAES:** La esperanza **no** tiene que ser un valor entero, aunque $X$ solo tome valores enteros.

---

### 🛡️ 5. Varianza y Desviación Estándar de $X$

$$Var(X) = E(X^2) - [E(X)]^2$$

donde $E(X^2) = \sum x_i^2 \cdot P(X = x_i)$.

$$\sigma_X = \sqrt{Var(X)}$$

**Ejemplo (continuando con las 3 monedas):**

$E(X^2) = 0^2 \cdot \frac{1}{8} + 1^2 \cdot \frac{3}{8} + 2^2 \cdot \frac{3}{8} + 3^2 \cdot \frac{1}{8} = \frac{0+3+12+9}{8} = 3$.

$Var(X) = 3 - (1{,}5)^2 = 3 - 2{,}25 = 0{,}75$.

$\sigma_X = \sqrt{0{,}75} \approx 0{,}87$.

---

### 🛡️ 6. Distribución Binomial (Intuición)

Cuando un experimento tiene solo **dos resultados** (éxito/fracaso), se repite $n$ veces de forma **independiente** y la probabilidad de éxito es $p$ constante, se aplica la distribución binomial:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

| Parámetro | Significado |
| :--- | :--- |
| $n$ | Número de repeticiones |
| $p$ | Probabilidad de éxito en cada repetición |
| $k$ | Número de éxitos deseados |

**Esperanza:** $E(X) = n \cdot p$.

**Varianza:** $Var(X) = n \cdot p \cdot (1-p)$.

**Ejemplo:** Se lanza una moneda $10$ veces. ¿Cuál es la probabilidad de obtener exactamente $3$ caras?

$$P(X = 3) = \binom{10}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^7 = 120 \cdot \frac{1}{1024} = \frac{120}{1024} \approx 0{,}117$$

---

### 🛡️ 7. Ley de los Grandes Números

A medida que el número de repeticiones de un experimento aleatorio **aumenta**, el promedio de los resultados observados se **acerca** al valor esperado $E(X)$.

**Ejemplo:** Si lanzas un dado $6$ veces, probablemente no obtendrás exactamente un promedio de $3{,}5$. Pero si lo lanzas $6.000$ veces, el promedio se acercará mucho a $3{,}5$.

> **Tip PAES:** La ley de los grandes números NO dice que los resultados se "compensan" a corto plazo. No existe la "deuda" del azar.

---

> *"La probabilidad es paciencia. A largo plazo, las frecuencias relativas convergen a las probabilidades teóricas."*
> — **Jakob Bernoulli**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería PB05", expanded=False):
        st.markdown(r"""
### E01: Construir tabla de distribución y calcular $E(X)$

**Situación:** Un juego consiste en lanzar un dado. Si sale $6$, ganas $\$5.000$. Si sale par (distinto de $6$), ganas $\$1.000$. Si sale impar, pierdes $\$2.000$. Sea $X$ la ganancia.

**La Carpintería:**
1. Identificar valores de $X$ y probabilidades:

| Resultado | Valor de $X$ | $P(X)$ |
| :--- | :---: | :---: |
| Sale $6$ | $5.000$ | $\frac{1}{6}$ |
| Sale $2$ o $4$ | $1.000$ | $\frac{2}{6} = \frac{1}{3}$ |
| Sale $1, 3$ o $5$ | $-2.000$ | $\frac{3}{6} = \frac{1}{2}$ |

2. $E(X) = 5000 \cdot \frac{1}{6} + 1000 \cdot \frac{1}{3} + (-2000) \cdot \frac{1}{2}$
   $= \frac{5000}{6} + \frac{1000}{3} - \frac{2000}{2}$
   $= 833{,}3 + 333{,}3 - 1000 = 166{,}7$.
3. **Interpretación:** En promedio, se ganan $\$166{,}7$ por juego → conviene jugar.

---

### E02: Distribución binomial

**Situación:** Un examen de $5$ preguntas de alternativas (cada una con $4$ opciones) se responde al azar. ¿Probabilidad de acertar exactamente $2$?

**La Carpintería:**
1. $n = 5$ intentos, $p = \frac{1}{4}$ (probabilidad de acertar), $k = 2$.
2. $P(X = 2) = \binom{5}{2} \left(\frac{1}{4}\right)^2 \left(\frac{3}{4}\right)^3$.
3. $\binom{5}{2} = 10$.
4. $P = 10 \cdot \frac{1}{16} \cdot \frac{27}{64} = 10 \cdot \frac{27}{1024} = \frac{270}{1024} \approx 0{,}264$.

---

### E03: Verificar una distribución de probabilidad

**Situación:** ¿Es la siguiente una distribución de probabilidad válida?

| $x$ | $-1$ | $0$ | $1$ | $2$ |
| :--- | :---: | :---: | :---: | :---: |
| $P(X=x)$ | $0{,}1$ | $0{,}3$ | $0{,}4$ | $0{,}2$ |

**La Carpintería:**
1. ¿Todas las probabilidades son $\geq 0$? Sí ✅.
2. ¿Suman $1$? $0{,}1 + 0{,}3 + 0{,}4 + 0{,}2 = 1{,}0$ ✅.
3. **Sí, es válida.**
4. $E(X) = (-1)(0{,}1) + 0(0{,}3) + 1(0{,}4) + 2(0{,}2) = -0{,}1 + 0 + 0{,}4 + 0{,}4 = 0{,}7$.
""")

    with st.expander("❓ Cuestionario PB05: Variable Aleatoria y Distribuciones", expanded=False):
        st.markdown(r"""
**1. Si $X$ tiene la distribución: $P(X=1) = 0{,}2$, $P(X=2) = 0{,}5$, $P(X=3) = 0{,}3$, entonces $E(X) =$**

A) $2$
B) $2{,}0$
C) $2{,}1$
D) $1{,}8$

---

**2. Para que una tabla sea una distribución de probabilidad válida, se requiere que:**

A) Todas las probabilidades sean positivas
B) Al menos una probabilidad sea $1$
C) La suma de todas las probabilidades sea $1$ y cada una sea $\geq 0$
D) La suma sea mayor que $1$

---

**3. En una distribución binomial con $n = 4$ y $p = 0{,}5$, la esperanza $E(X)$ es:**

A) $0{,}5$
B) $4$
C) $2$
D) $8$

---

**4. La ley de los grandes números establece que:**

A) Después de muchas caras, debe salir sello
B) El promedio de resultados se acerca al valor esperado con muchas repeticiones
C) La probabilidad cambia con cada repetición
D) Todo resultado es igualmente probable

---

**5. Un juego cuesta $\$1.000$ para participar. Ganas $\$3.000$ con probabilidad $\frac{1}{4}$ y pierdes con probabilidad $\frac{3}{4}$. ¿Cuál es la ganancia neta esperada?**

A) $\$750$
B) $-\$250$
C) $\$0$
D) $\$500$

---

**6. $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ corresponde a la distribución:**

A) Normal
B) Uniforme
C) Binomial
D) Poisson

---

**7. Si $X$ solo toma los valores $0$ y $1$, con $P(X=1) = p$, entonces $E(X) =$**

A) $0$
B) $1$
C) $p$
D) $1-p$
""")

    with st.expander("🔑 Pauta Técnica PB05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $E(X) = 1(0{,}2) + 2(0{,}5) + 3(0{,}3) = 0{,}2 + 1{,}0 + 0{,}9 = 2{,}1$. |
| **2** | **C** | Dos condiciones: cada $P(X=x_i) \geq 0$ y la suma total es exactamente $1$. |
| **3** | **C** | $E(X) = np = 4 \cdot 0{,}5 = 2$. |
| **4** | **B** | Al aumentar las repeticiones, el promedio converge al valor esperado. No hay "compensación" a corto plazo. |
| **5** | **B** | Ganancia neta: $(3000 - 1000) \cdot \frac{1}{4} + (0 - 1000) \cdot \frac{3}{4} = 500 - 750 = -250$. |
| **6** | **C** | Es la fórmula exacta de la distribución binomial con parámetros $n$ y $p$. |
| **7** | **C** | $E(X) = 0 \cdot (1-p) + 1 \cdot p = p$. Variable de Bernoulli. |
""")
