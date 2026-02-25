import streamlit as st
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None

# --- 2. CSS PARA TARJETAS Y LIMPIEZA DE INTERFAZ ---
st.markdown("""
    <style>
    /* Estilo de botones grandes */
    div.stButton > button {
        height: 100px !important;
        border-radius: 12px !important;
        border: 1px solid #e0e0e0 !important;
        transition: all 0.3s ease !important;
    }
    /* Contenedor de la clase para que no se vea "suelto" */
    .clase-container {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #3b71ca;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL (PERFIL) ---
with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería en FCFM*")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])

# --- 4. LÓGICA DE NAVEGACIÓN ---
if menu == "🏠 Dashboard PAES":
    # CABECERAS (Azul y Roja)
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div style="background-color: #3b71ca; padding: 25px; border-radius: 15px 15px 0 0; color: white; position: relative; display: flex; align-items: center; justify-content: center; min-height: 100px;">
            <div style="font-size: 28px; font-weight: bold; text-align: center;">🐉 Lagrangianitos. Tus recursos PAES M1</div>
            <div style="position: absolute; right: 25px; text-align: right;">
                <div style="font-size: 22px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
            </div>
        </div>
        <div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center; border-radius: 0 0 15px 15px;">
            <div style="font-size: 22px; font-weight: bold;">⏳ Días: {(datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days}</div>
            <div style="font-size: 22px; font-weight: bold;">Hrs: {(datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600}</div>
            <div style="font-size: 22px; font-weight: bold;">Min: {((datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 60) % 60}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    if st.session_state.eje_actual is None:
        st.subheader("📚 Selecciona un Eje Temático")
        cols = st.columns(2)
        with cols[0]:
            if st.button("🔢 Números\nConjuntos y operatoria", use_container_width=True):
                st.session_state.eje_actual = "🔢 Números"; st.rerun()
        with cols[1]:
            if st.button("📉 Álgebra\nFunciones y más", use_container_width=True):
                st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
    else:
        # Mini Navegación Superior
        c_nav = st.columns(5)
        nombres = ["🏠 Inicio", "🔢 Números", "📉 Álgebra", "📐 Geometría", "📊 Datos"]
        for i, n in enumerate(nombres):
            if c_nav[i].button(n, key=f"nav_{i}", use_container_width=True):
                st.session_state.eje_actual = None if n == "🏠 Inicio" else n
                st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Categorías de Números")
                cs1, cs2, cs3 = st.columns(3)
                if cs1.button("📦 Conjuntos Numéricos", use_container_width=True):
                    st.session_state.sub_seccion_actual = "N01"; st.rerun()
            
            # --- RENDERIZADO DE LA CLASE N01 ---
            elif st.session_state.sub_seccion_actual == "N01":
                if st.button("⬅️ Volver"):
                    st.session_state.sub_seccion_actual = None; st.rerun()
                
                # Usamos st.container para darle un margen y que no se pegue a los bordes
                with st.container():
                    st.title("🔢 Eje Números")
                    st.subheader("N01: Teoría de Conjuntos - El Lenguaje Maestro")
                    st.divider()
                    
                    st.markdown("""
                    ### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
                    Bienvenido a la primera página de un viaje que no tiene vuelta atrás. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.
                    
                    ### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
                    **Georg Cantor** demostró que el infinito podía ser medido. Su valentía permitió que hoy podamos definir con precisión quirúrgica qué es un número.
                    
                    ### 🛡️ 3. El Marco de Referencia
                    * **El Universo ($\mathcal{U}$):** El todo.
                    * **El Vacío ($\emptyset$):** Nada matemática.
                    * **Pertenencia ($\in$):** Elemento a conjunto.
                    
                    | Operación | Símbolo | Significado |
                    | :--- | :---: | :--- |
                    | **Unión** | $\cup$ | Agrupar todo. |
                    | **Intersección** | $\cap$ | Solo lo repetido. |
                    
                    ### 🛡️ 5. Cardinalidad
                    La cardinalidad ($n$) es el número de elementos únicos.
                    Total de subconjuntos: $2^n$
                    """)
                    
                    st.info("Típ: Si $A \subset B$, entonces $A \cap B = A$ y $A \cup B = B$.")
                    st.divider()
                    st.caption("“En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla.” — Georg Cantor")

elif menu == "📂 Biblioteca de PDFs":
    st.header("Recursos descargables")
