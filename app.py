import streamlit as st
from contenidos import CONTENIDOS
import os

# 1. Configuración de página obligatoria al inicio
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# ==========================================
# CONFIGURACIÓN DEL LOGO (CAMBIA ESTO)
# ==========================================
# Si es un archivo local, asegúrate de que esté en la misma carpeta o usa la ruta relativa
# Ejemplo local: LOGO_PATH = "logo_dragon.png"
# Ejemplo URL: LOGO_PATH = "https://tu-sitio.com/logo.png"
LOGO_PATH = "https://via.placeholder.com/300x200.png?text=Logo+Dragon+Aqui" 
# ==========================================

def scroll_to_top():
    """Inyecta JS para subir al inicio al cambiar de clase."""
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
    # Estilo centrado para el login
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos Hub</h1>", unsafe_allow_html=True)
    
    # Intenta cargar el logo, si falla muestra un aviso
    try:
        st.image(LOGO_PATH, use_column_width=True)
    except:
        st.warning("⚠️ No se pudo cargar el logo. Revisa LOGO_PATH en app.py")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user = st.text_input("Usuario", key="login_user")
        password = st.text_input("Contraseña", type="password", key="login_pass")
        if st.button("Ingresar", use_container_width=True):
            # Credenciales corregidas: admin / admin
            if user == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas. Intenta con admin/admin")

def main():
    # --- OCULTAR BARRA LATERAL POR CSS ---
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stSidebarNav"] {display: none;}
            /* Ajuste opcional para reducir el margen superior */
            .block-container {padding-top: 1rem;}
        </style>
    """, unsafe_allow_html=True)

    # Inicialización de estados
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

    # --- PÁGINA DE INICIO ---
    if st.session_state.page == "Inicio":
        st.markdown("<h1 style='text-align:center;'>📚 Entrenamiento M1</h1>", unsafe_allow_html=True)
        
        # Centrar el logo en el inicio
        col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])
        with col_logo_2:
            try:
                st.image(LOGO_PATH, width=300)
            except:
                st.info("Espacio para el Logo del Dragón")

        st.divider()
        st.subheader("Selecciona tu materia:")
        
        materias = list(CONTENIDOS.keys())
        if materias:
            cols = st.columns(len(materias))
            for i, materia in enumerate(materias):
                with cols[i]:
                    if st.button(materia, use_container_width=True, key=f"btn_{materia}"):
                        st.session_state.materia_sel = materia
                        st.session_state.page = "Visor"
                        # Seleccionar primer eje y resetear índice
                        st.session_state.eje_sel = list(CONTENIDOS[materia]["subcategorias"].keys())[0]
                        st.session_state.clase_idx = 0
                        st.rerun()
        else:
            st.warning("No se encontraron materias en contenidos.py")

        st.divider()
        
        # Herramientas al final
        col_det, col_logout = st.columns([3, 1])
        with col_det:
            # st.toggle devuelve True/False directamente
            check_detective = st.toggle("🔍 Modo Detective (Debug)", value=st.session_state.modo_detective)
            if check_detective != st.session_state.modo_detective:
                st.session_state.modo_detective = check_detective
                st.rerun()

        with col_logout:
            if st.button("🚪 Cerrar Sesión", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()

    # --- PÁGINA DEL VISOR ---
    elif st.session_state.page == "Visor":
        # Ejecutar scroll al inicio al cargar la página
        scroll_to_top()
        
        # Cabecera del Visor
        col_back, col_info_det = st.columns([3, 1])
        with col_back:
            if st.button("🏠 Volver al Menú Principal", use_container_width=True):
                st.session_state.page = "Inicio"
                st.rerun()
        with col_info_det:
            if st.session_state.modo_detective:
                st.caption("🕵️ Debug Activo")

        st.divider()

        # Datos de la materia seleccionada
        materia_data = CONTENIDOS[st.session_state.materia_sel]
        
        # Selectores de Eje y Clase
        col_eje, col_clase = st.columns(2)
        ejes_list = list(materia_data["subcategorias"].keys())
        
        with col_eje:
            # Asegurar que el eje seleccionado exista, sino usar el primero
            if st.session_state.eje_sel not in ejes_list:
                st.session_state.eje_sel = ejes_list[0]
            
            idx_eje = ejes_list.index(st.session_state.eje_sel)
            eje_escogido = st.selectbox("🎯 Eje Temático:", ejes_list, index=idx_eje, key="select_eje")
            
            if eje_escogido != st.session_state.eje_sel:
                st.session_state.eje_sel = eje_escogido
                st.session_state.clase_idx = 0
                st.rerun()

        clases_dict = materia_data["subcategorias"][st.session_state.eje_sel]
        ids_clases = list(clases_dict.keys())
        
        with col_clase:
            # Asegurar que el índice esté dentro de rango
            st.session_state.clase_idx = min(st.session_state.clase_idx, len(ids_clases) - 1)
            
            clase_id = st.selectbox(
                "📖 Clase:", 
                ids_clases, 
                index=st.session_state.clase_idx,
                format_func=lambda x: clases_dict[x]["label"],
                key="select_clase"
            )
            # Actualizar índice si cambió por el selectbox
            new_idx = ids_clases.index(clase_id)
            if new_idx != st.session_state.clase_idx:
                st.session_state.clase_idx = new_idx
                st.rerun()

        # --- MODO DETECTIVE (DEBUG) ---
        if st.session_state.modo_detective:
            with st.expander("🕵️ Detalles Técnicos de la Clase (Debug)", expanded=True):
                st.json({
                    "Materia": st.session_state.materia_sel,
                    "Eje": st.session_state.eje_sel,
                    "ID Clase": clase_id,
                    "Índice": st.session_state.clase_idx,
                    "Label": clases_dict[clase_id]["label"],
                    "Tiene Render": "render" in clases_dict[clase_id]
                })

        st.divider()
        
        # --- RENDERIZADO DEL CONTENIDO DE LA CLASE ---
        if "render" in clases_dict[clase_id]:
            try:
                clases_dict[clase_id]["render"]()
            except Exception as e:
                st.error(f"❌ Error al renderizar la clase: {e}")
                if st.session_state.modo_detective:
                    st.exception(e)
        else:
            st.error("❌ No se encontró la función 'render' para esta clase.")

        st.divider()
        
        # --- NAVEGACIÓN INFERIOR (ANTERIOR / SIGUIENTE) ---
        c1, spacer, c2 = st.columns([1, 1, 1])
        with c1:
            if st.session_state.clase_idx > 0:
                if st.button("⬅️ Clase Anterior", use_container_width=True, key="btn_ant"):
                    st.session_state.clase_idx -= 1
                    # scroll_to_top() ya se ejecuta al inicio del renderizado
                    st.rerun()
        with c2:
            if st.session_state.clase_idx < len(ids_clases) - 1:
                if st.button("Siguiente Clase ➡️", use_container_width=True, key="btn_sig"):
                    st.session_state.clase_idx += 1
                    st.rerun()
            else:
                st.success("🎯 ¡Has completado este eje temático!")

if __name__ == "__main__":
    main()
