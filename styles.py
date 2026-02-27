import streamlit as st


def aplicar_estilos():
    st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* --- BARRA DE NAVEGACIÓN 🏠 / N / A / G / D --- */
    [data-testid="stHorizontalBlock"] { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 4px !important; }
    [data-testid="stHorizontalBlock"] > div { flex: 1 1 0% !important; min-width: 0 !important; }
    [data-testid="stHorizontalBlock"] button {
        width: 100% !important;
        min-height: 70px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        background-color: #1a1a2e !important;
        color: white !important;
        border: none !important;
    }

    /* --- BOTONES DE CATEGORÍA (Teoría / Ejercitación / Clases) --- */
    .cat-container div.stButton > button {
        min-height: 85px !important; border-radius: 15px !important; margin-bottom: 15px !important;
        width: 100% !important; font-size: 18px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important; box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }

    /* --- BOTONES DE EJES (colores individuales) --- */
    .eje-numeros div.stButton > button   { background-color: #1a237e !important; color: white !important; border: none !important; }
    .eje-algebra div.stButton > button   { background-color: #1b5e20 !important; color: white !important; border: none !important; }
    .eje-geometria div.stButton > button { background-color: #e65100 !important; color: white !important; border: none !important; }
    .eje-datos div.stButton > button     { background-color: #b71c1c !important; color: white !important; border: none !important; }

    /* --- BOTÓN PDF --- */
    .pdf-btn div.stButton > button {
        background-color: #4a0e8f !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 65px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* --- CRONÓMETRO --- */
    .crono-digital {
        font-family: 'Courier New', monospace;
        font-size: 35px;
        font-weight: bold;
        color: #3b71ca;
        text-align: center;
        width: 100%;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)
