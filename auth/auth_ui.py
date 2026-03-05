# auth/auth_ui.py
# Maneja login, registro y logout con Supabase Auth (email + Google OAuth)
#
# SETUP GOOGLE OAUTH (solo hay que hacerlo una vez):
# 1. Ve a console.cloud.google.com → Crear proyecto → APIs & Services → Credentials
# 2. Crear "OAuth 2.0 Client ID" de tipo "Web application"
# 3. En "Authorized redirect URIs" agrega:
#    https://<tu-proyecto>.supabase.co/auth/v1/callback
# 4. Copia Client ID y Client Secret
# 5. En Supabase → Authentication → Providers → Google → pega las credenciales
# 6. En secrets.toml agrega la URL pública de tu app:
#    [supabase]
#    url = "..."
#    key = "..."
#    redirect_url = "https://tu-app.streamlit.app"   # o http://localhost:8501 en local

import streamlit as st
from auth.supabase_client import get_supabase_client


def init_session():
    """Inicializa variables de sesión si no existen."""
    if "user" not in st.session_state:
        st.session_state.user = None
    if "access_token" not in st.session_state:
        st.session_state.access_token = None

    # Captura el token que Google devuelve en la URL tras el redirect OAuth
    _handle_oauth_callback()


def _handle_oauth_callback():
    """
    Después del redirect de Google, Supabase devuelve el token en los
    query params de la URL. Esta función lo captura y guarda la sesión.
    """
    if st.session_state.get("user"):
        return  # Ya hay sesión, no hacer nada

    params = st.query_params
    access_token = params.get("access_token")
    refresh_token = params.get("refresh_token")

    if access_token and refresh_token:
        supabase = get_supabase_client()
        try:
            response = supabase.auth.set_session(access_token, refresh_token)
            st.session_state.user = response.user
            st.session_state.access_token = access_token
            # Limpiar tokens de la URL
            st.query_params.clear()
            st.rerun()
        except Exception as e:
            st.error(f"Error al recuperar sesión de Google: {e}")


def is_logged_in() -> bool:
    """Retorna True si hay un usuario autenticado en sesión."""
    return st.session_state.get("user") is not None


def login_page():
    """
    Renderiza la pantalla de login/registro.
    Llama esta función en app.py cuando el usuario no está autenticado.
    """
    st.title("🐉 LAG Dragon — Lagrangianitos")
    st.markdown("### Inicia sesión para continuar")

    # ── BOTÓN GOOGLE (opción principal) ───────────────────────
    st.markdown("####")
    if st.button("🔵  Continuar con Google", use_container_width=True, type="primary"):
        _do_google_login()

    st.divider()
    st.markdown("##### O usa correo y contraseña")

    tab_login, tab_register = st.tabs(["Iniciar sesión", "Registrarse"])

    # ── TAB LOGIN ──────────────────────────────────────────────
    with tab_login:
        with st.form("form_login"):
            email = st.text_input("Correo electrónico")
            password = st.text_input("Contraseña", type="password")
            submitted = st.form_submit_button("Entrar", use_container_width=True)

        if submitted:
            if not email or not password:
                st.warning("Por favor completa todos los campos.")
            else:
                _do_login(email, password)

    # ── TAB REGISTRO ───────────────────────────────────────────
    with tab_register:
        with st.form("form_register"):
            nombre = st.text_input("Nombre completo")
            email_r = st.text_input("Correo electrónico")
            password_r = st.text_input("Contraseña", type="password")
            password_r2 = st.text_input("Repite la contraseña", type="password")
            submitted_r = st.form_submit_button("Crear cuenta", use_container_width=True)

        if submitted_r:
            if not nombre or not email_r or not password_r:
                st.warning("Por favor completa todos los campos.")
            elif password_r != password_r2:
                st.error("Las contraseñas no coinciden.")
            else:
                _do_register(nombre, email_r, password_r)


def logout():
    """Cierra la sesión del usuario."""
    supabase = get_supabase_client()
    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    st.session_state.user = None
    st.session_state.access_token = None
    st.rerun()


def show_user_sidebar():
    """
    Muestra info del usuario y botón de logout en el sidebar.
    Llama esto al inicio de cada página protegida.
    """
    if is_logged_in():
        user = st.session_state.user
        email = user.email if hasattr(user, "email") else "usuario"
        st.sidebar.markdown(f"👤 **{email}**")
        if st.sidebar.button("Cerrar sesión", use_container_width=True):
            logout()


# ── HELPERS PRIVADOS ───────────────────────────────────────────────────────────

def _do_google_login():
    """Redirige al usuario a Google para autenticarse vía OAuth."""
    supabase = get_supabase_client()
    redirect_url = st.secrets["supabase"].get("redirect_url", "http://localhost:8501")
    try:
        response = supabase.auth.sign_in_with_oauth({
            "provider": "google",
            "options": {"redirect_to": redirect_url}
        })
        # Redirigir al usuario a la URL de Google
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={response.url}">',
            unsafe_allow_html=True
        )
        st.info("Redirigiendo a Google...")
        st.stop()
    except Exception as e:
        st.error(f"Error al conectar con Google: {e}")


def _do_login(email: str, password: str):
    supabase = get_supabase_client()
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        st.session_state.user = response.user
        st.session_state.access_token = response.session.access_token
        st.success("¡Bienvenido/a!")
        st.rerun()
    except Exception as e:
        st.error(f"Error al iniciar sesión: {e}")


def _do_register(nombre: str, email: str, password: str):
    supabase = get_supabase_client()
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {"full_name": nombre}
            }
        })
        if response.user:
            st.success("✅ Cuenta creada. Revisa tu correo para confirmar (o inicia sesión directamente si desactivaste confirmación en Supabase).")
        else:
            st.error("No se pudo crear la cuenta. Intenta de nuevo.")
    except Exception as e:
        st.error(f"Error al registrarse: {e}")
