import streamlit as st


def render_N33():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("""## N33: Proporcionalidad Compuesta - El Sistema Total

    ---

    ### 🏛️ Contexto Histórico: La Logística de las Grandes Obras

    Desde la construcción de la Gran Muralla China hasta las líneas de ensamblaje de Henry Ford, el ser humano ha tenido que calcular sistemas donde muchas cosas cambian al mismo tiempo. No basta con saber cuántos obreros tienes; importa cuántas horas trabajan, qué tan rápido son y qué tan difícil es lo que están construyendo. Los ingenieros industriales del siglo XX perfeccionaron este cálculo para optimizar recursos: si tengo menos tiempo, ¿cuántas máquinas más debo comprar para fabricar el mismo producto? Hoy aprenderás a manejar todas las variables de un problema sin que se te escape ninguna.

    ---

    <div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1565C0; margin-top: 0;">🛡️ ¿Qué es la Proporcionalidad Compuesta?</h2>
        Es cuando intervienen <b>tres o más magnitudes</b> relacionadas entre sí. Aquí no solo comparamos "A con B", sino que vemos cómo un cambio en el tiempo o en la dificultad afecta a todo el resultado final.
        <br><br>
        <b>Típ:</b> Para no marearte con reglas de tres interminables, usa la estructura de <b>Causa y Efecto</b>. En el universo, las cosas que "hacen" el trabajo (causas) multiplicadas por el tiempo que duran, siempre producen un resultado (efecto).
    </div>

    ### 🛡️ El Método de la Constante Estructural
    Existe una relación que siempre se mantiene constante ($k$) en cualquier sistema de trabajo:

    $$\\frac{\\text{Causas} \\cdot \\text{Tiempo}}{\\text{Efecto}} = k$$

    * **Causas:** Quiénes trabajan (obreros, máquinas, animales, grifos).
    * **Tiempo:** Cuánto dura el proceso (horas, días, minutos).
    * **Efecto (Obra):** Qué se logra (metros construidos, piezas hechas, comida consumida).

    ### 🛡️ El Algoritmo de Resolución
    Igualamos la situación inicial (1) con la situación final (2) donde está nuestra incógnita:

    $$\\frac{C_1 \\cdot T_1}{E_1} = \\frac{C_2 \\cdot T_2}{E_2}$$



    ---

    "Dadme un punto de apoyo y moveré el mundo."  
    — **Arquímedes**""", unsafe_allow_html=True)
        st.markdown("---")

    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: El Método de Causa y Efecto

**E01. El Problema de los Obreros (Lógica Maestra).**
*5 obreros trabajando 6 horas diarias construyen un muro en 2 días. ¿Cuántos obreros se necesitan para construir el mismo muro en 1 día trabajando 10 horas diarias?*

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar C, T y E inicial | $C_1=5$ | $T_1=6 \\cdot 2=12$ | $E_1=1$ |
| 2 | Identificar C, T y E final | $C_2=x$ | $T_2=10 \\cdot 1=10$ | $E_2=1$ |
| 3 | Plantear la igualdad | $\\frac{5 \\cdot 12}{1} = \\frac{x \\cdot 10}{1}$ |
| 4 | Resolver la ecuación | $60 = 10x \\implies x = 6$ **obreros** |

**E02. Producción de Máquinas.**
*3 máquinas producen 1.500 envases en 5 horas. ¿Cuántos envases producirán 5 máquinas en 4 horas?*
**Análisis:** * Situación 1: $\\frac{3 \\cdot 5}{1500} = \\frac{15}{1500}$
* Situación 2: $\\frac{5 \\cdot 4}{x} = \\frac{20}{x}$
* Igualando: $\\frac{15}{1500} = \\frac{20}{x} \\implies 15x = 30.000 \\implies x = 2.000$ **envases**.

**E03. Consumo de Alimento.**
*20 vacas consumen 500 kg de pasto en 10 días. ¿Cuántos días durarán 800 kg de pasto para 40 vacas?*
**Análisis:**
* Situación 1: $\\frac{20 \\cdot 10}{500} = \\frac{200}{500} = \\frac{2}{5}$
* Situación 2: $\\frac{40 \\cdot x}{800} = \\frac{x}{20}$
* Igualando: $\\frac{2}{5} = \\frac{x}{20} \\implies 5x = 40 \\implies x = 8$ **días**.

**E04. Imprenta y Páginas.**
*4 impresoras imprimen 100 libros de 200 páginas en 4 horas. ¿Cuántas horas tardarán 2 impresoras en imprimir 50 libros de 400 páginas?*
**Típ:** El "Efecto" es el trabajo total, aquí sería (Libros $\\cdot$ Páginas).
* Situación 1: $\\frac{4 \\cdot 4}{100 \\cdot 200} = \\frac{16}{20.000}$
* Situación 2: $\\frac{2 \\cdot t}{50 \\cdot 400} = \\frac{2t}{20.000}$
* Como los denominadores son iguales: $16 = 2t \\implies t = 8$ **horas**.

**E05. Dificultad de la Obra (Avanzado).**
Si el efecto tiene una "dificultad", esta va multiplicando al efecto en el denominador. Si la segunda obra es el doble de difícil, $E_2$ se multiplica por 2.""")
    with st.expander("❓ Cuestionario N33", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿En qué parte de la fórmula de "Causa y Efecto" deben ubicarse las máquinas o trabajadores?', 'options': {'A': 'En el denominador (Efecto). \\', 'B': 'En el numerador (Causa). \\', 'C': 'No se incluyen en la fórmula. \\', 'D': 'Sumando al tiempo.'}, 'answer': 'B', 'explanation': 'Las causas son los agentes que ejecutan la acción, van arriba multiplicando.'},
            {'question': 'Si 3 pintores pintan 3 casas en 3 días, ¿cuántos días tardará 1 pintor en pintar 1 casa?', 'options': {'A': '1 día \\', 'B': '3 días \\', 'C': '9 días \\', 'D': '6 días'}, 'answer': 'B', 'explanation': '$\\frac{3 \\cdot 3}{3} = \\frac{1 \\cdot x}{1} \\implies 3 = x$. Sigue tardando 3 días.'},
            {'question': '10 camiones transportan 200 toneladas en 4 viajes. ¿Cuántos viajes deben hacer 5 camiones para transportar 100 toneladas?', 'options': {'A': '2 viajes \\', 'B': '4 viajes \\', 'C': '8 viajes \\', 'D': '10 viajes'}, 'answer': 'B', 'explanation': '$\\frac{10 \\cdot 4}{200} = \\frac{5 \\cdot x}{100} \\implies \\frac{40}{200} = \\frac{5x}{100} \\implies 0,2 = 0,05x \\implies x = 4$.'},
            {'question': '6 grifos llenan 2 piscinas en 10 horas. ¿Cuántas piscinas llenarán 3 grifos en 15 horas?', 'options': {'A': '1,5 piscinas \\', 'B': '2 piscinas \\', 'C': '1 piscina \\', 'D': '3 piscinas'}, 'answer': 'A', 'explanation': '$\\frac{6 \\cdot 10}{2} = \\frac{3 \\cdot 15}{x} \\implies 30 = \\frac{45}{x} \\implies x = 45/30 = 1,5$.'},
            {'question': 'Si 5 personas consumen 20 litros de agua en 2 días, ¿cuántos litros consumirán 10 personas en 5 días?', 'options': {'A': '40 litros \\', 'B': '100 litros \\', 'C': '50 litros \\', 'D': '80 litros'}, 'answer': 'B', 'explanation': '$\\frac{5 \\cdot 2}{20} = \\frac{10 \\cdot 5}{x} \\implies \\frac{10}{20} = \\frac{50}{x} \\implies 0,5 = \\frac{50}{x} \\implies x = 100$.'},
            {'question': 'Para resolver un problema de proporcionalidad compuesta donde una obra tiene el triple de dificultad, ese "3" debe:', 'options': {'A': 'Multiplicar al numerador de la primera situación. \\', 'B': 'Multiplicar al denominador de la situación con mayor dificultad. \\', 'C': 'Restarse al tiempo. \\', 'D': 'Multiplicar a las causas.'}, 'answer': 'B', 'explanation': 'La dificultad hace que el "efecto real" sea mayor, por lo que multiplica al denominador (obra).'},
            {'question': '8 obreros trabajando 9 horas diarias tardan 6 días en hacer una obra. ¿Cuántos días tardarán 4 obreros trabajando 8 horas diarias en hacer la misma obra?', 'options': {'A': '12 días \\', 'B': '13,5 días \\', 'C': '10 días \\', 'D': '15 días'}, 'answer': 'B', 'explanation': '$\\frac{8 \\cdot 9 \\cdot 6}{1} = \\frac{4 \\cdot 8 \\cdot x}{1} \\implies 432 = 32x \\implies x = 13,5$.'},
            {'question': 'En la fórmula $\\frac{C \\cdot T}{E} = k$, si el "Efecto" es "pavimentar una calle", ¿cuál de los siguientes datos es parte del Efecto?', 'options': {'A': 'El número de pavimentadoras. \\', 'B': 'Los metros de calle pavimentados. \\', 'C': 'Los días de trabajo. \\', 'D': 'El sueldo de los trabajadores.'}, 'answer': 'B', 'explanation': 'El efecto es el producto final o la medida de la obra realizada.'},
            {'question': 'Si 2 arañas tejen 2 telas en 2 minutos, ¿cuántas telas tejerán 10 arañas en 10 minutos?', 'options': {'A': '10 telas \\', 'B': '50 telas \\', 'C': '20 telas \\', 'D': '100 telas'}, 'answer': 'B', 'explanation': '$\\frac{2 \\cdot 2}{2} = \\frac{10 \\cdot 10}{x} \\implies 2 = \\frac{100}{x} \\implies x = 50$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n33_quiz")
    with st.expander("✅ Pauta - N33", expanded=False):
        st.markdown("""# ✅ Pauta - Cuestionario N33

1. **B.** Las causas son los agentes que ejecutan la acción, van arriba multiplicando.
2. **B.** $\\frac{3 \\cdot 3}{3} = \\frac{1 \\cdot x}{1} \\implies 3 = x$. Sigue tardando 3 días.
3. **C.** Si arriba multiplicas por $2 \\cdot 2 = 4$, abajo debes multiplicar por 4 para que la fracción no cambie.
4. **B.** $\\frac{10 \\cdot 4}{200} = \\frac{5 \\cdot x}{100} \\implies \\frac{40}{200} = \\frac{5x}{100} \\implies 0,2 = 0,05x \\implies x = 4$.
5. **A.** $\\frac{6 \\cdot 10}{2} = \\frac{3 \\cdot 15}{x} \\implies 30 = \\frac{45}{x} \\implies x = 45/30 = 1,5$.
6. **B.** $\\frac{5 \\cdot 2}{20} = \\frac{10 \\cdot 5}{x} \\implies \\frac{10}{20} = \\frac{50}{x} \\implies 0,5 = \\frac{50}{x} \\implies x = 100$.
7. **B.** La dificultad hace que el "efecto real" sea mayor, por lo que multiplica al denominador (obra).
8. **B.** $\\frac{8 \\cdot 9 \\cdot 6}{1} = \\frac{4 \\cdot 8 \\cdot x}{1} \\implies 432 = 32x \\implies x = 13,5$.
9. **B.** El efecto es el producto final o la medida de la obra realizada.
10. **B.** $\\frac{2 \\cdot 2}{2} = \\frac{10 \\cdot 10}{x} \\implies 2 = \\frac{100}{x} \\implies x = 50$.""")