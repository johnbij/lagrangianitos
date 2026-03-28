import streamlit as st
from contenidos import CONTENIDOS

# 1. Configuración de página
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

def scroll_to_top():
    """JS para subir al inicio al cambiar de clase."""
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

def login():
    # IMAGEN DEL DRAGÓN EN EL LOGIN
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos Hub</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/premium-photo/cute-baby-dragon-reading-book-study-room-generative-ai_955925-101.jpg", use_column_width=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        if st.button("Ingresar", use_container_width=True):
            if user == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas")

def main():
    # --- OCULTAR BARRA LATERAL POR CSS ---
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stSidebarNav"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'modo_detective' not in st.session_state:
        st.session_state.modo_detective = False
    
    if not st.session_state.logged_in:
        login()
        return

    # --- ESTADOS DE NAVEGACIÓN ---
    if 'page' not in st.session_state:
        st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state:
        st.session_state.materia_sel = None
    if 'eje_sel' not in st.session_state:
        st.session_state.eje_sel = None
    if 'clase_idx' not in st.session_state:
        st.session_state.clase_idx = 0

    # --- PÁGINA DE INICIO ---
    if st.session_state.page == "Inicio":
        st.markdown("<h1 style='text-align:center;'>📚 Entrenamiento M1</h1>", unsafe_allow_html=True)
        # FOTO DEL DRAGÓN EN EL MENÚ PRINCIPAL
        st.image("https://img.freepik.com/premium-photo/cute-baby-dragon-reading-book-study-room-generative-ai_955925-101.jpg", width=300)
        
        materias = list(CONTENIDOS.keys())
        cols = st.columns(len(materias))
        for i, materia in enumerate(materias):
            with cols[i]:
                if st.button(materia, use_container_width=True):
                    st.session_state.materia_sel = materia
                    st.session_state.page = "Visor"
                    st.session_state.eje_sel = list(CONTENIDOS[materia]["subcategorias"].keys())[0]
                    st.session_state.clase_idx = 0
                    st.rerun()
        
        st.divider()
        # BOTÓN MODO DETECTIVE
        if st.toggle("🔍 Modo Detective", value=st.session_state.modo_detective):
            st.session_state.modo_detective = True
        else:
            st.session_state.modo_detective = False
        
        if st.button("🚪 Cerrar Sesión"):
            st.session_state.logged_in = False
            st.rerun()

    # --- PÁGINA DEL VISOR ---
    elif st.session_state.page == "Visor":
        scroll_to_top()
        
        c_back, c_det = st.columns([3, 1])
        with c_back:
            if st.button("🏠 Volver al Menú Principal", use_container_width=True):
                st.session_state.page = "Inicio"
                st.rerun()
        with c_det:
            if st.session_state.modo_detective:
                st.success("🕵️ Modo Detective Activo")

        st.divider()

        materia_data = CONTENIDOS[st.session_state.materia_sel]
        col_eje, col_clase = st.columns(2)
        ejes_list = list(materia_data["subcategorias"].keys())
        
        with col_eje:
            idx_eje = ejes_list.index(st.session_state.eje_sel) if st.session_state.eje_sel in ejes_list else 0
            eje_escogido = st.selectbox("🎯 Eje Temático:", ejes_list, index=idx_eje)
            if eje_escogido != st.session_state.eje_sel:
                st.session_state.eje_sel = eje_escogido
                st.session_state.clase_idx = 0
                st.rerun()

        clases_dict = materia_data["subcategorias"][st.session_state.eje_sel]
        ids_clases = list(clases_dict.keys())
        
        with col_clase:
            idx_clase = min(st.session_state.clase_idx, len(ids_clases) - 1)
            clase_id = st.selectbox(
                "📖 Clase:", ids_clases, index=idx_clase,
                format_func=lambda x: clases_dict[x]["label"]
            )
            if ids_clases.index(clase_id) != st.session_state.clase_idx:
                st.session_state.clase_idx = ids_clases.index(clase_id)
                st.rerun()

        # RENDER Y LOGS (MODO DETECTIVE)
        if st.session_state.modo_detective:
            with st.expander("🛠️ Debug de Clase"):
                st.write(f"ID Clase: `{clase_id}`")
                st.write(f"Label: `{clases_dict[clase_id]['label']}`")
                if "render" in clases_dict[clase_id]:
                    st.write("✅ Función render detectada.")
                else:
                    st.error("❌ Función render no encontrada.")

        st.divider()
        if "render" in clases_dict[clase_id]:
            clases_dict[clase_id]["render"]()

        st.divider()
        c1, spacer, c2 = st.columns([1, 1, 1])
        with c1:
            if st.session_state.clase_idx > 0:
                if st.button("⬅️ Anterior", use_container_width=True):
                    st.session_state.clase_idx -= 1
                    st.rerun()
        with c2:
            if st.session_state.clase_idx < len(ids_clases) - 1:
                if st.button("Siguiente ➡️", use_container_width=True):
                    st.session_state.clase_idx += 1
                    st.rerun()

if __name__ == "__main__":
    main()
