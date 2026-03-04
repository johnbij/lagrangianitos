import streamlit as st


def render_N13():
    with st.expander("📚 Teoría", expanded=False):
        st.title("N13: Números Racionales II - Decimales y la Fracción Generatriz")

        st.markdown(r"""
    ### 🏛️ 1. Contexto Histórico: El Triunfo de la Coma
    Durante siglos, las fracciones como $\frac{1}{2}$ o $\frac{3}{4}$ dominaron el mundo. Pero cuando el comercio y la ciencia se volvieron más rápidos, escribir fracciones para todo era muy lento. En el siglo XVI, el matemático Simon Stevin introdujo la idea de las "fracciones decimales". Su objetivo era que la gente pudiera operar con fracciones con la misma facilidad que con los números enteros.

    Sin embargo, el mundo se dividió: los ingleses usaban el **punto** y los europeos la **coma**. Hoy, en Chile y la mayoría de los países hispanos, usamos la coma para separar el "entero" de la "parte pequeña". Lo que el alumno debe entender es que un decimal no es un número nuevo; es simplemente una fracción con un disfraz diferente, diseñada para ser medida en potencias de 10.

    ---

    ### 🛡️ 10.1 Tipos de Decimales Racionales
    No todos los decimales son iguales. En el conjunto $\mathbb{Q}$ (racionales), tenemos tres familias:

    1. **Decimales Finitos:** Tienen un fin claro. Ejemplo: $0,25$.
    2. **Decimales Periódicos:** Después de la coma, una cifra (o grupo de cifras) se repite infinitamente. Ejemplo: $0,333...$ (se escribe $0,\bar{3}$).
    3. **Decimales Semiperiódicos:** Tienen una parte que no se repite (**antoperiodo**) y luego una que sí (**periodo**). Ejemplo: $0,1\bar{6}$.

    ---

    ### 🛡️ 10.2 De Fracción a Decimal (El Camino de Ida)
    Para convertir una fracción a decimal, solo debes hacer lo que la fracción dice: **Dividir**.
    * **Ejemplo:** $\frac{3}{4} \rightarrow 3 \div 4 = 0,75$.
    * **Ejemplo:** $\frac{1}{3} \rightarrow 1 \div 3 = 0,333... = 0,\bar{3}$.

    ---

    ### 🛡️ 10.3 De Decimal a Fracción (La Fracción Generatriz)
    Este es el "Atajo del Pillo" para volver a la base. Cada tipo tiene su regla:

    * **Para Finitos:** Escribes el número completo arriba (sin coma) y abajo un 1 seguido de tantos **ceros** como decimales haya.
        * *Ejemplo:* $1,25 = \frac{125}{100}$ (y simplificamos).
    * **Para Periódicos:** Arriba el número completo menos la parte entera. Abajo, tantos **nueves** como cifras tenga el periodo.
        * *Ejemplo:* $0,\bar{5} = \frac{5 - 0}{9} = \frac{5}{9}$.
    * **Para Semiperiódicos:** Arriba el número completo menos **todo lo que no tiene rayita**. Abajo, un **nueve** por cada cifra periódica y un **cero** por cada cifra anteperiódica.
        * *Ejemplo:* $0,1\bar{6} = \frac{16 - 1}{90} = \frac{15}{90} = \frac{1}{6}$.

    ---

    ### 🛡️ 10.4 Aproximaciones: El Ojo del Carpintero
    En el taller, a veces no necesitamos el número exacto, sino uno que nos sirva.
    * **Truncamiento:** Es "cortar" el número a sangre fría en la posición pedida. Lo que sobra se borra.
    * **Redondeo:** Miras la cifra siguiente. Si es 5 o más, le sumas 1 a la posición anterior. Si es menor a 5, se queda igual.

    ---

    ### 🛡️ 10.5 Operatoria con Decimales
    * **Suma/Resta:** **La coma sobre la coma.** Si faltan espacios, rellena con ceros.
    * **Multiplicación:** Multiplica como si no hubiera coma. Al final, cuenta cuántos decimales había en total y corre la coma de derecha a izquierda.
    * **División:** ¡Usa la técnica de N10! Amplifica para "matar" la coma del divisor.

    > **Típ:** Si te toca sumar un decimal finito con uno periódico, **pásalo todo a fracción**. Es la única forma de no cometer errores de precisión. Sumar $0,333...$ a mano es un suicidio matemático.

    ---

    > "El sistema decimal es la forma en que los humanos tratamos de domesticar la continuidad de la naturaleza".
    > — **Adaptación de conceptos de Simon Stevin**
    """)


    with st.expander("❓ Cuestionario N13", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿Cuál de las siguientes relaciones de orden es CORRECTA?**\n\\', 'options': {'A': '$1/2 < 1/3$', 'B': '$2/5 > 3/7$', 'C': '$5/6 < 7/8$', 'D': '$3/4 = 9/12$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si ordenamos de mayor a menor los números $a = 2/3$, $b = 3/4$ y $c = 5/6$, el orden es:**\n\\', 'options': {'A': '$c, b, a$', 'B': '$a, b, c$', 'C': '$b, c, a$', 'D': '$c, a, b$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál de los siguientes números se encuentra entre $1/4$ y $1/3$?**\n\\', 'options': {'A': '$2/12$', 'B': '$5/12$', 'C': '$7/24$', 'D': '$1/5$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'En la recta numérica, el número racional $-7/2$ se ubica entre:**\n\\', 'options': {'A': '$-3$ y $-4$', 'B': '$-7$ y $-8$', 'C': '$-2$ y $-3$', 'D': '$3$ y $4$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál es la fracción más pequeña de este grupo? $\\{1/2, 2/5, 3/10, 1/4\\}$**\n\\', 'options': {'A': '$1/2$', 'B': '$2/5$', 'C': '$3/10$', 'D': '$1/4$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Al comparar $x = -0,5$ con $y = -2/3$, se puede afirmar que:**\n\\', 'options': {'A': '$x < y$', 'B': '$x > y$', 'C': '$x = y$', 'D': 'No se pueden comparar.'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Qué número es mayor que $-1/5$?**\n\\', 'options': {'A': '$-1/4$', 'B': '$-1/6$', 'C': '$-1/2$', 'D': '$-1$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál es el promedio exacto entre $1/2$ y $3/4$?**\n\\', 'options': {'A': '$1$', 'B': '$5/8$', 'C': '$4/6$', 'D': '$2/3$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si $a < 0$ y $b > 0$, entonces en la recta numérica:**\n\\', 'options': {'A': '$a$ está a la derecha de $b$.', 'B': '$b$ está a la izquierda del origen.', 'C': '$a$ está a la izquierda de $b$.', 'D': 'Ambos están al mismo lado del cero.'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si sumamos un número racional con su inverso aditivo, el resultado en la recta numérica se ubica en:**\n\\', 'options': {'A': 'El origen (cero).', 'B': 'A la derecha del cero.', 'C': 'A la izquierda del cero.', 'D': 'Depende del valor del número.'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál es la fracción equivalente a $1,25$?**\n\\', 'options': {'A': '$1/4$', 'B': '$5/4$', 'C': '$12/5$', 'D': '$125/10$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El decimal $0,\\bar{3}$ equivale a:**\n\\', 'options': {'A': '$3/10$', 'B': '$1/3$', 'C': '$3/100$', 'D': '$3/1$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Al transformar $0,2\\bar{5}$ a fracción se obtiene:**\n\\', 'options': {'A': '$23/90$', 'B': '$25/90$', 'C': '$23/99$', 'D': '$25/100$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál es el valor de $0,\\bar{1} + 0,\\bar{2}$?**\n\\', 'options': {'A': '$0,3$', 'B': '$1/3$', 'C': '$3/10$', 'D': '$0,33$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El número $2,1\\bar{4}$ expresado como fracción es:**\n\\', 'options': {'A': '$193/90$', 'B': '$214/90$', 'C': '$193/99$', 'D': '$214/100$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si $A = 0,5$ y $B = 0,\\bar{5}$, ¿cuál es la diferencia $B - A$?**\n\\', 'options': {'A': '$0$', 'B': '$1/10$', 'C': '$1/18$', 'D': '$5/90$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Qué decimal equivale a la fracción $5/9$?**\n\\', 'options': {'A': '$0,5$', 'B': '$0,55$', 'C': '$0,\\bar{5}$', 'D': '$0,0\\bar{5}$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El resultado de $1,5 \\cdot 0,\\bar{3}$ es:**\n\\', 'options': {'A': '$0,5$', 'B': '$1/2$', 'C': '$0,\\bar{5}$', 'D': 'Solo A y B son correctas.'}, 'answer': 'A', 'explanation': ''},
            {'question': 'La fracción irreductible de $0,12$ es:**\n\\', 'options': {'A': '$12/100$', 'B': '$6/50$', 'C': '$3/25$', 'D': '$1/8$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un ciclista recorre $0,\\bar{6}$ de una pista. Si la pista mide 90 metros, ¿cuántos metros recorrió?**\n\\', 'options': {'A': '60 metros', 'B': '54 metros', 'C': '66 metros', 'D': '45 metros'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Al truncar el número $7,4582$ a la centésima, se obtiene:**\n\\', 'options': {'A': '$7,45$', 'B': '$7,46$', 'C': '$7,5$', 'D': '$7,4$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si redondeamos $12,345$ a la décima, el resultado es:**\n\\', 'options': {'A': '$12,3$', 'B': '$12,4$', 'C': '$12,35$', 'D': '$12,0$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál es el truncamiento a la milésima del número $0,0098$?**\n\\', 'options': {'A': '$0,01$', 'B': '$0,010$', 'C': '$0,009$', 'D': '$0,008$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El número $5,\\bar{2}$ redondeado a la centésima es:**\n\\', 'options': {'A': '$5,22$', 'B': '$5,23$', 'C': '$5,2$', 'D': '$5,3$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál de las siguientes afirmaciones es CORRECTA respecto al número $3,14159$?**\n\\', 'options': {'A': 'Truncado a la décima es $3,2$.', 'B': 'Redondeado a la milésima es $3,142$.', 'C': 'Truncado a la centésima es $3,15$.', 'D': 'Redondeado a la unidad es $4$.'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Al redondear a la milésima el número $0,12345$, obtenemos:**\n\\', 'options': {'A': '$0,123$', 'B': '$0,124$', 'C': '$0,12$', 'D': '$0,1235$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si $x = 2,718$, el valor de $x$ truncado a la unidad es:**\n\\', 'options': {'A': '$2$', 'B': '$3$', 'C': '$2,7$', 'D': '$2,8$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Estime el valor de $0,66 + 0,33$ redondeando cada término a la décima:**\n\\', 'options': {'A': '$0,9$', 'B': '$1,0$', 'C': '$1,1$', 'D': '$0,99$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El número $-4,56$ truncado a la décima es:**\n\\', 'options': {'A': '$-4,5$', 'B': '$-4,6$', 'C': '$-5$', 'D': '$-4,0$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Al redondear a la centésima el resultado de $1/3$, se obtiene:**\n\\', 'options': {'A': '$0,3$', 'B': '$0,33$', 'C': '$0,34$', 'D': '$0,333$'}, 'answer': 'A', 'explanation': ''}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n13_quiz")




