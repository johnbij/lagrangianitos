import streamlit as st
import matplotlib.pyplot as plt


def render_N02():

    st.markdown("""
## N02: Los Números Naturales ($\\mathbb{N}$) - El Génesis del Conteo

---

### 🛡️  El Portal: El Instinto de Cuantificar
Mucho antes de que existieran las pizarras o los computadores, el ser humano tuvo una necesidad vital: **¿Cuántos hay?** Los Números Naturales no fueron inventados; fueron descubiertos como la herramienta de supervivencia definitiva para contar presas, días y ciclos.

---

### 🛡️  Crónica del Origen: El Hueso de Ishango y Peano
Hace más de 20.000 años, alguien talló marcas en un hueso (el Hueso de Ishango) para llevar una cuenta. Siglos después, **Giuseppe Peano** definió los "Axiomas de Peano", demostrando que solo necesitábamos un punto de partida (el 1) y un sucesor para construir todo el universo matemático.

---

### 🛡️ Definición y Características Formales
Se denota con la letra $\\mathbb{N}$ y se define como el conjunto infinito:
$$\\mathbb{N} = \\{1, 2, 3, 4, 5, 6, 7, ...\\}$$
* **Primer Elemento:** El **1** es el inicio absoluto. Carece de antecesor en este conjunto.
* **Infinitud:** No existe un número máximo.
* **Discretitud:** Es un conjunto "con saltos". Entre el 4 y el 5 **no hay nada**.
""")

    # ── FIGURA: Recta de los Números Naturales ───────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.axhline(0, color='black', lw=2)
    ax.set_xlim(0, 8)
    ax.set_ylim(-0.5, 0.5)
    for x in range(1, 8):
        ax.plot(x, 0, 'ro', markersize=8)
        ax.text(x, -0.2, str(x), ha='center', fontsize=12, fontweight='bold')
    ax.axvline(1, ymin=0.3, ymax=0.7, color='navy', lw=3)
    ax.text(0.5, 0.1, "Prohibido", color='red', fontsize=8, ha='center', fontweight='bold')
    ax.annotate('', xy=(8, 0), xytext=(7.5, 0),
                arrowprops=dict(facecolor='black', shrink=0, width=1))
    plt.title("Recta de los Números Naturales ($\\mathbb{N}$)", fontsize=14, fontweight='bold')
    plt.axis('off')
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("""
---

### 🛡️  La Ley de Tricotomía: El Juez de los Números
Esta es la regla que permite el orden. Establece que si tomas dos números naturales cualesquiera, $a$ y $b$, **solo una** de estas tres realidades es posible:
1. **$a < b$** ($a$ está a la izquierda de $b$).
2. **$a > b$** ($a$ está a la derecha de $b$).
3. **$a = b$** (Son el mismo número).

---

### 🛡️  Relaciones de Vecindad
* **El Sucesor:** Todo $n \\in \\mathbb{N}$ tiene un sucesor único: $(n + 1)$.
* **El Antecesor:** Todo $n \\in \\mathbb{N}$, **con excepción del 1**, tiene un antecesor único: $(n - 1)$.

> **💡 Tip:** Si un problema dice que "el antecesor de $n$ es natural", el contrato te dice que $n$ no puede ser 1.

---

### 🛡️  Las Reglas del Juego: Propiedades Estructurales
Para operar en $\\mathbb{N}$, debemos conocer las leyes que gobiernan el comportamiento de los números:
* **Clausura (Cierre):** Un conjunto es "cerrado" si al operar dos de sus elementos, el resultado **siempre** es un elemento del mismo conjunto.
* **Conmutativa:** El orden de los sumandos o factores no altera el resultado ($a + b = b + a$).
* **Asociativa:** La forma en que agrupas los números no cambia el total $(a + b) + c = a + (b + c)$.
* **Distributiva:** La multiplicación se "reparte" sobre la suma: $a \\cdot (b + c) = (a \\cdot b) + (a \\cdot c)$.

**Análisis de Clausura en $\\mathbb{N}$:**

| Operación | ¿Es Cerrada? | Carpintería Técnica |
| :--- | :---: | :--- |
| **Adición (+)** | ✅ SÍ | Natural + Natural = Siempre Natural. |
| **Multiplicación ($\\cdot$)** | ✅ SÍ | Natural $\\cdot$ Natural = Siempre Natural. |
| **Sustracción (-)** | ❌ NO | Si el sustraendo es mayor, sales del conjunto. |
| **División (:)** | ❌ NO | No toda división resulta en un número "entero". |

> **💡 Tip:** En la PAES, la propiedad distributiva es el motor de la factorización. Si la aprendes bien aquí, el álgebra será mucho más fácil.

---

> *"El número es la sustancia de todas las cosas".*
>
> — **Pitágoras**
""")
