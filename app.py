import streamlit as st
from contenidos import CONTENIDOS
from datetime import datetime, date
import os
import base64
from streamlit_gsheets import GSheetsConnection # IMPORTANTE: Debes tener esta librería

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# ==========================================
# CONEXIÓN A GOOGLE SHEETS (EL CEREBRO)
# ==========================================
conn = st.connection("gsheets", type=GSheetsConnection)

def cargar_usuario(user_input, pass_input):
    try:
        df = conn.read(worksheet="Usuarios")
        # Buscamos si existe el usuario y coincide la pass
        user_row = df[(df['User'] == user_input) & (df['Pass'] == str(pass_input))]
        return user_row if not user_row.empty else None
    except:
        return None

def actualizar_xp(user, nueva_xp):
    # Aquí irá la lógica para escribir en el Sheets cuando gane puntos
    pass

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
            border-bottom: 4px solid #00F2FF; /* Azul neón Beaucheff */
        }

        .user-stats {
            background: rgba(255, 255, 255, 0.05);
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #FFD700;
            margin-bottom: 20px;
        }

        .contador-timer {
            background-color: #D32F2F;
            color: white;
            padding: 0.8rem;
            text-align: center;
            border-radius: 10px;
            margin-top: -0.5rem;
            margin-bottom: 2rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# COMPONENTES ESPECIALES (LAGRANGIANITOS)
# ==========================================

def render_radar_habilidades():
    st.markdown("### 📊 Tu Radar de Habilidades")
    # Aquí usaremos Plotly más adelante para dibujar el pentágono
    st.info("Completa quices para ver tu nivel en cada eje temático.")

def modo_detective(clase_id):
    st.markdown("### 🕵️‍♂️ MODO DETECTIVE: ¡Encuentra la pifia!")
    st.warning("El siguiente desarrollo tiene un error sutil. ¿En qué paso está?")
    # Ejemplo de lógica:
    col1, col2, col3 = st.columns(3)
    if col1.button("Paso 1"): st.error("Incorrecto. El Paso 1 es legal.")
    if col2.button("Paso 2"): st.success("¡Efectivo! No puedes dividir por cero.")
    if col3.button("Paso 3"): st.error("Incorrecto. Si el paso 2 fuera real, el 3 estaría bien.")

# ==========================================
# FUNCIONES DE APOYO EXISTENTES
# ==========================================

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
            <p style="color:#FFD700; font-style:italic;">"Conceptos reales para puntajes reales"</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# LÓGICA PRINCIPAL
# ==========================================

def main():
    if 'logged_in' not in st.session_state: st.session_state.logged_in = False
    if 'user_data' not in st.session_state: st.session_state.user_data = None
    if 'page' not in st.session_state: st.session_state.page = "Inicio"

    if not st.session_state.logged_in:
        render_header()
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.markdown("### 🔒 Ingreso a la Plataforma")
            user = st.text_input("Usuario (Tu correo)")
            password = st.text_input("Contraseña", type="password")
            if st.button("🚀 Entrar al Hub", use_container_width=True):
                # VALIDACIÓN CONTRA GOOGLE SHEETS
                res = cargar_usuario(user, password)
                if res is not None:
                    st.session_state.logged_in = True
                    st.session_state.user_data = res.iloc[0].to_dict()
                    st.rerun()
                else:
                    st.error("Usuario o contraseña incorrectos. Revisa el Sheets.")
    else:
        # PANTALLA PRINCIPAL POST-LOGIN
        if st.session_state.page == "Inicio":
            render_header()
            
            # MOSTRAR STATS DEL ALUMNO
            u = st.session_state.user_data
            st.markdown(f"""
                <div class="user-stats">
                    👋 ¡Hola <b>{u['User']}</b>! | 🏆 Nivel: {u['Nivel']} | ✨ XP: {u['XP']}
                </div>
            """, unsafe_allow_html=True)
            
            col_main, col_side = st.columns([0.7, 0.3])
            
            with col_main:
                st.subheader("📚 Tus Desafíos PAES M1")
                materias = list(CONTENIDOS.keys())
                for m in materias:
                    if st.button(f"📘 {m}", use_container_width=True):
                        st.session_state.materia_sel = m
                        st.session_state.page = "Visor"
                        st.rerun()

            with col_side:
                render_radar_habilidades()

        elif st.session_state.page == "Visor":
            # (Tu lógica de visor se mantiene, pero agregamos el Modo Detective al final)
            st.button("🏠 VOLVER AL MENÚ", on_click=lambda: setattr(st.session_state, 'page', 'Inicio'))
            
            # Simulamos el visor que ya tenías...
            st.title(f"Clase: {st.session_state.get('materia_sel', 'Matemáticas')}")
            
            # INSERTAMOS EL MODO DETECTIVE ANTES DEL FINAL
            modo_detective("E02_LOGS")

if __name__ == "__main__":
    main()
