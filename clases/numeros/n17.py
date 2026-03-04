import streamlit as st


def render_N17():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("## N17: Potencias - El Motor del Crecimiento Exponencial")
        st.markdown("---")

        # Contexto histórico
        st.markdown("### 🏛️ Contexto Histórico: El Trigo de Sissa y la Arena de Arquímedes")
        st.markdown("""
    La necesidad de representar cantidades inmensas llevó a los antiguos a descubrir que la suma no era suficiente. En el siglo III a.C., **Arquímedes** escribió *El Contador de Arena*, donde diseñó un sistema de potencias para calcular cuántos granos de arena llenarían el universo, demostrando que incluso lo que parece infinito puede ser cuantificado.

    Esta fuerza multiplicadora se ilustra perfectamente en la **Leyenda de Sissa**. Al inventar el ajedrez, el sabio Sissa pidió al Rey de la India una recompensa en **granos de trigo**: un grano por el primer casillero ($2^0$), dos por el segundo ($2^1$), cuatro por el tercero ($2^2$), y así sucesivamente, duplicando la cantidad hasta completar los 64 cuadros.

    Lo que parecía una petición modesta resultó ser una trampa matemática. La suma total de los granos equivale a $2^{64} - 1$. Este \"menos uno\" surge de una propiedad de las progresiones: la suma de todas las potencias anteriores siempre es igual a la siguiente potencia menos una unidad (por ejemplo: $1 + 2 + 4 = 8 - 1$). El resultado final era una cifra que superaba con creces toda la producción mundial de trigo, demostrando que el crecimiento exponencial es, al principio, invisible, pero finalmente explosivo.
        """)
        st.markdown("---")

        # Definición
        st.markdown("""
    <div style="background-color: #E8F5E9; border-left: 8px solid #2E7D32; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1B5E20; margin-top: 0;">¿Qué es una Potencia?</h2>
        Es una forma abreviada de escribir una multiplicación de un mismo factor (base) una cantidad determinada de veces (exponente).
        $$a^n = a \\cdot a \\cdot a \\cdot ... \\cdot a$$ en este caso n veces.
    </div>
    """, unsafe_allow_html=True)

        st.markdown("### 🛡️ Las 3 Reglas de Oro de los Signos")
        st.markdown("""
    Para no morir en la PAES por un signo:
    1. **Base positiva:** El resultado es **SIEMPRE positivo**.
    2. **Base negativa con exponente PAR:** El resultado es **Positivo**.  
       *Ej: $(-2)^2 = (-2) \\cdot (-2) = 4$*
    3. **Base negativa con exponente IMPAR:** El resultado es **Negativo**.  
       *Ej: $(-2)^3 = (-2) \\cdot (-2) \\cdot (-2) = -8$*
        """)
        st.markdown("---")
        st.markdown("""
    **⚠️ Típ:** No es lo mismo $(-3)^2$ que $-3^2$.
    - $(-3)^2 = 9$ (El paréntesis incluye al signo en la multiplicación).
    - $-3^2 = -9$ (El signo menos está afuera, solo el 3 se eleva al cuadrado).
        """)
        st.markdown("---")

        st.markdown("### 🛡️ Propiedades de las Potencias (Indispensables)")
        st.markdown("""
    | Operación | Propiedad | Ejemplo |
    | :--- | :--- | :--- |
    | **Multiplicación (Igual Base)** | Se mantiene la base y **suman** exponentes. | $2^3 \\cdot 2^4 = 2^7$ |
    | **División (Igual Base)** | Se mantiene la base y **restan** exponentes. | $5^6 : 5^2 = 5^4$ |
    | **Multiplicación (Igual Exponente)** | Se multiplican las bases, mantiene exponente. | $2^3 \\cdot 5^3 = 10^3$ |
    | **División (Igual Exponente)** | Se dividen las bases, mantiene exponente. | $10^4 : 2^4 = 5^4$ |
    | **Potencia de una Potencia** | Se mantiene la base y **multiplican** exponentes. | $(3^2)^4 = 3^8$ |
        """)
        st.markdown("---")

        st.markdown("### 🛡️ El Exponente Especial")
        st.markdown("""
    1. **Exponente Cero:** Todo número (distinto de cero) elevado a 0 es **1**. ($a^0 = 1$).
    2. **Exponente Negativo:** ¡El número se invierte! Es el \"ascensor\" de las matemáticas.
       - $a^{-n} = \\left(\\dfrac{1}{a}\\right)^n$
       - $\\left(\\dfrac{a}{b}\\right)^{-n} = \\left(\\dfrac{b}{a}\\right)^n$

    > **Típ:** El exponente negativo es como un ticket de vuelta: da vuelta la fracción y el exponente se vuelve positivo. Si ves un signo menos arriba, solo \"gira la tortilla\".
        """)
        st.markdown("---")

        # Guía de ejemplos

    with st.expander("📝 Guía de Ejemplos: Paso a Paso de Potencias"):
        st.markdown("""
**E01. Multiplicación de igual base.** $3^2 \\cdot 3^1 \\cdot 3^4$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mantener base y sumar exponentes | $3^{(2+1+4)}$ |
| 2 | Resultado final | $3^7$ |

**E02. División de igual base.** $5^8 : 5^5$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mantener base y restar exponentes | $5^{(8-5)}$ |
| 2 | Resultado final | $5^3 = 125$ |

**E03. Multiplicación de bases distintas, igual exponente.** $2^4 \\cdot 3^4$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar las bases | $(2 \\cdot 3)^4$ |
| 2 | Resultado final | $6^4$ |

**E04. División de bases distintas, igual exponente.** $20^3 : 5^3$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Dividir las bases | $(20 : 5)^3$ |
| 2 | Resultado final | $4^3 = 64$ |

**E05. Potencia de una potencia.** $(10^2)^3$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mantener base y multiplicar exponentes | $10^{(2 \\cdot 3)}$ |
| 2 | Resultado final | $10^6$ |

**E06. Exponente cero.** $(-567)^0$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Aplicar propiedad de exponente cero | $1$ |

**E07. Exponente negativo (Entero).** $2^{-3}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir la base (el \"ascensor\") | $(1/2)^3$ |
| 2 | Elevar al cubo | $1/8$ |

**E08. Exponente negativo (Fracción).** $(2/5)^{-2}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | \"Girar la tortilla\" (Invertir fracción) | $(5/2)^2$ |
| 2 | Elevar ambos términos al cuadrado | $25/4$ |

**E09. Base negativa y exponente par.** $(-3)^4$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar que exponente par elimina el menos | $3^4$ |
| 2 | Resultado final | $81$ |

**E10. Prioridad de operaciones con potencias.** $2 \\cdot 3^2$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Resolver primero la potencia | $2 \\cdot 9$ |
| 2 | Multiplicar | $18$ |
        """)

    # Cuestionario
    with st.expander("❓ Cuestionario N17", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿Cuál es el resultado de $(-5)^2$?', 'options': {'A': '$-25$', 'B': '$25$', 'C': '$10$', 'D': '$-10$'}, 'answer': 'B', 'explanation': 'Al estar entre paréntesis, el signo se multiplica por sí mismo: $(-5) \\cdot (-5) = 25$.'},
            {'question': 'El valor de la expresión $-3^2$ es:', 'options': {'A': '$9$', 'B': '$-9$', 'C': '$6$', 'D': '$-6$'}, 'answer': 'B', 'explanation': 'El signo no está afectado por el exponente, solo el 3: $-(3 \\cdot 3) = -9$.'},
            {'question': '¿Qué expresión es equivalente a $4^2 \\cdot 4^5$?', 'options': {'A': '$4^{10}$', 'B': '$16^7$', 'C': '$4^7$', 'D': '$16^{10}$'}, 'answer': 'C', 'explanation': 'En multiplicación de igual base, se conserva la base y se suman los exponentes ($2+5=7$).'},
            {'question': 'Al simplificar $(2^3)^2$ se obtiene:', 'options': {'A': '$2^5$', 'B': '$2^6$', 'C': '$2^9$', 'D': '$4^6$'}, 'answer': 'B', 'explanation': 'Potencia de una potencia, se deben multiplicar los exponentes ($3 \\cdot 2 = 6$).'},
            {'question': 'El valor de $10^{-2}$ es:', 'options': {'A': '$-100$', 'B': '$0{,}01$', 'C': '$0{,}1$', 'D': '$-0{,}01$'}, 'answer': 'B', 'explanation': 'El exponente negativo invierte la base: $10^{-2} = 1/10^2 = 1/100 = 0{,}01$.'},
            {'question': '¿Cuál es el resultado de $12^0$ (con base distinta de cero)?', 'options': {'A': '$0$', 'B': '$12$', 'C': '$1$', 'D': 'No está definido'}, 'answer': 'C', 'explanation': 'Todo número distinto de cero elevado a cero es siempre igual a 1 por definición.'},
            {'question': 'Si $a = -2$, ¿cuál es el valor de $a^3$?', 'options': {'A': '$8$', 'B': '$-8$', 'C': '$6$', 'D': '$-6$'}, 'answer': 'B', 'explanation': '$(-2)^3 = (-2) \\cdot (-2) \\cdot (-2) = -8$. Base negativa con exponente impar da resultado negativo.'},
            {'question': '¿Qué expresión es equivalente a $3^4 : 3^2$?', 'options': {'A': '$3^2$', 'B': '$1^2$', 'C': '$3^6$', 'D': '$3^8$'}, 'answer': 'A', 'explanation': 'En división de igual base, se conserva la base y se restan los exponentes ($4-2=2$).'},
            {'question': 'El valor de la fracción $(1/2)^{-1}$ es:', 'options': {'A': '$1/2$', 'B': '$-1/2$', 'C': '$2$', 'D': '$1$'}, 'answer': 'C', 'explanation': 'El exponente $-1$ invierte la fracción: $1/2$ se transforma en $2/1 = 2$.'},
            {'question': 'Si sumamos $2^3 + 2^3$, el resultado es:', 'options': {'A': '$2^4$', 'B': '$2^6$', 'C': '$2^9$', 'D': '$4^3$'}, 'answer': 'A', 'explanation': 'Sumar $2^3 + 2^3$ es equivalente a tener dos veces $2^3$, es decir, $2^1 \\cdot 2^3$. Al sumar los exponentes, resulta $2^4$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n17_quiz")

    # Pauta


    st.markdown("---")
    st.markdown("> *\"En el crecimiento exponencial, el comienzo es casi imperceptible, pero el final es una explosión.\"*  \n> — **Adaptación de conceptos de Carl Sagan**")
