import streamlit as st
from datetime import datetime
import pytz

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS (UI/UX) :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* Header Azul Responsivo */
    .header-azul { background-color: #3b71ca; padding: 20px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 24px; font-weight: bold; line-height: 1.2; margin-bottom: 10px; }
    .reloj-header { font-size: 18px; font-family: monospace; background: rgba(0,0,0,0.2); padding: 5px 15px; border-radius: 10px; display: inline-block; }
    
    /* Botones y Contenedores */
    div.stButton > button { height: auto !important; min-height: 80px !important; border-radius: 12px !important; border: 1px solid #e0e0e0 !important; transition: all 0.3s ease !important; color: #31333F !important; padding: 15px !important; }
    .clase-box { max-width: 900px; margin: 0 auto; padding: 20px; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería en FCFM*")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada. Uno se llama ayer y otro mañana... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    # ::: Cabeceras (Reloj y Countdown) :::
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="reloj-header">🕒 {ahora.strftime("%H:%M:%S")}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center; border-radius: 0 0 15px 15px; flex-wrap: wrap; gap: 10px;"><div style="font-size: 20px; font-weight: bold;">⏳ Días: {(datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days}</div><div style="font-size: 20px; font-weight: bold;">Hrs: {(datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600}</div></div>', unsafe_allow_html=True)

    st.write("---")

    # ::: Lógica de Ejes (Nivel 0) :::
    if st.session_state.eje_actual is None:
        st.subheader("📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números\nConjuntos y operatoria", key="main_n", use_container_width=True):
            st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra\nFunciones y más", key="main_a", use_container_width=True):
            st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
    
    # ::: Navegación dentro del Eje (Nivel 1) :::
    else:
        n_ejes = ["🏠 Inicio", "🔢 Números", "📉 Álgebra", "📐 Geometría", "📊 Datos"]
        cols_nav = st.columns(len(n_ejes))
        for i, n in enumerate(n_ejes):
            if cols_nav[i].button(n, key=f"nav_top_{i}", use_container_width=True):
                st.session_state.eje_actual = None if n == "🏠 Inicio" else n
                st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        # ::: SECCIÓN: NÚMEROS :::
        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Categorías de Números")
                cs1, cs2, cs3 = st.columns(3)
                if cs1.button("📦 Conjuntos Numéricos", key="cat_conj", use_container_width=True):
                    st.session_state.sub_seccion_actual = "N01"; st.rerun()
                if cs2.button("➕ Operatoria", key="cat_ope", use_container_width=True): pass
                if cs3.button("📝 Ejercitación", key="cat_ejer", use_container_width=True): pass
            
            # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            # ::: CLASE N01: TEORÍA DE CONJUNTOS ::::::::::::::::::::::::::::::
            # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            elif st.session_state.sub_seccion_actual == "N01":
                # Botones de navegación interna
                col_back = st.columns(3)
                if col_back[0].button("⬅️ Volver a Menú", key="back_menu", use_container_width=True):
                    st.session_state.sub_seccion_actual = None; st.rerun()
                if col_back[1].button("➕ Ir a Operatoria", key="go_ope", use_container_width=True): pass
                if col_back[2].button("📝 Ir a Ejercitación", key="go_ejer", use_container_width=True): pass
                
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                
                # ::: BLOQUE 1: MATERIA ORIGINAL :::
                st.markdown("""
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás...
...
---

### 🛡️ 6. Cartografía Visual (Diagramas de Venn-Euler)
Para dominar la PAES, debes "ver" la operación antes de calcularla...

---
> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla". — **Georg Cantor**
""", unsafe_allow_html=True)

                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                # ::: BLOQUE 2: EJEMPLOS PASO A PASO (E02) ::::::::::::::::::::
                # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                # Aquí insertaremos la siguiente parte...

                st.markdown('</div>', unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 5. OTRAS PÁGINAS (PDFs) ::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos PDF")
