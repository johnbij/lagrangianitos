import streamlit as st
from contenidos import CONTENIDOS
from datetime import datetime, date
import os
import base64

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# ==========================================
# CONFIGURACIÓN VISUAL
# ==========================================
LOGO_PATH = "logo.png" 
FECHA_PAES = date(2026, 11, 20) 

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stSidebarNav"] {display: none;}
        .block-container {padding-top: 1rem;}
        
        .paes-header {
            background-color: #0E2439;
            color: white;
            padding: 1.5rem;
            text-align: center;
            border-radius: 15px;
            margin-bottom: 1rem;
        }
        
        .paes-header img {
            max-width: 120px;
            height: auto;
            margin-bottom: 10px;
        }

        .paes-header h1 {
            color: white; 
            font-weight: 800; 
            font-size: clamp(1.2rem, 7vw, 2.5rem);
            margin: 0.5rem 0;
            text-transform: uppercase;
        }
        
        .paes-header .lema { font-style: italic; color: #FFD700; font-size: 0.9rem; }
        
        .contador-timer {
            background-color: #D32F2F;
            color: white;
            padding: 0.8rem;
            text-align: center;
            border-radius: 10px;
            margin-top: -0.5rem;
            margin-bottom: 2rem;
            font-weight: bold;
            display: flex;
            justify-content: space-around;
        }
        
        /* Estilo para el botón de volver */
        .stButton button[kind="secondary"] {
            background-color: #f0f2f6;
            border: 1px solid #dcdfe6;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# FUNCIONES DE APOYO
# ==========================================

def scroll_to_top():
    """Scroll simple sin keys para evitar errores de renderizado."""
    st.components.v1.html(
        "<script>window.parent.document.querySelector('section.main').scrollTo(0,0);</script>",
        height=0
    )

def render_header():
    logo_html = ""
    if os.path.exists(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            logo_html = f'<img src="data:image/png;base64,{data}">'
    else:
        logo_html = '<h1 style="font-size:3rem; margin:0;">🐉</h1>'

    st.markdown(f"""
        <div class="paes-header">
            {logo_html}
            <h1>LAGRANGIANITOS</h1>
            <p class="lema">"Enseñamos conceptos, no solo tricks"</p>
            <p class="info">📍 Santiago • 🕒 {datetime.now().strftime('%H:%M')} • 🚀 Preparación PAES M1</p>
        </div>
    """, unsafe_allow_html=True)

def render_timer():
    hoy = date.today()
    dias = (FECHA_PAES - hoy).days
    st.markdown(f"""
        <div class="contador-timer">
            <span>⏳ Días: {max(0, dias)}</span>
            <span>Hrs: {23 - datetime.now().hour}</span>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# LÓGICA PRINCIPAL
# ==========================================

def main():
    if 'logged_in' not in st.session_state: st.session_state.logged_in = False
    if 'page' not in st.session_state: st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state: st.session_state.materia_sel = None
    if 'eje_sel' not in st.session_state: st.session_state.eje_sel = None
    if 'clase_idx' not in st.session_state: st.session_state.clase_idx = 0

    if not st.session_state.logged_in:
        render_header()
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col2:
            st.markdown("### Ingreso")
            user = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            if st.button("Ingresar", use_container_width=True):
                if user == "admin" and password == "admin":
                    st.session_state.logged_in = True
                    st.rerun()
                else: st.error("Acceso denegado")
    else:
        # --- PÁGINA INICIO ---
        if st.session_state.page == "Inicio":
            render_header()
            render_timer()
            st.subheader("📚 Contenidos del curso M1")
            
            materias = list(CONTENIDOS.keys())
            cols = st.columns(2)
            for i, m in enumerate(materias):
                with cols[i % 2]:
                    if st.button(f"📘 {m}", use_container_width=True, key=f"btn_{m}"):
                        st.session_state.materia_sel = m
                        st.session_state.eje_sel = list(CONTENIDOS[m]["subcategorias"].keys())[0]
                        st.session_state.clase_idx = 0
                        st.session_state.page = "Visor"
                        st.rerun()
            
            st.divider()
            if st.button("🚪 Cerrar Sesión"):
                st.session_state.logged_in = False
                st.rerun()

        # --- PÁGINA VISOR ---
        elif st.session_state.page == "Visor":
            # Botón de volver prominente al inicio del visor
            if st.button("⬅️ VOLVER AL MENÚ PRINCIPAL", use_container_width=True):
                st.session_state.page = "Inicio"
                st.session_state.materia_sel = None
                st.session_state.eje_sel = None
                st.session_state.clase_idx = 0
                st.rerun()

            st.divider()
            
            m_data = CONTENIDOS[st.session_state.materia_sel]
            ejes = list(m_data["subcategorias"].keys())
            
            # Selectores Desplegables
            col_e, col_c = st.columns(2)
            
            with col_e:
                idx_eje = ejes.index(st.session_state.eje_sel) if st.session_state.eje_sel in ejes else 0
                eje_sel = st.selectbox("🎯 Eje Temático:", ejes, index=idx_eje)
                if eje_sel != st.session_state.eje_sel:
                    st.session_state.eje_sel = eje_sel
                    st.session_state.clase_idx = 0
                    st.rerun()

            with col_c:
                clases_dict = m_data["subcategorias"][st.session_state.eje_sel]
                ids_clases = list(clases_dict.keys())
                st.session_state.clase_idx = min(st.session_state.clase_idx, len(ids_clases) - 1)
                
                clase_id = st.selectbox(
                    "📖 Clase:", ids_clases, 
                    index=st.session_state.clase_idx,
                    format_func=lambda x: clases_dict[x]["label"]
                )
                if ids_clases.index(clase_id) != st.session_state.clase_idx:
                    st.session_state.clase_idx = ids_clases.index(clase_id)
                    st.rerun()

            st.divider()
            
            # Contenido de la clase
            if "render" in clases_dict[clase_id]:
                clases_dict[clase_id]["render"]()
            
            st.divider()
            
            # Navegación entre clases
            c1, c2 = st.columns(2)
            with c1:
                if st.session_state.clase_idx > 0:
                    if st.button("⬅️ Clase Anterior", use_container_width=True):
                        st.session_state.clase_idx -= 1
                        st.rerun()
            with c2:
                if st.session_state.clase_idx < len(ids_clases) - 1:
                    if st.button("Siguiente Clase ➡️", use_container_width=True):
                        st.session_state.clase_idx += 1
                        st.rerun()
            
            # Ejecutar scroll después de renderizar contenido
            scroll_to_top()

if __name__ == "__main__":
    main()
