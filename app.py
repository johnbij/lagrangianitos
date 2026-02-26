import streamlit as st
from datetime import datetime
import pytz
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state: st.session_state.eje_actual = None
if 'sub_eje_actual' not in st.session_state: st.session_state.sub_eje_actual = None
if 'sub_seccion_actual' not in st.session_state: st.session_state.sub_seccion_actual = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None

if 'cronometro_activo' not in st.session_state: st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state: st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS (REPARADO Y SIN CAJAS SOBRANTES) ::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* Headers principales */
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; margin-bottom: 20px; }
    
    /* Cronómetro */
    .crono-container-barton { background-color: white; padding: 10px; border-radius: 10px; text-align: center; border: 2px solid #3b71ca; }
    .crono-digital-azul { font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; color: #3b71ca; }
    
    /* Botones */
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; }

    /* ELIMINACIÓN DEL RECUADRO BLANCO (EL RAYADO CON PLUMÓN) */
    /* Quitamos el padding excesivo que Streamlit pone por defecto en los contenedores de texto */
    [data-testid="stVerticalBlock"] > div {
        padding-top: 0px !important;
        margin-top: 0px !important;
    }

    /* CAJA DE LA CLASE: Optimizada */
    .clase-box-final {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        color: #1a1a1a;
        margin-top: -15px; /* Esto sube la clase para eliminar el espacio blanco */
    }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. DASHBOARD :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    # Reloj y Tiempo
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div style="font-size: 20px; font-weight: bold;">🐉 Lagrangianitos. Tus recursos PAES M1</div><div style="font-size: 14px; opacity: 0.9;">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    dias_paes = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    st.markdown(f'<div class="header-rojo">⏳ Días para PAES: {dias_paes} </div>', unsafe_allow_html=True)

    # Cronómetro Digital
    c1, c2 = st.columns([1, 3])
    with c1:
        if not st.session_state.cronometro_activo:
            if st.button("▶️ Iniciar"): st.session_state.tiempo_inicio = time.time(); st.session_state.cronometro_activo = True; st.rerun()
        else:
            if st.button("⏹️ Detener"): st.session_state.cronometro_activo = False; st.session_state.tiempo_inicio = None; st.rerun()
    with c2:
        if st.session_state.cronometro_activo:
            t = int(time.time() - st.session_state.tiempo_inicio)
            st.markdown(f'<div class="crono-container-barton"><span class="crono-digital-azul">{t//60:02d}:{t%60:02d}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="crono-container-barton" style="border: 2px dashed #e0e0e0;"><span style="color:#e0e0e0; font-size:32px; font-family:Courier New; font-weight:bold;">00:00</span></div>', unsafe_allow_html=True)

    st.divider()

    # --- LÓGICA DE NAVEGACIÓN ---
    if st.session_state.eje_actual is None:
        st.subheader("Selecciona un Eje")
        if st.button("🔢 Números"): st.session_state.eje_actual = "🔢 Números"; st.rerun()
    
    elif st.session_state.sub_eje_actual is None:
        st.subheader("🔢 Números")
        if st.button("🛡️ 1. Conjuntos"): st.session_state.sub_eje_actual = "Conjuntos"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.eje_actual = None; st.rerun()

    elif st.session_state.sub_seccion_actual is None:
        st.subheader("🛡️ Conjuntos")
        if st.button("📘 Teoría y Conceptos"): st.session_state.sub_seccion_actual = "Teoria"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.sub_eje_actual = None; st.rerun()

    elif st.session_state.clase_seleccionada is None:
        st.subheader("Clases")
        if st.button("📖 N01: Teoría de Conjuntos"): st.session_state.clase_seleccionada = "N01"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.sub_seccion_actual = None; st.rerun()

    else:
        # --- PANTALLA DE CLASE FINAL ---
        if st.button("🔙 Volver"): 
            st.session_state.clase_seleccionada = None
            st.rerun()
        
        # Contenedor que "succiona" el contenido hacia arriba para borrar el espacio blanco
        st.markdown('<div class="clase-box-final">', unsafe_allow_html=True)
        
        st.markdown("""
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos</span>

---

### 🛡️ 1. El Portal
Aprender Teoría de Conjuntos es aprender a pensar con orden y entender que todo gran sistema se basa en quién pertenece a qué.

---

### 🛡️ 2. El Legado de Cantor
Georg Cantor demostró que los conjuntos nos permiten comparar tamaños de infinitos.

---

### 🛡️ 3. El Marco de Referencia
* **El Universo ($\mathcal{U}$):** Contiene todos los elementos del problema.
* **El Vacío ($\emptyset$):** Un conjunto sin elementos.
* **Pertenencia ($\in$):** Relación de un elemento hacia un conjunto.

> **Típ:** ... Si $A \subset B$, entonces $A \cap B = A$ y $A \cup B = B$.

---

### 🛡️ 4. Operaciones
* **Unión ($\cup$):** Agrupar todos los elementos.
* **Intersección ($\cap$):** Solo los elementos comunes.
* **Diferencia ($-$):** Quitar los elementos del segundo al primero.

---

### 🛡️ 5. Cardinalidad
* **Total de Subconjuntos:** $2^n$

> **Típ:** ... El total de subconjuntos siempre incluye al **Vacío** y al **propio conjunto $A$**.

---

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".  
> — **Georg Cantor**
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.cronometro_activo:
    time.sleep(1)
    st.rerun()
