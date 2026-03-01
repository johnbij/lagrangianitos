import streamlit as st


def render_D01():
    st.title("D01: Tipos de Datos y Tablas de Frecuencia — Ordenando el Mundo con Números")

    st.markdown(r"""
### 🛡️ 1. El Portal: ¿Qué Son los Datos?

Cada vez que mides, cuentas o clasificas algo, estás generando **datos**. La estadística es la disciplina que nos enseña a recopilarlos, organizarlos, analizarlos e interpretarlos para tomar decisiones informadas. En la PAES, saber distinguir el tipo de dato y construir una tabla de frecuencia es el primer paso para responder correctamente.

---

### 🛡️ 1.1 Población y Muestra

| Concepto | Definición | Ejemplo |
| :--- | :--- | :--- |
| **Población** | Conjunto **total** de individuos o elementos que se estudian | Todos los estudiantes de Chile |
| **Muestra** | Subconjunto representativo de la población | 500 estudiantes seleccionados al azar |

> **Tip PAES:** Si el enunciado dice "se encuestó a **todos** los alumnos del curso", estás trabajando con una **población** (del curso). Si dice "se seleccionaron al azar 30 alumnos", es una **muestra**.

---

### 🛡️ 2. Clasificación de Variables

Las variables se dividen en dos grandes familias:

| Tipo | Subtipo | ¿Qué mide? | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Cualitativa (categórica)** | Nominal | Categorías sin orden | Color favorito, género |
| **Cualitativa** | Ordinal | Categorías con orden | Nivel educacional (básica, media, superior) |
| **Cuantitativa** | Discreta | Valores contables (enteros) | N.° de hermanos, goles en un partido |
| **Cuantitativa** | Continua | Valores medibles (cualquier real) | Estatura ($1{,}73$ m), temperatura ($36{,}5°$C) |

> **Regla rápida:** Si puedes contar → **discreta**. Si puedes medir con decimales infinitos → **continua**. Si no es un número → **cualitativa**.

---

### 🛡️ 3. Frecuencias: Las Columnas que Cuentan la Historia

| Frecuencia | Símbolo | ¿Qué indica? | Fórmula |
| :--- | :---: | :--- | :--- |
| **Absoluta** | $f_i$ | Cuántas veces aparece cada dato | Contar |
| **Relativa** | $h_i$ | Proporción respecto al total | $h_i = \dfrac{f_i}{n}$ |
| **Porcentual** | $\%$ | Porcentaje respecto al total | $h_i \times 100\%$ |
| **Absoluta acumulada** | $F_i$ | Suma de frecuencias absolutas hasta ese valor | $F_i = f_1 + f_2 + \cdots + f_i$ |
| **Relativa acumulada** | $H_i$ | Suma de frecuencias relativas hasta ese valor | $H_i = h_1 + h_2 + \cdots + h_i$ |

> **Verificación:** La suma de todas las $f_i$ debe ser $n$ (total de datos). La suma de todas las $h_i$ debe ser $1$.

---

### 🛡️ 4. Tabla de Frecuencia para Datos No Agrupados

Si los datos toman pocos valores distintos, se construye una tabla directa.

**Ejemplo:** Notas de 10 alumnos: $5, 6, 4, 5, 7, 5, 6, 4, 5, 6$.

| Nota ($x_i$) | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :---: | :---: | :---: | :---: | :---: |
| $4$ | $2$ | $0{,}20$ | $2$ | $0{,}20$ |
| $5$ | $4$ | $0{,}40$ | $6$ | $0{,}60$ |
| $6$ | $3$ | $0{,}30$ | $9$ | $0{,}90$ |
| $7$ | $1$ | $0{,}10$ | $10$ | $1{,}00$ |
| **Total** | $10$ | $1{,}00$ | — | — |

---

### 🛡️ 5. Tabla de Frecuencia para Datos Agrupados en Intervalos

Cuando los datos son continuos o hay muchos valores distintos, se agrupan en **intervalos** (clases).

**Pasos para construirla:**
1. Determinar el **rango**: $R = x_{\max} - x_{\min}$.
2. Elegir el número de clases $k$ (frecuentemente $k \approx \sqrt{n}$).
3. Calcular la **amplitud** de cada clase: $A = \dfrac{R}{k}$ (se redondea hacia arriba).
4. Construir los intervalos con la convención $[a, b)$ (cerrado a la izquierda, abierto a la derecha).
5. La **marca de clase** es el punto medio del intervalo: $m_i = \dfrac{a + b}{2}$.

| Intervalo | Marca de clase ($m_i$) | $f_i$ | $h_i$ | $F_i$ |
| :---: | :---: | :---: | :---: | :---: |
| $[150, 155)$ | $152{,}5$ | $3$ | $0{,}15$ | $3$ |
| $[155, 160)$ | $157{,}5$ | $7$ | $0{,}35$ | $10$ |
| $[160, 165)$ | $162{,}5$ | $6$ | $0{,}30$ | $16$ |
| $[165, 170)$ | $167{,}5$ | $4$ | $0{,}20$ | $20$ |
| **Total** | — | $20$ | $1{,}00$ | — |

---

> *"Los datos son el nuevo petróleo, pero sin refinar no sirven de nada."*
> — **Clive Humby**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería D01", expanded=False):
        st.markdown(r"""
### E01: Clasificar variables

**Situación:** Un hospital registra de cada paciente: nombre, tipo de sangre, edad, peso y número de consultas previas. Clasifica cada variable.

**La Carpintería:**
1. **Nombre** → Cualitativa nominal (categoría sin orden numérico).
2. **Tipo de sangre** (A, B, AB, O) → Cualitativa nominal.
3. **Edad** (en años cumplidos: $25, 30, \ldots$) → Cuantitativa discreta (valores enteros contables).
4. **Peso** ($68{,}3$ kg, $72{,}1$ kg) → Cuantitativa continua (admite decimales infinitos).
5. **Número de consultas previas** ($0, 1, 2, \ldots$) → Cuantitativa discreta.

| Variable | Tipo | Subtipo |
| :--- | :--- | :--- |
| Nombre | Cualitativa | Nominal |
| Tipo de sangre | Cualitativa | Nominal |
| Edad (años cumplidos) | Cuantitativa | Discreta |
| Peso | Cuantitativa | Continua |
| N.° de consultas | Cuantitativa | Discreta |

---

### E02: Construir tabla de frecuencia (datos no agrupados)

**Situación:** En una prueba, 15 alumnos obtuvieron: $3, 4, 5, 5, 6, 4, 5, 7, 6, 5, 4, 6, 5, 4, 6$.

**La Carpintería:**
1. Ordenar datos: $3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7$.
2. Contar frecuencias absolutas.
3. Calcular $h_i = f_i / 15$.
4. Acumular.

| $x_i$ | $f_i$ | $h_i$ | $F_i$ | $H_i$ |
| :---: | :---: | :---: | :---: | :---: |
| $3$ | $1$ | $0{,}067$ | $1$ | $0{,}067$ |
| $4$ | $4$ | $0{,}267$ | $5$ | $0{,}333$ |
| $5$ | $5$ | $0{,}333$ | $10$ | $0{,}667$ |
| $6$ | $4$ | $0{,}267$ | $14$ | $0{,}933$ |
| $7$ | $1$ | $0{,}067$ | $15$ | $1{,}000$ |
| **Total** | $15$ | $1{,}000$ | — | — |

**Verificación:** $\sum f_i = 15$ ✅ y $\sum h_i = 1$ ✅.

---

### E03: Construir tabla con intervalos

**Situación:** Se miden las estaturas (cm) de 20 estudiantes: $152, 158, 161, 155, 167, 163, 154, 159, 160, 166, 157, 162, 168, 153, 156, 164, 161, 155, 165, 160$.

**La Carpintería:**
1. **Rango:** $R = 168 - 152 = 16$.
2. **N.° de clases:** $k = \sqrt{20} \approx 4{,}47 \Rightarrow k = 4$.
3. **Amplitud:** $A = 16 / 4 = 4$.
4. **Intervalos:** $[152, 156)$, $[156, 160)$, $[160, 164)$, $[164, 168]$.
5. Clasificar cada dato en su intervalo y contar.

| Intervalo | $m_i$ | $f_i$ | $h_i$ | $F_i$ |
| :---: | :---: | :---: | :---: | :---: |
| $[152, 156)$ | $154$ | $5$ | $0{,}25$ | $5$ |
| $[156, 160)$ | $158$ | $4$ | $0{,}20$ | $9$ |
| $[160, 164)$ | $162$ | $6$ | $0{,}30$ | $15$ |
| $[164, 168]$ | $166$ | $5$ | $0{,}25$ | $20$ |
| **Total** | — | $20$ | $1{,}00$ | — |

**Marca de clase:** $m_i = \frac{152 + 156}{2} = 154$, etc.
""")

    with st.expander("❓ Cuestionario D01: Tipos de Datos y Tablas de Frecuencia", expanded=False):
        st.markdown(r"""
**1. La variable "número de hijos" de una familia es:**

A) Cualitativa nominal
B) Cuantitativa continua
C) Cuantitativa discreta
D) Cualitativa ordinal

---

**2. Si en una encuesta de $n = 40$ personas, un dato aparece $8$ veces, su frecuencia relativa es:**

A) $8$
B) $0{,}08$
C) $0{,}20$
D) $20$

---

**3. La suma de todas las frecuencias relativas de una tabla debe ser:**

A) $0$
B) $100$
C) $n$
D) $1$

---

**4. ¿Cuál de las siguientes variables es cualitativa ordinal?**

A) Color de ojos
B) Nivel de satisfacción (bajo, medio, alto)
C) Temperatura corporal
D) Número de mascotas

---

**5. En una tabla de datos agrupados, la marca de clase del intervalo $[20, 30)$ es:**

A) $20$
B) $30$
C) $25$
D) $10$

---

**6. Si la frecuencia acumulada hasta la clase $[40, 50)$ es $35$ y la frecuencia absoluta de esa clase es $10$, entonces la frecuencia acumulada hasta la clase anterior es:**

A) $45$
B) $35$
C) $25$
D) $10$

---

**7. En un estudio, se seleccionan 200 personas de un país con 19 millones de habitantes. Las 200 personas corresponden a:**

A) La población
B) Una variable
C) La muestra
D) Un parámetro
""")

    with st.expander("🔑 Pauta Técnica D01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | El número de hijos se cuenta ($0, 1, 2, \ldots$). Es cuantitativa discreta. |
| **2** | **C** | $h_i = \frac{8}{40} = 0{,}20$. Frecuencia relativa = frecuencia absoluta dividida por el total. |
| **3** | **D** | $\sum h_i = 1$ siempre. Si se expresa en porcentaje, sería $100\%$. |
| **4** | **B** | "Bajo, medio, alto" son categorías con un orden natural → ordinal. |
| **5** | **C** | $m_i = \frac{20 + 30}{2} = 25$. La marca de clase es el promedio de los extremos del intervalo. |
| **6** | **C** | $F_{\text{anterior}} = F_i - f_i = 35 - 10 = 25$. La acumulada crece sumando la frecuencia de cada clase. |
| **7** | **C** | Las 200 personas son un subconjunto seleccionado de la población → muestra. |
""")
