import streamlit as st
from contenidos import CONTENIDOS

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# 2. RUTA DEL LOGO (Asegúrate de que el archivo esté en la misma carpeta)
LOGO_PATH = "logo.png" 

# 3. FUNCIÓN DE SCROLL AL INICIO
def scroll_to_top():
    """Inyecta JS para subir al inicio al cambiar de clase usando una key única."""
    unique_key = f"scroll_{st.session_state.get('clase_idx', 0)}_{st.session_state.get('eje_sel', 'none')}"
    st.components.v1.html(
        """
        <script>
            var mainContent = window.parent.document.querySelector('section.main');
            if (mainContent) {
                mainContent.scrollTo({top: 0, behavior: 'auto'});
            }
        </script>
        """,
        height=0,
        key=unique_key
    )

# 4. PANTALLA DE LOGIN
def login():
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos Hub</h1>", unsafe_allow_html=True)
    
    col_img_1, col_img_2, col_img_3 = st.columns([1, 1, 1])
    with col_img_2:
        try:
            st.image(LOGO_PATH, use_container_width=True)
        except:
            st.info("Coloca tu archivo 'logo.png' en la carpeta raíz")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user = st.text_input("Usuario", key="user_input")
        password = st.text_input("Contraseña", type="password", key="pass_input")
        if st.button("Ingresar", use_container_width=True):
            if user == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas")

# 5. LÓGICA PRINCIPAL
def main():
    # CSS para ocultar la barra lateral y ajustar márgenes
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stSidebarNav"] {display: none;}
            .block-container {padding-top: 2rem;}
        </style>
    """, unsafe_allow_html=True)

    # Inicializar estados de sesión
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'modo_detective' not in st.session_state:
        st.session_state.modo_detective = False
    if 'page' not in st.session_state:
        st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state:
        st.session_state.materia_sel = None
    if 'eje_sel' not in st.session_state:
        st.session_state.eje_sel = None
    if 'clase_idx' not in st.session_state:
        st.session_state.clase_idx = 0

    if not st.session_state.logged_in:
        login()
        return

    # --- PÁGINA DE INICIO (MENÚ PRINCIPAL) ---
    if st.session_state.page == "Inicio":
        st.markdown("<h1 style='text-align:center;'>📚 Entrenamiento M1</h1>", unsafe_allow_html=True)
        
        col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
        with col_logo_2:
            try:
                st.image(LOGO_PATH, width=300)
            except:
                st.caption("Dragon Logo")

        st.divider()
        st.subheader("Selecciona tu materia para comenzar:")
        
        materias = list(CONTENIDOS.keys())
        cols = st.columns(len(materias))
        for i, materia in enumerate(materias):
            with cols[i]:
                if st.button(materia, use_container_width=True, key=f"btn_main_{materia}"):
                    st.session_state.materia_sel = materia
                    st.session_state.page = "Visor"
                    st.session_state.eje_sel = list(CONTENIDOS[materia]["subcategorias"].keys())[0]
                    st.session_state.clase_idx = 0
                    st.rerun()
        
        st.divider()
        
        c_det, c_out = st.columns([3, 1])
        with c_det:
            st.session_state.modo_detective = st.toggle("🔍 Modo Detective", value=st.session_state.modo_detective)
        with c_out:
            if st.button("🚪 Cerrar Sesión", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()

    # --- PÁGINA DEL VISOR DE CLASES ---
    elif st.session_state.page == "Visor":
        scroll_to_top()
        
        c_nav, c_status = st.columns([4, 1])
        with c_nav:
            if st.button("🏠 Volver al Menú Principal", use_container_width=True):
                st.session_state.page = "Inicio"
                st.rerun()
        with c_status:
            if st.session_state.modo_detective:
                st.success("🕵️ Modo Detective Activo")

        st.divider()

        # Cargar datos de la materia
        materia_data = CONTENIDOS[st.session_state.materia_sel]
        ejes_list = list(materia_data["subcategorias"].keys())
        
        # Selectores superiores
        col_eje, col_clase = st.columns(2)
        
        with col_eje:
            if st.session_state.eje_sel not in ejes_list:
                st.session_state.eje_sel = ejes_list[0]
            
            eje_escogido = st.selectbox(
                "🎯 Eje Temático:", 
                ejes_list, 
                index=ejes_list.index(st.session_state.eje_sel)
            )
            if eje_escogido != st.session_state.eje_sel:
                st.session_state.eje_sel = eje_escogido
                st.session_state.clase_idx = 0
                st.rerun()

        clases_dict = materia_data["subcategorias"][st.session_state.eje_sel]
        ids_clases = list(clases_dict.keys())
        
        with col_clase:
            st.session_state.clase_idx = min(st.session_state.clase_idx, len(ids_clases) - 1)
            clase_id = st.selectbox(
                "📖 Clase:", 
                ids_clases, 
                index=st.session_state.clase_idx,
                format_func=lambda x: clases_dict[x]["label"]
            )
            new_clase_idx = ids_clases.index(clase_id)
            if new_clase_idx != st.session_state.clase_idx:
                st.session_state.clase_idx = new_clase_idx
                st.rerun()

        # MODO DETECTIVE (DEBUG)
        if st.session_state.modo_detective:
            with st.expander("🛠️ Información de la Clase", expanded=True):
                st.json({
                    "Materia": st.session_state.materia_sel,
                    "Eje": st.session_state.eje_sel,
                    "ID": clase_id,
                    "Ruta": f"clases/{st.session_state.materia_sel}/{clase_id}.py"
                })

        st.divider()

        # RENDERIZADO DEL CONTENIDO
        if "render" in clases_dict[clase_id]:
            try:
                clases_dict[clase_id]["render"]()
            except Exception as e:
                st.error(f"Error al cargar la clase: {e}")
        else:
            st.error("No se encontró la función render.")

        st.divider()

        # NAVEGACIÓN INFERIOR
        c_prev, c_spacer, c_next = st.columns([1, 1, 1])
        with c_prev:
            if st.session_state.clase_idx > 0:
                if st.button("⬅️ Anterior", use_container_width=True):
                    st.session_state.clase_idx -= 1
                    st.rerun()
        with c_next:
            if st.session_state.clase_idx < len(ids_clases) - 1:
                if st.button("Siguiente ➡️", use_container_width=True):
                    st.session_state.clase_idx += 1
                    st.rerun()
            else:
                st.info("Has llegado al final de este eje.")

if __name__ == "__main__":
    main()
