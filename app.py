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
    except: return None

def registrar_acceso(usuario):
    try:
        ahora = datetime.now()
        nuevo_log = pd.DataFrame([{"User": usuario, "Fecha": ahora.strftime("%Y-%m-%d"), "Hora": ahora.strftime("%H:%M:%S"), "IP_Info": "Acceso Web"}])
        df_existente = conn.read(worksheet="Logs_Acceso", ttl=0)
        conn.update(worksheet="Logs_Acceso", data=pd.concat([df_existente, nuevo_log], ignore_index=True))
    except: pass

def registrar_progreso(clase_id, buenas=0, totales=0):
    try:
        usuario_actual = st.session_state.user_data['User']
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        malas = totales - buenas
        df_progreso = conn.read(worksheet="Progreso", ttl=0)
        mask = (df_progreso['User'] == usuario_actual) & (df_progreso['ID_Clase'] == clase_id)
        if mask.any():
            df_progreso.loc[mask, ["Buenas", "Malas", "Timestamp"]] = [buenas, malas, ahora]
        else:
            nuevo = pd.DataFrame([{"User": usuario_actual, "ID_Clase": clase_id, "Completado": True, "Buenas": buenas, "Malas": malas, "Timestamp": ahora}])
            df_progreso = pd.concat([df_progreso, nuevo], ignore_index=True)
        conn.update(worksheet="Progreso", data=df_progreso)
        return True
    except: return False

st.session_state.registrar_progreso = registrar_progreso

# ==========================================
# 3. VISUALIZACIÓN DE RENDIMIENTO
# ==========================================
def render_stats(user_email):
    try:
        df_p = conn.read(worksheet="Progreso", ttl=0)
        user_p = df_p[df_p['User'] == user_email]
        if user_p.empty:
            st.info("🎯 ¡Comienza tu primera clase!")
            return
        tb, tm = user_p['Buenas'].sum(), user_p['Malas'].sum()
        total = tb + tm
        pb = (tb/total*100) if total > 0 else 0
        pm = (tm/total*100) if total > 0 else 0
        c1, c2 = st.columns(2)
        c1.markdown(f'<div style="background-color:#007BFF;padding:15px;border-radius:10px;text-align:center;border:2px solid #00F2FF;"><p style="margin:0;color:white;font-size:0.8rem;">ÉXITO</p><h3 style="margin:0;color:white;">{pb:.1f}%</h3></div>', unsafe_allow_html=True)
        c2.markdown(f'<div style="background-color:#FF4136;padding:15px;border-radius:10px;text-align:center;border:2px solid #FFAAAA;"><p style="margin:0;color:white;font-size:0.8rem;">ERROR</p><h3 style="margin:0;color:white;">{pm:.1f}%</h3></div>', unsafe_allow_html=True)
    except: pass

def header_principal():
    st.markdown('<div style="background-color:#0E2439;color:white;padding:1.5rem;text-align:center;border-radius:15px;border-bottom:4px solid #00F2FF;margin-bottom:20px;"><h1 style="margin:0;font-size:2.2rem;font-weight:800;">LAGRANGIANITOS</h1><p style="color:#FFD700;margin:0;">M1: Conceptos Reales para Puntajes Reales</p></div>', unsafe_allow_html=True)

# ==========================================
# 4. LÓGICA DE NAVEGACIÓN
# ==========================================
def main():
    if 'logged_in' not in st.session_state: st.session_state.logged_in = False
    if 'page' not in st.session_state: st.session_state.page = "Inicio"
    if 'clase_target' not in st.session_state: st.session_state.clase_target = None

    if not st.session_state.logged_in:
        header_principal()
        _, col2, _ = st.columns([1, 2, 1])
        with col2:
            with st.form("login"):
                u, p = st.text_input("Usuario"), st.text_input("Pass", type="password")
                if st.form_submit_button("🚀 INGRESAR", use_container_width=True):
                    res = cargar_usuario(u, p)
                    if res is not None:
                        st.session_state.logged_in = True
                        st.session_state.user_data = res.iloc[0].to_dict()
                        registrar_acceso(u); st.rerun()
                    else: st.error("Error de acceso")
    else:
        user = st.session_state.user_data
        
        if st.session_state.page == "Inicio":
            header_principal()
            izq, der = st.columns([0.6, 0.4])
            with izq:
                st.title(f"¡Hola, {user['User']}!")
                st.divider()
                for materia in CONTENIDOS.keys():
                    if st.button(f"{materia}", key=f"m_{materia}", use_container_width=True):
                        st.session_state.materia_sel = materia
                        st.session_state.page = "Visor"
                        st.session_state.clase_target = None # Reset para cargar la primera del eje
                        st.rerun()
                if str(user['User']).lower() == 'admin':
                    if st.button("🕵️‍♂️ ADMIN"): st.session_state.page = "Admin"; st.rerun()
            with der:
                render_stats(user['User'])
                if st.button("🚪 Salir", use_container_width=True): st.session_state.logged_in = False; st.rerun()

        elif st.session_state.page == "Visor":
            if st.button("⬅️ Hub"): st.session_state.page = "Inicio"; st.rerun()
            
            m_sel = st.session_state.materia_sel
            ejes = list(CONTENIDOS[m_sel]["subcategorias"].keys())
            
            c_eje, c_clase = st.columns(2)
            with c_eje:
                eje_sel = st.selectbox("🎯 Eje:", ejes)
            
            clases_dict = CONTENIDOS[m_sel]["subcategorias"][eje_sel]
            lista_ids = list(clases_dict.keys())

            # Forzar la primera clase si no hay una seleccionada o si cambiamos de eje
            if st.session_state.clase_target not in lista_ids:
                st.session_state.clase_target = lista_ids[0]

            with c_clase:
                # Usamos una key dinámica para que el selectbox se "resetee" al cambiar de clase vía botón
                clase_id = st.selectbox(
                    "📖 Clase:", lista_ids, 
                    index=lista_ids.index(st.session_state.clase_target),
                    format_func=lambda x: clases_dict[x]["label"],
                    key=f"selector_{st.session_state.clase_target}" 
                )
                st.session_state.clase_target = clase_id

            st.divider()
            if "render" in clases_dict[clase_id]:
                clases_dict[clase_id]["render"]()
                st.divider()
                idx = lista_ids.index(clase_id)
                if idx < len(lista_ids) - 1:
                    # El botón ahora actualiza el target y lanza el rerun
                    if st.button(f"Siguiente: {clases_dict[lista_ids[idx+1]]['label']} ➡️", use_container_width=True):
                        st.session_state.clase_target = lista_ids[idx + 1]
                        st.rerun()
                else:
                    st.success("✨ ¡Eje completado!")

        elif st.session_state.page == "Admin":
            if st.button("🏠 Inicio"): st.session_state.page = "Inicio"; st.rerun()
            st.dataframe(conn.read(worksheet="Logs_Acceso", ttl=0).sort_index(ascending=False), use_container_width=True)

if __name__ == "__main__":
    main()
