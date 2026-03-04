import streamlit as st


def render_N08():
    with st.expander("📚 Teoría", expanded=False):
        st.title("N08: La Arquitectura de los Números - Primos y Divisibilidad")

        st.markdown(r"""
    ### 🏛️ 1. Contexto Histórico: Los Átomos de Grecia
    Hace más de 2.300 años, en la Antigua Grecia, **Euclides** ya sabía que los números no eran todos iguales. Él se dio cuenta de que algunos números eran "básicos" (no se podían desarmar) y otros eran "construcciones".

    Euclides demostró que **existen infinitos números primos**. No importa qué tan grande sea el número que encuentres, siempre habrá un primo más grande. En la actualidad, estos números son la base de la **Criptografía**: cada vez que haces una transferencia bancaria o mandas un mensaje por WhatsApp, hay números primos gigantes protegiendo tus datos. Si puedes desarmar un número en sus primos, tienes la llave del candado.

    ---

    ### 🛡️ 8.1 Los Ladrillos del Universo: Números Primos
    Un número natural se considera **Primo** si y solo si tiene **exactamente dos divisores**: el 1 y sí mismo.

    ### 🛡️ 8.2 Clasificación de los Naturales
    Para no perderse en la batalla, el alumno debe clasificar los números según cuántos divisores tienen:

    1. **El Uno (1):** Es el "paria". No es primo ni compuesto, porque solo tiene **un divisor** (él mismo).
    2. **Números Primos:** Tienen exactamente **dos divisores**.
       * **Lista Sagrada (Memoria Obligatoria):** $\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, ...\}$
       * **El Gran 2:** Es el único primo par. Todos los demás son impares (pero ojo, no todos los impares son primos).
    3. **Números Compuestos:** Tienen **más de dos divisores**. Se pueden "desarmar".

    ### 🛡️ 8.3 El "Club Exclusivo": ¿Quiénes quedan fuera?
    Es vital entender por qué ciertos candidatos no califican como primos bajo el rigor matemático:

    * **¿Por qué el 0 no es primo?** Tiene infinitos divisores y no entra en la categoría de "átomo".
    * **¿Por qué el 1 no es primo?** Solo tiene un divisor. Si lo aceptáramos, la descomposición de los números dejaría de ser única.
    * **¿Por qué un decimal (como 2,5) no es primo?** Los primos son ladrillos enteros. Un decimal ya está fragmentado; en su mundo, todo es divisible por todo y no existen bloques básicos.

    | Candidato | ¿Es Primo? | Razón de la "Expulsión" |
    | :--- | :---: | :--- |
    | **0** | ❌ No | Infinitos divisores. |
    | **1** | ❌ No | Solo 1 divisor. |
    | **2,5** | ❌ No | No es un número entero. |

    ---

    ### 🛡️ 8.4 Teorema Fundamental de la Aritmética
    Este es el corazón de la operatoria. Dice que todo número compuesto se puede expresar de forma **única** como un producto de números primos. Es la "huella dactilar" o el ADN del número.

    * **Ejemplo:** $60 = 2^2 \cdot 3 \cdot 5$.
    * No importa cómo empieces a desarmar el 60, al final siempre llegarás a dos "2", un "3" y un "5".

    ### 🛡️ 8.5 Criterios de Divisibilidad (Velocidad de Combate)
    Para ganar tiempo en la PAES, hay que saber por quién "atacar" un número sin hacer la división:

    * **Por 2:** El número termina en 0 o cifra par ($2, 4, 6, 8$).
    * **Por 3:** La **suma de sus dígitos** es un múltiplo de 3. (Ej: 123 $\rightarrow 1+2+3=6$, ¡sirve!).
    * **Por 4:** Sus últimas dos cifras son ceros o un múltiplo de 4.
    * **Por 5:** Termina en 0 o en 5.
    * **Por 6:** Cumple la regla del 2 y del 3 al mismo tiempo.
    * **Por 9:** La suma de sus dígitos es múltiplo de 9.

    ---

    ### 🛡️ 8.6 Algoritmos de Búsqueda: mcm y MCD
    Aquí se decide quién saca los 1000 puntos. La clave es la **intuición** detrás de la herramienta:

    * **MCD (Máximo Común Divisor): "Fragmentar"**. Se usa cuando necesitas **repartir, cortar o dividir** objetos de distintos tamaños en trozos que sean iguales y lo más grandes posibles.
    * **mcm (Mínimo Común Múltiplo): "Sincronizar"**. Se usa para calcular cuándo volverán a **coincidir, encontrarse o repetirse** eventos que tienen frecuencias diferentes.

    | Herramienta | Acción Mental | ¿Cómo se calcula? |
    | :--- | :--- | :--- |
    | **MCD** | **Achicar** (Repartir) | Factores primos **comunes** con su **menor** exponente. |
    | **mcm** | **Agrandar** (Coincidir) | **Todos** los factores primos con su **mayor** exponente. |

    ---

    > **Típ:** El número **91** es la trampa favorita de la PAES. Parece primo, pero es $7 \times 13$. Apréndetelo para que no te pillen. Que se memorice los primos hasta el 23 como si fueran su RUT.

    ---

    > "Los números primos son los ladrillos con los que la naturaleza construye los números; entenderlos es entender la música de las esferas".
    > — **Adaptación de Marcus du Sautoy**
    """)


    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería N08", expanded=False):
        st.markdown(r"""
### E02: Descomposición y el "ADN" Numérico
**Situación:** Encontrar la descomposición en factores primos del número 360.

**La Carpintería:**
1. **Analizar:** El número termina en 0, es par. Empezamos con el primo menor (2).
2. **Iterar:** Dividimos sucesivamente hasta llegar a la unidad.
3. **Sintetizar:** Expresamos los factores como potencias.

| Dividendo | Divisor Primo | Resultado |
| :--- | :---: | :--- |
| 360 | 2 | 180 |
| 180 | 2 | 90 |
| 90 | 2 | 45 |
| 45 | 3 | 15 |
| 15 | 3 | 5 |
| 5 | 5 | 1 |

**Resultado:** $360 = 2^3 \cdot 3^2 \cdot 5^1$

---

### E03: Aplicando el MCD (El Gran Repartidor)
**Situación:** Un carpintero tiene dos tablones de madera de 120 cm y 180 cm. Quiere cortarlos en trozos iguales, lo más largos posibles y sin que sobre madera. ¿Cuánto debe medir cada trozo?

**La Carpintería:**
1. **Identificar:** Como pide "cortar" y "el más largo posible", usamos **MCD**.
2. **Descomponer:** * $120 = 2^3 \cdot 3 \cdot 5$
   * $180 = 2^2 \cdot 3^2 \cdot 5$
3. **Regla de Oro:** Factores comunes con su **menor** exponente.
   * $2^2$, $3^1$ y $5^1$.

| Factores | 120 | 180 | MCD (Comunes menores) |
| :--- | :---: | :---: | :--- |
| ADN | $2^3 \cdot 3 \cdot 5$ | $2^2 \cdot 3^2 \cdot 5$ | $2^2 \cdot 3 \cdot 5 = 60$ |

**Respuesta:** Cada trozo debe medir 60 cm.

---

### E04: Aplicando el mcm (El Gran Sincronizador)
**Situación:** En un faro, una luz parpadea cada 15 segundos y otra cada 20 segundos. Si acaban de coincidir, ¿en cuántos segundos volverán a brillar juntas?

**La Carpintería:**
1. **Identificar:** Como pide "volver a coincidir", usamos **mcm**.
2. **Descomponer:**
   * $15 = 3 \cdot 5$
   * $20 = 2^2 \cdot 5$
3. **Regla de Oro:** Todos los factores con su **mayor** exponente.
   * $2^2$, $3^1$ y $5^1$.

| Factores | 15 | 20 | mcm (Todos los mayores) |
| :--- | :---: | :---: | :--- |
| ADN | $3 \cdot 5$ | $2^2 \cdot 5$ | $2^2 \cdot 3 \cdot 5 = 60$ |

**Respuesta:** Volverán a coincidir en 60 segundos.

---

### E05: Criterios de Divisibilidad "Flash"
**Situación:** Sin dividir, determinar si 5.424 es divisible por 4 y por 6.

**La Carpintería:**
1. **Prueba del 4:** Observar las últimas dos cifras: **24**. Como $24 = 4 \cdot 6$, sí es divisible.
2. **Prueba del 6:** Debe ser divisible por 2 y 3.
   * Por 2: Termina en 4 (par). ✅
   * Por 3: $5+4+2+4 = 15$. Como 15 es múltiplo de 3, ✅.

| Divisor | Razón | ¿Es divisible? |
| :--- | :--- | :---: |
| **4** | Últimas dos cifras (24) son múltiplo de 4. | ✅ |
| **6** | Es par y la suma de cifras (15) es múltiplo de 3. | ✅ |

---

### E06: Clasificación Express
**Situación:** Determinar si los números 1 y 91 son primos o compuestos.

**La Carpintería:**
* **Caso 1:** El número **1** solo tiene un divisor. Por definición, no es primo ni compuesto.
* **Caso 2:** El número **91**. Probamos criterios: No es par, la suma de cifras es 10 (no es divisible por 3), no termina en 0 o 5. Pero al probar con el 7: $91 \div 7 = 13$.

| Número | Divisores | Clasificación |
| :--- | :---: | :--- |
| **1** | {1} | Ninguno |
| **91** | {1, 7, 13, 91} | Compuesto |
""")

    with st.expander("❓ Cuestionario N08", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿Cuál de los siguientes números es el único número primo que es par?**\n\\', 'options': {'A': '0', 'B': '1', 'C': '2', 'D': '4'}, 'answer': 'C', 'explanation': 'Por definición, el 2 es el único par con solo dos divisores.'},
            {'question': '¿Cuál es la descomposición en factores primos del número 84?**\n\\', 'options': {'A': '$2 \\cdot 3 \\cdot 14$', 'B': '$2^2 \\cdot 3 \\cdot 7$', 'C': '$2^3 \\cdot 3 \\cdot 7$', 'D': '$4 \\cdot 3 \\cdot 7$'}, 'answer': 'B', 'explanation': '$84 \\div 2 = 42 \\rightarrow 42 \\div 2 = 21 \\rightarrow 21 \\div 3 = 7 \\rightarrow 7 \\div 7 = 1$.'},
            {'question': 'Respecto al número 1, es CORRECTO afirmar que:**\n\\', 'options': {'A': 'Es el número primo más pequeño.', 'B': 'Es un número compuesto.', 'C': 'No es primo ni compuesto.', 'D': 'Es un número irracional.'}, 'answer': 'C', 'explanation': 'El 1 solo tiene un divisor, por lo que no cumple la definición de primo (2 divisores) ni de compuesto (+2).'},
            {'question': '¿Cuál es el Máximo Común Divisor (MCD) entre 48 y 72?**\n\\', 'options': {'A': '12', 'B': '24', 'C': '48', 'D': '144'}, 'answer': 'B', 'explanation': '$48 = 2^4 \\cdot 3$; $72 = 2^3 \\cdot 3^2$. Comunes menores: $2^3 \\cdot 3 = 24$.'},
            {'question': 'Si dos campanas suenan cada 8 y 12 minutos respectivamente, ¿cada cuántos minutos volverán a sonar al mismo tiempo?**\n\\', 'options': {'A': '4 minutos.', 'B': '12 minutos.', 'C': '24 minutos.', 'D': '96 minutos.'}, 'answer': 'C', 'explanation': 'mcm(8, 12). $8 = 2^3$; $12 = 2^2 \\cdot 3$. Mayores: $2^3 \\cdot 3 = 24$.'},
            {'question': 'El número 1.233 es divisible por:**\n\\', 'options': {'A': '2', 'B': '5', 'C': '9', 'D': '10'}, 'answer': 'C', 'explanation': 'Suma de cifras: $1+2+3+3 = 9$. Como la suma es 9, es divisible por 9.'},
            {'question': '¿Cuál de los siguientes números es primo?**\n\\', 'options': {'A': '51', 'B': '87', 'C': '91', 'D': '97'}, 'answer': 'D', 'explanation': '$51=3 \\cdot 17$; $87=3 \\cdot 29$; $91=7 \\cdot 13$. 97 no tiene divisores aparte del 1 y sí mismo.'},
            {'question': 'El MCD de dos números primos distintos entre sí es siempre:**\n\\', 'options': {'A': 'El producto de ambos.', 'B': '1', 'C': '0', 'D': 'El menor de ellos.'}, 'answer': 'B', 'explanation': 'Los números primos no comparten factores entre sí más que el 1 (son primos entre sí).'},
            {'question': 'Para que el número $4.2X2$ sea divisible por 3, ¿qué valor NO puede tomar $X$?**\n\\', 'options': {'A': '1', 'B': '4', 'C': '7', 'D': '2'}, 'answer': 'D', 'explanation': 'Suma: $4+2+X+2 = 8+X$. Si $X=2$, suma=10 (no divisible por 3).'},
            {'question': 'Si un número es divisible por 2 y por 3 simultáneamente, entonces es divisible por:**\n\\', 'options': {'A': '5', 'B': '6', 'C': '9', 'D': '12'}, 'answer': 'B', 'explanation': 'Es el criterio de divisibilidad del 6.'},
            {'question': 'Un satélite pasa sobre Chile cada 15 días y otro cada 20 días. ¿En cuántos días más volverán a pasar ambos al mismo tiempo?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'A', 'explanation': '**Sincronizar:** Buscamos un punto común en el futuro.'},
            {'question': 'Se quieren armar bolsas de regalo con 30 dulces y 45 chocolates, de modo que todas las bolsas tengan la misma cantidad de cada producto y esta sea la máxima posible.', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'B', 'explanation': '**Repartir:** Buscamos la mayor agrupación común.'},
            {'question': 'Tengo tres cintas de 12, 18 y 24 metros. Necesito cortarlas en trozos iguales de la mayor longitud posible sin desperdiciar nada.', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'B', 'explanation': '**Fragmentar:** Cortar en trozos máximos iguales.'},
            {'question': 'Tres campanas suenan con intervalos de 2, 3 y 4 minutos respectivamente. Si suenan juntas a las 12:00, ¿a qué hora vuelven a sonar juntas?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'A', 'explanation': '**Ciclos:** Repetición de eventos periódicos.'},
            {'question': 'Un número $x$ es el mayor número que divide exactamente a 100 y a 150. ¿Qué herramienta define a $x$?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'B', 'explanation': '**Divisor:** Literalmente pide el número mayor que divide.'},
            {'question': 'Un médico receta a un paciente una pastilla cada 6 horas y un jarabe cada 8 horas. ¿Cada cuántas horas debe tomar ambos medicamentos juntos?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'A', 'explanation': '**Coincidencia:** Encuentro de dos frecuencias distintas.'},
            {'question': 'Se desea embaldosar un patio de 400 cm de largo por 300 cm de ancho con baldosas cuadradas lo más grandes posibles, sin cortarlas. ¿De qué tamaño debe ser el lado de cada baldosa?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'B', 'explanation': '**Fragmentar:** Dividir el área en cuadrados iguales máximos.'},
            {'question': 'Dos luces de Navidad parpadean: una cada 4 segundos y la otra cada 10 segundos. Si coinciden ahora, ¿cuántas veces volverán a coincidir en un minuto?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'A', 'explanation': '**Sincronizar:** Buscar el primer múltiplo común de los parpadeos.'},
            {'question': 'Se tienen 60 litros de jugo de naranja y 84 litros de jugo de piña. Se quiere envasar en bidones de igual capacidad máxima. ¿Cuál es la capacidad de cada bidón?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'B', 'explanation': '**Repartir:** Capacidad máxima para dividir ambos volúmenes.'},
            {'question': 'Tres corredores parten juntos en una pista circular. El primero tarda 10 min en dar una vuelta, el segundo 12 min y el tercero 15 min. ¿En cuánto tiempo se encontrarán nuevamente en el punto de partida?', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': '—', 'D': '—'}, 'answer': 'A', 'explanation': '**Coincidencia:** Punto de encuentro de velocidades diferentes.'},
            {'question': 'Si un problema pregunta por el momento en que tres luces vuelven a parpadear juntas, ¿qué debes calcular?**\n\\', 'options': {'A': 'Máximo Común Divisor (MCD)', 'B': 'Mínimo Común Múltiplo (mcm)', 'C': 'La suma de los tiempos.', 'D': 'El promedio de los intervalos.'}, 'answer': 'B', 'explanation': '**Coincidencia:** Los eventos periódicos se encuentran en el futuro (mcm).'},
            {'question': 'Si necesitas dividir dos cordeles en trozos iguales de la mayor longitud posible, ¿qué herramienta es la correcta?**\n\\', 'options': {'A': 'Mínimo Común Múltiplo (mcm)', 'B': 'Máximo Común Divisor (MCD)', 'C': 'Descomposición en factores primos.', 'D': 'Multiplicación de las longitudes.'}, 'answer': 'B', 'explanation': '**Fragmentar:** Dividir en los trozos más grandes posibles (MCD).'},
            {'question': '¿Cuál de estos números NO es primo?**\n\\', 'options': {'A': '2', 'B': '13', 'C': '51', 'D': '97'}, 'answer': 'C', 'explanation': '**Trampa:** $5+1=6$ (múltiplo de 3). Por tanto, $51 = 17 \\cdot 3$.'},
            {'question': 'El MCD de dos números que no comparten ningún factor primo (aparte del 1) es:**\n\\', 'options': {'A': '0', 'B': '1', 'C': 'El producto de ambos.', 'D': 'No existe.'}, 'answer': 'B', 'explanation': 'Se llaman **coprimos**. Su único divisor común es la unidad.'},
            {'question': '¿Qué sucede con el mcm de dos números si uno es múltiplo del otro?**\n\\', 'options': {'A': 'El mcm es el número menor.', 'B': 'El mcm es el número mayor.', 'C': 'El mcm es 1.', 'D': 'El mcm es el producto de ambos.'}, 'answer': 'B', 'explanation': 'Si uno contiene al otro, el múltiplo más pequeño que los contiene es el mayor.'},
            {'question': 'Para simplificar la fracción $\\frac{120}{180}$ de un solo golpe a su forma irreductible, conviene dividir numerador y denominador por su:**\n\\', 'options': {'A': 'mcm', 'B': 'MCD', 'C': 'Suma', 'D': 'Producto'}, 'answer': 'B', 'explanation': 'El **MCD** es el divisor más grande, simplifica la fracción al máximo.'},
            {'question': 'Si la descomposición de $A$ es $2^3 \\cdot 5$ y la de $B$ es $2^2 \\cdot 3 \\cdot 5$, el MCD entre ellos es:**\n\\', 'options': {'A': '$2^2 \\cdot 5$', 'B': '$2^3 \\cdot 3 \\cdot 5$', 'C': '$2 \\cdot 5$', 'D': '2'}, 'answer': 'A', 'explanation': 'Regla MCD: Factores **comunes** ($2$ y $5$) con su **menor** exponente ($2^2$ y $5^1$).'},
            {'question': 'La frase "máxima cantidad de grupos iguales sin que sobre nada" es una señal de:**\n\\', 'options': {'A': 'mcm', 'B': 'MCD', 'C': 'Valor Absoluto', 'D': 'División Euclidiana'}, 'answer': 'B', 'explanation': 'Palabras clave para la aplicación del Máximo Común Divisor.'},
            {'question': '¿Cuál es el único número primo que es par?**\n\\', 'options': {'A': '0', 'B': '1', 'C': '2', 'D': '4'}, 'answer': 'C', 'explanation': 'Dato sagrado. El 2 es el primer primo y el único par.'},
            {'question': 'Si el mcm de dos números es 12, ¿cuál de estos NO puede ser uno de esos números?**\n\\', 'options': {'A': '4', 'B': '6', 'C': '8', 'D': '3'}, 'answer': 'C', 'explanation': '12 **no es múltiplo** de 8. El mcm siempre es divisible por los números originales.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n08_quiz")

    with st.expander("🔑 Pauta Técnica N08", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | Por definición, el 2 es el único par con solo dos divisores. |
| **2** | **B** | $84 \div 2 = 42 \rightarrow 42 \div 2 = 21 \rightarrow 21 \div 3 = 7 \rightarrow 7 \div 7 = 1$. |
| **3** | **C** | El 1 solo tiene un divisor, por lo que no cumple la definición de primo (2 divisores) ni de compuesto (+2). |
| **4** | **B** | $48 = 2^4 \cdot 3$; $72 = 2^3 \cdot 3^2$. Comunes menores: $2^3 \cdot 3 = 24$. |
| **5** | **C** | mcm(8, 12). $8 = 2^3$; $12 = 2^2 \cdot 3$. Mayores: $2^3 \cdot 3 = 24$. |
| **6** | **C** | Suma de cifras: $1+2+3+3 = 9$. Como la suma es 9, es divisible por 9. |
| **7** | **D** | $51=3 \cdot 17$; $87=3 \cdot 29$; $91=7 \cdot 13$. 97 no tiene divisores aparte del 1 y sí mismo. |
| **8** | **B** | Los números primos no comparten factores entre sí más que el 1 (son primos entre sí). |
| **9** | **D** | Suma: $4+2+X+2 = 8+X$. Si $X=2$, suma=10 (no divisible por 3). |
| **10** | **B** | Es el criterio de divisibilidad del 6. |

---

> "Dios no juega a los dados".
> — **Albert Einstein**
""")



    with st.expander("🔑 Pauta Técnica N08.B: Control de Estrategia", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Logística (La Razón) |
| :--- | :---: | :--- |
| **1** | **A** | **Sincronizar:** Buscamos un punto común en el futuro. |
| **2** | **B** | **Repartir:** Buscamos la mayor agrupación común. |
| **3** | **B** | **Fragmentar:** Cortar en trozos máximos iguales. |
| **4** | **A** | **Ciclos:** Repetición de eventos periódicos. |
| **5** | **B** | **Divisor:** Literalmente pide el número mayor que divide. |
| **6** | **A** | **Coincidencia:** Encuentro de dos frecuencias distintas. |
| **7** | **B** | **Fragmentar:** Dividir el área en cuadrados iguales máximos. |
| **8** | **A** | **Sincronizar:** Buscar el primer múltiplo común de los parpadeos. |
| **9** | **B** | **Repartir:** Capacidad máxima para dividir ambos volúmenes. |
| **10** | **A** | **Coincidencia:** Punto de encuentro de velocidades diferentes. |

---

> **Típ:** Si el problema te pide "cortar", "repartir" o "bidones/baldosas/bolsas", saca el **MCD**. Si te pide "volver a sonar", "volver a pasar" o "coincidir", saca el **mcm**.
""")



    with st.expander("🔑 Pauta Técnica N08.C: Control de Divisibilidad", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | **Coincidencia:** Los eventos periódicos se encuentran en el futuro (mcm). |
| **2** | **B** | **Fragmentar:** Dividir en los trozos más grandes posibles (MCD). |
| **3** | **C** | **Trampa:** $5+1=6$ (múltiplo de 3). Por tanto, $51 = 17 \cdot 3$. |
| **4** | **B** | Se llaman **coprimos**. Su único divisor común es la unidad. |
| **5** | **B** | Si uno contiene al otro, el múltiplo más pequeño que los contiene es el mayor. |
| **6** | **B** | El **MCD** es el divisor más grande, simplifica la fracción al máximo. |
| **7** | **A** | Regla MCD: Factores **comunes** ($2$ y $5$) con su **menor** exponente ($2^2$ y $5^1$). |
| **8** | **B** | Palabras clave para la aplicación del Máximo Común Divisor. |
| **9** | **C** | Dato sagrado. El 2 es el primer primo y el único par. |
| **10** | **C** | 12 **no es múltiplo** de 8. El mcm siempre es divisible por los números originales. |

---

> **Típ:** Si fallaste en la 7, recuerda la regla: el MCD es "egoísta" (solo lo común y poquito), el mcm es "ambicioso" (todo y mucho).
""")
