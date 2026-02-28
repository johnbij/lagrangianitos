import streamlit as st


def render_N14():
    st.title("N14: El Lenguaje del Reparto - Algoritmos y Vocabulario")

    st.markdown(r"""
### 🏛️ 1. Contexto Histórico: El Nacimiento de la Raya Fraccionaria
¿Te has fijado que el signo de división ($\div$) es literalmente una fracción con dos puntos? Durante siglos, cada cultura escribía la división como podía. Los árabes introdujeron la **"barra de fracción"** (al-ghubar) para separar lo que tengo de lo que reparto.

Pero antes de la fracción, existió el **Algoritmo de la División**. Los babilonios y egipcios necesitaban saber no solo cuánto tocaba, sino cuánto sobraba. Si repartes 13 flechas entre 3 guerreros, a cada uno le tocan 4, pero sobra 1. Esa "sobra" es la que obligó a inventar los decimales y las fracciones. No es solo un cálculo; es la contabilidad de la realidad.

---

### 🛡️ 9.C.1 Las Partes del Motor (Vocabulario Técnico)
En el taller, si pides un "cosito" nadie te entiende. En matemática, cada parte tiene su nombre:

* **Factor:** Es cualquier número que se está multiplicando para dar un resultado.
  * *Ejemplo:* En $2 \cdot 3 = 6$, el 2 y el 3 son factores.
* **Divisor:** Es el número que "corta". En $10 \div 2$, el 2 es el divisor.
* **Múltiplo:** Es el resultado de multiplicar un número por un entero. (El 10 es múltiplo de 2 y de 5).
* **Divisibilidad:** Decimos que un número es "divisible" por otro si al dividirlos el **Resto es CERO**.

---

### 🛡️ 9.C.2 El Algoritmo de la División (La Identidad)
Para cualquier par de números naturales $D$ (Dividendo) y $d$ (divisor), existen siempre un único cociente $q$ y un resto $r$ que cumplen:
$$D = d \cdot q + r$$
**Condición sagrada:** El resto ($r$) siempre debe ser menor que el divisor ($d$). Si el resto es más grande, es que todavía puedes seguir repartiendo.

**Relación con la Fracción:**
Cuando escribes $\frac{13}{3}$, el algoritmo te dice: $13 = 3 \cdot 4 + 1$.
* El **4** es el entero (cociente).
* El **1** es lo que queda arriba de la fracción (resto).
* El **3** sigue abajo (divisor).
* Resultado: $4 \frac{1}{3}$.

---

### 🛡️ 9.C.3 ¿Por qué usamos la notación de Fracción?
Usamos la barra $\frac{a}{b}$ por una razón de "limpieza" táctica:
1. **Precisión:** $1 \div 3$ es $0,3333...$ (nunca terminas de escribirlo). En cambio, $\frac{1}{3}$ es el valor exacto, sin perder ni un átomo de información.
2. **Operatividad:** Es mucho más fácil simplificar $\frac{120}{180}$ que andar dividiendo números gigantes con decimales. La fracción es la "forma comprimida" de una división.

---

### 🛡️ 9.C.4 Factores vs. Divisores (La gran confusión)
* Los **Factores** construyen el número (multiplicando).
* Los **Divisores** desarman el número (dividiendo).
* **Dato de Pillo:** En los números enteros, los factores y los divisores son prácticamente los mismos. Si 3 es factor de 12 ($3 \cdot 4$), entonces 3 también es divisor de 12 ($12 \div 3$).

> **Típ:** En la PAES, cuando te hablen de "el factor de un número", piensa inmediatamente en qué números multiplicados dan ese valor. Si te hablan de "divisor", piensa en quién lo parte de forma exacta.

---

> "Dividir es la forma más noble de multiplicar la justicia".
> — **Anónimo (proverbio de mercaderes)**
""")

    with st.expander("❓ Cuestionario N14: El Lenguaje del Reparto", expanded=False):
        st.markdown(r"""
> **¡Ojo con los términos!** En este cuestionario no solo operamos, evaluamos si conoces las piezas del motor. Lee bien cada palabra: divisor, cociente, resto y factor.

**1. Según el Algoritmo de la División, si el dividendo es 17 y el divisor es 5, ¿cuál es el valor del resto?**
\
A) 1
\
B) 2
\
C) 3
\
D) 5

**2. ¿Cuál de las siguientes afirmaciones sobre el Resto (r) es siempre verdadera?**
\
A) El resto puede ser igual al divisor.
\
B) El resto debe ser menor que el divisor.
\
C) El resto debe ser mayor que el cociente.
\
D) El resto siempre es cero en los números racionales.

**3. Si un número se puede expresar como $24 = 3 \cdot 8$, ¿qué nombre técnico reciben el 3 y el 8?**
\
A) Divisores y múltiplos.
\
B) Factores.
\
C) Restos.
\
D) Dividendos.

**4. Al transformar la fracción impropia $\frac{23}{4}$ a número mixto usando el algoritmo de la división, obtenemos:**
\
A) $5 \frac{1}{4}$
\
B) $4 \frac{3}{4}$
\
C) $5 \frac{3}{4}$
\
D) $6 \frac{1}{4}$

**5. ¿Qué significa que un número sea "divisible" por otro?**
\
A) Que el resultado es un número decimal.
\
B) Que el resto de la división es cero.
\
C) Que el cociente es mayor que el dividendo.
\
D) Que ambos números son primos.

**6. Si el cociente de una división es 6, el divisor es 4 y el resto es 3, ¿cuál es el dividendo?**
\
A) 24
\
B) 27
\
C) 18
\
D) 13

**7. En la fracción $\frac{12}{18}$, ¿cuál es el Máximo Común Divisor (MCD) que permite llegar a la fracción irreductible de un solo golpe?**
\
A) 2
\
B) 3
\
C) 6
\
D) 9

**8. ¿Cuál es la principal ventaja de usar la notación de fracción ($\frac{1}{3}$) en lugar de su forma decimal ($0,333...$)?**
\
A) Es más fácil de escribir.
\
B) Representa el valor exacto sin perder información.
\
C) No requiere conocer el algoritmo de la división.
\
D) Las fracciones siempre son números enteros.

**9. Si el resto de una división es 0, podemos afirmar que:**
\
A) El dividendo es un número primo.
\
B) El divisor es un factor del dividendo.
\
C) El cociente es igual al resto.
\
D) La división no se puede realizar.

**10. En el número mixto $7 \frac{2}{5}$, ¿cuál de los siguientes elementos representa el "Resto" del algoritmo original?**
\
A) 7
\
B) 5
\
C) 2
\
D) 35
""")

    with st.expander("🔑 Pauta Técnica N14: Algoritmos y Vocabulario", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El Paso a Paso) |
| :--- | :---: | :--- |
| **1** | **B** | $17 \div 5 = 3$ y sobran **2**. ($17 = 5 \cdot 3 + 2$). |
| **2** | **B** | Regla sagrada: El resto $r$ siempre debe cumplir $0 \le r < d$. |
| **3** | **B** | Los números que se multiplican para formar un producto son **factores**. |
| **4** | **C** | $23 \div 4 = 5$ (entero) y sobran **3** (numerador). Resultado: $5 \frac{3}{4}$. |
| **5** | **B** | Divisibilidad implica una división exacta, es decir, resto **cero**. |
| **6** | **B** | Aplicando $D = d \cdot q + r \rightarrow D = 4 \cdot 6 + 3 = 24 + 3 = 27$. |
| **7** | **C** | Los divisores de 12 son {1,2,3,4,6,12} y de 18 {1,2,3,6,9,18}. El mayor común es **6**. |
| **8** | **B** | La fracción evita el error de aproximación de los decimales infinitos. |
| **9** | **B** | Si la división es exacta, el divisor "cabe" justo, por lo tanto es un **factor**. |
| **10** | **C** | Al pasar de impropia a mixto, el numerador resultante es siempre el **resto**. |

---

> **Típ:** Si en un problema de planteo te preguntan "¿cuántas piezas sobran?", te están pidiendo el **Resto** ($r$) del algoritmo de la división. No sigas dividiendo con decimales, quédate con el número entero que sobró.
""")
