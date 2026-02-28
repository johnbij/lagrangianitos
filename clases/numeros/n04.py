import streamlit as st
import matplotlib.pyplot as plt


def render_N04():
    st.title("N04: Los Números Enteros (ℤ) — La Simetría y el Imperio de la Resta")

    st.markdown(r"""
### 🛡️ 1. El Portal: El Escándalo de los Números "Absurdos"

Imagínate que eres un matemático griego de la época de Pitágoras. Para ti, los números son geometría: el 3 es un triángulo, el 4 es un cuadrado. Bajo esa lógica, **¿qué demonios es un -2?** ¿Un cuadrado con lados negativos? ¡Imposible! Durante más de mil años, Occidente se negó a aceptar los negativos, llamándolos *numeri absurdi*.

Sin embargo, en el otro lado del mundo, los comerciantes de la Ruta de la Seda no tenían esos prejuicios. Los matemáticos indios como **Brahmagupta** (año 628) ya hablaban de "Fortuna" (positivos) y "Deuda" (negativos). Ellos entendieron que el universo es simétrico: por cada montaña hay un valle, por cada grado sobre cero hay uno bajo cero.

Al crear los Enteros ($\mathbb{Z}$, del alemán *Zahlen*), la humanidad dejó de ver los números como "cosas" y empezó a verlos como **posiciones y direcciones**. Fue el nacimiento del álgebra moderna.

---

### 🛡️ 2. Definición y Características

Se denota con la letra $\mathbb{Z}$ y se define como el conjunto que incluye a los naturales, sus opuestos y el cero:

$$\mathbb{Z} = \{..., -3, -2, -1, 0, 1, 2, 3, ...\}$$

* **El Espejo Infinito:** A diferencia de $\mathbb{N}$ y $\mathbb{N}_0$, aquí **no hay un primer elemento**. Si caminas hacia la izquierda, nunca encontrarás una pared.
* **El Antecesor Universal:** En $\mathbb{Z}$, **absolutamente todos** los números tienen un antecesor y un sucesor. La estructura es perfectamente uniforme.
* **Componentes del Conjunto:**

$\mathbb{Z}^+$: Enteros positivos (igual a $\mathbb{N}$).

$\mathbb{Z}^-$: Enteros negativos.

$\{0\}$: El origen (ni positivo ni negativo).
""")

    fig, ax = plt.subplots(figsize=(12, 3))
    ax.axhline(0, color='black', lw=2)
    for x in range(-5, 6):
        color = 'blue' if x > 0 else ('red' if x < 0 else 'black')
        ax.plot(x, 0, 'o', color=color, markersize=8)
        ax.text(x, -0.4, str(x), ha='center', fontsize=12, fontweight='bold')
    ax.annotate('', xy=(3, 0.2), xytext=(0, 0.2), arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
    ax.text(1.5, 0.4, "|3| = 3", color='blue', ha='center', fontweight='bold')
    ax.annotate('', xy=(-3, 0.2), xytext=(0, 0.2), arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(-1.5, 0.4, "|-3| = 3", color='red', ha='center', fontweight='bold')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    plt.title("Simetría en los Enteros y Valor Absoluto", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown(r"""
---

### 🛡️ 3. Valor Absoluto ($|a|$): La Carpintería de la Distancia

El valor absoluto es el "limpiador de signos". Epistemológicamente, mide la **distancia** de un número al cero. Como las distancias físicas no pueden ser negativas (no puedes correr -5 kilómetros), el resultado del valor absoluto es siempre $\geq 0$.

**Definición Axiomática:**

$$|a| = \begin{cases} a & \text{si } a \ge 0 \\ -a & \text{si } a < 0 \end{cases}$$

> **Típ:** Ese signo "$-$" en la segunda parte de la fórmula es un operador de cambio. Dice: "Si el número es negativo, ponle otro menos adelante para que se vuelva positivo". No es que el resultado sea negativo.

**Propiedades de Mantenimiento:**
1. **Simetría:** $|a| = |-a|$. (La distancia del 5 y el -5 al origen es la misma).
2. **Multiplicativa:** $|a \cdot b| = |a| \cdot |b|$.

---

### 🛡️ 4. El Opuesto Aditivo

En este conjunto, cada número tiene un "némesis". Para todo $a$, existe un $-a$ tal que al encontrarse se anulan: $a + (-a) = 0$.

> **Típ:** En la PAES, cuando te pidan el "opuesto" o "inverso aditivo", solo debes cambiar el signo. No lo confundas con el inverso multiplicativo (dar vuelta la fracción), que requiere que el resultado sea 1, no 0.

---

### 🛡️ 5. Clausura: La Victoria de la Resta

¿Por qué nos mudamos de los Naturales a los Enteros? Por la **clausura de la sustracción**.

| Operación | ¿Es Cerrada en $\mathbb{Z}$? | Razón Técnica de Carpintería |
| :--- | :---: | :--- |
| **Adición (+)** | ✅ SÍ | Sumar deudas o fortunas siempre da un entero. |
| **Sustracción (-)** | ✅ SÍ | **Aquí está el premio.** $3 - 10 = -7$, y el -7 vive en $\mathbb{Z}$. |
| **Multiplicación ($\cdot$)** | ✅ SÍ | La regla de los signos mantiene el resultado en $\mathbb{Z}$. |
| **División (:)** | ❌ NO | $1 : 2$ sigue rompiendo el conjunto. |

---

> "Las matemáticas son el juez de lo que es posible; los números negativos son la prueba de que lo imposible es solo una dirección que aún no hemos tomado".
> — **Ada Lovelace**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería N04", expanded=False):
        st.markdown(r"""
### E01: Operativa de Signos y Clausura

**Situación:** Resolver la expresión $12 - (15 - 8)$ y determinar si el resultado pertenece a $\mathbb{Z}$.

**La Carpintería:**
1. **Resolver paréntesis:** $15 - 8 = 7$.
2. **Aplicar resta externa:** $12 - 7 = 5$.
3. **Verificar pertenencia:** El 5 es un entero positivo.
4. **Conclusión:** El resultado es un entero. La resta es cerrada en $\mathbb{Z}$ incluso cuando el resultado es positivo.

| Paso | Operación | Resultado | ¿Es Entero? |
| :--- | :--- | :---: | :---: |
| 1 | Paréntesis $(15 - 8)$ | 7 | ✅ SÍ |
| 2 | Resta final $(12 - 7)$ | 5 | ✅ SÍ |

---

### E02: El Valor Absoluto como Distancia

**Situación:** Calcular el valor de $A = |-10| + |3| - |-5|$.

**La Carpintería:**
1. **Evaluar $|-10|$:** La distancia de -10 al cero es 10.
2. **Evaluar $|3|$:** La distancia de 3 al cero es 3.
3. **Evaluar $|-5|$:** La distancia de -5 al cero es 5.
4. **Operar:** $10 + 3 - 5 = 8$.

| Término | Valor Absoluto | Resultado Numérico |
| :--- | :--- | :---: |
| $|-10|$ | Distancia de -10 al 0 | 10 |
| $|3|$ | Distancia de 3 al 0 | 3 |
| $|-5|$ | Distancia de -5 al 0 | 5 |
| **Total** | **$10 + 3 - 5$** | **8** |

---

### E03: La Definición Axiomática (La Trampa del $-a$)

**Situación:** Si $x = -8$, ¿cuál es el valor de $-x$ y de $|x|$?

**La Carpintería:**
1. **Calcular $-x$:** Es el opuesto de $x$. Como $x$ es $-8$, entonces $-(-8) = 8$.
2. **Calcular $|x|$:** Aplicamos la definición: "Si el número es negativo, el resultado es $-x$".
3. **Resultado:** $|-8| = -(-8) = 8$.
4. **Conclusión:** Ambos valores son iguales y positivos.

| Variable | Expresión | Proceso | Resultado |
| :--- | :--- | :--- | :---: |
| $x$ | Valor inicial | Dado | -8 |
| $-x$ | Opuesto | $-(-8)$ | 8 |
| $|x|$ | Valor Absoluto | Distancia al 0 | 8 |

---

### E04: Relación de Orden y Tricotomía

**Situación:** Dados $a = -15$ y $b = -10$, ¿cuál es la relación de orden correcta?

**La Carpintería:**
1. **Ubicación en la recta:** El -15 está más a la izquierda que el -10.
2. **Regla de negativos:** En los negativos, el que tiene mayor valor absoluto es el menor.
3. **Comparar:** $|-15| = 15$ y $|-10| = 10$. Como $15 > 10$, entonces $-15 < -10$.
4. **Resultado:** $a < b$.

| Número | Valor Absoluto | Posición en Recta | Relación |
| :--- | :---: | :--- | :---: |
| -15 | 15 | Más a la izquierda | **Menor** |
| -10 | 10 | Menos a la izquierda | **Mayor** |

---

### E05: El Opuesto del Valor Absoluto

**Situación:** Resolver la expresión $-| -12 + 4 |$.

**La Carpintería:**
1. **Operar dentro:** $-12 + 4 = -8$.
2. **Aplicar Valor Absoluto:** $|-8| = 8$.
3. **Aplicar signo exterior:** El signo "$-$" está fuera del valor absoluto, por lo que afecta al resultado final.
4. **Resultado:** $-8$.

| Paso | Operación | Resultado Parcial |
| :--- | :--- | :---: |
| 1 | Interior del $| \cdot |$ | -8 |
| 2 | Aplicar $|-8|$ | 8 |
| 3 | Aplicar "$-$" externo | **-8** |
""")

    with st.expander("❓ Cuestionario N04: Números Enteros", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el resultado de la operación $-5 - (-8)$?**

A) -13  
B) -3  
C) 3  
D) 13

---

**2. Si $x \in \mathbb{Z}^-$, ¿cuál de las siguientes afirmaciones es SIEMPRE verdadera respecto a $|x|$?**

A) $|x| = x$  
B) $|x| < 0$  
C) $|x| = -x$  
D) $|x| = 0$

---

**3. La distancia entre el número -7 y el número 5 en la recta numérica es:**

A) 2  
B) -2  
C) 12  
D) -12

---

**4. ¿Cuál de las siguientes frases define correctamente al conjunto de los números enteros?**

A) Es el conjunto de los naturales y el cero.  
B) Es la unión de los naturales, sus opuestos y el cero.  
C) Es un conjunto con un primer elemento definido.  
D) Es el conjunto donde la división es siempre cerrada.

---

**5. Si el opuesto de $a$ es 15, ¿cuál es el valor de $a$?**

A) 15  
B) 0  
C) -15  
D) $|-15|$

---

**6. ¿Cuál es el resultado de $-| -10 | + | -4 |$?**

A) 14  
B) 6  
C) -6  
D) -14

---

**7. Si $a < b$, donde $a$ y $b$ son enteros negativos, entonces se cumple que:**

A) $|a| < |b|$  
B) $|a| > |b|$  
C) $|a| = |b|$  
D) $a$ está a la derecha de $b$ en la recta.

---

**8. ¿Cuál de estas operaciones NO cumple la propiedad de clausura en $\mathbb{Z}$?**

A) Suma  
B) Resta  
C) Multiplicación  
D) División

---

**9. Si $n$ es un entero par, ¿cuál es el sucesor par de $n + 1$?**

A) $n + 2$  
B) $n + 3$  
C) $n$  
D) $n + 4$

---

**10. El valor absoluto de un número entero es:**

A) Siempre mayor que cero.  
B) Siempre menor que cero.  
C) Siempre no negativo.  
D) Siempre igual al número original.
""")

    with st.expander("🔑 Pauta Técnica N04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **C** | Aplicamos la regla de signos: $-5 - (-8) = -5 + 8$. Al tener signos distintos, restamos los valores absolutos ($8 - 5 = 3$) y conservamos el signo del mayor valor absoluto (+). |
| **2** | **C** | Esta es la definición axiomática. Si $x$ es negativo (por ejemplo $-5$), su valor absoluto es $-x$, es decir, $-(-5) = 5$. Esto garantiza que la distancia sea siempre positiva. |
| **3** | **C** | La distancia entre dos puntos $a$ y $b$ es $|a - b|$. Entonces: $|5 - (-7)| = |5 + 7| = |12| = 12$. Visualmente: 7 pasos al cero y 5 más hacia el positivo. |
| **4** | **B** | Definición estructural de $\mathbb{Z}$. A diferencia de los naturales, este conjunto requiere la simetría de los negativos y el elemento neutro (cero). |
| **5** | **C** | El opuesto o inverso aditivo es simplemente cambiar el signo. Si el resultado de ese cambio es 15, el número original debía ser $-15$. |
| **6** | **C** | ¡Cuidado con el signo exterior! Primero resolvemos el valor absoluto: $|-10| = 10$. Luego aplicamos el menos de afuera: $-10$. Finalmente: $-10 + 4 = -6$. |
| **7** | **B** | En la recta numérica, mientras más a la izquierda está un negativo, "menor" es. Pero al estar más lejos del cero, su **distancia** (valor absoluto) es mayor. Ejemplo: $-100 < -1$, pero $|-100| > |-1|$. |
| **8** | **D** | La división es la operación "rebelde". Al dividir $1 : 2$, el resultado ($0,5$) no pertenece al conjunto de los enteros, por lo que no hay clausura. |
| **9** | **A** | Si $n$ es par (ej: 4), $n+1$ es impar (5). El sucesor de 5 es 6, que se escribe como $4+2$, es decir, $n+2$. Los pares van de 2 en 2. |
| **10** | **C** | **Trampa conceptual:** Muchos dicen "siempre positivo", pero el valor absoluto de 0 es 0, y el 0 no es positivo. Por eso lo correcto es "no negativo" ($\geq 0$). |

---

> **Típ:** En la pregunta 6, el error más común es pensar que el menos de afuera se anula con el de adentro. El valor absoluto es como un paréntesis blindado: primero se resuelve lo de adentro y el signo de afuera espera su turno al final.
""")
