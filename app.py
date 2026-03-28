import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from streamlit_gsheets import GSheetsConnection
from contenidos import CONTENIDOS

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="Lagrangianitos - M1",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Conexión a Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# ==========================================
# 2. FUNCIONES DE DATOS
# ==========================================

def cargar_usuario(user_input, pass_input):
    try:
        df = conn.read(worksheet="Usuarios", ttl=0)
        # Forzamos string para evitar líos con números en el Excel
        user_row = df[(df['User'].astype(str) == str(user_input)) & 
                      (df['Pass'].astype(str) == str(pass_input))]
        return user_row if not user_row.empty else None
    except Exception:
        return None

def registrar_acceso(usuario):
    try:
        ahora = datetime.now()
        nuevo_log = pd.DataFrame([{
            "User": usuario,
            "Fecha": ahora.strftime("%Y-%m-%d"),
            "Hora": ahora.strftime("%H:%M:%S"),
            "IP_Info": "Acceso Web"
        }])
        df_existente = conn.read(worksheet="Logs_Acceso", ttl=0)
        df_final = pd.concat([df_existente, nuevo_log], ignore_index=True)
        conn.update(worksheet="Logs_Acceso", data=df_final)
    except:
        pass

# ==========================================
# 3. RADAR DE HABILIDADES
# ==========================================
def render_radar(user_email):
    try:
        df_progreso = conn.read(worksheet="Progreso", ttl=0)
        user_prog = df_progreso[(df_progreso['User'] == user_email) & (df_progreso['Completado'] == True)]
        
        # Mapeo exacto a las llaves de tu contenidos.py
        mapping = {
            'Números': 'Números',
            'Álgebra': 'Álgebra y Funciones',
            'Geometría': 'Geometría',
            'Datos': 'Probabilidad y Estadística'
        }
        
        ejes_label = list(mapping.keys())
        puntajes = []

        for label, llave_real in mapping.items():
            # Contar total de clases en contenidos.py para este eje
            subcats = CONTENIDOS["📐 Matemáticas"]["subcategorias"].get(llave_real, {})
            total_clases = len(subcats)
            
            # Contar cuántas ha completado el usuario (basado en el ID de clase)
            hechas = len(user_prog[user_prog['ID_Clase'].isin(subcats.keys())])
            
            progreso = (hechas / total_clases * 100) if total_clases > 0 else 0
            puntajes.append(progreso)

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=puntajes + [puntajes[0]],
            theta=ejes_label + [ejes_label[0]],
            fill='toself',
            fillcolor='rgba(0, 242, 255, 0.3)',
            line=dict(color='#00F2FF', width=2)
        ))

        fig.update_layout(
            polar=dict(
                bgcolor='rgba(0,0,0,0)',
                radialaxis=dict(visible=True, range=[0, 100], color="white", gridcolor="rgba(255,255,255,0.1)"),
                angularaxis=dict(color="white")
            ),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=40, r=40, t=30, b=30)
        )
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.info("🎯 Completa tu primera clase para activar el radar.")

# ==========================================
# 4. INTERFAZ VISUAL (UI)
# ==========================================
def header_principal():
    st.markdown("""
        <div style="background-color: #0E2439; color: white; padding: 1.5rem; text-align: center; border-radius: 15px; border-bottom: 4px solid #00F2FF; margin-bottom: 20px;">
            <h1 style="margin:0; font-size: 2.5rem; font-weight:800; letter-spacing: 2px;">LAGRANGIANITOS</h1>
            <p style="color: #FFD700; font-size: 1.1rem; margin:0;">M1: Conceptos Reales para Puntajes Reales</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 5. LÓGICA DE NAVEGACIÓN
# ==========================================
def main():
    if 'logged_in' not in st.session_state: st.session_state.logged_in = False
    if 'page' not in st.session_state: st.session_state.page = "Inicio"

    # PANTALLA DE LOGIN
    if not st.session_state.logged_in:
        header_principal()
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.form("login_form"):
                st.subheader("🔐 Acceso Alumnos")
                u_input = st.text_input("Usuario (Email)")
                p_input = st.text_input("Contraseña", type="password")
                submit = st.form_submit_button("🚀 INGRESAR", use_container_width=True)
                
                if submit:
                    res = cargar_usuario(u_input, p_input)
                    if res is not None:
                        st.session_state.logged_in = True
                        st.session_state.user_data = res.iloc[0].to_dict()
                        registrar_acceso(u_input)
                        st.rerun()
                    else:
                        st.error("Credenciales incorrectas. Revisa mayúsculas/minúsculas.")

    # PANTALLA POST-LOGIN
    else:
        user = st.session_state.user_data
        
        # --- PÁGINA: INICIO ---
        if st.session_state.page == "Inicio":
            header_principal()
            col_izq, col_der = st.columns([0.6, 0.4])
            
            with col_izq:
                st.title(f"¡Hola, {user['User']}!")
                st.markdown(f"**Rango:** {user['Nivel']} | **Puntos de Experiencia:** {user['XP']} XP")
                st.divider()
                
                st.subheader("📚 Elige tu ruta de hoy:")
                for materia in CONTENIDOS.keys():
                    if st.button(f"{materia}", use_container_width=True):
                        st.session_state.materia_sel = materia
                        st.session_state.page = "Visor"
                        st.rerun()
                
                if str(user['User']).lower() == 'admin':
                    st.divider()
                    if st.button("🕵️‍♂️ MODO DETECTIVE", type="secondary", use_container_width=True):
                        st.session_state.page = "Admin"
                        st.rerun()

            with col_der:
                st.markdown("<h4 style='text-align:center;'>Tu Dominio del Universo PAES</h4>", unsafe_allow_html=True)
                render_radar(user['User'])
                
                st.divider()
                if st.button("🚪 Cerrar Sesión", use_container_width=True):
                    st.session_state.logged_in = False
                    st.rerun()

        # --- PÁGINA: VISOR DE CLASES ---
        elif st.session_state.page == "Visor":
            if st.button("⬅️ Volver al Hub"):
                st.session_state.page = "Inicio"
                st.rerun()
            
            m_sel = st.session_state.materia_sel
            st.header(f"Explorando {m_sel}")
            
            # Selector de Eje y Clase
            ejes = list(CONTENIDOS[m_sel]["subcategorias"].keys())
            col_eje, col_clase = st.columns(2)
            
            with col_eje:
                eje_sel = st.selectbox("🎯 Selecciona un Eje:", ejes)
            
            clases_opciones = CONTENIDOS[m_sel]["subcategorias"][eje_sel]
            with col_clase:
                clase_id = st.selectbox("📖 Selecciona la Clase:", 
                                      list(clases_opciones.keys()), 
                                      format_func=lambda x: clases_opciones[x]["label"])
            
            st.divider()
            
            # Renderizar el contenido de la clase
            if "render" in clases_opciones[clase_id]:
                clases_opciones[clase_id]["render"]()
            else:
                st.info("Esta clase está en preparación. ¡Vuelve pronto!")

        # --- PÁGINA: ADMIN DETECTIVE ---
        elif st.session_state.page == "Admin":
            st.title("🕵️‍♂️ Panel de Control: Rastreo de Pillos")
            if st.button("🏠 Volver al Inicio"):
                st.session_state.page = "Inicio"
                st.rerun()
            
            try:
                df_logs = conn.read(worksheet="Logs_Acceso", ttl=0)
                st.dataframe(df_logs.sort_index(ascending=False), use_container_width=True)
            except:
                st.error("No se encontró la pestaña 'Logs_Acceso'.")

if __name__ == "__main__":
    main()
