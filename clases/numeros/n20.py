import streamlit as st


def render_N20():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("## N20: Raíces - Potencias con Exponente Fraccionario")
        st.markdown("---")

        st.markdown("### 🏛️ Contexto Histórico: El Secreto de los Pitagóricos")
        st.markdown("""
    Para los antiguos griegos, el universo era orden y números enteros. Sin embargo, cuando intentaron calcular la diagonal de un cuadrado de lado 1, se toparon con $\\sqrt{2}$. La leyenda cuenta que Hipaso de Metaponto reveló que este número no podía escribirse como fracción (era irracional), rompiendo la armonía sagrada de los Pitagóricos. Se dice que lo lanzaron por la borda de un barco para que el secreto de las raíces no destruyera su filosofía. Hoy, las raíces no son un secreto mortal, sino la herramienta base para entender la geometría y el crecimiento en la naturaleza.
        """)
        st.markdown("---")

        st.markdown("""
    <div style="background-color: #E8F5E9; border-left: 8px solid #2E7D32; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1B5E20; margin-top: 0;">¿Qué es una Raíz?</h2>
        La raíz enésima de un número es la operación inversa a la potencia. Buscamos un número que elevado al índice ($n$) nos dé la cantidad subradical ($a$).
        $$\\sqrt[n]{a} = b \\iff b^n = a$$
    </div>
    """, unsafe_allow_html=True)

        st.markdown("### 🛡️ El Puente Sagrado: Raíz a Potencia")
        st.markdown("""
    Esta es la clave para resolver el 90% de los ejercicios. Cualquier raíz se puede escribir como una potencia donde el exponente es una fracción:
    $$\\sqrt[n]{a^m} = a^{\\frac{m}{n}}$$

    **Típ:** El que está **adentro** va **arriba** (numerador) y el que está **afuera** (índice) va **abajo** (denominador).
        """)
        st.markdown("---")

        st.markdown("### 🛡️ Propiedades de las Raíces")
        st.markdown("""
    | Propiedad | Definición | Ejemplo |
    | :--- | :--- | :--- |
    | **Multiplicación (Igual Índice)** | Se multiplican las cantidades subradicales. | $\\sqrt{2} \\cdot \\sqrt{8} = \\sqrt{16} = 4$ |
    | **División (Igual Índice)** | Se dividen las cantidades subradicales. | $\\sqrt{18} : \\sqrt{2} = \\sqrt{9} = 3$ |
    | **Raíz de una Raíz** | Se multiplican los índices. | $\\sqrt[3]{\\sqrt{2}} = \\sqrt[6]{2}$ |
    | **Potencia de una Raíz** | El exponente entra a la base. | $(\\sqrt[3]{5})^2 = \\sqrt[3]{5^2}$ |
        """)

        st.markdown("### 🛡️ Introducción de un factor bajo la raíz")
        st.markdown("""
    Para meter un número dentro de una raíz, entra elevado al índice:
    $$b \\cdot \\sqrt[n]{a} = \\sqrt[n]{b^n \\cdot a}$$
    - **Ejemplo:** $2 \\cdot \\sqrt{3} = \\sqrt{2^2 \\cdot 3} = \\sqrt{12}$

    **Típ:** Las raíces solo se pueden sumar o restar si tienen el mismo índice y la misma cantidad subradical. No puedes sumar $\\sqrt{2} + \\sqrt{3}$ y decir que es $\\sqrt{5}$. Eso es traición a la patria matemática.
        """)
        st.markdown("---")


    with st.expander("📝 Guía de Ejemplos: Dominando Radicales"):
        st.markdown("""
**1. De Raíz a Potencia.** Escribir $\\sqrt[5]{x^3}$ como potencia.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar exponente interior ($m$) e índice ($n$) | $m=3, n=5$ |
| 2 | Aplicar el puente $a^{m/n}$ | $x^{3/5}$ |

**2. De Potencia a Raíz.** Escribir $7^{1/2}$ como raíz.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | El denominador 2 pasa a ser índice | $\\sqrt[2]{7^1}$ |
| 2 | Simplificar notación | $\\sqrt{7}$ |

**3. Multiplicación de igual índice.** Calcular $\\sqrt[3]{2} \\cdot \\sqrt[3]{4}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Conservar índice y multiplicar bases | $\\sqrt[3]{2 \\cdot 4}$ |
| 2 | Resolver multiplicación | $\\sqrt[3]{8}$ |
| 3 | Extraer raíz exacta | $2$ |

**4. División de igual índice.** Calcular $\\sqrt{50} / \\sqrt{2}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Conservar índice y dividir bases | $\\sqrt{50/2}$ |
| 2 | Resolver división | $\\sqrt{25}$ |
| 3 | Extraer raíz exacta | $5$ |

**5. Raíz de una raíz.** Simplificar $\\sqrt{\\sqrt[3]{64}}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar índices ($2 \\cdot 3$) | $\\sqrt[6]{64}$ |
| 2 | Extraer raíz exacta ($2^6 = 64$) | $2$ |

**6. Meter factor bajo raíz.** Expresar $3\\sqrt{2}$ como una sola raíz.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Elevar el factor al índice (cuadrado) | $3^2 = 9$ |
| 2 | Multiplicar por el de adentro | $9 \\cdot 2$ |
| 3 | Resultado final | $\\sqrt{18}$ |

**7. Suma de raíces semejantes.** Calcular $5\\sqrt{2} + 3\\sqrt{2} - \\sqrt{2}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Sumar/Restar coeficientes externos | $(5 + 3 - 1)$ |
| 2 | Mantener la raíz semejante | $7\\sqrt{2}$ |

**8. Simplificar raíz (Descomposición).** Simplificar $\\sqrt{50}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Buscar un cuadrado perfecto que divida al 50 | $25 \\cdot 2$ |
| 2 | Aplicar raíz a cada uno | $\\sqrt{25} \\cdot \\sqrt{2}$ |
| 3 | Resultado final | $5\\sqrt{2}$ |

**9. Potencia de una raíz.** Calcular $(\\sqrt[4]{3})^4$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | El exponente anula a la raíz si son iguales | $3$ |

**10. Raíz de una fracción.** Calcular $\\sqrt{9/16}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Aplicar raíz a numerador y denominador | $\\sqrt{9} / \\sqrt{16}$ |
| 2 | Resultado final | $3/4$ |
        """)

    with st.expander("❓ Cuestionario N20", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿Cuál es el valor de $\\sqrt[3]{-27}$?', 'options': {'A': '$3$', 'B': '$-3$', 'C': '$9$', 'D': 'No es un número real'}, 'answer': 'B', 'explanation': 'Porque $(-3)^3 = -27$. Las raíces de índice impar aceptan números negativos.'},
            {'question': 'La expresión $\\sqrt[4]{a^3}$ escrita como potencia es:', 'options': {'A': '$a^{4/3}$', 'B': '$a^7$', 'C': '$a^{3/4}$', 'D': '$a^{12}$'}, 'answer': 'C', 'explanation': 'Aplicando el puente: el de adentro (3) arriba, el de afuera (4) abajo.'},
            {'question': 'El resultado de $\\sqrt{2} \\cdot \\sqrt{32}$ es:', 'options': {'A': '$\\sqrt{34}$', 'B': '$8$', 'C': '$16$', 'D': '$64$'}, 'answer': 'B', 'explanation': '$\\sqrt{2 \\cdot 32} = \\sqrt{64} = 8$.'},
            {'question': '¿A qué es igual la expresión $\\sqrt{\\sqrt{81}}$?', 'options': {'A': '$9$', 'B': '$81$', 'C': '$3$', 'D': '$\\sqrt{3}$'}, 'answer': 'C', 'explanation': 'Raíz de raíz: $2 \\cdot 2 = 4$. $\\sqrt[4]{81} = 3$ (porque $3^4 = 81$).'},
            {'question': 'El valor de $5\\sqrt{3} - 2\\sqrt{3}$ es:', 'options': {'A': '$3$', 'B': '$3\\sqrt{6}$', 'C': '$3\\sqrt{3}$', 'D': '$\\sqrt{3}$'}, 'answer': 'C', 'explanation': 'Se restan los coeficientes ($5-2=3$) y se mantiene la raíz de 3.'},
            {'question': 'Al meter el 2 dentro de la raíz en $2\\sqrt[3]{5}$, se obtiene:', 'options': {'A': '$\\sqrt[3]{10}$', 'B': '$\\sqrt[3]{20}$', 'C': '$\\sqrt[3]{40}$', 'D': '$\\sqrt[3]{50}$'}, 'answer': 'C', 'explanation': 'El 2 entra como $2^3 = 8$. Luego $8 \\cdot 5 = 40$. Resultado: $\\sqrt[3]{40}$.'},
            {'question': '¿Cuál es el resultado de $(\\sqrt{7})^2$?', 'options': {'A': '$49$', 'B': '$7$', 'C': '$\\sqrt{14}$', 'D': '$14$'}, 'answer': 'B', 'explanation': 'El cuadrado anula la raíz cuadrada.'},
            {'question': 'La expresión $\\sqrt{12}$ simplificada es:', 'options': {'A': '$2\\sqrt{3}$', 'B': '$3\\sqrt{2}$', 'C': '$6$', 'D': '$4\\sqrt{3}$'}, 'answer': 'A', 'explanation': '$\\sqrt{12} = \\sqrt{4 \\cdot 3} = \\sqrt{4} \\cdot \\sqrt{3} = 2\\sqrt{3}$.'},
            {'question': '¿Cuál es el valor de $\\sqrt{0{,}25}$?', 'options': {'A': '$0{,}05$', 'B': '$0{,}5$', 'C': '$5$', 'D': '$0{,}125$'}, 'answer': 'B', 'explanation': '$\\sqrt{0{,}25} = \\sqrt{25/100} = 5/10 = 0{,}5$.'},
            {'question': 'La suma $\\sqrt{9} + \\sqrt{16}$ es igual a:', 'options': {'A': '$\\sqrt{25}$', 'B': '$7$', 'C': '$12$', 'D': '$5$'}, 'answer': 'B', 'explanation': 'Se resuelven por separado: $3 + 4 = 7$. ¡Cuidado! No es $\\sqrt{25}$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n20_quiz")


    st.markdown("---")
    st.markdown("> *\"El pensamiento es solo un relámpago en medio de una larga noche. Pero es ese relámpago lo que lo es todo.\"*  \n> — **Henri Poincaré**")
