# auth/supabase_client.py
# Requiere: pip install supabase

import streamlit as st
from supabase import create_client, Client


def is_supabase_configured() -> bool:
    """
    Retorna True si las credenciales de Supabase están disponibles en secrets.
    Útil para deshabilitar auth en entornos sin secrets (stlite/demo).
    """
    try:
        _ = st.secrets["supabase"]["url"]
        _ = st.secrets["supabase"]["key"]
        return True
    except Exception:
        return False


def get_supabase_client() -> Client:
    """
    Retorna el cliente de Supabase usando st.secrets.
    En tu archivo .streamlit/secrets.toml agrega:

    [supabase]
    url = "https://xxxx.supabase.co"
    key = "tu_anon_key_aqui"
    redirect_url = "https://tu-app.streamlit.app"
    """
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)
