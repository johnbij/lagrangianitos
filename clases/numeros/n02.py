import streamlit as st
import matplotlib.pyplot as plt


def render_N02():
    with st.expander("📚 Teoría", expanded=False):

        st.markdown("""
  
    ## N02: Los Números Naturales ($\mathbb{N}$) — El Génesis del Conteo

    ---

    ### 🛡️ El Portal: El Instinto de Cuantificar
    Mucho antes de que existieran las pizarras o los computadores, el ser humano tuvo una necesidad vital: **¿Cuántos hay?** Los Números Naturales no fueron inventados; fueron descubiertos como la herramienta de supervivencia definitiva para contar presas, días y ciclos.

    ---

    ### 🛡️ Crónica del Origen: El Hueso de Ishango y Peano
    Hace más de 20.000 años, alguien talló marcas en un hueso (el Hueso de Ishango) para llevar una cuenta. Siglos después, **Giuseppe Peano** definió los "Axiomas de Peano", demostrando que solo necesitábamos un punto de partida (el 1) y un sucesor para construir todo el universo matemático.

    ---

    ### 🛡️ Definición y Características Formales
    Se denota con la letra $\mathbb{N}$ y se define como el conjunto infinito:
    $$\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, ...\}$$
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
        plt.title("Recta de los Números Naturales ($\mathbb{N}$)", fontsize=14, fontweight='bold')
        plt.axis('off')
        st.pyplot(fig)
        plt.close(fig)

        st.markdown("""
    ---

    ### 🛡️ La Ley de Tricotomía: El Juez de los Números
    Esta es la regla que permite el orden. Establece que si tomas dos números naturales cualesquiera, $a$ y $b$, **solo una** de estas tres realidades es posible:
    1. **$a < b$** ($a$ está a la izquierda de $b$).
    2. **$a > b$** ($a$ está a la derecha de $b$).
    3. **$a = b$** (Son el mismo número).

    ---

    ### 🛡️ Relaciones de Vecindad
    * **El Sucesor:** Todo $n \in \mathbb{N}$ tiene un sucesor único: $(n + 1)$.
    * **El Antecesor:** Todo $n \in \mathbb{N}$, **con excepción del 1**, tiene un antecesor único: $(n - 1)$.

    > **Típ:** Si un problema dice que "el antecesor de $n$ es natural", el contrato te dice que $n$ no puede ser 1.

    ---

    ### 🛡️ Las Reglas del Juego: Propiedades Estructurales
    * **Clausura (Cierre):** Un conjunto es "cerrado" si al operar dos de sus elementos, el resultado **siempre** es un elemento del mismo conjunto.
    * **Conmutativa:** El orden de los sumandos o factores no altera el resultado ($a + b = b + a$).
    * **Asociativa:** La forma en que agrupas los números no cambia el total $(a + b) + c = a + (b + c)$.
    * **Distributiva:** La multiplicación se "reparte" sobre la suma: $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$.

    **Análisis de Clausura en $\mathbb{N}$:**

    | Operación | ¿Es Cerrada? | Carpintería Técnica |
    | :--- | :---: | :--- |
    | **Adición (+)** | ✅ SÍ | Natural + Natural = Siempre Natural. |
    | **Multiplicación ($\cdot$)** | ✅ SÍ | Natural $\cdot$ Natural = Siempre Natural. |
    | **Sustracción (-)** | ❌ NO | Si el sustraendo es mayor, sales del conjunto. |
    | **División (:)** | ❌ NO | No toda división resulta en un número natural. |

    > **Típ:** En la PAES, la propiedad distributiva es el motor de la factorización. Si la aprendes bien aquí, el álgebra será mucho más fácil.

    ---

    > *"El número es la sustancia de todas las cosas".*
    >
    > — **Pitágoras**
    """)


    with st.expander("❓ Cuestionario N02", expanded=False):
        from utils import render_multiple_choice_quiz
        _quiz_data = [
            {
                "question": "¿Cuál de las siguientes operaciones NO cumple con la propiedad de clausura en el conjunto $\mathbb{N}$?",
                "options": {
                    "A": "$15 + 45$",
                    "B": "$12 \cdot 3$",
                    "C": "$10 - 10$",
                    "D": "$2^3$"
                },
                "answer": "C",
                "explanation": "$10 - 10 = 0$. Como el 0 no pertenece a $\mathbb{N}$, la resta no es cerrada en este caso."
            },
            {
                "question": "Si aplicamos la propiedad distributiva a la expresión $5 \cdot (a + 2)$, ¿cuál es el resultado correcto?",
                "options": {
                    "A": "$5a + 2$",
                    "B": "$5a + 10$",
                    "C": "$7a$",
                    "D": "$10a$"
                },
                "answer": "B",
                "explanation": "Se distribuye el 5: $(5 \cdot a) + (5 \cdot 2) = 5a + 10$."
            },
            {
                "question": "Según la Ley de Tricotomía, si tenemos dos naturales $x$ e $y$, y sabemos que NO es cierto que $x > y$ ni que $x = y$, entonces:",
                "options": {
                    "A": "$x$ es el sucesor de $y$.",
                    "B": "$x$ es el antecesor de $y$.",
                    "C": "$x < y$",
                    "D": "No se puede determinar."
                },
                "answer": "C",
                "explanation": "Por Tricotomía, si descartas el \">\" y el \"=\", la única opción restante es \"<\"."
            },
            {
                "question": "¿Cuál es el valor del antecesor del sucesor de 1.000?",
                "options": {
                    "A": "999",
                    "B": "1.000",
                    "C": "1.001",
                    "D": "1.002"
                },
                "answer": "B",
                "explanation": "El sucesor es 1.001. El antecesor de 1.001 vuelve a ser 1.000."
            },
            {
                "question": "La propiedad que garantiza que $12 + (8 + 5) = (12 + 8) + 5$ se denomina:",
                "options": {
                    "A": "Clausura",
                    "B": "Conmutativa",
                    "C": "Asociativa",
                    "D": "Distributiva"
                },
                "answer": "C",
                "explanation": "La Asociativa permite cambiar los paréntesis de lugar sin alterar la suma."
            },
            {
                "question": "Si $n$ es un número natural mayor que 1, ¿cuál de las siguientes expresiones representa siempre a un número natural?",
                "options": {
                    "A": "$n - 1$",
                    "B": "$1 - n$",
                    "C": "$n : 2$",
                    "D": "$n - (n + 1)$"
                },
                "answer": "A",
                "explanation": "Si $n > 1$, su antecesor ($n-1$) será al menos 1, garantizando que sea natural."
            },
            {
                "question": "Al resolver $4 \cdot 3 + 4 \cdot 7$, un alumno decide factorizar por 4 usando la distributiva inversa. ¿Qué expresión obtiene?",
                "options": {
                    "A": "$4 \cdot (3 \cdot 7)$",
                    "B": "$8 \cdot (10)$",
                    "C": "$4 \cdot (3 + 7)$",
                    "D": "$16 \cdot (21)$"
                },
                "answer": "C",
                "explanation": "Se identifica el factor común (4) y se agrupan los sumandos: $4(3 + 7)$."
            },
            {
                "question": "En la recta numérica de los naturales, ¿qué característica define que 'entre el 2 y el 3 no existan otros números'?",
                "options": {
                    "A": "Infinitud",
                    "B": "Discretitud",
                    "C": "Clausura",
                    "D": "Tricotomía"
                },
                "answer": "B",
                "explanation": "La discretitud establece que hay 'saltos' vacíos entre los números."
            },
            {
                "question": "Si el antecesor de $(p + 1)$ es 20, ¿cuál es el valor de $p$?",
                "options": {
                    "A": "19",
                    "B": "20",
                    "C": "21",
                    "D": "22"
                },
                "answer": "B",
                "explanation": "El antecesor de $(p + 1)$ es $(p + 1) - 1 = p$. Por lo tanto, $p = 20$."
            },
            {
                "question": "'El orden de los factores no altera el producto' es una frase que describe la propiedad:",
                "options": {
                    "A": "Asociativa",
                    "B": "Distributiva",
                    "C": "Conmutativa",
                    "D": "Elemento Neutro"
                },
                "answer": "C",
                "explanation": "La Conmutativa indica que $a \cdot b = b \cdot a$."
            }
        ]
        render_multiple_choice_quiz(_quiz_data, key_prefix="n02_quiz")
