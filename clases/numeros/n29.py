import streamlit as st


def render_N29():
    st.markdown("""## N29: Manipulación de Fórmulas Científicas

---

### 🏛️  Contexto Histórico: El Arte de Equilibrar el Universo

Durante siglos, la humanidad observó el mundo de forma descriptiva: decían que algo era "pesado" o que un proceso era "lento". El gran salto ocurrió cuando mentes como **Newton, Boyle u Ohm** entendieron que la naturaleza no funciona al azar, sino mediante **equilibrios perfectos**.

Comprendieron que una fórmula no es una sentencia escrita en piedra, sino una **balanza dinámica**. Si los antiguos ingenieros no hubiesen sabido manipular estas relaciones, los grandes acueductos se habrían reventado por la presión y los puentes habrían colapsado bajo su propio peso. Despejar una fórmula es, en esencia, el arte de interrogar a la naturaleza: si conoces cuánto espacio tienes y a qué velocidad vas, el álgebra te obliga a saber cuánto tiempo tardarás. Hoy dejarás de ver letras extrañas para empezar a ver los hilos que mueven la realidad.



---

<div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1565C0; margin-top: 0;">🛡️ La Regla de Oro: La Igualdad como Balanza</h2>
    Para manipular cualquier fórmula científica, debes visualizar el signo igual ($=$) como el eje de una balanza en equilibrio. Si mueves algo de un lado al otro, debe pasar haciendo lo <b>opuesto</b> para que el equilibrio se mantenga.
    <br><br>
    <b>1. El Salto de la Igualdad:</b> Cuando un término "salta" al otro lado, cambia su jerarquía de operación:
    <ul>
        <li><b>Suma $\\leftrightarrow$ Resta:</b> Si algo suma, pasa restando.</li>
        <li><b>Multiplicación $\\leftrightarrow$ División:</b> Si algo multiplica arriba, pasa dividiendo abajo.</li>
        <li><b>Potencia $\\leftrightarrow$ Raíz:</b> Para sacar un cuadrado ($x^2$), aplicas raíz ($\\sqrt{x}$).</li>
    </ul>
    <br>
    <b>2. Ejemplos de Movimiento Paso a Paso:</b>
    <br><br>
    <b>Caso A (La Variable está abajo):</b> En la fórmula de Presión $P = \\frac{F}{A}$, queremos despejar el Área ($A$).
    <ol>
        <li>Como la $A$ está dividiendo, la subimos multiplicando al otro lado para que quede arriba: $P \\cdot A = F$</li>
        <li>Ahora, como la $P$ estorba a nuestra $A$ (la está multiplicando), la pasamos dividiendo al otro lado: $A = \\frac{F}{P}$</li>
    </ol>
    <br>
    <b>Caso B (Despeje con Suma):</b> En la fórmula $V_f = V_i + a \\cdot t$, queremos despejar $V_i$.
    <ol>
        <li>El bloque $(a \\cdot t)$ completo está sumando a nuestra incógnita.</li>
        <li>Lo movemos íntegro al otro lado de la balanza haciendo la operación opuesta (restar): $V_f - (a \\cdot t) = V_i$</li>
    </ol>
</div>



### 🛡️ Las 12 Fórmulas para "Soltar la Mano"
**Típ:** No importa si no sabes qué significa la letra, lo que importa es dejarla sola. Trata a los grupos de letras que multiplican como un solo bloque que pasa dividiendo.

| Área | Fórmula Original | Objetivo | Despeje Correcto |
| :--- | :--- | :--- | :--- |
| **Gases** | $P \\cdot V = n \\cdot R \\cdot T$ | Despejar $T$ | $T = \\frac{P \\cdot V}{n \\cdot R}$ |
| **Gases** | $P \\cdot V = n \\cdot R \\cdot T$ | Despejar $n$ | $n = \\frac{P \\cdot V}{R \\cdot T}$ |
| **Cinemática** | $V_f = V_i + a \\cdot t$ | Despejar $a$ | $a = \\frac{V_f - V_i}{t}$ |
| **Gravedad** | $F = G \\cdot \\frac{m_1 \\cdot m_2}{r^2}$ | Despejar $r$ | $r = \\sqrt{\\frac{G \\cdot m_1 \\cdot m_2}{F}}$ |
| **Energía** | $E_c = \\frac{1}{2} m \\cdot v^2$ | Despejar $v$ | $v = \\sqrt{\\frac{2E_c}{m}}$ |
| **Electricidad** | $V = I \\cdot R$ | Despejar $I$ | $I = \\frac{V}{R}$ |
| **Resistencia** | $R = \\rho \\cdot \\frac{L}{A}$ | Despejar $A$ | $A = \\frac{\\rho \\cdot L}{R}$ |
| **Calor** | $Q = m \\cdot c \\cdot \\Delta T$ | Despejar $c$ | $c = \\frac{Q}{m \\cdot \\Delta T}$ |
| **Densidad** | $D = \\frac{m}{V}$ | Despejar $V$ | $V = \\frac{m}{D}$ |
| **Péndulo** | $T = 2\\pi \\sqrt{\\frac{L}{g}}$ | Despejar $L$ | $L = g \\cdot \\left(\\frac{T}{2\\pi}\\right)^2$ |
| **Presión** | $P = \\frac{F}{A}$ | Despejar $A$ | $A = \\frac{F}{P}$ |
| **Finanzas** | $I = C \\cdot r \\cdot t$ | Despejar $r$ | $r = \\frac{I}{C \\cdot t}$ |

---

"La simplicidad es la forma final de la sofisticación."  
— **Leonardo da Vinci**""", unsafe_allow_html=True)
    st.markdown("---")
    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: Despejes Progresivos

**E01. Despejar el radio ($r$) de la Ley de Gravitación.** $F = G \\cdot \\frac{m_1 \\cdot m_2}{r^2}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Subir el $r^2$ que divide al otro lado | $F \\cdot r^2 = G \\cdot m_1 \\cdot m_2$ |
| 2 | Bajar la $F$ que ahora estorba a $r^2$ | $r^2 = \\frac{G \\cdot m_1 \\cdot m_2}{F}$ |
| 3 | Aplicar raíz para eliminar la potencia | $r = \\sqrt{\\frac{G \\cdot m_1 \\cdot m_2}{F}}$ |

**E02. Despejar la velocidad ($v$) en Energía Cinética.** $E_c = \\frac{1}{2} m \\cdot v^2$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | El 2 que divide pasa multiplicando | $2 \\cdot E_c = m \\cdot v^2$ |
| 2 | La masa ($m$) que multiplica pasa dividiendo | $\\frac{2 \\cdot E_c}{m} = v^2$ |
| 3 | El cuadrado pasa como raíz cuadrada | $v = \\sqrt{\\frac{2E_c}{m}}$ |

**E03. Despejar el Área ($A$) en la Resistencia.** $R = \\rho \\cdot \\frac{L}{A}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Subir $A$ y bajar $R$ (Intercambio) | $A = \\rho \\cdot \\frac{L}{R}$ |
| 2 | Multiplicar términos de arriba | $A = \\frac{\\rho \\cdot L}{R}$ |

**E04. Despejar la aceleración ($a$) en Cinemática.** $V_f = V_i + a \\cdot t$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Mover primero lo que suma ($V_i$) restando | $V_f - V_i = a \\cdot t$ |
| 2 | El tiempo ($t$) que multiplica pasa dividiendo | $\\frac{V_f - V_i}{t} = a$ |

**E05. Despejar la longitud ($L$) del Péndulo.** $T = 2\\pi \\sqrt{\\frac{L}{g}}$
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | El bloque $2\\pi$ pasa dividiendo | $\\frac{T}{2\\pi} = \\sqrt{\\frac{L}{g}}$ |
| 2 | Para eliminar la raíz, elevamos al cuadrado | $\\left(\\frac{T}{2\\pi}\\right)^2 = \\frac{L}{g}$ |
| 3 | La gravedad ($g$) sube multiplicando | $L = g \\cdot \\left(\\frac{T}{2\\pi}\\right)^2$ |""")
    with st.expander("❓ Cuestionario N29", expanded=False):
        st.markdown("""# ❓ Cuestionario N29: Manipulación de Fórmulas

**1. En la fórmula $P \\cdot V = n \\cdot R \\cdot T$, ¿cuál es el despeje correcto de $n$?** \\
A) $n = P \\cdot V \\cdot R \\cdot T$ \\
B) $n = \\frac{P \\cdot V}{R \\cdot T}$ \\
C) $n = \\frac{R \\cdot T}{P \\cdot V}$ \\
D) $n = P \\cdot V - R \\cdot T$

**2. Si $V = I \\cdot R$, ¿cómo se expresa $R$?** \\
A) $R = V \\cdot I$ \\
B) $R = \\frac{I}{V}$ \\
C) $R = \\frac{V}{I}$ \\
D) $R = V - I$

**3. Al despejar $V$ de la fórmula de densidad $D = \\frac{m}{V}$, obtenemos:** \\
A) $V = \\frac{m}{D}$ \\
B) $V = \\frac{D}{m}$ \\
C) $V = m \\cdot D$ \\
D) $V = m + D$

**4. En $E = m \\cdot c^2$, ¿cuál es el despeje de $c$?** \\
A) $c = \\frac{E}{m}$ \\
B) $c = \\sqrt{\\frac{E}{m}}$ \\
C) $c = \\left(\\frac{E}{m}\\right)^2$ \\
D) $c = \\sqrt{E \\cdot m}$

**5. Dada la fórmula $Q = m \\cdot c \\cdot \\Delta T$, despejar $\\Delta T$ resulta en:** \\
A) $\\Delta T = \\frac{Q}{m \\cdot c}$ \\
B) $\\Delta T = Q \\cdot m \\cdot c$ \\
C) $\\Delta T = \\frac{m \\cdot c}{Q}$ \\
D) $\\Delta T = Q - m - c$

**6. Si $P = \\frac{F}{A}$, ¿cómo se despeja $F$?** \\
A) $F = \\frac{P}{A}$ \\
B) $F = P \\cdot A$ \\
C) $F = \\frac{A}{P}$ \\
D) $F = P + A$

**7. En la fórmula $I = C \\cdot r \\cdot t$, el despeje de $t$ es:** \\
A) $t = \\frac{I}{C \\cdot r}$ \\
B) $t = \\frac{C \\cdot r}{I}$ \\
C) $t = I \\cdot C \\cdot r$ \\
D) $t = \\frac{I \\cdot C}{r}$

**8. Si despejamos $v$ de la fórmula $E_c = \\frac{1}{2} m \\cdot v^2$, el resultado es:** \\
A) $v = \\frac{2E_c}{m}$ \\
B) $v = \\sqrt{\\frac{E_c}{2m}}$ \\
C) $v = \\sqrt{\\frac{2E_c}{m}}$ \\
D) $v = \\left(\\frac{2E_c}{m}\\right)^2$

**9. En la fórmula $V_f = V_i + a \\cdot t$, el despeje de $V_i$ es:** \\
A) $V_i = V_f - a \\cdot t$ \\
B) $V_i = \\frac{V_f}{a \\cdot t}$ \\
C) $V_i = V_f + a \\cdot t$ \\
D) $V_i = a \\cdot t - V_f$

**10. Al despejar $L$ de la fórmula $R = \\rho \\cdot \\frac{L}{A}$, obtenemos:** \\
A) $L = \\frac{R \\cdot A}{\\rho}$ \\
B) $L = \\frac{\\rho \\cdot A}{R}$ \\
C) $L = R \\cdot A \\cdot \\rho$ \\
D) $L = \\frac{R}{\\rho \\cdot A}$""")
    with st.expander("✅ Pauta - N29", expanded=False):
        st.markdown("""# ✅ Pauta - Cuestionario N29

1. **B.** Los términos $R$ y $T$ multiplican a $n$, por lo que pasan dividiendo juntos al otro lado.
2. **C.** La intensidad ($I$) multiplica, pasa dividiendo bajo el voltaje ($V$).
3. **A.** Primero subimos $V$ multiplicando al lado de $D$, y luego bajamos $D$ dividiendo.
4. **B.** Primero la masa ($m$) divide a $E$, y luego el cuadrado pasa como raíz.
5. **A.** El bloque $(m \\cdot c)$ está multiplicando, pasa dividiendo íntegro.
6. **B.** El área está dividiendo a la fuerza, pasa multiplicando a la presión.
7. **A.** Es un despeje directo: todo lo que acompaña a $t$ pasa dividiendo.
8. **C.** El 2 multiplica, la $m$ divide y la potencia pasa como raíz.
9. **A.** El término $(a \\cdot t)$ se considera un solo bloque sumando, pasa restando.
10. **A.** El área $A$ sube multiplicando y la resistividad $\\rho$ baja dividiendo.""")