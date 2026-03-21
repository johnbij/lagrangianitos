# auth/supabase_client.py
# Requiere: pip install supabase

import streamlit as st
from supabase import create_client, Client


def is_supabase_configured() -> bool:
    """
    Retorna True si las credenciales de Supabase están presentes
    y contienen valores reales (no placeholders).
    """
    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["key"]
    except (KeyError, FileNotFoundError):
        return False

    if not url or not key:
        return False

    # Rechazar URLs placeholder que no apuntan a un proyecto real
    placeholders = ("https://xxxx", "https://tu-proyecto", "https://your-project")
    if any(url.startswith(p) for p in placeholders):
        return False

    return True


def get_supabase_client() -> Client:
    """
    Retorna el cliente de Supabase usando st.secrets.
    En tu archivo .streamlit/secrets.toml agrega:
    
    [supabase]
    url = "https://xxxx.supabase.co"
    key = "tu_anon_key_aqui"
    """
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)
