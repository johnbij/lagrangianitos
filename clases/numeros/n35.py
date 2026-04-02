import streamlit as st


def render_N35():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("""
    ## N35: Aplicaciones Maestras de las Proporciones

    ---

    ### 🏛️  Contexto Histórico: El Lenguaje de las Soluciones

    Desde que los alquimistas buscaban la mezcla perfecta en sus laboratorios hasta que los ingenieros ferroviarios calcularon los tiempos de encuentro de los trenes en el siglo XIX, las proporciones dejaron de ser solo números para convertirse en herramientas de precisión. Saber que las velocidades se suman cuando dos objetos van de frente, o que el tiempo de trabajo se reduce cuando sumamos esfuerzos, es lo que permitió coordinar la logística de un mundo en movimiento. Hoy aprenderás a aplicar el álgebra para "hackear" problemas de la vida real que parecen complejos, pero que se rinden ante una buena razón matemática.

    ---

    ### 🕒 El Tiempo en las Razones (Edades)
    Los problemas de edades son comparaciones de razones en distintas líneas de tiempo. El secreto es entender que los años pasan para todos por igual: si tú cumples un año, tu papá también.

    **La Estructura de Resolución:**
    1. **Definir el Presente:** Usa la constante $k$ para las edades actuales (ej: $5k$ y $2k$).
    2. **Viajar en el Tiempo:** Suma años para el "Futuro" o réstalos para el "Pasado". **Importante:** Debes aplicarlo a ambos sujetos por igual.
    3. **Establecer la Nueva Igualdad:** Vincula la nueva situación con la razón que te da el problema para encontrar el valor de $k$.



    ---

    ### 🧪 Mezclas y Concentraciones (Pureza)
    En las mezclas, el concepto clave es que el **soluto** (alcohol, azúcar, sal) es lo único que permanece constante si no lo agregas directamente.

    **Lógica de la Mezcla:**
    * **Componente A:** $\\text{Volumen} \\cdot \\text{Concentración} = \\text{Cantidad Pura}$.
    * **Componente B:** $\\text{Volumen} \\cdot \\text{Concentración} = \\text{Cantidad Pura}$.
    * **Mezcla Final:** Sumas las cantidades puras y las divides por el volumen total de la mezcla para obtener el nuevo equilibrio.

    **Típ:** Si agregas agua pura, la concentración es $0\\%$. Si agregas sustancia pura al 100%, recuerda que en el cálculo usas el valor $1$.

    ---

    ### 🏎️ Móviles: Encuentros y Persecuciones
    Aquí aplicamos la **Velocidad Relativa**, que es la rapidez con la que se acorta la distancia entre dos cuerpos.

    1. **Encuentro (Sentidos opuestos):** Las velocidades se **suman** porque ambos trabajan para cerrar la brecha.
       $$t_{encuentro} = \\frac{\\text{Distancia Total}}{v_1 + v_2}$$
    2. **Persecución (Mismo sentido):** La velocidad del más rápido debe "restarle" la del más lento para saber qué tan rápido lo pilla.
       $$t_{alcance} = \\frac{\\text{Distancia Inicial}}{v_1 - v_2}$$



    ---

    ### 🔢 El Sistema Decimal (Dígitos)
    Un número no es solo una unión de cifras, es una suma de valores posicionales.
    * **Decena ($x$):** Su valor real es $10x$.
    * **Unidad ($y$):** Su valor real es $y$.

    El valor total de un número de dos dígitos se representa como $10x + y$. Si el problema dice que "se invierten los dígitos", el nuevo valor resultante es $10y + x$.

    **Típ:** Si te dicen que la suma de los dígitos es 9, la relación es simplemente $x + y = 9$.

    ---

    ### 🛠️ Rendimiento y Trabajo (Suma de Esfuerzos)
    Cuando dos entidades trabajan juntas, no sumamos sus tiempos (eso daría un tiempo mayor), sumamos sus **capacidades por hora**.

    Si el grifo A tarda $a$ horas y el B tarda $b$ horas, el equilibrio de la tarea conjunta se define como:
    $$\\frac{1}{a} + \\frac{1}{b} = \\frac{1}{T}$$

    --------------
    **Típ:** Si hay un desagüe que quita agua, ese término entra restando en el modelo: $\\frac{1}{a} - \\frac{1}{\\text{desagüe}}$.

    ---

    "Nada se crea, nada se pierde, todo se transforma."  
    — **Antoine Lavoisier**""", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
    ## 🕒 Caso I: El Tiempo en las Razones (Edades)

    El estudio de las edades ha sido un clásico en el álgebra desde los tiempos de Diofanto. Estos problemas no solo miden tu capacidad de plantear ecuaciones, sino tu comprensión de una constante universal: el tiempo fluye igual para todos. Si para una persona pasan 10 años, para la otra también.

    La herramienta definitiva aquí es la **Tabla de Doble Entrada**. Nos permite organizar el "antes", el "ahora" y el "después" sin que las variables se nos mezclen. La lógica fundamental es que la diferencia entre las edades de dos personas es un valor constante en cualquier punto de la historia.

    La relación que rige estos movimientos temporales es:

    $$\\mathbf{Edad \\ Futura = Edad \\ Actual + n \\ (años)}$$

    $$\\mathbf{Edad \\ Pasada = Edad \\ Actual - n \\ (años)}$$

    **Típ:** Anota: Tip... la diferencia de edades nunca cambia. Si hoy te llevo 5 años, en 100 años más (si seguimos vivos) te seguiré llevando 5 años.

    ---

    ### 📝 Ejemplos con Método de Tabla

    **E01. Salto al futuro con razón conocida (Básico)**
    *La razón de las edades de Ana y Beto es $2:3$. En 10 años más, la razón será $3:4$. ¿Qué edad tienen hoy?*

    | Personaje | Hoy (Razón $2:3$) | En 10 años |
    | :--- | :--- | :--- |
    | **Ana** | $2k$ | $2k + 10$ |
    | **Beto** | $3k$ | $3k + 10$ |

    * **Planteamiento:** Usamos la columna del futuro para igualar a la nueva razón:
      $$\\mathbf{\\frac{2k+10}{3k+10} = \\frac{3}{4}}$$
    * **Desarrollo:** $4(2k + 10) = 3(3k + 10) \\implies 8k + 40 = 9k + 30 \\implies \\mathbf{k = 10}$.
    * **Resultado:** Ana tiene $2(10) = \\mathbf{20}$ y Beto $3(10) = \\mathbf{30}$.

    **E02. Encontrar el tiempo transcurrido (Medio)**
    *Un padre tiene 40 años y su hijo 10. ¿En cuántos años más su razón será $2:1$?*

    | Personaje | Hoy | En $x$ años |
    | :--- | :--- | :--- |
    | **Padre** | $40$ | $40 + x$ |
    | **Hijo** | $10$ | $10 + x$ |

    * **Planteamiento:** En el futuro, la razón debe ser $2/1$:
      $$\\mathbf{\\frac{40+x}{10+x} = \\frac{2}{1}}$$
    * **Desarrollo:** $40 + x = 2(10 + x) \\implies 40 + x = 20 + 2x \\implies \\mathbf{x = 20}$.
    * **Resultado:** Deben pasar **20 años**.

    **E03. Uso de la suma de edades (Medio)**
    *Hace 5 años, la razón de dos hermanos era $1:3$. Si hoy sus edades suman 50 años, ¿qué edad tienen hoy?*

    | Personaje | Hace 5 años | Hoy |
    | :--- | :--- | :--- |
    | **Hermano 1** | $1k$ | $k + 5$ |
    | **Hermano 2** | $3k$ | $3k + 5$ |

    * **Planteamiento:** La suma de la columna "Hoy" debe ser 50:
      $$\\mathbf{(k + 5) + (3k + 5) = 50 \\implies 4k + 10 = 50 \\implies k = 10}$$
    * **Resultado:** Hoy tienen $10+5 = \\mathbf{15}$ y $30+5 = \\mathbf{35}$ años.

    **E04. Viaje del presente al pasado (Medio)**
    *La razón actual de dos personas es $5:4$. Hace 10 años, su razón era $3:2$. ¿Cuáles son sus edades?*

    | Personaje | Hace 10 años | Hoy |
    | :--- | :--- | :--- |
    | **Persona A** | $5k - 10$ | $5k$ |
    | **Persona B** | $4k - 10$ | $4k$ |

    * **Planteamiento:** Usamos la columna del pasado para igualar a la razón $3:2$:
      $$\\mathbf{\\frac{5k-10}{4k-10} = \\frac{3}{2}}$$
    * **Desarrollo:** $2(5k - 10) = 3(4k - 10) \\implies 10k - 20 = 12k - 30 \\implies \\mathbf{k = 5}$.
    * **Resultado:** Hoy tienen $5(5) = \\mathbf{25}$ y $4(5) = \\mathbf{20}$ años.

    **E05. EL DESAFÍO: Triple salto temporal (Avanzado)**
    *Tengo el doble de la edad que tú tenías cuando yo tenía la edad que tú tienes. Si cuando tú tengas la edad que yo tengo, la suma de nuestras edades será 63 años, ¿qué edad tengo?*

    | Personaje | Pasado | Hoy | Futuro |
    | :--- | :--- | :--- | :--- |
    | **Yo** | $y$ | $2x$ | $y + (y-x)$ |
    | **Tú** | $x$ | $y$ | $2x + (y-x)$ |

    * **Planteamiento 1 (Diferencia constante):** $\\mathbf{2x - y = y - x \\implies 3x = 2y}$.
    * **Planteamiento 2 (Suma futura):** La diferencia entre edades es $2x - y$. En el futuro sumarán 63:
      $$\\mathbf{(2x) + (2x + (2x-y)) = 63}$$
    * **Resultado:** Resolviendo el sistema, $x = 14$ e $y = 21$. Mi edad es $2x = \\mathbf{28 \\text{ años.}}$""", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""## 🧪 Caso II: Mezclas y Concentraciones

    Históricamente, el estudio de las mezclas nació de la necesidad de alquimistas y boticarios por estandarizar medicamentos y aleaciones de metales. En el contexto escolar, estos problemas miden tu capacidad para entender que en una mezcla hay elementos que cambian (el volumen total) y elementos que permanecen constantes (la cantidad de sustancia pura o soluto).

    La fórmula que domina este mundo es:

    $$\\mathbf{Soluto = Volumen \\ Total \\cdot Porcentaje}$$

    Y para mezclas de dos sustancias ($A$ y $B$):

    $$\\mathbf{(V_A \\cdot P_A) + (V_B \\cdot P_B) = V_{Final} \\cdot P_{Final}}$$

    --------------
    **Típ:** Si agregas agua pura, su porcentaje de soluto es $0\\%$. Si agregas la sustancia pura (sal, azúcar, alcohol), su porcentaje es $100\\%$.

    ---

    ### 📝 Ejemplos con Método de Tabla

    **E06. Mezcla de dos intensidades (Básico)**
    *Se mezclan 2L de jugo al 10% de azúcar con 3L al 20%. ¿Qué porcentaje de azúcar tiene el total?*

    | Componente | Volumen (L) | Porcentaje | Soluto (Puro) |
    | :--- | :--- | :--- | :--- |
    | **Jugo A** | $2$ | $10\\%$ | $0,2$ |
    | **Jugo B** | $3$ | $20\\%$ | $0,6$ |
    | **Final** | $5$ | $x\\%$ | $0,8$ |

    * **Planteamiento:** El soluto final ($0,8$) es el $x\\%$ del volumen total ($5$):
      $$\\mathbf{0,8 = x \\cdot 5}$$
    * **Resultado:** $x = 0,16 \\implies \\mathbf{16\\%}$.

    **E07. Rebajar con agua pura (Medio)**
    *A 8L de una mezcla de sal al 25%, ¿cuánta agua pura (0%) agregar para bajar al 10%?*

    | Componente | Volumen (L) | Porcentaje | Soluto (Puro) |
    | :--- | :--- | :--- | :--- |
    | **Inicial** | $8$ | $25\\%$ | $2$ |
    | **Agua** | $x$ | $0\\%$ | $0$ |
    | **Final** | $8 + x$ | $10\\%$ | $2$ |

    * **Planteamiento:** En la mezcla final, el soluto ($2$) es el $10\\%$ del nuevo volumen:
      $$\\mathbf{2 = 0,10 \\cdot (8 + x)}$$
    * **Resultado:** $2 = 0,8 + 0,1x \\implies \\mathbf{x = 12 \\text{ L.}}$

    **E08. Aumentar pureza con soluto puro (Medio)**
    *¿Cuánta sal pura (100%) agregar a 9L al 20% para que suba al 40%?*

    | Componente | Volumen (L) | Porcentaje | Soluto (Puro) |
    | :--- | :--- | :--- | :--- |
    | **Inicial** | $9$ | $20\\%$ | $1,8$ |
    | **Sal Pura** | $x$ | $100\\%$ | $x$ |
    | **Final** | $9 + x$ | $40\\%$ | $1,8 + x$ |

    * **Planteamiento:** $\\mathbf{1,8 + x = 0,40(9 + x)}$
    * **Resultado:** $1,8 + x = 3,6 + 0,4x \\implies 0,6x = 1,8 \\implies \\mathbf{x = 3 \\text{ L.}}$

    **E09. Evaporación de líquido (Medio-Avanzado)**
    *De 10L de alcohol al 20% se evaporan 2L de agua. ¿Nueva concentración?*

    | Estado | Volumen (L) | Porcentaje | Soluto (Puro) |
    | :--- | :--- | :--- | :--- |
    | **Inicial** | $10$ | $20\\%$ | $2$ |
    | **Evaporado** | $-2$ | $0\\%$ | $0$ |
    | **Final** | $8$ | $x\\%$ | $2$ |

    * **Planteamiento:** $\\mathbf{2 = x \\cdot 8}$
    * **Resultado:** $x = 0,25 \\implies \\mathbf{25\\%}$.

    **E10. EL DESAFÍO: Mezcla con incógnitas dobles (Avanzado)**
    *Un químico tiene una solución al 30% y otra al 80%. ¿Cuántos litros de cada una debe mezclar para obtener 100L al 50%?*

    | Componente | Volumen (L) | Porcentaje | Soluto (Puro) |
    | :--- | :--- | :--- | :--- |
    | **Sol. A** | $x$ | $30\\%$ | $0,3x$ |
    | **Sol. B** | $100 - x$ | $80\\%$ | $0,8(100 - x)$ |
    | **Final** | $100$ | $50\\%$ | $50$ |

    * **Planteamiento:** $\\mathbf{0,3x + 0,8(100 - x) = 50}$
    * **Desarrollo:** $0,3x + 80 - 0,8x = 50 \\implies 30 = 0,5x \\implies x = 60$.
    * **Resultado:** Necesita **60L al 30% y 40L al 80%.**""", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""## 🏎️ Caso III: Móviles (Encuentro y Alcance)

    Desde que el ser humano empezó a desplazarse, calcular el tiempo de llegada ha sido vital. Estos problemas se basan en la cinemática básica aplicada al álgebra. La dificultad real es entender cómo interactúan dos cuerpos que se mueven al mismo tiempo. El concepto clave aquí es la **Velocidad Relativa**.

    La relación fundamental que usaremos en cada fila de nuestra tabla es:

    $$\\mathbf{Distancia = Velocidad \\cdot Tiempo}$$

    De la cual despejaremos el tiempo según necesitemos:

    $$\\mathbf{Tiempo = \\frac{Distancia}{Velocidad}}$$

    ---------------

    **Típ:** En problemas de **Encuentro**, sumamos las velocidades. En problemas de **Alcance**, restamos la velocidad del más rápido menos la del más lento.

    ---

    ### 📝 Ejemplos con Método de Tabla

    **E11. Encuentro frontal (Básico)**
    *Dos autos están a 500km de distancia. El Auto A va a 60 km/h y el Auto B a 40 km/h. ¿En cuánto tiempo se encuentran?*

    | Móvil | Velocidad | Tiempo | Distancia |
    | :--- | :--- | :--- | :--- |
    | **Auto A** | $60$ | $t$ | $60t$ |
    | **Auto B** | $40$ | $t$ | $40t$ |
    | **Total** | $-$ | $-$ | **500** |

    * **Planteamiento:** La suma de las distancias es la separación inicial:
      $$\\mathbf{60t + 40t = 500 \\implies 100t = 500 \\implies t = 5}$$
    * **Resultado:** Se encuentran en **5 horas**.

    **E12. Alcance por persecución (Medio)**
    *Un ladrón huye a 80 km/h. Una patrulla sale 60km detrás a 100 km/h. ¿Cuánto tarda en alcanzarlo?*

    | Móvil | Velocidad | Tiempo | Distancia |
    | :--- | :--- | :--- | :--- |
    | **Ladrón** | $80$ | $t$ | $80t$ |
    | **Patrulla** | $100$ | $t$ | $100t$ |

    * **Planteamiento:** La patrulla recorre lo mismo que el ladrón más la ventaja:
      $$\\mathbf{100t = 80t + 60 \\implies 20t = 60 \\implies t = 3}$$
    * **Resultado:** Lo alcanza en **3 horas**.

    **E13. Diferencia de tiempos (Medio)**
    *Dos personas van al mismo lugar. Una a 4 km/h y otra a 5 km/h. La primera tarda 1 hora más que la segunda. ¿Cuál es la distancia al lugar?*

    | Persona | Velocidad | Tiempo | Distancia |
    | :--- | :--- | :--- | :--- |
    | **Lenta** | $4$ | $t + 1$ | $4(t + 1)$ |
    | **Rápida** | $5$ | $t$ | $5t$ |

    * **Planteamiento:** Como la distancia es la misma para ambos:
      $$\\mathbf{4(t + 1) = 5t \\implies 4t + 4 = 5t \\implies t = 4}$$
    * **Resultado:** Distancia = $5 \\cdot 4 = \\mathbf{20 \\text{ km.}}$

    **E14. Cruce de Tren (Medio-Avanzado)**
    *Un tren de 100m de largo viaja a 20 m/s y cruza un túnel de 300m. ¿Cuánto tarda en pasar completamente?*

    | Elemento | Distancia Total | Velocidad |
    | :--- | :--- | :--- |
    | **Cruce** | $100 + 300 = 400$ | $20$ |

    * **Planteamiento:** $\\mathbf{T = \\frac{400}{20}}$
    * **Resultado:** Tarda **20 segundos.**

    **E15. EL DESAFÍO: Encuentro con desfase temporal (Avanzado)**
    *Las ciudades A y B están a 300km. Un bus sale de A a las 8:00 a 60 km/h hacia B. Un auto sale de B a las 9:00 a 90 km/h hacia A. ¿A qué hora se encuentran?*

    | Móvil | Velocidad | Tiempo | Distancia |
    | :--- | :--- | :--- | :--- |
    | **Bus** | $60$ | $t$ | $60t$ |
    | **Auto** | $90$ | $t - 1$ | $90(t - 1)$ |

    * **Planteamiento:** $\\mathbf{60t + 90(t - 1) = 300}$
    * **Desarrollo:** $150t - 90 = 300 \\implies 150t = 390 \\implies t = 2,6 \\text{ h.}$
    * **Conversión:** $0,6$ horas son $36$ minutos. Tiempo total: $2$h $36$min.
    * **Resultado:** Salida (8:00) + 2:36 = **10:36 horas.**""", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""## 🔢 Caso IV: Sistema Decimal (Dígitos)

    Nuestro sistema numérico es posicional y de base 10. Esto significa que un dígito no vale por lo que "parece", sino por "donde está". No es lo mismo un 7 en la unidad que un 7 en la decena. Debemos descomponer el número según su valor posicional para poder operar algebraicamente.

    Un número de dos cifras se expresa correctamente como:

    $$\\mathbf{Valor = 10x + y}$$

    Donde $x$ es la decena e $y$ la unidad. Si invertimos sus cifras, el valor es:

    $$\\mathbf{Valor \\ Invertido = 10y + x}$$

    **Típ:** Anota: Tip... ten cuidado al leer si el problema te pide el número original, la suma de sus dígitos o el producto de los mismos.

    ---

    ### 📝 Ejemplos con Método de Tabla

    **E16. Suma y relación (Básico)**
    *La suma de los dígitos de un número de dos cifras es 9. Si la unidad es el doble de la decena, ¿cuál es el número?*

    | Posición | Dígito | Relación |
    | :--- | :--- | :--- |
    | **Decena** | $x$ | $x$ |
    | **Unidad** | $y$ | $2x$ |

    * **Planteamiento:** $\\mathbf{x + 2x = 9 \\implies 3x = 9 \\implies x = 3}$
    * **Resultado:** Decena 3, Unidad 6 $\\implies$ Número = **36**.

    **E17. Inversión por resta (Medio)**
    *Un número de dos cifras excede en 45 unidades al número que resulta de invertir sus cifras. ¿Cuál es la diferencia entre sus dígitos?*

    | Estado | Valor |
    | :--- | :--- |
    | **Original** | $10x + y$ |
    | **Invertido** | $10y + x$ |

    * **Planteamiento:** $\\mathbf{(10x + y) - (10y + x) = 45}$
    * **Desarrollo:** $\\mathbf{9x - 9y = 45 \\implies x - y = 5}$.
    * **Resultado:** La diferencia es **5**.

    **E18. Múltiplo de la suma (Medio)**
    *Un número de dos cifras es igual a 7 veces la suma de sus dígitos. Encuentra un número que cumpla esto.*

    | Atributo | Expresión |
    | :--- | :--- |
    | **Número** | $10x + y$ |
    | **Suma** | $x + y$ |

    * **Planteamiento:** $\\mathbf{10x + y = 7(x + y)}$
    * **Resultado:** $10x + y = 7x + 7y \\implies 3x = 6y \\implies \\mathbf{x = 2y}$ (Ejemplo: **21**).

    **E19. Unidad excede a decena (Medio)**
    *La suma de los dígitos es 13. Si la unidad excede a la decena en 3, ¿cuál es el número?*

    | Posición | Dígito |
    | :--- | :--- |
    | **Decena** | $x$ |
    | **Unidad** | $x + 3$ |

    * **Planteamiento:** $\\mathbf{x + (x + 3) = 13 \\implies 2x = 10 \\implies x = 5}$
    * **Resultado:** Decena 5, Unidad 8 $\\implies$ **58**.

    **E20. EL DESAFÍO: Sistema con inversión (Avanzado)**
    *La suma de los dígitos de un número es 12. Si se invierten los dígitos, el nuevo número es 18 unidades menor que el original. ¿Cuál es el producto de sus dígitos?*

    * **Sistema:**
      1) $\\mathbf{x + y = 12}$
      2) $\\mathbf{(10y + x) = (10x + y) - 18 \\implies 9x - 9y = 18 \\implies x - y = 2}$
    * **Resolución:** Al sumar las ecuaciones: $2x = 14 \\implies x = 7$. Luego $y = 5$.
    * **Resultado:** El número es 75, el producto de sus dígitos es **35**.""", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""## 🛠️ Caso V: Rendimiento y Trabajo

    Este es el caso más contraintuitivo. Lo que sumamos no son los tiempos, sino el "Rendimiento" o "Capacidad", que es cuánto trabajo logra completar cada individuo en un intervalo de tiempo fijo (normalmente una hora). Pensamos en "fracción de obra por hora".

    La ecuación fundamental para dos personas trabajando juntas es:

    $$\\mathbf{\\frac{1}{T_1} + \\frac{1}{T_2} = \\frac{1}{T_{Total}}}$$

    Donde $T$ es el tiempo que tarda cada uno por separado.

    **Típ:** El tiempo final trabajando juntos **siempre** debe ser menor que el tiempo del trabajador más rápido por sí solo.

    ---

    ### 📝 Ejemplos con Método de Tabla

    **E21. Dos obreros (Básico)**
    *Juan tarda 2h en armar un mueble y Pedro tarda 3h. ¿Cuánto tardan trabajando juntos?*

    | Sujeto | Tiempo Total | Capacidad (por hora) |
    | :--- | :--- | :--- |
    | **Juan** | $2$ | $1/2$ |
    | **Pedro** | $3$ | $1/3$ |
    | **Juntos** | $x$ | $1/x$ |

    * **Planteamiento:** $\\mathbf{\\frac{1}{2} + \\frac{1}{3} = \\frac{5}{6}}$
    * **Resultado:** Inverso $\\implies 6/5 = \\mathbf{1,2 \\text{ horas.}}$

    **E22. Llenado y vaciado (Medio)**
    *Una llave llena un estanque en 4h. Una fuga en la base lo vacía en 12h. ¿En cuánto tiempo se llena el estanque si ambos están abiertos?*

    | Sujeto | Capacidad |
    | :--- | :--- |
    | **Llave** | $+1/4$ |
    | **Fuga** | $-1/12$ |
    | **Total** | $1/x$ |

    * **Planteamiento:** $\\mathbf{\\frac{1}{4} - \\frac{1}{12} = \\frac{3-1}{12} = \\frac{2}{12} = \\frac{1}{6}}$
    * **Resultado:** Inverso $\\implies \\mathbf{6 \\text{ horas.}}$

    **E23. Encontrar un tiempo individual (Medio)**
    *Trabajando juntos, un maestro y su ayudante tardan 4h. Si el maestro solo tarda 6h, ¿cuánto tardaría el ayudante solo?*

    | Sujeto | Capacidad |
    | :--- | :--- |
    | **Maestro** | $1/6$ |
    | **Ayudante** | $1/x$ |
    | **Juntos** | $1/4$ |

    * **Planteamiento:** $\\mathbf{\\frac{1}{6} + \\frac{1}{x} = \\frac{1}{4} \\implies \\frac{1}{x} = \\frac{1}{4} - \\frac{1}{6} = \\frac{1}{12}}$
    * **Resultado:** El ayudante solo tarda **12 horas.**

    **E24. Tres llaves (Medio-Avanzado)**
    *Tres llaves tardan 2h, 4h y 8h respectivamente en llenar un contenedor. ¿Cuánto tardan las tres juntas?*

    | Capacidades | Suma |
    | :--- | :--- |
    | $1/2, 1/4, 1/8$ | $\\mathbf{7/8}$ |

    * **Resultado:** Inverso $\\implies 8/7 \\approx \\mathbf{1,14 \\text{ horas.}}$

    **E25. EL DESAFÍO: Rendimiento con avance previo (Avanzado)**
    *Juan tarda 10h en una obra. Trabaja solo 2h y luego se une Pedro, quien solo tardaría 15h. ¿En cuántas horas terminan lo que queda de la obra?*

    1. **Avance Juan:** En 2h hizo $2/10 = 1/5$ de la obra. Falta por hacer $4/5$.
    2. **Capacidad Juntos:** $\\mathbf{\\frac{1}{10} + \\frac{1}{15} = \\frac{5}{30} = \\frac{1}{6}}$.
    3. **Planteamiento:** $\\mathbf{\\frac{1}{6} \\cdot t = \\frac{4}{5}}$ (donde $t$ es el tiempo restante).
    4. **Desarrollo:** $t = \\frac{4 \\cdot 6}{5} = \\frac{24}{5} = 4,8$.
    * **Resultado:** Terminan lo restante en **4,8 horas.**""", unsafe_allow_html=True)
        st.markdown("---")

    with st.expander("❓ Cuestionario N35", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': 'La edad de un padre es el triple de la de su hijo. Si hace 5 años la edad del padre era el cuádruple de la del hijo, ¿cuál es la edad actual del padre?', 'options': {'A': '30 años', 'B': '45 años', 'C': '50 años', 'D': '60 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Dos ciclistas parten de un mismo punto en sentidos opuestos. El primero viaja a 18 km/h y el segundo a 12 km/h. ¿En cuánto tiempo estarán separados por 75 km?', 'options': {'A': '1,5 horas', 'B': '2,0 horas', 'C': '2,5 horas', 'D': '3,0 horas'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un número de dos cifras es tal que la cifra de las decenas excede en 4 a la cifra de las unidades. Si se suma el número con el que resulta de invertir sus cifras, se obtiene 154. ¿Cuál es el número original?', 'options': {'A': '73', 'B': '84', 'C': '95', 'D': '62'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Una llave puede llenar un estanque en 3 horas y otra lo puede hacer en 6 horas. Si se abren ambas simultáneamente, ¿cuánto tiempo tardarán en llenar el estanque?', 'options': {'A': '1 hora', 'B': '2 horas', 'C': '4 horas', 'D': '4,5 horas'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuántos litros de agua pura deben añadirse a 10 litros de una solución de alcohol al 40% para obtener una mezcla que esté al 25%?', 'options': {'A': '4 litros', 'B': '6 litros', 'C': '8 litros', 'D': '10 litros'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Hace 10 años, la razón de las edades de dos personas era 2:1. Si hoy sus edades suman 65 años, ¿qué edad tiene el mayor hoy?', 'options': {'A': '30 años', 'B': '35 años', 'C': '40 años', 'D': '45 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un tren de 150 metros de largo viaja a una velocidad constante de 25 m/s. ¿Cuánto tiempo tarda en atravesar completamente un túnel de 850 metros?', 'options': {'A': '34 segundos', 'B': '40 segundos', 'C': '45 segundos', 'D': '50 segundos'}, 'answer': 'A', 'explanation': ''},
            {'question': 'La suma de las dos cifras de un número es 12. Si el número se divide por la suma de sus cifras, el cociente es 4 y el resto es 3. ¿Cuál es el número?', 'options': {'A': '48', 'B': '75', 'C': '57', 'D': '39'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un maestro puede realizar un trabajo en 10 días y su aprendiz en 15 días. El maestro trabaja solo durante 2 días y luego se le une el aprendiz. ¿En cuántos días más terminarán la obra?', 'options': {'A': '4,2 días', 'B': '4,8 días', 'C': '5,0 días', 'D': '6,0 días'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Se tienen 20 litros de una mezcla de ácido al 15%. ¿Qué cantidad de ácido puro se debe agregar para que la mezcla final tenga una concentración del 32%?', 'options': {'A': '5 litros', 'B': '6 litros', 'C': '7 litros', 'D': '8 litros'}, 'answer': 'A', 'explanation': ''},
            {'question': 'La razón entre las edades de dos personas es 5:3. Si hace 4 años la razón era 2:1, ¿cuántos años sumarán sus edades en 5 años más?', 'options': {'A': '24 años', 'B': '32 años', 'C': '42 años', 'D': '45 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un automóvil sale de la ciudad A hacia la ciudad B a 90 km/h. Simultáneamente, un camión sale de B hacia A a 60 km/h. Si la distancia entre A y B es de 450 km, ¿a qué distancia de la ciudad A se producirá el encuentro?', 'options': {'A': '180 km', 'B': '200 km', 'C': '270 km', 'D': '300 km'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un número consta de dos dígitos cuya suma es 15. Si se intercambian los dígitos, el número resultante es 9 unidades menor que el original. ¿Cuál es el producto de los dígitos del número original?', 'options': {'A': '48', 'B': '54', 'C': '56', 'D': '63'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Tres bombas de agua trabajando juntas pueden llenar una piscina en 2 horas. Si la bomba A sola tarda 6 horas y la bomba B sola tarda 4 horas, ¿cuánto tiempo tardaría la bomba C en llenar la piscina trabajando sola?', 'options': {'A': '8 horas', 'B': '10 horas', 'C': '12 horas', 'D': '15 horas'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Se mezcla café de $5.000 el kilo con café de $8.000 el kilo. Si se desea obtener 30 kg de una mezcla que cueste $6.000 el kilo, ¿cuántos kilos del café más barato se deben utilizar?', 'options': {'A': '10 kg', 'B': '15 kg', 'C': '20 kg', 'D': '25 kg'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Pedro tiene el doble de la edad de su hija. En 12 años más, la edad de Pedro será 1,5 veces la edad de su hija. ¿Qué edad tiene Pedro actualmente?', 'options': {'A': '24 años', 'B': '36 años', 'C': '48 años', 'D': '50 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un maratonista corre a una velocidad de 12 km/h. Si un ciclista parte del mismo punto 30 minutos después a una velocidad de 20 km/h, ¿cuánto tiempo tardará el ciclista en alcanzar al corredor?', 'options': {'A': '30 minutos', 'B': '45 minutos', 'C': '1 hora', 'D': '1 hora 15 min'}, 'answer': 'A', 'explanation': ''},
            {'question': 'En un número de dos cifras, el dígito de las unidades es el triple del dígito de las decenas. Si se le suma 54 al número, los dígitos se invierten. ¿Cuál es la suma de los dígitos de dicho número?', 'options': {'A': '8', 'B': '10', 'C': '12', 'D': '14'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un estanque tiene dos llaves de llenado y un desagüe. La primera llave lo llena en 8 horas, la segunda en 12 horas y el desagüe lo vacía en 6 horas. Si se abren los tres dispositivos a la vez estando el estanque vacío, ¿qué fracción del estanque se llenará en una hora?', 'options': {'A': '1/24', 'B': '5/24', 'C': '1/8', 'D': '1/12'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuántos litros de una solución al 10% de sal deben mezclarse con 5 litros de una solución al 25% para obtener una mezcla al 15%?', 'options': {'A': '5 litros', 'B': '10 litros', 'C': '15 litros', 'D': '20 litros'}, 'answer': 'A', 'explanation': ''},
            {'question': 'La edad de un abuelo es 7 veces la edad de su nieto. Hace 6 años, la edad del abuelo era 13 veces la edad del nieto. ¿Cuántos años faltan para que el nieto cumpla la mayoría de edad (18 años)?', 'options': {'A': '4 años', 'B': '6 años', 'C': '8 años', 'D': '10 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Dos barcos parten de un mismo puerto a las 10:00 AM. El barco A navega hacia el Este a 30 km/h y el barco B hacia el Oeste a 45 km/h. ¿A qué hora la distancia entre ellos será de 225 km?', 'options': {'A': '12:00 PM', 'B': '12:30 PM', 'C': '1:00 PM', 'D': '1:30 PM'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El dígito de las decenas de un número es el doble del dígito de las unidades. Si se restan 27 unidades al número, los dígitos se invierten. ¿Cuál es el número original?', 'options': {'A': '42', 'B': '63', 'C': '84', 'D': '21'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un pintor puede decorar una fachada en 12 días, mientras que su colega tarda 20 días. Si ambos trabajan juntos por 5 días y luego el primer pintor se retira, ¿cuántos días tardará el segundo pintor en terminar lo que falta?', 'options': {'A': '5 días', 'B': '6,6 días', 'C': '7,5 días', 'D': '8,3 días'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Se tienen 400 ml de una loción con un 15% de alcohol. ¿Qué cantidad de alcohol puro se debe agregar para que la concentración suba al 32%?', 'options': {'A': '80 ml', 'B': '100 ml', 'C': '120 ml', 'D': '150 ml'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si al triple de la edad que tendré en 5 años se le resta el doble de la edad que tenía hace 2 años, resulta mi edad actual aumentada en 25. ¿Qué edad tengo?', 'options': {'A': '5 años', 'B': '6 años', 'C': '8 años', 'D': '10 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un mensajero en motocicleta viaja a 60 km/h para entregar un paquete. A mitad de camino se da cuenta de que olvidó un documento y regresa a 80 km/h. Si en total tardó 3,5 horas en ir y volver al punto de partida, ¿a qué distancia estaba del origen cuando decidió regresar?', 'options': {'A': '100 km', 'B': '120 km', 'C': '140 km', 'D': '160 km'}, 'answer': 'A', 'explanation': ''},
            {'question': 'La diferencia entre un número de dos cifras y el que resulta de invertir sus cifras es siempre divisible por:', 'options': {'A': '5', 'B': '7', 'C': '9', 'D': '11'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un depósito se puede llenar mediante un tubo en 2 horas y vaciar por otro en 3 horas. Si el depósito tiene agua hasta la mitad de su capacidad y se abren ambos tubos, ¿en cuánto tiempo se terminará de llenar?', 'options': {'A': '1 hora', 'B': '2 horas', 'C': '3 horas', 'D': '6 horas'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Se mezclan dos tipos de vino: uno de 2.400 pesos el litro y otro de 3.600 pesos el litro. Si la mezcla resultante de 60 litros cuesta 2.900 pesos el litro, ¿cuántos litros del vino más caro se utilizaron?', 'options': {'A': '20 litros', 'B': '25 litros', 'C': '30 litros', 'D': '35 litros'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un padre le dice a su hijo: "Hoy mi edad es el triple de la tuya, pero hace 10 años era el quíntuple". ¿Cuántos años sumarán las edades de ambos en 2 años más?', 'options': {'A': '56 años', 'B': '60 años', 'C': '64 años', 'D': '68 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Dos ciudades A y B distan 400 km. Un bus sale de A hacia B a 80 km/h y, 30 minutos después, sale un auto de B hacia A a 100 km/h. ¿A qué distancia de B se encuentran?', 'options': {'A': '150 km', 'B': '180 km', 'C': '200 km', 'D': '220 km'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Si a un número de dos cifras se le resta el número que resulta de invertir sus cifras, se obtiene el doble de la suma de sus dígitos. Si la suma de sus dígitos es 9, ¿cuál es el número?', 'options': {'A': '54', 'B': '63', 'C': '72', 'D': '81'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un tanque de combustible se llena con dos mangueras. La primera tarda 12 minutos y la segunda 15 minutos. Si se usa una tercera manguera de desagüe, el tanque se llena en 10 minutos. ¿Cuánto tarda la manguera de desagüe en vaciar el tanque sola?', 'options': {'A': '18 minutos', 'B': '20 minutos', 'C': '25 minutos', 'D': '30 minutos'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Se tienen dos lingotes de oro: uno con un 60% de pureza y otro con un 90%. ¿Cuántos gramos del primer lingote se necesitan para obtener 600 g de oro con un 80% de pureza?', 'options': {'A': '150 g', 'B': '200 g', 'C': '300 g', 'D': '400 g'}, 'answer': 'A', 'explanation': ''},
            {'question': 'La edad de una madre es el cuádruple de la de su hijo. En 20 años más, la edad de la madre será el doble de la del hijo. ¿Qué edad tenía la madre cuando nació su hijo?', 'options': {'A': '20 años', 'B': '25 años', 'C': '30 años', 'D': '35 años'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un bote navega en un río cuya corriente tiene una velocidad de 2 km/h. Si el bote tarda el mismo tiempo en recorrer 12 km río abajo que 8 km río arriba, ¿cuál es la velocidad del bote en aguas tranquilas?', 'options': {'A': '6 km/h', 'B': '8 km/h', 'C': '10 km/h', 'D': '12 km/h'}, 'answer': 'A', 'explanation': ''},
            {'question': 'En un número de dos cifras, la cifra de las unidades es el cuadrado de la cifra de las decenas. Si se invierten los dígitos, el número aumenta en 54. ¿Cuál es el número original?', 'options': {'A': '11', 'B': '24', 'C': '39', 'D': '41'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Un equipo de 3 obreros tarda 6 horas en terminar un muro. Si después de 2 horas de trabajo uno de ellos se enferma y los otros dos deben terminar la pega, ¿cuánto tiempo adicional (desde que se fue el compañero) tardarán en terminar?', 'options': {'A': '4 horas', 'B': '5 horas', 'C': '6 horas', 'D': '7 horas'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Se mezclan 30 litros de leche al 2% de grasa con 20 litros de leche al 4% de grasa. Si de la mezcla resultante se retiran 10 litros y se reemplazan por 10 litros de leche descremada (0% grasa), ¿cuál es el porcentaje final de grasa?', 'options': {'A': '2,24%', 'B': '2,40%', 'C': '2,56%', 'D': '2,80%'}, 'answer': 'A', 'explanation': ''}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n35_quiz")
