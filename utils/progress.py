# utils/progress.py
# Guarda y lee el progreso del estudiante en Supabase

import streamlit as st
from datetime import datetime
from auth.supabase_client import get_supabase_client


def get_user_id() -> str | None:
    """Retorna el UUID del usuario logueado, o None si no hay sesión."""
    user = st.session_state.get("user")
    return str(user.id) if user else None


# ── GUARDAR RESULTADO DE QUIZ ──────────────────────────────────────────────────

def save_quiz_result(class_id: str, score: int, total: int):
    """
    Guarda el resultado de un quiz en la tabla 'quiz_results'.
    
    Params:
        class_id  : identificador de la clase, ej. "G01", "A03"
        score     : cantidad de respuestas correctas
        total     : total de preguntas
    
    Tabla esperada en Supabase:
        quiz_results (
            id          uuid default gen_random_uuid() primary key,
            user_id     uuid references auth.users(id),
            class_id    text,
            score       int,
            total       int,
            pct         float,
            created_at  timestamptz default now()
        )
    """
    user_id = get_user_id()
    if not user_id:
        return

    supabase = get_supabase_client()
    pct = round(score / total * 100, 1) if total > 0 else 0

    try:
        supabase.table("quiz_results").insert({
            "user_id": user_id,
            "class_id": class_id,
            "score": score,
            "total": total,
            "pct": pct,
            "created_at": datetime.utcnow().isoformat()
        }).execute()
    except Exception as e:
        st.warning(f"No se pudo guardar el progreso: {e}")


# ── MARCAR CLASE COMO VISTA ────────────────────────────────────────────────────

def mark_class_completed(class_id: str):
    """
    Marca una clase como completada en la tabla 'progress'.
    Usa upsert para evitar duplicados.
    
    Tabla esperada en Supabase:
        progress (
            id          uuid default gen_random_uuid() primary key,
            user_id     uuid references auth.users(id),
            class_id    text,
            completed   boolean default true,
            updated_at  timestamptz default now(),
            unique(user_id, class_id)
        )
    """
    user_id = get_user_id()
    if not user_id:
        return

    supabase = get_supabase_client()
    try:
        supabase.table("progress").upsert({
            "user_id": user_id,
            "class_id": class_id,
            "completed": True,
            "updated_at": datetime.utcnow().isoformat()
        }, on_conflict="user_id,class_id").execute()
    except Exception as e:
        st.warning(f"No se pudo marcar la clase: {e}")


# ── LEER PROGRESO DEL USUARIO ──────────────────────────────────────────────────

def get_completed_classes() -> list[str]:
    """
    Retorna lista de class_id que el usuario ha completado.
    Ej: ["G01", "G02", "A01"]
    """
    user_id = get_user_id()
    if not user_id:
        return []

    supabase = get_supabase_client()
    try:
        response = (
            supabase.table("progress")
            .select("class_id")
            .eq("user_id", user_id)
            .eq("completed", True)
            .execute()
        )
        return [row["class_id"] for row in response.data]
    except Exception:
        return []


def get_quiz_history(class_id: str | None = None) -> list[dict]:
    """
    Retorna el historial de quizzes del usuario.
    Si se pasa class_id, filtra por esa clase.
    """
    user_id = get_user_id()
    if not user_id:
        return []

    supabase = get_supabase_client()
    try:
        query = (
            supabase.table("quiz_results")
            .select("class_id, score, total, pct, created_at")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
        )
        if class_id:
            query = query.eq("class_id", class_id)
        return query.execute().data
    except Exception:
        return []


def get_best_score(class_id: str) -> float | None:
    """
    Retorna el mejor porcentaje obtenido en una clase, o None si no hay intentos.
    """
    history = get_quiz_history(class_id)
    if not history:
        return None
    return max(row["pct"] for row in history)
