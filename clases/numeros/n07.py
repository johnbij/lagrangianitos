import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def render_N07():
    st.title("N07: Los Números Reales (ℝ) — La Recta Numérica Completa")

    st.markdown(r"""
### 🛡️ 1. El Portal: El Mapa del Tesoro Completo

Imagínate que hasta ahora estábamos explorando el mapa de una isla, pero solo veíamos los árboles (Naturales) o los senderos (Racionales). Los **Números Reales** son la isla completa, con cada grano de arena y cada gota de agua.

Históricamente, la matemática pasó siglos intentando "tapar los hoyos" de la recta numérica. Cuando por fin unimos a los Racionales con los Irracionales, logramos la **Continuidad**. Si tiras un dardo a la recta numérica, no importa dónde caiga, SIEMPRE vas a clavar un Número Real. No hay vacíos.

---

### 🛡️ 7.1 La Recta Numérica Continua

Los Reales son el conjunto que llena la recta.

* **$\mathbb{R} = \mathbb{Q} \cup \mathbb{I}$**: Es la unión final.
* **Disjuntos:** Recuerda que un número no puede estar en crisis de identidad: o es **$\mathbb{Q}$** o es **$\mathbb{I}$**. No hay nada en la intersección ($\mathbb{Q} \cap \mathbb{I} = \emptyset$).

---

### 🛡️ 7.2 ¿Qué NO es un Real? (Zonas de Peligro)

Para la PAES, el alumno debe saber que hay "monstruos" fuera del mapa real:

1. **Raíces de índice par con base negativa:** $\sqrt{-4}$. No existe ningún número real que al elevarlo al cuadrado te dé algo negativo. Eso es un número **Imaginario**.
2. **Divisiones por cero:** $k/0$. Eso no es un número, es una **Indefinición**.

---

### 🏛️ 7.3 El Rigor Técnico: ¿Qué es un Axioma y un Cuerpo?

Antes de entrar a la tabla, hay que entender el idioma que hablamos en las grandes ligas (como en el plan común de ingeniería):

* **¿Qué es un Axioma?** Es una verdad absoluta que no requiere demostración. Es una regla de oro que aceptamos para poder empezar a construir todo lo demás.
* **¿Qué es un Cuerpo?** Es una estructura matemática donde la suma y la multiplicación se portan "bien". Es decir, puedes operar sin miedo a que el sistema explote (mientras no dividas por cero).

---

### 🛡️ 7.4 Los Axiomas de Cuerpo de los Reales

Para que un conjunto sea un **Cuerpo**, debe cumplir estas leyes para cualquier trío de números $a, b, c \in \mathbb{R}$:

| Propiedad | Definición en Suma ($+$) | Definición en Multiplicación ($\cdot$) |
| :--- | :--- | :--- |
| **Clausura** | $a + b \in \mathbb{R}$ | $a \cdot b \in \mathbb{R}$ |
| **Conmutatividad** | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| **Asociatividad** | $a + (b + c) = (a + b) + c$ | $a \cdot (b \cdot c) = (a \cdot b) \cdot c$ |
| **Elemento Neutro** | $a + 0 = a$ | $a \cdot 1 = a$ |
| **Elemento Inverso** | $a + (-a) = 0$ | $a \cdot \frac{1}{a} = 1$ (con $a \neq 0$) |
| **Distributividad** | \multicolumn{2}{c\|}{$a \cdot (b + c) = ab + ac$} |

> **Típ:** Los axiomas son como las leyes de la física en un videojuego. No te preguntas por qué la gravedad funciona, simplemente la usas para saltar. En la PAES, cuando despejas una ecuación, estás usando estos axiomas sin darte cuenta.

---

> "Las leyes de la matemática no son meras invenciones humanas, son la descripción de la estructura misma de la realidad".
> — **Roger Penrose**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería N07", expanded=False):
        st.markdown(r"""
### E02: El Filtro de la Realidad

**Situación:** Clasificar si los siguientes números pertenecen al conjunto de los Reales ($\mathbb{R}$): $\sqrt{25}$, $\sqrt{-25}$, $0/7$, $7/0$.

**La Carpintería:**
1. **Analizar $\sqrt{25}$:** Es $5$. El 5 es un entero, por ende es Racional y **Real**.
2. **Analizar $\sqrt{-25}$:** No existe ningún número real que al cuadrado dé $-25$. Es un número **Imaginario**.
3. **Analizar $0/7$:** El resultado es $0$. El cero es un número **Real**.
4. **Analizar $7/0$:** La división por cero no está permitida en ningún conjunto numérico. Es una **Indefinición**.

| Número | Resultado | ¿Es Real? | Razón Técnica |
| :--- | :---: | :---: | :--- |
| $\sqrt{25}$ | 5 | ✅ SÍ | Raíz de base positiva. |
| $\sqrt{-25}$ | $5i$ | ❌ NO | Raíz par de base negativa. |
| $0/7$ | 0 | ✅ SÍ | El cero es un número real. |
| $7/0$ | $\nexists$ | ❌ NO | Indefinición matemática. |

---

### E03: Aplicando el Axioma de Inverso

**Situación:** Hallar el inverso aditivo de $-3$ y el inverso multiplicativo de $2/5$.

**La Carpintería:**
1. **Inverso Aditivo:** Es el número que sumado con $-3$ da el neutro ($0$). Por axioma, es $3$.
2. **Inverso Multiplicativo:** Es el número que multiplicado por $2/5$ da el neutro ($1$). Por axioma, es dar vuelta la fracción: $5/2$.

| Tipo de Inverso | Número Original | Resultado | Comprobación |
| :--- | :---: | :---: | :--- |
| **Aditivo** | $-3$ | $3$ | $-3 + 3 = 0$ |
| **Multiplicativo** | $2/5$ | $5/2$ | $2/5 \cdot 5/2 = 1$ |

---

### E04: Identificación de Propiedades (Axiomas)

**Situación:** ¿Qué axioma se aplica en la expresión $3 \cdot (x + 4) = 3x + 12$?

**La Carpintería:**
1. **Observar:** El 3 que estaba multiplicando afuera entró a multiplicar a cada término del paréntesis.
2. **Relacionar:** Esta es la propiedad que conecta la multiplicación con la suma.
3. **Conclusión:** Se aplicó el Axioma de **Distributividad**.

| Expresión Inicial | Operación | Axioma Aplicado |
| :--- | :--- | :--- |
| $3(x + 4)$ | $3 \cdot x + 3 \cdot 4$ | **Distributividad** |

---

### E05: El Neutro en Operaciones Combinadas

**Situación:** Resolver la expresión $\pi \cdot 1 + (5 + (-5))$ usando axiomas.

**La Carpintería:**
1. **Parte 1:** $\pi \cdot 1$. Por axioma de **Neutro Multiplicativo**, cualquier número por 1 es el mismo número. Resultado: $\pi$.
2. **Parte 2:** $5 + (-5)$. Por axioma de **Inverso Aditivo**, un número más su opuesto es cero. Resultado: $0$.
3. **Suma Final:** $\pi + 0$. Por axioma de **Neutro Aditivo**, el resultado es $\pi$.

| Paso | Operación | Resultado | Axioma Usado |
| :--- | :---: | :---: | :--- |
| 1 | $\pi \cdot 1$ | $\pi$ | Neutro Multiplicativo |
| 2 | $5 + (-5)$ | 0 | Inverso Aditivo |
| 3 | $\pi + 0$ | **$\pi$** | Neutro Aditivo |

---

### E06: Jerarquía y Subconjuntos

**Situación:** Indicar la clasificación más específica para el número $-4$.

**La Carpintería:**
1. **¿Es Natural?** No, los naturales son positivos.
2. **¿Es Entero?** Sí, es un número sin decimales y negativo.
3. **¿Es Racional?** Sí, se puede escribir como $-4/1$.
4. **¿Es Real?** Sí, todos los anteriores están dentro de los Reales.

| Conjunto | ¿Pertenece? | Razón |
| :--- | :---: | :--- |
| $\mathbb{N}$ | ❌ No | Es negativo. |
| $\mathbb{Z}$ | ✅ Sí | Es un valor exacto. |
| $\mathbb{Q}$ | ✅ Sí | Se expresa como fracción. |
| $\mathbb{R}$ | ✅ Sí | Pertenece a la recta numérica. |
""")

    with st.expander("❓ Cuestionario N07: Los Números Reales", expanded=False):
        st.markdown(r"""
**1. ¿Cuál de los siguientes números NO pertenece al conjunto de los números Reales ($\mathbb{R}$)?**

A) $\sqrt{2}$  
B) $\sqrt{-9}$  
C) $0 / \pi$  
D) $-10,5$

---

**2. Si $a$ es un número real, el axioma que garantiza que $a + 0 = a$ se denomina:**

A) Clausura.  
B) Elemento Neutro Aditivo.  
C) Inverso Aditivo.  
D) Conmutatividad.

---

**3. ¿Cuál es el inverso multiplicativo de $-0,75$?**

A) $0,75$  
B) $4/3$  
C) $-4/3$  
D) $-3/4$

---

**4. La expresión $a \cdot (b + c) = ab + ac$ es la representación del axioma de:**

A) Asociatividad.  
B) Conmutatividad.  
C) Distributividad.  
D) Inverso Multiplicativo.

---

**5. Respecto a los subconjuntos de los Reales, ¿cuál de las siguientes afirmaciones es CORRECTA?**

A) Todo número real es también un número racional.  
B) El conjunto de los irracionales está contenido en los racionales.  
C) Los Reales son la unión de los Racionales y los Irracionales.  
D) El cero es el único número que es Racional e Irracional a la vez.

---

**6. ¿Qué ocurre con la operación $5 / (4 - 4)$ en el conjunto de los Reales?**

A) El resultado es $0$.  
B) El resultado es $5$.  
C) Es una indefinición (no es un número real).  
D) El resultado es un número irracional.

---

**7. El axioma de Conmutatividad en la multiplicación establece que:**

A) El orden de los factores no altera el producto.  
B) Todo número multiplicado por 1 es el mismo número.  
C) Los números se pueden agrupar de distintas formas.  
D) Todo número multiplicado por 0 es 0.

---

**8. Si $x$ es un número irracional, ¿cuál de los siguientes números es SIEMPRE un número real?**

A) $x + 5$  
B) $x^2$  
C) $x / 0$  
D) $\sqrt{-x}$ (asumiendo $x$ positivo)

---

**9. ¿Cuál es el inverso aditivo de $\sqrt{2}$?**

A) $1 / \sqrt{2}$  
B) $2$  
C) $-\sqrt{2}$  
D) $0$

---

**10. Un número que puede ser escrito como $a/b$ (con $a, b \in \mathbb{Z}$ y $b \neq 0$) pertenece a $\mathbb{Q}$. Al unir todos estos con los que NO pueden escribirse así, formamos:**

A) Los Enteros ($\mathbb{Z}$).  
B) Los Imaginarios.  
C) Los Reales ($\mathbb{R}$).  
D) Los Naturales ($\mathbb{N}$).
""")

    with st.expander("🔑 Pauta Técnica N07: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | Las raíces de índice par (como la cuadrada) con cantidad subradical negativa no son reales, son imaginarias. |
| **2** | **B** | El neutro es el elemento que "no altera" al otro en la operación. En la suma es el $0$. |
| **3** | **C** | $-0,75 = -3/4$. Su inverso multiplicativo es "dar vuelta" la fracción manteniendo el signo: $-4/3$. |
| **4** | **C** | Es la propiedad que permite distribuir el factor exterior a cada sumando del paréntesis. |
| **5** | **C** | Es la definición estructural de $\mathbb{R}$: $\mathbb{Q} \cup \mathbb{I}$. |
| **6** | **C** | $4 - 4 = 0$. La división por cero no está definida en los números reales. |
| **7** | **A** | $a \cdot b = b \cdot a$. El intercambio de posición no afecta el resultado final. |
| **8** | **A** | Por el axioma de clausura, la suma de dos reales (irracional + racional) siempre da un real. |
| **9** | **C** | El inverso aditivo (u opuesto) es el mismo número con el signo contrario para que la suma sea $0$. |
| **10** | **C** | Es el resumen de la clase: Racionales + Irracionales = El universo Real completo. |
""")
