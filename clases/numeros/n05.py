import streamlit as st
import matplotlib.pyplot as plt


def render_N05():
    st.title("N05: Los Números Racionales (ℚ) — La Densidad y el Cociente")

    st.markdown(r"""
### 🛡️ 1. El Portal: El Arte de Partir el Todo

Hasta ahora, en nuestra carpintería matemática, solo trabajábamos con "piezas completas" (vigas de 1 metro, de 2 metros). Pero la realidad es más compleja: a veces necesitas media viga o un tercio de tabla.

El nombre **Racional** viene de "Razón" (un cociente entre dos cantidades). Los antiguos egipcios ya usaban fracciones para repartir el grano y medir tierras tras las crecidas del Nilo. Al crear $\mathbb{Q}$ (del italiano *Quoziente*), la humanidad logró por fin la **Clausura de la División**: ahora cualquier reparto tiene un número que lo representa.

---

### 🛡️ 2. Definición Formal y Axiomática

Un número es **Racional** si y solo si puede expresarse como el cociente entre dos enteros:

$$\mathbb{Q} = \left\{ \frac{a}{b} \mid a, b \in \mathbb{Z}, b \neq 0 \right\}$$

**Análisis de los Componentes:**
* **Numerador ($a$):** Es el "contador". Nos dice cuántas partes tomamos.
* **Denominador ($b$):** Es el "divisor". Define en cuántas partes iguales se cortó la unidad.
* **⚠️ La Restricción Suprema:** El denominador **jamás puede ser cero**. La división por cero es el "agujero negro" de la matemática; si la intentas, la lógica se rompe.

---

### 🛡️ 3. La Propiedad de Densidad: El Fin de los Saltos

Este es el concepto clave para los 1000 puntos.

* En $\mathbb{N}, \mathbb{N}_0$ y $\mathbb{Z}$, los niveles son **discretos** (hay saltos vacíos entre ellos). Existe el concepto de "el que viene después".
* **En $\mathbb{Q}$ NO existe el sucesor ni el antecesor.** El conjunto es **Denso**.

**¿Qué significa esto?** Que entre dos racionales, por muy pegados que los dibujes, siempre hay **infinitos** números más. La recta ya no tiene puntos aislados, ahora es una alfombra casi continua.
""")

    fig, ax = plt.subplots(figsize=(12, 3))
    ax.axhline(0, color='black', lw=2)
    racionales = {0: "0", 1/4: "1/4", 1/3: "1/3", 1/2: "1/2", 2/3: "2/3", 3/4: "3/4", 1: "1"}
    for val, label in racionales.items():
        color = 'red' if val in [0, 1] else 'blue'
        ax.plot(val, 0, 'o', color=color, markersize=8)
        ax.text(val, 0.05, label, ha='center', va='bottom', fontsize=11, fontweight='bold', color=color)
    for d in range(5, 12):
        for n in range(1, d):
            v = n/d
            if v not in racionales:
                ax.plot(v, 0, '|', color='gray', alpha=0.5, markersize=10)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 0.2)
    ax.axis('off')
    plt.title("Propiedad de Densidad: Entre el 0 y el 1 existen infinitos Racionales", fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🛡️ 4. Representación Decimal y Clasificación

Todo racional se puede "disfrazar" de decimal dividiendo el numerador por el denominador. Solo existen tres especies en este reino:

1. **Decimales Finitos:** Tienen una cantidad limitada de cifras decimales (Ej: $1/4 = 0,25$).
2. **Infinitos Periódicos:** El ciclo de repetición empieza inmediatamente tras la coma (Ej: $1/3 = 0,\bar{3}$).
3. **Infinitos Semiperiódicos:** Tienen una parte que no se repite (anteperiodo) antes del periodo (Ej: $0,1\bar{6}$).

---

### 🛡️ 5. Clausura: El Club casi Perfecto

| Operación | ¿Es Cerrada en $\mathbb{Q}$? | Carpintería Técnica |
| :--- | :---: | :--- |
| **Suma / Resta / Multi.** | ✅ SÍ | Siempre dan otro racional. |
| **División (:)** | ⚠️ CASI | Es cerrada **siempre y cuando el divisor no sea cero**. |

---

### 🛡️ 6. Manteniendo la Igualdad: Amplificar y Simplificar

Para trabajar con fracciones, debemos entender que una misma cantidad puede escribirse con distintos números sin cambiar su valor. Esto se conoce como **Fracciones Equivalentes**.

* **Amplificar:** Es multiplicar el numerador y el denominador por el mismo número natural ($>1$). Se usa principalmente para **igualar denominadores** y poder sumar o restar.
    * Ejemplo: $\frac{2}{3} \xrightarrow{\cdot 4} \frac{8}{12}$ (Es la misma cantidad, pero cortada en trozos más chicos).
* **Simplificar:** Es dividir el numerador y el denominador por un divisor común. Se usa para llegar a la **Fracción Irreducible**.
    * Ejemplo: $\frac{15}{20} \xrightarrow{: 5} \frac{3}{4}$

> **Típ:** En la PAES, nunca entregues una respuesta sin simplificar al máximo. Si tu cálculo te da $20/40$, es muy probable que en las alternativas solo aparezca el $1/2$. Simplificar es "limpiar" la zona de trabajo.

---

> "Las matemáticas son el lenguaje con el que se describe el mundo, y las fracciones son las palabras que nos permiten ser precisos".
> — **Henri Poincaré**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería N05", expanded=False):
        st.markdown(r"""
### E01: Transformación de Decimal Finito a Fracción

**Situación:** Expresar el número $0,75$ como una fracción irreducible.

**La Carpintería:**
1. **Numerador:** Se escribe el número sin coma ($75$).
2. **Denominador:** Una potencia de 10 con tantos ceros como decimales tenga el número (2 decimales = $100$).
3. **Simplificar:** Buscamos un divisor común. Dividimos ambos por $25$.
4. **Resultado:** $3/4$.

| Paso | Operación | Resultado |
| :--- | :--- | :---: |
| 1 | Escribir numerador | 75 |
| 2 | Escribir denominador ($10^2$) | 100 |
| 3 | Simplificar por 25 | **3/4** |

---

### E02: Transformación de Decimal Periódico

**Situación:** Expresar $0,\bar{6}$ como una fracción de enteros.

**La Carpintería:**
1. **Numerador:** Se toma el número completo ($6$) y se le resta la parte entera ($0$).
2. **Denominador:** Tantos "9" como cifras tenga el periodo (1 cifra = un "9").
3. **Simplificar:** Dividimos por 3 para llegar a la irreducible.
4. **Resultado:** $2/3$.

| Componente | Proceso | Valor |
| :--- | :--- | :---: |
| Numerador | $6 - 0$ | 6 |
| Denominador | Un "9" por el periodo | 9 |
| **Final** | **$6/9$ simplificado** | **2/3** |

---

### E03: Uso de la Amplificación para Comparar

**Situación:** ¿Cuál de estas fracciones es mayor: $2/3$ o $3/5$?

**La Carpintería:**
1. **Problema:** Los denominadores son distintos, no puedo comparar "peras con manzanas".
2. **Amplificar:** Buscamos un denominador común (MCM entre 3 y 5 es 15).
3. **Transformar:** $2/3$ lo multiplicamos por 5: $10/15$. / $3/5$ lo multiplicamos por 3: $9/15$.
4. **Resultado:** Como $10/15 > 9/15$, entonces $2/3 > 3/5$.

| Fracción Original | Amplificación | Fracción Equivalente |
| :--- | :---: | :---: |
| $2/3$ | $\cdot 5$ | $10/15$ |
| $3/5$ | $\cdot 3$ | $9/15$ |

---

### E04: El Desafío del Semiperiódico

**Situación:** Transformar $0,1\bar{6}$ a fracción.

**La Carpintería:**
1. **Numerador:** El número sin coma ($16$) menos la parte que no tiene raya ($1$). Resultado: $15$.
2. **Denominador:** Un "9" (por el periodo 6) y un "0" (por el anteperiodo 1). Resultado: $90$.
3. **Simplificar:** Dividimos por 15.
4. **Resultado:** $1/6$.

| Parte | Valor | Razón |
| :--- | :---: | :--- |
| Numerador | 15 | $16 - 1$ |
| Denominador | 90 | Un "9" y un "0" |
| **Resultado** | **1/6** | Simplificación máxima |

---

### E05: La Densidad en Práctica (El Promedio)

**Situación:** Encontrar un número racional que se encuentre exactamente entre $1/4$ y $1/2$.

**La Carpintería:**
1. **Amplificar para igualar:** $1/2$ es igual a $2/4$.
2. **Problema:** Entre $1/4$ y $2/4$ no se ve espacio. Amplificamos de nuevo ambos por 2.
3. **Nuevos valores:** $2/8$ y $4/8$.
4. **Identificar el punto medio:** Claramente es $3/8$.
5. **Resultado:** $3/8$ (o $0,375$).

| Racional A | Racional B | Promedio (A+B)/2 |
| :---: | :---: | :---: |
| $2/8$ ($0,25$) | $4/8$ ($0,50$) | **3/8** ($0,375$) |
""")

    with st.expander("❓ Cuestionario N05: Números Racionales", expanded=False):
        st.markdown(r"""
**1. ¿Cuál de los siguientes números NO puede escribirse como una fracción de la forma $a/b$ con $b \neq 0$?**

A) 0  
B) $-10$  
C) $1,\bar{3}$  
D) Un decimal cuyas cifras no tienen patrón ni fin.

---

**2. Al simplificar al máximo la fracción $45/60$, obtenemos:**

A) $9/12$  
B) $15/20$  
C) $3/4$  
D) $0,75$

---

**3. ¿Qué número resulta al amplificar la fracción $2/7$ por 4?**

A) $8/7$  
B) $2/28$  
C) $8/28$  
D) $6/11$

---

**4. El número decimal $0,4\bar{6}$ corresponde a la fracción:**

A) $46/90$  
B) $42/90$  
C) $46/99$  
D) $7/15$

---

**5. Si sumamos dos números racionales, el resultado SIEMPRE será un racional. Esta propiedad se llama:**

A) Densidad  
B) Clausura  
C) Conmutativa  
D) Distributiva

---

**6. ¿Cuál de las siguientes afirmaciones sobre la propiedad de densidad es CORRECTA?**

A) Entre $1/2$ y $1/3$ no hay más números.  
B) Solo existen números racionales entre enteros.  
C) Entre cualquier pareja de racionales hay infinitos racionales.  
D) El sucesor de $0,5$ es $0,6$.

---

**7. Al dividir $1$ por $3$, el resultado es un decimal de tipo:**

A) Finito  
B) Infinito Periódico  
C) Infinito Semiperiódico  
D) No Racional

---

**8. Si $x = 0,25$ y $y = 1/4$, ¿cuál de las siguientes opciones es verdadera?**

A) $x > y$  
B) $x < y$  
C) $x = y$  
D) No se pueden comparar.

---

**9. La fracción irreducible equivalente a $12/100$ es:**

A) $6/50$  
B) $3/25$  
C) $0,12$  
D) $12/100$ no se puede simplificar.

---

**10. En la división de racionales, la clausura falla únicamente cuando:**

A) El dividendo es negativo.  
B) El resultado es un decimal infinito.  
C) El divisor es cero.  
D) Las fracciones tienen distinto denominador.
""")

    with st.expander("🔑 Pauta Técnica N05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **D** | Los racionales requieren orden (periodo) o fin. Si el decimal es infinito y caótico, es Irracional. |
| **2** | **C** | $45$ y $60$ son divisibles por $15$. $45:15=3$ y $60:15=4$. |
| **3** | **C** | Amplificar es multiplicar arriba y abajo por el mismo número: $2\cdot4=8$ y $7\cdot4=28$. |
| **4** | **D** | Numerador: $46-4=42$. Denominador: $90$. Fracción $42/90$. Simplificando por 6 da $7/15$. |
| **5** | **B** | La clausura garantiza que el resultado de la operación se mantiene dentro del mismo conjunto. |
| **6** | **C** | Es la esencia de la densidad; la recta se vuelve "tupida" de números. |
| **7** | **B** | $1:3 = 0,333...$ El periodo empieza inmediatamente tras la coma. |
| **8** | **C** | $0,25$ es la representación decimal de la fracción $1/4$. Son el mismo valor. |
| **9** | **B** | Ambos son pares, dividimos por 4: $12:4=3$ y $100:4=25$. |
| **10** | **C** | La división por cero es una indefinición, lo que rompe la regla de clausura en $\mathbb{Q}$. |
""")
