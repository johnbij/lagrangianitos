import streamlit as st
import matplotlib.pyplot as plt


def render_N04():
    st.title("N04: Los Números Enteros (ℤ) — La Simetría y el Imperio de la Resta")

    # ── PORTAL ──────────────────────────────────────────────────────────────
    st.header("🛡️ 1. El Portal: El Escándalo de los Números \"Absurdos\"")
    st.markdown(r"""
Imagínate que eres un matemático griego de la época de Pitágoras. Para ti, los números son
geometría: el 3 es un triángulo, el 4 es un cuadrado. Bajo esa lógica, **¿qué demonios es un -2?**
¿Un cuadrado con lados negativos? ¡Imposible! Durante más de mil años, Occidente se negó a
aceptar los negativos, llamándolos *numeri absurdi*.

Sin embargo, los matemáticos indios como **Brahmagupta** (año 628) ya hablaban de
"Fortuna" (positivos) y "Deuda" (negativos). Ellos entendieron que el universo es simétrico:
por cada montaña hay un valle, por cada grado sobre cero hay uno bajo cero.

Al crear los Enteros ($\mathbb{Z}$, del alemán *Zahlen*), la humanidad dejó de ver los números
como "cosas" y empezó a verlos como **posiciones y direcciones**.
""")

    # ── DEFINICIÓN ──────────────────────────────────────────────────────────
    st.header("🛡️ 2. Definición y Características")
    st.markdown(r"""
$$\mathbb{Z} = \{..., -3, -2, -1, 0, 1, 2, 3, ...\}$$

- **El Espejo Infinito:** No hay primer elemento. Si caminas hacia la izquierda, nunca encuentras una pared.
- **El Antecesor Universal:** **Todos** los números tienen antecesor y sucesor.
- **Componentes:**
  - $\mathbb{Z}^+$: Enteros positivos (igual a $\mathbb{N}$)
  - $\mathbb{Z}^-$: Enteros negativos
  - $\{0\}$: El origen (ni positivo ni negativo)
""")

    # ── FIGURA ──────────────────────────────────────────────────────────────
    st.subheader("📊 La Recta Numérica Simétrica")
    fig, ax = plt.subplots(figsize=(11, 3))
    ax.axhline(0, color='black', lw=2.5)

    for x in range(-5, 6):
        color = '#1565C0' if x > 0 else ('#c0392b' if x < 0 else '#2e7d32')
        ax.plot(x, 0, 'o', color=color, markersize=10, zorder=3)
        ax.text(x, -0.35, str(x), ha='center', fontsize=12, fontweight='bold', color=color)
        ax.vlines(x, -0.1, 0.1, color='black', lw=1)

    # Valor absoluto de -3 y 3
    ax.annotate('', xy=(3, 0.45), xytext=(0, 0.45),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
    ax.text(1.5, 0.6, '|3| = 3', ha='center', color='purple', fontweight='bold', fontsize=11)
    ax.annotate('', xy=(-3, 0.45), xytext=(0, 0.45),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
    ax.text(-1.5, 0.6, '|-3| = 3', ha='center', color='purple', fontweight='bold', fontsize=11)

    # Flechas infinitud
    ax.annotate('', xy=(6, 0), xytext=(5.5, 0), arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(-6, 0), xytext=(-5.5, 0), arrowprops=dict(arrowstyle='->', lw=2))

    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-0.7, 0.9)
    ax.axis('off')
    plt.title("La Recta de los Enteros: Simetría perfecta respecto al 0", fontsize=13, fontweight='bold', pad=10)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # ── VALOR ABSOLUTO ──────────────────────────────────────────────────────
    st.header("🛡️ 3. Valor Absoluto (|a|): La Carpintería de la Distancia")
    st.markdown(r"""
El valor absoluto mide la **distancia** de un número al cero. El resultado es siempre $\geq 0$.

$$|a| = \begin{cases} a & \text{si } a \geq 0 \\ -a & \text{si } a < 0 \end{cases}$$

**Propiedades:**
- **Simetría:** $|a| = |-a|$
- **Multiplicativa:** $|a \cdot b| = |a| \cdot |b|$
""")
    st.info("💡 **Tip PAES:** El «$-$» en la segunda parte no dice que el resultado sea negativo. Dice: «ponle otro menos para que se vuelva positivo».")

    # ── OPUESTO ADITIVO ─────────────────────────────────────────────────────
    st.header("🛡️ 4. El Opuesto Aditivo")
    st.markdown(r"""
Para todo $a$, existe $-a$ tal que $a + (-a) = 0$.
""")
    st.info("💡 **Tip PAES:** El 'opuesto' o 'inverso aditivo' = solo cambiar el signo. No confundir con el inverso multiplicativo (dar vuelta la fracción).")

    # ── CLAUSURA ────────────────────────────────────────────────────────────
    st.header("🛡️ 5. Clausura: La Victoria de la Resta")
    st.markdown(r"""
| Operación | Cerrada en ℤ | Carpintería |
|:---|:---:|:---|
| **Adición (+)** | ✅ SÍ | Sumar deudas o fortunas da un entero |
| **Sustracción (−)** | ✅ SÍ | **Aquí está el premio:** $3 - 10 = -7 \in \mathbb{Z}$ |
| **Multiplicación (×)** | ✅ SÍ | La regla de signos mantiene el resultado en ℤ |
| **División (÷)** | ❌ NO | $1 \div 2 = 0,5$ sale del conjunto |
""")

    st.markdown("""
---
> *"Las matemáticas son el juez de lo que es posible; los números negativos son la prueba de que lo imposible es solo una dirección que aún no hemos tomado."*
> — **Ada Lovelace**
""")

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Carpintería de Ejemplos N04", expanded=False):
        st.markdown(r"""
### E01: Operativa de Signos y Clausura
**Resolver** $12 - (15 - 8)$ y verificar si pertenece a $\mathbb{Z}$.

1. $15 - 8 = 7$
2. $12 - 7 = 5$
3. $5 \in \mathbb{Z}$ ✅

---
### E02: Valor Absoluto y Signos
**Calcular** $|-7| + |3| - |-2|$

| Término | Valor | Razón |
|:---|:---:|:---|
| $\|-7\|$ | 7 | Distancia de -7 al 0 |
| $\|3\|$ | 3 | Ya es positivo |
| $\|-2\|$ | 2 | Distancia de -2 al 0 |

**Resultado:** $7 + 3 - 2 = 8$

---
### E03: Identificar el Opuesto
El opuesto aditivo de $-5$ es $5$ porque $-5 + 5 = 0$ ✅

---
### E04: Regla de los Signos
| Operación | Resultado | Pertenece a ℤ |
|:---|:---:|:---:|
| $(-3) \cdot (-4)$ | $+12$ | ✅ |
| $(-3) \cdot (+4)$ | $-12$ | ✅ |
| $(-6) \div (-2)$ | $+3$ | ✅ |
| $(-5) \div 2$ | $-2,5$ | ❌ |

---
### E05: Distancia entre dos Enteros
**Distancia entre -7 y 5:** $|-7 - 5| = |-12| = 12$
""")

    # ── CUESTIONARIO ────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario N04", expanded=False):
        st.markdown(r"""
**1.** ¿Cuál es el resultado de $-5 - (-8)$?
- A) -13 · B) -3 · C) **3** · D) 13

**2.** Si $x \in \mathbb{Z}^-$, ¿qué es SIEMPRE verdad sobre $|x|$?
- A) $|x| = x$ · B) $|x| < 0$ · C) **$|x| = -x$** · D) $|x| = 0$

**3.** La distancia entre -7 y 5 en la recta numérica es:
- A) 2 · B) -2 · C) **12** · D) -12

**4.** ¿Cuál define correctamente a los enteros?
- A) $\{1, 2, 3, ...\}$ · B) $\{0, 1, 2, ...\}$ · C) **$\{..., -2, -1, 0, 1, 2, ...\}$** · D) Los que no tienen decimales y son positivos

**5.** ¿Qué operación NO es cerrada en ℤ?
- A) Suma · B) Resta · C) Multiplicación · D) **División**
""")

    with st.expander("🔑 Pauta N04", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería |
|:---:|:---:|:---|
| 1 | **C** | $-5 - (-8) = -5 + 8 = 3$. Signos distintos: resta y conserva el del mayor valor absoluto. |
| 2 | **C** | Definición axiomática: si $x < 0$, entonces $\|x\| = -x$ (cambia el signo para hacerlo positivo). |
| 3 | **C** | Distancia $= \|-7 - 5\| = \|-12\| = 12$. |
| 4 | **C** | Los enteros incluyen negativos, el cero y positivos. |
| 5 | **D** | $1 \div 2 = 0,5 \notin \mathbb{Z}$. La división "rompe" el conjunto. |
""")
