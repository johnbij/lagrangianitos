import streamlit as st
import pandas as pd
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
# 2. FUNCIONES DE DATOS Y PROGRESO
# ==========================================

def cargar_usuario(user_input, pass_input):
    try:
        df = conn.read(worksheet="Usuarios", ttl=0)
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

def registrar_progreso(clase_id, buenas=0, totales=0):
    try:
        usuario_actual = st.session_state.user_data['User']
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        malas = totales - buenas
        nuevo_dato = pd.DataFrame([{
            "User": usuario_actual, "ID_Clase": clase_id, "Completado": True,
            "Buenas": buenas, "Malas": malas, "Timestamp": ahora
        }])
        df_progreso = conn.read(worksheet="Progreso", ttl=0)
        mask = (df_progreso['User'] == usuario_actual) & (df_progreso['ID_Clase'] == clase_id)
        if mask.any():
            df_progreso.loc[mask, ["Buenas", "Malas", "Timestamp"]] = [buenas, malas, ahora]
            df_final = df_progreso
        else:
            df_final = pd.concat([df_progreso, nuevo_dato], ignore_index=True)
        conn.update(worksheet="Progreso", data=df_final)
        return True
    except Exception as e:
        st.error(f"Error al guardar progreso: {e}")
        return False

st.session_state.registrar_progreso = registrar_progreso

# ==========================================
# 3. VISUALIZACIÓN DE RENDIMIENTO
# ==========================================
def render_stats(user_email):
    try:
        df_progreso = conn.read(worksheet="Progreso", ttl=0)
        user_prog = df_progreso[df_progreso['User'] == user_email]
        if user_prog.empty:
            st.info("🎯 Completa tu primera clase para ver tu rendimiento.")
            return

        total_buenas = user_prog['Buenas'].sum()
        total_malas = user_prog['Malas'].sum()
        total_preguntas = total_buenas + total_malas
        p_buenas = (total_buenas / total_preguntas * 100) if total_preguntas > 0 else 0
        p_malas = (total_malas / total_preguntas * 100) if total_preguntas > 0 else 0

        col_ok, col_err = st.columns(2)
        with col_ok:
            st.markdown(f'<div style="background-color: #007BFF; padding: 20px; border-radius: 12px; text-align: center; border: 2px solid #00F2FF;"><p style="margin:0; font-size: 0.9rem; color: white; opacity: 0.9;">ÉXITO TOTAL</p><h2 style="margin:0; color: white; font-size: 2rem;">{p_buenas:.1f}%</h2></div>', unsafe_allow_html=True)
        with col_err:
            st.markdown(f'<div style="background-color: #FF4136; padding: 20px; border-radius: 12px; text-align: center; border: 2px solid #FFAAAA;"><p style="margin:0; font-size: 0.9rem; color: white; opacity: 0.9;">ERROR TOTAL</p><h2 style="margin:0; color: white; font-size: 2rem;">{p_malas:.1f}%</h2></div>', unsafe_allow_html=True)
        st.caption(f"📊 Resumen de {int(total_preguntas)} ejercicios realizados.")
    except:
        st.info("🎯 Estadísticas en camino...")

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
    if 'clase_target' not in st.session_state: st.session_state.clase_target = None

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
                        st.error("Credenciales incorrectas.")
    else:
        user = st.session_state.user_data
        
        if st.session_state.page == "Inicio":
            header_principal()
            col_izq, col_der = st.columns([0.6, 0.4])
            with col_izq:
                st.title(f"¡Hola, {user['User']}!")
                st.markdown(f"**Rango:** {user['Nivel']} | **XP:** {user['XP']} XP")
                st.divider()
                for materia in CONTENIDOS.keys():
                    if st.button(f"{materia}", key=f"btn_{materia}", use_container_width=True):
                        st.session_state.materia_sel = materia
                        st.session_state.page = "Visor"
                        st.session_state.clase_target = None 
                        st.rerun()
                if str(user['User']).lower() == 'admin':
                    if st.button("🕵️‍♂️ MODO DETECTIVE", use_container_width=True):
                        st.session_state.page = "Admin"; st.rerun()

            with col_der:
                st.markdown("<h4 style='text-align:center;'>Tu Rendimiento</h4>", unsafe_allow_html=True)
                render_stats(user['User'])
                if st.button("🚪 Cerrar Sesión", use_container_width=True):
                    st.session_state.logged_in = False; st.rerun()

        elif st.session_state.page == "Visor":
            if st.button("⬅️ Volver al Hub"):
                st.session_state.page = "Inicio"; st.rerun()
            
            m_sel = st.session_state.materia_sel
            ejes = list(CONTENIDOS[m_sel]["subcategorias"].keys())
            
            col_eje, col_clase = st.columns(2)
            with col_eje:
                eje_sel = st.selectbox("🎯 Eje:", ejes)
            
            clases_dict = CONTENIDOS[m_sel]["subcategorias"][eje_sel]
            lista_ids = list(clases_dict.keys())

            # Logica de salto de clase corregida
            if st.session_state.clase_target not in lista_ids:
                st.session_state.clase_target = lista_ids[0]

            with col_clase:
                clase_id = st.selectbox(
                    "📖 Clase:", lista_ids, 
                    index=lista_ids.index(st.session_state.clase_target),
                    format_func=lambda x: clases_dict[x]["label"],
                    key="clase_selector"
                )
                st.session_state.clase_target = clase_id # Sincronizar por si el usuario cambia el select manual

            st.divider()
            if "render" in clases_dict[clase_id]:
                clases_dict[clase_id]["render"]()
                st.divider()
                indice_actual = lista_ids.index(clase_id)
                if indice_actual < len(lista_ids) - 1:
                    if st.button(f"Siguiente Clase: {clases_dict[lista_ids[indice_actual+1]]['label']} ➡️", use_container_width=True):
                        st.session_state.clase_target = lista_ids[indice_actual + 1]
                        st.rerun()
                else:
                    st.success("✨ ¡Eje completado!")
            else:
                st.info("Próximamente...")

        elif st.session_state.page == "Admin":
            st.title("🕵️‍♂️ Panel de Control")
            if st.button("🏠 Inicio"): st.session_state.page = "Inicio"; st.rerun()
            df_logs = conn.read(worksheet="Logs_Acceso", ttl=0)
            st.dataframe(df_logs.sort_index(ascending=False), use_container_width=True)

if __name__ == "__main__":
    main()
