import streamlit as st


def render_N18():
    st.markdown("## N18: Notación Científica - El Tamaño del Universo")
    st.markdown("---")

    st.markdown("### 🏛️ Contexto Histórico: De los Grandes Números al Microcosmos")
    st.markdown("""
Desde que los astrónomos empezaron a medir la distancia entre las estrellas y los biólogos el tamaño de las células, surgió un problema: escribir números con 20 o 30 ceros era poco práctico y propenso a errores. La notación científica nació como un lenguaje universal para simplificar el caos. Al usar potencias de base 10, no solo ahorramos espacio, sino que podemos comparar órdenes de magnitud de forma inmediata, permitiéndonos entender desde la masa de un átomo hasta el peso de una galaxia sin perdernos en una marea de ceros.
    """)
    st.markdown("---")

    st.markdown("""
<div style="background-color: #f1f8e9; padding: 25px; border-radius: 10px; border: 1px solid #c8e6c9;">
    <h2 style="color: #388E3C; margin-top: 0;">Notación Científica</h2>
    Se usa para escribir números muy grandes o muy pequeños de forma eficiente.<br>
    Estructura: <b>$k \\cdot 10^n$</b><br>
    Donde $1 \\le k < 10$ (k debe ser un número entre 1 y 9,99...).
</div>
""", unsafe_allow_html=True)

    st.markdown("### 🛡️ Cómo mover la coma")
    st.markdown("""
- **Hacia la IZQUIERDA:** El exponente de la potencia de 10 **aumenta** (Positivo).
  - Ej: $540.000 = 5{,}4 \\cdot 10^5$
- **Hacia la DERECHA:** El exponente de la potencia de 10 **disminuye** (Negativo).
  - Ej: $0{,}00003 = 3 \\cdot 10^{-5}$
    """)
    st.markdown("---")

    st.markdown("### 🛡️ Prefijos del Sistema Internacional (SI)")
    st.markdown("""
Es vital conocer los prefijos que usan potencias de 10:
- **Kilo (k):** $10^3$ (Mil)
- **Mega (M):** $10^6$ (Millón)
- **Giga (G):** $10^9$ (Mil millones)
- **Mili (m):** $10^{-3}$ (Milésima)
- **Micro ($\\mu$):** $10^{-6}$ (Millonésima)
- **Nano (n):** $10^{-9}$ (Mil millonésima)

**⚠️ Típ:** En la PAES te van a pedir comparar potencias de 10. Si el exponente es más grande, el número es más grande. Punto. No te compliques la vida contando ceros.
    """)
    st.markdown("---")

    with st.expander("📝 Guía de Ejemplos: Notación Científica y Base 10"):
        st.markdown("""
**E01. Convertir número grande a notación científica.** $4.500.000$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Ubicar la coma al final y moverla a la izquierda | Mover 6 espacios |
| 2 | Dejar un número entre 1 y 10 | $4{,}5$ |
| 3 | Exponente según espacios movidos | $4{,}5 \\cdot 10^6$ |

**E02. Convertir número pequeño a notación científica.** $0{,}0000078$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mover la coma a la derecha | Mover 6 espacios |
| 2 | Dejar un número entre 1 y 10 | $7{,}8$ |
| 3 | Exponente negativo (hacia la derecha) | $7{,}8 \\cdot 10^{-6}$ |

**E03. De notación científica a decimal.** $3{,}2 \\cdot 10^4$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mover la coma 4 espacios a la derecha | $32.000$ |

**E04. De notación científica a decimal (negativo).** $9{,}1 \\cdot 10^{-3}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mover la coma 3 espacios a la izquierda | $0{,}0091$ |

**E05. Multiplicación en notación científica.** $(2 \\cdot 10^3) \\cdot (4 \\cdot 10^5)$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar los números (k) | $2 \\cdot 4 = 8$ |
| 2 | Sumar los exponentes de 10 | $10^{(3+5)} = 10^8$ |
| 3 | Resultado final | $8 \\cdot 10^8$ |

**E06. Ajuste de notación científica.** $45 \\cdot 10^4$ (No está en formato correcto)
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Convertir el 45 a $4{,}5 \\cdot 10^1$ | $4{,}5 \\cdot 10^1 \\cdot 10^4$ |
| 2 | Sumar exponentes | $4{,}5 \\cdot 10^5$ |

**E07. División en notación científica.** $(9 \\cdot 10^8) : (3 \\cdot 10^2)$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Dividir los números | $9 : 3 = 3$ |
| 2 | Restar exponentes | $10^{(8-2)} = 10^6$ |
| 3 | Resultado | $3 \\cdot 10^6$ |

**E08. Comparación de números.** ¿Qué es mayor, $5 \\cdot 10^{-4}$ o $2 \\cdot 10^{-3}$?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mirar exponentes | $-3$ es mayor que $-4$ |
| 2 | Conclusión | $2 \\cdot 10^{-3}$ es mayor |

**E09. Potencia de una potencia.** $(2 \\cdot 10^4)^2$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Elevar el número al cuadrado | $2^2 = 4$ |
| 2 | Multiplicar exponentes del 10 | $10^{(4 \\cdot 2)} = 10^8$ |
| 3 | Resultado | $4 \\cdot 10^8$ |

**E10. Suma de potencias de 10.** $3 \\cdot 10^2 + 5 \\cdot 10^2$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Como tienen igual exponente, sumar k | $(3+5) \\cdot 10^2$ |
| 2 | Resultado | $8 \\cdot 10^2$ |
        """)

    with st.expander("❓ Cuestionario N18: Notación Científica"):
        st.markdown("""
**1. ¿Cuál es la representación correcta de $0{,}00045$ en notación científica?**  
A) $45 \\cdot 10^{-5}$ &nbsp;&nbsp; B) $4{,}5 \\cdot 10^{-4}$ &nbsp;&nbsp; C) $4{,}5 \\cdot 10^4$ &nbsp;&nbsp; D) $0{,}45 \\cdot 10^{-3}$

**2. El número $7{,}2 \\cdot 10^5$ expresado en forma decimal es:**  
A) $72.000$ &nbsp;&nbsp; B) $720.000$ &nbsp;&nbsp; C) $7.200.000$ &nbsp;&nbsp; D) $0{,}000072$

**3. ¿Cuál de los siguientes números es el más pequeño?**  
A) $5 \\cdot 10^{-2}$ &nbsp;&nbsp; B) $8 \\cdot 10^{-3}$ &nbsp;&nbsp; C) $2 \\cdot 10^{-2}$ &nbsp;&nbsp; D) $9 \\cdot 10^{-4}$

**4. Al multiplicar $(3 \\cdot 10^4) \\cdot (2 \\cdot 10^{-2})$ resulta:**  
A) $6 \\cdot 10^6$ &nbsp;&nbsp; B) $6 \\cdot 10^2$ &nbsp;&nbsp; C) $6 \\cdot 10^{-8}$ &nbsp;&nbsp; D) $5 \\cdot 10^2$

**5. La expresión $0{,}04 \\cdot 10^6$ escrita correctamente en notación científica es:**  
A) $4 \\cdot 10^4$ &nbsp;&nbsp; B) $4 \\cdot 10^8$ &nbsp;&nbsp; C) $4 \\cdot 10^5$ &nbsp;&nbsp; D) $40 \\cdot 10^3$

**6. ¿Cuántos metros hay en 5 kilómetros expresados en notación científica?**  
A) $5 \\cdot 10^2$ m &nbsp;&nbsp; B) $5 \\cdot 10^3$ m &nbsp;&nbsp; C) $5 \\cdot 10^4$ m &nbsp;&nbsp; D) $0{,}5 \\cdot 10^4$ m

**7. El resultado de $(8 \\cdot 10^{12}) : (2 \\cdot 10^4)$ es:**  
A) $4 \\cdot 10^3$ &nbsp;&nbsp; B) $4 \\cdot 10^8$ &nbsp;&nbsp; C) $4 \\cdot 10^{16}$ &nbsp;&nbsp; D) $6 \\cdot 10^8$

**8. Un nanómetro equivale a $10^{-9}$ metros. ¿Cómo se escribe $0{,}000000001$ m en notación científica?**  
A) $1 \\cdot 10^{-8}$ &nbsp;&nbsp; B) $1 \\cdot 10^{-9}$ &nbsp;&nbsp; C) $10 \\cdot 10^{-10}$ &nbsp;&nbsp; D) $0{,}1 \\cdot 10^{-8}$

**9. ¿Cuál es el valor de $(4 \\cdot 10^{-3})^2$?**  
A) $16 \\cdot 10^{-6}$ &nbsp;&nbsp; B) $1{,}6 \\cdot 10^{-5}$ &nbsp;&nbsp; C) $8 \\cdot 10^{-6}$ &nbsp;&nbsp; D) $16 \\cdot 10^{-5}$

**10. Al sumar $2{,}5 \\cdot 10^3 + 0{,}5 \\cdot 10^3$ obtenemos:**  
A) $3 \\cdot 10^6$ &nbsp;&nbsp; B) $3 \\cdot 10^3$ &nbsp;&nbsp; C) $2{,}55 \\cdot 10^3$ &nbsp;&nbsp; D) $30 \\cdot 10^2$
        """)

    with st.expander("✅ Pauta Explicativa - Cuestionario N18"):
        st.markdown("""
1. **B.** Movemos la coma 4 espacios a la derecha para que quede $4{,}5$. Como es a la derecha, el exponente es $-4$.
2. **B.** Movemos la coma 5 espacios a la derecha: el primer espacio pasa el 2, y agregamos 4 ceros. Resulta $720.000$.
3. **D.** El exponente más pequeño (más negativo) es $-4$. Por lo tanto, $9 \\cdot 10^{-4}$ es el menor.
4. **B.** Multiplicamos $3 \\cdot 2 = 6$ y sumamos exponentes: $4 + (-2) = 2$. Queda $6 \\cdot 10^2$.
5. **A.** El $0{,}04$ es $4 \\cdot 10^{-2}$. Luego, $4 \\cdot 10^{-2} \\cdot 10^6 = 4 \\cdot 10^4$.
6. **B.** Kilo significa $10^3$. Por lo tanto, $5$ km son $5 \\cdot 10^3$ metros.
7. **B.** Dividimos $8 : 2 = 4$ y restamos exponentes: $12 - 4 = 8$. Queda $4 \\cdot 10^8$.
8. **B.** Se cuenta desde la coma hasta después del 1: son 9 espacios a la derecha. $1 \\cdot 10^{-9}$.
9. **A.** El número se eleva al cuadrado ($4^2 = 16$) y el exponente se multiplica ($-3 \\cdot 2 = -6$).
10. **B.** Como las potencias son iguales ($10^3$), sumamos los coeficientes: $2{,}5 + 0{,}5 = 3$. Se mantiene el $10^3$.
        """)

    st.markdown("---")
    st.markdown("> *\"El espíritu humano es capaz de alcanzar, a través de los números, una visión de los infinitos que nos rodean, desde lo más pequeño hasta lo más vasto.\"*  \n> — **Georg Cantor**")
