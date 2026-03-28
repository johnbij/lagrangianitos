import streamlit as st
from contenidos import CONTENIDOS
from datetime import datetime, date

# 1. CONFIGURACIÓN DE PÁGINA OBLIGATORIA (DEBE SER LO PRIMERO)
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# ==========================================
# CONFIGURACIÓN VISUAL Y DE IDENTIDAD
# ==========================================
# URL del logo real del dragón verde
LOGO_URL = "https://raw.githubusercontent.com/tucarpeta/tu-repo/main/logo_dragon.png" # <--- REEMPLAZA ESTO CON LA URL REAL O LA RUTA LOCAL

# Fecha de la PAES (Ejemplo: 20 de Noviembre de 2024) - Ajusta esto
FECHA_PAES = date(2024, 11, 20) 

# Estilos CSS personalizados para la identidad visual y ocultar sidebar
st.markdown(f"""
    <style>
        /* Ocultar barra lateral */
        [data-testid="stSidebar"] {{display: none;}}
        [data-testid="stSidebarNav"] {{display: none;}}
        .block-container {{padding-top: 0rem;}}

        /* Estilo para el banner azul oscuro superior */
        .paes-header {{
            background-color: #0E2439; /* Azul oscuro */
            color: white;
            padding: 2rem;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 2rem;
        }}
        
        .paes-header h1 {{color: white; font-weight: bold; margin-bottom: 0.5rem;}}
        .paes-header .lema {{font-style: italic; color: #FFD700; margin-bottom: 1.5rem;}} /* Dorado */
        .paes-header .info {{font-size: 0.9rem; color: #CCCCCC;}}

        /* Estilo para el contador de tiempo inferior rojo */
        .contador-timer {{
            background-color: #D32F2F; /* Rojo */
            color: white;
            padding: 1rem;
            text-align: center;
            border-radius: 10px;
            margin-top: -1.5rem; /* Para pegarlo al banner azul */
            margin-bottom: 2rem;
            font-weight: bold;
            display: flex;
            justify-content: space-around;
        }}

        /* Estilo para los botones de materia estilo tarjeta */
        div.stButton > button {{
            background-color: #1E3A5F; /* Azul grisáceo */
            color: white;
            border-radius: 10px;
            padding: 1.5rem;
            border: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            text-align: left;
            height: auto;
            display: block;
        }}
        
        div.stButton > button:hover {{
            background-color: #264A7A;
            box-shadow: 0 6px 8px rgba(0,0,0,0.2);
            transform: translateY(-2px);
        }}

        div.stButton > button p {{margin: 0;}}
        div.stButton > button .emoji {{font-size: 1.5rem; margin-right: 0.5rem;}}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

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

def render_header_lagrangianitos():
    """Renderiza el banner azul oscuro superior con el logo y el lema."""
    st.markdown(f"""
        <div class="paes-header">
            <img src="{LOGO_URL}" width="150" style="margin-bottom: 1rem;">
            <h1>LAGRANGIANITOS</h1>
            <p class="lema">"Enseñamos conceptos, no solo tricks"</p>
            <p class="info">Tu plataforma de preparación PAES M1.<br>Matemática con profundidad, desde los fundamentos hasta la prueba. 🚀</p>
            <p class="info">📍 Santiago • 🕒 {datetime.now().strftime('%H:%M')} • 👁️ 10 visitas</p>
        </div>
    """, unsafe_allow_html=True)

def render_contador_paes():
    """Renderiza el contador dinámico de tiempo hasta la PAES."""
    hoy = date.today()
    dias_restantes = (FECHA_PAES - hoy).days
    
    if dias_restantes < 0:
        texto_dias = "¡La PAES ya pasó!"
        texto_horas = ""
    else:
        texto_dias = f"⌛ Días: {dias_restantes}"
        # Para las horas, calculamos el tiempo hasta la medianoche de hoy
        ahora = datetime.now()
        horas_restantes = 23 - ahora.hour
        texto_horas = f"Hrs: {horas_restantes}"

    st.markdown(f"""
        <div class="contador-timer">
            <span>{texto_dias}</span>
            <span>{texto_horas}</span>
        </div>
    """, unsafe_allow_html=True)

# 6. PANTALLA DE LOGIN
def login():
    render_header_lagrangianitos() # Mostrar identidad también en login
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("Ingreso de Alumnos")
        user = st.text_input("Usuario", key="user_input")
        password = st.text_input("Contraseña", type="password", key="pass_input")
        if st.button("Ingresar", use_container_width=True):
            if user == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas")

# 7. LÓGICA PRINCIPAL (APP LOGUEADA)
def main():
    # Inicializar estados de sesión si no existen
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
        render_header_lagrangianitos() # Banner Azul Superior
        render_contador_paes()         # Contador Rojo Inferior

        st.subheader("📚 Contenidos del curso M1")
        
        # Mapeo de emojis y descripciones cortas para los botones de materia
        info_materias = {
            "📐 Matemáticas": {"emoji": "🔢", "desc": "Conjuntos • Álgebra • Geometría • Datos"},
            "⚛️ Física": {"emoji": "🌌", "desc": "Ondas • Mecánica • Energía • Tierra"},
            "🧪 Química": {"emoji": "⚗️", "desc": "Átomo • Orgánica • Reacciones"},
            "🌿 Biología": {"emoji": "🧬", "desc": "Célula • Herencia • Ecosistema"}
        }

        materias = list(CONTENIDOS.keys())
        # Creamos una cuadrícula de 2x2 para imitar la captura
        col1, col2 = st.columns(2)
        
        for i, materia in enumerate(materias):
            with col1 if i % 2 == 0 else col2:
                # Obtenemos info extra si existe
                info = info_materias.get(materia, {"emoji": "📖", "desc": ""})
                
                # HTML dentro del botón para dar el formato de dos líneas
                button_html = f"<span class='emoji'>{info['emoji']}</span> {materia}<br><span style='font-size:0.8rem; font-weight:normal; color:#CCCCCC;'>{info['desc']}</span>"
                
                if st.button(button_html, use_container_width=True, key=f"btn_main_{materia}"):
                    st.session_state.materia_sel = materia
                    st.session_state.page = "Visor"
                    # Seleccionar primer eje y resetear índice
                    if CONTENIDOS[materia]["subcategorias"]:
                        st.session_state.eje_sel = list(CONTENIDOS[materia]["subcategorias"].keys())[0]
                    st.session_state.clase_idx = 0
                    st.rerun()
        
        st.divider()
        
        c_det, c_out = st.columns([3, 1])
        with c_det:
            st.session_state.modo_detective = st.toggle("🔍 Modo Detective (Debug)", value=st.session_state.modo_detective)
        with c_out:
            if st.button("🚪 Cerrar Sesión", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()

    # --- PÁGINA DEL VISOR DE CLASES ---
    elif st.session_state.page == "Visor":
        # Ejecutar scroll al inicio al cargar la página
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

        # Cargar datos de la materia seleccionada
        if st.session_state.materia_sel not in CONTENIDOS:
             st.error("Error: Materia no encontrada.")
             st.session_state.page = "Inicio"
             st.rerun()

        materia_data = CONTENIDOS[st.session_state.materia_sel]
        ejes_list = list(materia_data["subcategorias"].keys())
        
        if not ejes_list:
            st.warning("Esta materia aún no tiene ejes temáticos definidos.")
            return

        # Selectores superiores (Eje y Clase)
        col_eje, col_clase = st.columns(2)
        
        with col_eje:
            # Asegurar que el eje seleccionado exista
            if st.session_state.eje_sel not in ejes_list:
                st.session_state.eje_sel = ejes_list[0]
            
            eje_escogido = st.selectbox(
                "🎯 Eje Temático:", 
                ejes_list, 
                index=ejes_list.index(st.session_state.eje_sel)
            )
            
            if eje_escogido != st.session_state.eje_sel:
                st.session_state.eje_sel = eje_escogido
                st.session_state.clase_idx = 0 # Resetear clase al cambiar eje
                st.rerun()

        clases_dict = materia_data["subcategorias"][st.session_state.eje_sel]
        ids_clases = list(clases_dict.keys())
        
        if not ids_clases:
            st.warning("Este eje temático aún no tiene clases definidas.")
            return

        with col_clase:
            # Asegurar que el índice esté dentro de rango
            st.session_state.clase_idx = min(st.session_state.clase_idx, len(ids_clases) - 1)
            
            clase_id = st.selectbox(
                "📖 Clase:", 
                ids_clases, 
                index=st.session_state.clase_idx,
                format_func=lambda x: clases_dict[x]["label"]
            )
            # Actualizar índice si cambió por el selectbox
            new_clase_idx = ids_clases.index(clase_id)
            if new_clase_idx != st.session_state.clase_idx:
                st.session_state.clase_idx = new_clase_idx
                st.rerun()

        # --- MODO DETECTIVE (DEBUG) ---
        if st.session_state.modo_detective:
            with st.expander("🛠️ Información Técnica de la Clase (Debug)", expanded=True):
                st.json({
                    "Materia": st.session_state.materia_sel,
                    "Eje": st.session_state.eje_sel,
                    "ID Clase": clase_id,
                    "Índice actual": st.session_state.clase_idx,
                    "Total clases eje": len(ids_clases),
                    "Función render": "render" in clases_dict[clase_id]
                })

        st.divider()

        # --- RENDERIZADO DEL CONTENIDO DE LA CLASE ---
        if "render" in clases_dict[clase_id]:
            try:
                clases_dict[clase_id]["render"]() # Llama a la función render_XX()
            except Exception as e:
                st.error(f"❌ Error al cargar el contenido de la clase '{clase_id}': {e}")
                if st.session_state.modo_detective:
                    st.exception(e)
        else:
            st.error(f"❌ No se encontró la función 'render' para la clase '{clase_id}'. Revisa contenidos.py.")

        st.divider()

        # --- NAVEGACIÓN INFERIOR (ANTERIOR / SIGUIENTE) ---
        c_prev, c_spacer, c_next = st.columns([1, 1, 1])
        with c_prev:
            if st.session_state.clase_idx > 0:
                if st.button("⬅️ Clase Anterior", use_container_width=True, key="btn_prev_clase"):
                    st.session_state.clase_idx -= 1
                    # scroll_to_top() se ejecuta al inicio del renderizado de la página
                    st.rerun()
        with c_next:
            if st.session_state.clase_idx < len(ids_clases) - 1:
                if st.button("Siguiente Clase ➡️", use_container_width=True, key="btn_next_clase"):
                    st.session_state.clase_idx += 1
                    st.rerun()
            else:
                st.success("🎯 ¡Has completado todas las clases de este eje temático!")

if __name__ == "__main__":
    main()
