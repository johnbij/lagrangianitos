# auth/supabase_client.py
# Requiere: pip install supabase

import streamlit as st
from supabase import create_client, Client

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
