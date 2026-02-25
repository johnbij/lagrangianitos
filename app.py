import streamlit as st
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# Estado para controlar la navegación
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None

# --- 2. INYECCIÓN DE CSS (TARJETAS PRO) ---
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        background-color: white !important;
        padding: 10px !important;
        border-radius: 0 0 15px 15px !important;
    }
    div.stButton > button {
        height: 110px !important;
        border-radius: 15px !important;
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        padding: 20px !important;
        white-space: pre-wrap !important;
        text-align: left !important;
        margin-bottom: 15px !important;
        color: #31333F !important;
    }
    div.stButton > button:hover {
        border-color: #3b71ca !important;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1) !important;
        transform: translateY(-2px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería en FCFM Universidad de Chile*")
    st.markdown("### Redes Sociales \n- [📸 Instagram: @lagrangianitos](https://instagram.com/lagrangianitos)")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("""
    Sólo existen dos días en el año en los que no se puede hacer nada. Uno se llama ayer y otro mañana. 
    Por lo tanto, hoy es el día ideal para amar, crecer, hacer y principalmente vivir. 
    Dalai Lama
    """)

# --- 4. LÓGICA DE NAVEGACIÓN ---
if menu == "🏠 Dashboard PAES":
    # Cabecera Azul (Título 28px centrado + Reloj Santiago)
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div style="background-color: #3b71ca; padding: 25px; border-radius: 15px 15px 0 0; color: white; position: relative; display: flex; align-items: center; justify-content: center; min-height: 100px;">
            <div style="font-size: 28px; font-weight: bold; text-align: center; padding: 0 120px; line-height: 1.2;">
                🐉 Lagrangianitos. Tus recursos PAES M1
            </div>
            <div style="position: absolute; right: 25px; text-align: right;">
                <div style="font-size: 14px; opacity: 0.9;">Santiago, Chile</div>
                <div style="font-size: 22px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Cabecera Roja (Countdown con Minutos - Tamaño 22px)
    fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    faltan = fecha_paes - ahora
    st.markdown(f"""
        <div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center;">
            <div style="font-size: 22px; font-weight: bold;">⏳ Días: {faltan.days}</div>
            <div style="font-size: 22px; font-weight: bold;">Hrs: {faltan.seconds // 3600}</div>
            <div style="font-size: 22px; font-weight: bold;">Min: {(faltan.seconds // 60) % 60}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    if st.session_state.eje_actual is None:
        # PÁGINA A: MENÚ DE EJES
        st.subheader("📚 Selecciona un Eje Temático")
        ejes_info = {"🔢 Números": "Conjuntos, operatoria, potencias, raíces y razones.", "📉 Álgebra": "Operatoria algebraica y funciones", "📐 Geometría": "Teoremas, perímetros, áreas y volúmenes. Vectores", "📊 Datos y Azar": "Medidas de tendencia y tablas. Azar, eventos y combinatoria."}
        for nombre, desc in ejes_info.items():
            if st.button(f"{nombre}\n{desc}", key=f"btn_{nombre}", use_container_width=True):
                st.session_state.eje_actual = nombre
                st.rerun()
    else:
        # PÁGINA B: DENTRO DEL EJE (Navegación superior)
        col_nav = st.columns([1, 1, 1, 1, 1])
        botones = ["🏠 Inicio", "🔢 Números", "📉 Álgebra", "📐 Geometría", "📊 Datos"]
        for i, texto in enumerate(botones):
            with col_nav[i]:
                if st.button(texto, key=f"nav_{i}", use_container_width=True):
                    st.session_state.eje_actual = None if texto == "🏠 Inicio" else (f"📊 Datos y Azar" if texto == "📊 Datos" else f"{texto}")
                    st.session_state.sub_seccion_actual = None
                    st.rerun()

        st.write("---")
        
        # Lógica de SUB-SECCIONES en Números
        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Selecciona una categoría:")
                c1, c2, c3 = st.columns(3)
                with c1:
                    if st.button("📦 Conjuntos Numéricos", key="sub_conj", use_container_width=True):
                        st.session_state.sub_seccion_actual = "Conjuntos"
                        st.rerun()
                with c2:
                    if st.button("➕ Operatoria", key="sub_ope", use_container_width=True): pass
                with c3:
                    if st.button("📝 Ejercitación", key="sub_ejer", use_container_width=True): pass
            
            # --- DESPLIEGUE DE LA CLASE N01 ---
            elif st.session_state.sub_seccion_actual == "Conjuntos":
                if st.button("⬅️ Volver a Categorías"):
                    st.session_state.sub_seccion_actual = None
                    st.rerun()
                
                st.markdown("""
                # <span style="color:darkblue">Eje Números</span>
                ## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

                ---

                ### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
                Bienvenido a la primera página de un viaje que no tiene vuelta atrás. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.

                Este eje de **Números** no se trata de hacer cuentas rápidas; se trata de aprender a clasificar el caos. Durante las próximas unidades, descubriremos que los números habitan en estructuras organizadas llamadas **Conjuntos**.

                ---

                ### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
                A finales del siglo XIX, **Georg Cantor** se atrevió a decir que el infinito no era un muro infranqueable, sino un jardín que podía ser medido. Su valentía permitió que hoy podamos definir con precisión quirúrgica qué es un número.

                ---

                ### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
                * **El Universo ($\mathcal{U}$):** Contexto total que contiene todos los elementos.
                * **El Vacío ($\emptyset$ o $\{\}$):** Un conjunto sin elementos.
                * **Pertenencia ($\in$):** Relación de un **elemento** hacia un conjunto.
                * **Subconjunto ($\subset$):** $A \subset B$ si **todos** los elementos de $A$ están también en $B$.

                > **Típ:** ... Si $A \subset B$, entonces $A \cap B = A$ y $A \cup B = B$.

                ---

                ### 🛡️ 4. Operaciones de "1000 Puntos"

                | Operación | Símbolo | Significado Lógico | Carpintería Técnica |
                | :--- | :---: | :--- | :--- |
                | **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ | Agrupar todos los elementos. |
                | **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ | Solo los repetidos. |
                | **Diferencia** | $-$ | $x \in A$ pero $x \notin B$ | Borrar lo del segundo al primero. |
                | **Complemento** | $A^c$ | $x \in \mathcal{U}$ pero $x \notin A$ | Lo que le falta para ser Universo. |

                ---

                ### 🛡️ 5. Cardinalidad y Conjunto Potencia
                * **Cardinalidad ($n$):** Número de elementos únicos.
                * **Regla de Oro:** $\#(A \cup B) = \#A + \#B - \#(A \cap B)$.
                * **Total de Subconjuntos:** $2^n$

                ---

                > "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
                > — **Georg Cantor**
                """, unsafe_allow_html=True)
        else:
            st.header(st.session_state.eje_actual)
            st.info("Contenido en desarrollo.")
