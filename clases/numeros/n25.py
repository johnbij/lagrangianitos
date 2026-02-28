import streamlit as st


def render_N25():
    st.markdown("""## N25: Simetría - Las 8 Caras de la Proporción

---

### 🏛️ Contexto Histórico: El Equilibrio de las Balanzas

En el mundo antiguo, antes de que existieran los números escritos, el comercio se basaba en la **balanza de platos**. Los mercaderes sabían que el equilibrio se mantenía si se cambiaban las pesas de lugar siguiendo ciertas reglas lógicas. Si una balanza estaba en equilibrio, podías dar vuelta ambos platos y el equilibrio seguía ahí. Esa noción de "simetría" es lo que hoy aplicamos en el álgebra: mientras el producto cruzado sea el mismo, la igualdad no se rompe. Hoy veremos cómo mover las piezas del tablero sin perder el equilibrio.

---

<div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1565C0; margin-top: 0;"> La Madre de todas las reglas</h2>
    Partimos de la proporción base:
    $$\\frac{a}{b} = \\frac{c}{d}$$
    Donde el producto cruzado siempre es: <b>$a \\cdot d = b \\cdot c$</b>. Mientras este producto se mantenga, la proporción es válida.
</div>

### 🛡️ Las 8 Maneras Lógicas
Para despejar rápido, puedes transformar la proporción original en cualquiera de estas 8 formas sin que deje de ser verdadera:

1. **La Original:** $\\frac{a}{b} = \\frac{c}{d}$
2. **Alternar Medios:** $\\frac{a}{c} = \\frac{b}{d}$ (Cambias $b$ con $c$)
3. **Alternar Extremos:** $\\frac{d}{b} = \\frac{c}{a}$ (Cambias $a$ con $d$)
4. **Invertir Razones:** $\\frac{b}{a} = \\frac{d}{c}$ (Das vuelta ambas fracciones)
5. **Invertir y Alternar Medios:** $\\frac{d}{c} = \\frac{b}{a}$
6. **Invertir y Alternar Extremos:** $\\frac{b}{d} = \\frac{a}{c}$
7. **Transponer Miembros:** $\\frac{c}{d} = \\frac{a}{b}$ (Cambias el orden de los platos)
8. **La Totalmente Invertida:** $\\frac{c}{a} = \\frac{d}{b}$

---

### 🛡️ Aplicación en el Despeje
A veces la $x$ (incógnita) queda abajo y es un cacho despejarla. Si conoces estas reglas, simplemente inviertes ambas razones (Propiedad 4) y dejas la $x$ arriba en un segundo.

-----------------
**Típ:** Si la $x$ está abajo, ¡no sufras! Da vuelta las dos fracciones al mismo tiempo. La igualdad se mantiene y el despeje sale solo. Dominar la simetría es dominar el álgebra.

---

"La simetría es una idea por la cual el hombre a través de los siglos ha tratado de comprender y crear el orden, la belleza y la perfección."  
— **Hermann Weyl**""", unsafe_allow_html=True)
    st.markdown("---")
    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: Transformaciones Simétricas

**E01. Invertir razones para despejar.** Hallar $x$ en la proporción $5 : x = 10 : 2$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Escribir como fracciones | $\\frac{5}{x} = \\frac{10}{2}$ |
| 2 | Invertir ambas (Propiedad 4) | $\\frac{x}{5} = \\frac{2}{10}$ |
| 3 | Pasar el 5 multiplicando | $x = \\frac{2 \\cdot 5}{10}$ |
| 4 | Resultado final | $x = 1$ |

**E02. Alternar medios.** Dada la proporción $\\frac{a}{8} = \\frac{15}{24}$, transfórmala alternando medios.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar medios | Los medios son $8$ y $15$ |
| 2 | Cambiarlos de lugar | $\\frac{a}{15} = \\frac{8}{24}$ |
| 3 | Simplificar la razón de la derecha | $\\frac{a}{15} = \\frac{1}{3}$ |
| 4 | Despejar $a$ | $a = 15/3 = 5$ |

**E03. Alternar extremos.** En la proporción $3 : 4 = 6 : 8$, cambia los extremos de lugar.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar extremos | $3$ y $8$ |
| 2 | Cambiarlos (Propiedad 3) | $8 : 4 = 6 : 3$ |
| 3 | Verificar igualdad | $2 = 2$ |
| 4 | Conclusión | La proporción sigue siendo válida. |

**E04. Transponer miembros.** Si $\\frac{x}{3} = 4$, ¿cómo se ve aplicando la transposición?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Entender que $4$ es $\\frac{4}{1}$ | $\\frac{x}{3} = \\frac{4}{1}$ |
| 2 | Cambiar de lado (Propiedad 7) | $\\frac{4}{1} = \\frac{x}{3}$ |
| 3 | Despejar $x$ | $12 = x$ |
| 4 | Resultado | $x = 12$ |

**E05. Invertir y alternar extremos.** Transforma $\\frac{a}{b} = \\frac{c}{d}$ según la Propiedad 6.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Partir de la original | $\\frac{a}{b} = \\frac{c}{d}$ |
| 2 | Invertir ambas | $\\frac{b}{a} = \\frac{d}{c}$ |
| 3 | Alternar los nuevos extremos ($b$ y $c$) | $\\frac{c}{a} = \\frac{d}{b}$ |
| 4 | Resultado final | Se mantiene el producto $bc = ad$ |""")
    with st.expander("❓ Cuestionario N25", expanded=False):
        st.markdown("""# ❓ Cuestionario N25: Simetría Algebraica

**1. Si tenemos la proporción $\\frac{4}{x} = \\frac{8}{10}$, ¿cuál es la forma invertida correcta para despejar $x$?** \\
A) $\\frac{x}{4} = \\frac{10}{8}$\\
B) $\\frac{x}{4} = \\frac{8}{10}$\\
C) $\\frac{4}{8} = \\frac{x}{10}$\\
D) $\\frac{10}{x} = \\frac{8}{4}$

**2. Al alternar los medios en $\\frac{a}{b} = \\frac{c}{d}$, la nueva proporción es:** \\
A) $\\frac{d}{b} = \\frac{c}{a}$\\
B) $\\frac{a}{c} = \\frac{b}{d}$\\
C) $\\frac{b}{a} = \\frac{d}{c}$\\
D) $\\frac{c}{d} = \\frac{a}{b}$

**3. Si invertimos las razones en $3 : 5 = 6 : 10$, obtenemos:** \\
A) $5 : 3 = 10 : 6$\\
B) $3 : 6 = 5 : 10$\\
C) $10 : 5 = 6 : 3$\\
D) $5 : 10 = 3 : 6$

**4. ¿Cuál de estas proporciones es equivalente a $\\frac{x}{y} = \\frac{2}{3}$ alternando extremos?** \\
A) $\\frac{3}{y} = \\frac{2}{x}$\\
B) $\\frac{x}{2} = \\frac{y}{3}$\\
C) $\\frac{y}{x} = \\frac{3}{2}$\\
D) $\\frac{2}{y} = \\frac{x}{3}$

**5. Si en una proporción $\\frac{a}{b} = \\frac{c}{d}$ sabemos que $a \\cdot d = 20$, ¿cuánto debe valer $b \\cdot c$?** \\
A) 10\\
B) 20\\
C) 40\\
D) No se puede saber

**6. La propiedad de "Invertir Razones" es útil principalmente cuando:** \\
A) La incógnita está en el numerador\\
B) La incógnita está en el denominador\\
C) Los números son muy grandes\\
D) No hay incógnita

**7. Al transponer los miembros de $15 : 3 = 10 : 2$, la igualdad queda:** \\
A) $2 : 10 = 3 : 15$\\
B) $10 : 2 = 15 : 3$\\
C) $15 : 10 = 3 : 2$\\
D) $10 : 15 = 2 : 3$

**8. Si aplicamos la Propiedad 8 (Totalmente Invertida) a $\\frac{x}{5} = \\frac{y}{2}$, resulta:** \\
A) $\\frac{y}{x} = \\frac{2}{5}$\\
B) $\\frac{2}{x} = \\frac{5}{y}$\\
C) $\\frac{y}{2} = \\frac{x}{5}$\\
D) $\\frac{2}{5} = \\frac{x}{y}$

**9. En la proporción $\\frac{7}{3} = \\frac{x}{y}$, ¿cuál de las siguientes opciones NO es válida?** \\
A) $\\frac{7}{x} = \\frac{3}{y}$\\
B) $\\frac{3}{7} = \\frac{y}{x}$\\
C) $\\frac{y}{3} = \\frac{x}{7}$\\
D) $\\frac{7}{y} = \\frac{x}{3}$

**10. Si $\\frac{12}{x} = 4$, al invertir ambas razones (considerando $4 = 4/1$) obtenemos:** \\
A) $\\frac{x}{12} = \\frac{1}{4}$\\
B) $\\frac{x}{12} = 4$\\
C) $12x = 4$\\
D) $x = 48$""")
    with st.expander("✅ Pauta - N25", expanded=False):
        st.markdown("""# ✅ Pauta - Cuestionario N25

1. **A.** Invertir razones significa dar vuelta ambas fracciones: $4/x \\to x/4$ y $8/10 \\to 10/8$.
2. **B.** Los medios son $b$ y $c$. Cambiarlos de lugar nos da $a/c = b/d$.
3. **A.** $3/5 \\to 5/3$ y $6/10 \\to 10/6$.
4. **A.** Los extremos son $x$ y $3$. Al cambiarlos queda $3/y = 2/x$.
5. **B.** Por el teorema fundamental, el producto de extremos ($ad$) es igual al de medios ($bc$).
6. **B.** Al invertir, la incógnita pasa del denominador al numerador, facilitando el despeje.
7. **B.** Transponer miembros es simplemente cambiar de lado la igualdad completa.
8. **A.** Es el resultado de transponer y luego alternar medios.
9. **D.** En la opción D, el producto cruzado sería $7 \\cdot 3 = xy$, lo cual es distinto al original $7y = 3x$.
10. **A.** Invertimos $12/x$ a $x/12$ e invertimos $4/1$ a $1/4$.""")