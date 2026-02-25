import streamlit as st
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

# Estado para que la página recuerde qué eje elegiste
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = "🔢 Números"

# --- 2. INYECCIÓN DE CSS (TARJETAS PRO) ---
st.markdown("""
    <style>
    /* Estilo de la barra blanca debajo de las cabeceras */
    [data-testid="stHorizontalBlock"] {
        background-color: white !important;
        padding: 10px !important;
        border-radius: 0 0 15px 15px !important;
    }
    
    /* Transformación de Botones en CONTENEDORES (Cards) */
    div.stButton > button {
        height: 120px !important;
        border-radius: 15px !important;
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        padding: 20px !important;
        white-space: pre-wrap !important;
        text-align: left !important;
        margin-bottom: 15px !important;
    }
    
    div.stButton > button:hover {
        border-color: #3b71ca !important;
        box-shadow: 0px 6px 15px rgba(59, 113, 202, 0.2) !important;
        transform: translateY(-2px) !important;
        color: #3b71ca !important;
    }

    /* Color azul para el Eje Álgebra */
    .blue-title {
        color: #3b71ca;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Seba** \n*Estudiante de Ingeniería*")
    st.markdown("### Redes Sociales \n- [📸 Instagram: @lagrangianitos](https://instagram.com/lagrangianitos)")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca PDFs"])
    st.divider()
    st.write("Típ: El diseño de tarjetas facilita la navegación táctil.")

# --- 4. LÓGICA DE NAVEGACIÓN ---
if menu == "🏠 Dashboard PAES":
    # Cabecera Azul (Reloj)
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div style="background-color: #3b71ca; padding: 20px; border-radius: 15px 15px 0 0; color: white; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 22px; font-weight: bold;">🚀 Centro de Recursos PAES</div>
            <div style="font-size: 18px; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
        </div>
        """, unsafe_allow_html=True)

    # Cabecera Roja (Countdown)
    fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    faltan = fecha_paes - ahora
    st.markdown(f"""
        <div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center;">
            <div style="font-size: 16px; font-weight: bold;">⏳ Días: {faltan.days}</div>
            <div style="font-size: 16px; font-weight: bold;">Hrs: {faltan.seconds // 3600}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("📚 Planes de Estudio")

    # Los 5 Ejes como Tarjetas Pro
    ejes_info = {
        "🔢 Números": "Conjuntos, potencias y razones.",
        "📉 Álgebra": "Ecuaciones, funciones y álgebra.",
        "📐 Geometría": "Teoremas, áreas y volúmenes.",
        "📊 Estadística": "Medidas de tendencia y tablas.",
        "📊 Probabilidad": "Azar, eventos y combinatoria."
    }

    for nombre, desc in ejes_info.items():
        if st.button(f"{nombre}\\n{desc}", key=f"btn_{nombre}", use_container_width=True):
            st.session_state.eje_actual = nombre

    st.write("---")
    
    # Contenido del Eje Seleccionado
    eje_selec = st.session_state.eje_actual
    if eje_selec == "📉 Álgebra":
        st.markdown('<h1 class="blue-title">Eje Álgebra</h1>', unsafe_allow_html=True)
    else:
        st.header(eje_selec)
    
    st.info(f"Seleccionaste el eje de {eje_selec[2:]}. Aquí aparecerán tus 121 clases.")

elif menu == "📂 Biblioteca PDFs":
    st.header("📂 Biblioteca de Recursos PDF")
    
    def cargar_archivo(nombre):
        try:
            with open(f"pdfs/{nombre}", "rb") as f: return f.read()
        except: return None

    recursos = {
        "📄 Temario PAES M1 2027": "2027I-TemarioPaesM1.pdf",
        "📝 Ensayo PAES M1 2026": "2026V-PaesM1.pdf",
        "🔑 Clavijero PAES M1 2026": "2026V-ClavijeroPaesM1.pdf"
    }

    for etiqueta, archivo in recursos.items():
        data = cargar_archivo(archivo)
        if data:
            st.download_button(label=etiqueta, data=data, file_name=archivo, use_container_width=True)
