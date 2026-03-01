import streamlit as st


def render_D02():
    st.title("D02: Medidas de Tendencia Central — El Corazón de los Datos")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Qué Número Representa al Grupo?

Cuando tienes un conjunto de datos, necesitas un **valor representativo** que resuma toda la información en un solo número. Las medidas de tendencia central buscan exactamente eso: el "centro" del conjunto de datos. La PAES te pedirá calcularlas, compararlas y decidir cuál es más apropiada según el contexto.

---

### 🛡️ 2. Media Aritmética ($\bar{x}$)

Es el **promedio** tradicional: sumas todos los valores y divides por la cantidad.

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

**Ejemplo rápido:** Notas $5, 6, 4, 7, 3$ → $\bar{x} = \frac{5+6+4+7+3}{5} = \frac{25}{5} = 5$.

**Propiedades clave:**
- Es sensible a **datos extremos** (outliers). Un valor muy alto o muy bajo la "arrastra".
- Si sumamos o restamos una constante $k$ a todos los datos, la media cambia en $k$.
- Si multiplicamos todos los datos por $k$, la media se multiplica por $k$.

---

### 🛡️ 3. Media Ponderada

Cuando cada dato tiene un **peso** o importancia distinta:

$$\bar{x}_p = \frac{\sum w_i \cdot x_i}{\sum w_i}$$

**Ejemplo:** Tres pruebas con ponderaciones $30\%$, $30\%$, $40\%$ y notas $6{,}0$; $5{,}0$; $7{,}0$:

$$\bar{x}_p = \frac{0{,}3 \cdot 6 + 0{,}3 \cdot 5 + 0{,}4 \cdot 7}{0{,}3 + 0{,}3 + 0{,}4} = \frac{1{,}8 + 1{,}5 + 2{,}8}{1} = 6{,}1$$

---

### 🛡️ 4. Media para Datos Agrupados

Cuando los datos están en una tabla de frecuencias (con o sin intervalos):

$$\bar{x} = \frac{\sum f_i \cdot x_i}{n} = \frac{\sum f_i \cdot m_i}{n}$$

donde $m_i$ es la marca de clase si los datos están agrupados en intervalos.

---

### 🛡️ 5. Mediana ($Me$)

Es el **valor central** cuando los datos están ordenados de menor a mayor.

- Si $n$ es **impar**: la mediana es el dato en la posición $\dfrac{n+1}{2}$.
- Si $n$ es **par**: la mediana es el promedio de los datos en las posiciones $\dfrac{n}{2}$ y $\dfrac{n}{2} + 1$.

**Ejemplo ($n$ impar):** Datos ordenados: $2, 3, 5, 7, 9$ → posición $\frac{5+1}{2} = 3$ → $Me = 5$.

**Ejemplo ($n$ par):** Datos ordenados: $2, 3, 5, 7$ → posiciones $2$ y $3$ → $Me = \frac{3+5}{2} = 4$.

> **Ventaja:** La mediana **no** se ve afectada por datos extremos. Es más robusta que la media en presencia de outliers.

---

### 🛡️ 6. Moda ($Mo$)

Es el dato que **más se repite** (mayor frecuencia absoluta).

- Un conjunto puede ser **unimodal** (una moda), **bimodal** (dos modas) o **multimodal**.
- Si todos los datos tienen la misma frecuencia, **no hay moda**.

**Ejemplo:** $3, 5, 5, 7, 8, 5, 9$ → $Mo = 5$ (aparece $3$ veces).

---

### 🛡️ 7. ¿Cuándo Usar Cada Medida?

| Medida | Ideal cuando... | Evitar cuando... |
| :--- | :--- | :--- |
| **Media** | Los datos son simétricos, sin valores extremos | Hay outliers que distorsionan el promedio |
| **Mediana** | Hay datos extremos o distribución asimétrica | — (siempre es informativa) |
| **Moda** | Los datos son cualitativos o buscas lo más frecuente | Todos los valores son distintos |

> **Ejemplo clásico PAES:** Sueldos en una empresa: $\$500.000$; $\$500.000$; $\$600.000$; $\$550.000$; $\$8.000.000$. La media da $\$2.030.000$ (distorsionada por el sueldo alto), la mediana da $\$550.000$ (mucho más representativa).

---

> *"El promedio es una ficción estadística. Puedes tener la cabeza en el horno y los pies en el hielo, y en promedio estás cómodo."*
> — **Anónimo**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería D02", expanded=False):
        st.markdown(r"""
### E01: Calcular media, mediana y moda

**Situación:** Las edades de 9 participantes de un taller son: $18, 22, 19, 25, 22, 30, 22, 20, 24$.

**La Carpintería:**
1. **Ordenar:** $18, 19, 20, 22, 22, 22, 24, 25, 30$.
2. **Media:** $\bar{x} = \frac{18+19+20+22+22+22+24+25+30}{9} = \frac{202}{9} \approx 22{,}4$.
3. **Mediana:** $n = 9$ (impar), posición $\frac{9+1}{2} = 5$ → $Me = 22$.
4. **Moda:** $22$ aparece $3$ veces → $Mo = 22$.

| Medida | Valor |
| :--- | :---: |
| Media | $22{,}4$ |
| Mediana | $22$ |
| Moda | $22$ |

---

### E02: Media ponderada para notas finales

**Situación:** Un alumno tiene: Prueba 1 ($25\%$): nota $5{,}5$; Prueba 2 ($25\%$): nota $6{,}0$; Examen ($50\%$): nota $4{,}8$.

**La Carpintería:**
1. Multiplicar cada nota por su ponderación:
   - $5{,}5 \times 0{,}25 = 1{,}375$
   - $6{,}0 \times 0{,}25 = 1{,}500$
   - $4{,}8 \times 0{,}50 = 2{,}400$
2. Sumar: $1{,}375 + 1{,}500 + 2{,}400 = 5{,}275$.
3. Dividir por la suma de pesos ($1{,}00$): $\bar{x}_p = 5{,}275 \approx 5{,}3$.

| Evaluación | Nota | Peso | $w_i \cdot x_i$ |
| :--- | :---: | :---: | :---: |
| Prueba 1 | $5{,}5$ | $0{,}25$ | $1{,}375$ |
| Prueba 2 | $6{,}0$ | $0{,}25$ | $1{,}500$ |
| Examen | $4{,}8$ | $0{,}50$ | $2{,}400$ |
| **Total** | — | $1{,}00$ | $5{,}275$ |

---

### E03: Media para datos agrupados

**Situación:** Tabla de frecuencias de estaturas de 20 alumnos:

| Intervalo (cm) | $m_i$ | $f_i$ |
| :---: | :---: | :---: |
| $[150, 155)$ | $152{,}5$ | $3$ |
| $[155, 160)$ | $157{,}5$ | $7$ |
| $[160, 165)$ | $162{,}5$ | $6$ |
| $[165, 170)$ | $167{,}5$ | $4$ |

**La Carpintería:**
1. Calcular $f_i \cdot m_i$: $457{,}5$; $1102{,}5$; $975$; $670$.
2. Sumar: $\sum f_i \cdot m_i = 3205$.
3. Dividir: $\bar{x} = \frac{3205}{20} = 160{,}25$ cm.

---

### E04: Efecto de un dato extremo

**Situación:** Un grupo tiene notas $5, 5, 6, 6, 5, 6, 5$. Si se agrega una nota $1$, ¿cómo cambian las medidas?

**La Carpintería:**

| Medida | Sin el $1$ ($n=7$) | Con el $1$ ($n=8$) | ¿Cambió mucho? |
| :--- | :---: | :---: | :--- |
| Media | $\frac{38}{7} \approx 5{,}43$ | $\frac{39}{8} = 4{,}875$ | Sí, bajó |
| Mediana | $5$ | $5$ | No |
| Moda | $5$ | $5$ | No |

**Conclusión:** La media es la más sensible a outliers.
""")

    with st.expander("❓ Cuestionario D02: Medidas de Tendencia Central", expanded=False):
        st.markdown(r"""
**1. La media aritmética de $3, 5, 7, 9, 11$ es:**

A) $5$
B) $7$
C) $9$
D) $35$

---

**2. La mediana del conjunto $\{2, 8, 4, 10, 6\}$ es:**

A) $4$
B) $6$
C) $8$
D) $10$

---

**3. ¿Cuál medida de tendencia central NO se ve afectada por datos extremos?**

A) Media aritmética
B) Media ponderada
C) Mediana
D) Ninguna de las anteriores

---

**4. En el conjunto $\{3, 3, 5, 7, 7, 7, 9\}$, la moda es:**

A) $3$
B) $5$
C) $7$
D) $9$

---

**5. Un alumno tiene promedio $5{,}0$ en 4 pruebas. ¿Qué nota necesita en la 5.ª prueba para subir su promedio a $5{,}4$?**

A) $5{,}4$
B) $6{,}0$
C) $7{,}0$
D) $6{,}4$

---

**6. Si todos los datos de un conjunto se multiplican por $3$, la media:**

A) No cambia
B) Se triplica
C) Se suma $3$
D) Se divide por $3$

---

**7. Tres pruebas tienen ponderación $20\%$, $30\%$ y $50\%$. Con notas $7$, $5$ y $6$, la media ponderada es:**

A) $6{,}0$
B) $5{,}9$
C) $6{,}2$
D) $5{,}5$
""")

    with st.expander("🔑 Pauta Técnica D02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $\bar{x} = \frac{3+5+7+9+11}{5} = \frac{35}{5} = 7$. |
| **2** | **B** | Ordenando: $2, 4, 6, 8, 10$. El dato central (posición $3$) es $6$. |
| **3** | **C** | La mediana solo depende de la posición central, no de cuán extremos sean los valores. |
| **4** | **C** | $7$ aparece $3$ veces, más que cualquier otro valor. |
| **5** | **C** | Suma actual = $5{,}0 \times 4 = 20$. Necesita $\frac{20 + x}{5} = 5{,}4 \Rightarrow 20 + x = 27 \Rightarrow x = 7{,}0$. |
| **6** | **B** | Si $x_i' = 3x_i$, entonces $\bar{x}' = \frac{\sum 3x_i}{n} = 3\bar{x}$. |
| **7** | **B** | $\bar{x}_p = 0{,}2 \times 7 + 0{,}3 \times 5 + 0{,}5 \times 6 = 1{,}4 + 1{,}5 + 3{,}0 = 5{,}9$. |
""")
