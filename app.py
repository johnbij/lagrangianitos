import streamlit as st
from contenidos import CONTENIDOS
from datetime import datetime, date
import os
import base64
from streamlit_gsheets import GSheetsConnection

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# ==========================================
# CONEXIÓN A GOOGLE SHEETS (EL CEREBRO)
# ==========================================
conn = st.connection("gsheets", type=GSheetsConnection)

def cargar_usuario(user_input, pass_input):
    try:
        # ttl=0 fuerza a la app a leer el Sheets en tiempo real (sin caché)
        df = conn.read(worksheet="Usuarios", ttl=0)
        # Convertimos todo a string para evitar atados con formatos de celda
        user_row = df[(df['User'].astype(str) == str(user_input)) & 
                      (df['Pass'].astype(str) == str(pass_input))]
        return user_row if not user_row.empty else None
    except Exception as e:
        st.error(f"Error de conexión con Sheets: {e}")
        return None

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
        .paes-header h1 { color: white; font-weight: 800; margin: 0.5rem 0; text-transform: uppercase; }
        .contador-timer {
            background-color: #D32F2F;
            color: white;
            padding: 0.8rem;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 2rem;
            font-weight: bold;
        }
        .btn-volver button { background-color: #0E2439 !important; color: white !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

def render_header():
    logo_html = ""
    if os.path.exists(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            logo_html = f'<img src="data:image/png;base64,{data}" style="max-width:120px;">'
    else:
        logo_html = '<h1 style="font-size:3rem; margin:0;">🐉</h1>'

    st.markdown(f"""
        <div class="paes-header">
            {logo_html}
            <h1>LAGRANGIANITOS</h1>
            <p style="color: #FFD700; font-style: italic;">"Enseñamos conceptos, no solo tricks"</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# LÓGICA PRINCIPAL
# ==========================================

def main():
    # Inicialización de estados
    if 'logged_in' not in st.session_state: st.session_state.logged_in = False
    if 'user_data' not in st.session_state: st.session_state.user_data = None
    if 'page' not in st.session_state: st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state: st.session_state.materia_sel = None
    if 'eje_sel' not in st.session_state: st.session_state.eje_sel = None
    if 'clase_idx' not in st.session_state: st.session_state.clase_idx = 0
    if 'do_scroll' not in st.session_state: st.session_state.do_scroll = False

    if not st.session_state.logged_in:
        render_header()
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.markdown("### 🔐 Ingreso Alumnos")
            user = st.text_input("Usuario (Email)")
            password = st.text_input("Contraseña", type="password")
            if st.button("🚀 Entrar al Hub", use_container_width=True):
                res = cargar_usuario(user, password)
                if res is not None:
                    st.session_state.logged_in = True
                    st.session_state.user_data = res.iloc[0].to_dict()
                    st.rerun()
                else:
                    st.error("Acceso denegado. Revisa tus datos en el Sheets.")
    else:
        if st.session_state.page == "Inicio":
            render_header()
            
            # Info del Alumno desde el Sheets
            u = st.session_state.user_data
            st.info(f"👋 ¡Hola **{u['User']}**! | 🏆 Nivel: {u['Nivel']} | ✨ XP: {u['XP']}")
            
            st.subheader("📚 Contenidos M1")
            materias = list(CONTENIDOS.keys())
            cols = st.columns(2)
            for i, m in enumerate(materias):
                with cols[i % 2]:
                    if st.button(f"📘 {m}", use_container_width=True, key=f"btn_{m}"):
                        st.session_state.materia_sel = m
                        st.session_state.eje_sel = list(CONTENIDOS[m]["subcategorias"].keys())[0]
                        st.session_state.clase_idx = 0
                        st.session_state.page = "Visor"
                        st.session_state.do_scroll = True
                        st.rerun()

            st.divider()
            if st.button("🚪 Cerrar Sesión"):
                for key in list(st.session_state.keys()): del st.session_state[key]
                st.rerun()

        elif st.session_state.page == "Visor":
            # Manejo de scroll automático
            if st.session_state.do_scroll:
                st.markdown('<a name="top-anchor"></a>', unsafe_allow_html=True)
                st.markdown('<meta http-equiv="refresh" content="0;url=#top-anchor">', unsafe_allow_html=True)
                st.session_state.do_scroll = False
            
            if st.button("🏠 VOLVER AL MENÚ", use_container_width=True):
                st.session_state.page = "Inicio"
                st.rerun()

            st.divider()

            # Lógica de navegación de clases (tu código original)
            m_data = CONTENIDOS[st.session_state.materia_sel]
            ejes = list(m_data["subcategorias"].keys())
            idx_eje = ejes.index(st.session_state.eje_sel) if st.session_state.eje_sel in ejes else 0
            eje_sel = st.selectbox("🎯 Eje Temático:", ejes, index=idx_eje)

            if eje_sel != st.session_state.eje_sel:
                st.session_state.eje_sel = eje_sel
                st.session_state.clase_idx = 0
                st.session_state.do_scroll = True
                st.rerun()

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
                st.session_state.do_scroll = True
                st.rerun()

            st.divider()
            # Renderizado de la clase desde contenidos.py
            if "render" in clases_dict[clase_id]:
                clases_dict[clase_id]["render"]()

            st.divider()
            c1, c2 = st.columns(2)
            with c1:
                if st.session_state.clase_idx > 0:
                    if st.button("⬅️ Anterior", use_container_width=True):
                        st.session_state.clase_idx -= 1
                        st.session_state.do_scroll = True
                        st.rerun()
            with c2:
                if st.session_state.clase_idx < len(ids_clases) - 1:
                    if st.button("Siguiente ➡️", use_container_width=True):
                        st.session_state.clase_idx += 1
                        st.session_state.do_scroll = True
                        st.rerun()

if __name__ == "__main__":
    main()
