# ⚙️ Guía de Configuración — Lagrangianitos

Esta guía explica todo lo que debes configurar en **Supabase**, **Google Cloud** y **Streamlit Cloud** para que la app funcione correctamente, incluyendo el login con Google.

---

## 1. 🗄️ Supabase

### 1.1 Crear el proyecto

1. Ve a [supabase.com](https://supabase.com) e inicia sesión.
2. Crea un nuevo proyecto (o usa el existente).
3. Anota tu **Project URL** y tu **anon key** desde *Settings → API*.

### 1.2 Activar el proveedor Google OAuth

1. En Supabase, ve a **Authentication → Providers → Google**.
2. Activa el proveedor.
3. Pega el **Client ID** y **Client Secret** que obtendrás de Google Cloud Console (paso 2).
4. Guarda los cambios.

### 1.3 Configurar URLs de redirección permitidas

1. Ve a **Authentication → URL Configuration**.
2. En **Redirect URLs** agrega:
   ```
   https://lagrangianitos.streamlit.app
   http://localhost:8501
   ```
3. En **Site URL** coloca:
   ```
   https://lagrangianitos.streamlit.app
   ```
4. Guarda los cambios.

### 1.4 Crear las tablas de base de datos

En el **SQL Editor** de Supabase, ejecuta el siguiente script completo:

```sql
-- Tabla: progreso de clases vistas
create table if not exists progress (
    id          uuid default gen_random_uuid() primary key,
    user_id     uuid references auth.users(id) on delete cascade,
    class_id    text not null,
    completed   boolean default true,
    updated_at  timestamptz default now(),
    unique(user_id, class_id)
);

-- Tabla: historial de quizzes
create table if not exists quiz_results (
    id          uuid default gen_random_uuid() primary key,
    user_id     uuid references auth.users(id) on delete cascade,
    class_id    text not null,
    score       int not null,
    total       int not null,
    pct         float,
    created_at  timestamptz default now()
);

-- Seguridad a nivel de fila (RLS) — cada usuario solo ve sus propios datos
alter table progress     enable row level security;
alter table quiz_results enable row level security;

create policy "Usuarios ven su propio progreso"
    on progress for all
    using  (auth.uid() = user_id)
    with check (auth.uid() = user_id);

create policy "Usuarios ven sus propios resultados"
    on quiz_results for all
    using  (auth.uid() = user_id)
    with check (auth.uid() = user_id);
```

---

## 2. ☁️ Google Cloud Console

> Necesitas esto para que el botón **"Continuar con Google"** funcione.  
> El error 403 que aparece en la imagen se soluciona configurando esto correctamente.

### 2.1 Crear el proyecto y habilitar la API

1. Ve a [console.cloud.google.com](https://console.cloud.google.com).
2. Crea un nuevo proyecto o selecciona uno existente.
3. Ve a **APIs & Services → Library** y habilita:
   - **Google+ API** (o Google Identity)

### 2.2 Configurar la pantalla de consentimiento OAuth

1. Ve a **APIs & Services → OAuth consent screen**.
2. Selecciona **External** (para que cualquier usuario de Google pueda entrar).
3. Completa:
   - **App name**: `Lagrangianitos`
   - **User support email**: tu correo
   - **Authorized domains**: agrega `supabase.co`
4. En **Scopes**, agrega: `email`, `profile`, `openid`.
5. Cambia el estado de **Testing** a **Production** (¡importante! Si queda en Testing, solo los correos de la lista de prueba podrán entrar y Google devolverá 403 para los demás).
   > **Nota**: Para los scopes básicos (`email`, `profile`, `openid`) el paso a Production normalmente es inmediato. Si Google requiere verificación adicional (para scopes sensibles), el proceso puede tomar algunos días. Para esta app, los scopes necesarios son básicos y no deberían requerir revisión extensa.

### 2.3 Crear las credenciales OAuth 2.0

1. Ve a **APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID**.
2. Tipo de aplicación: **Web application**.
3. Nombre: `Lagrangianitos Streamlit`.
4. En **Authorized JavaScript origins** agrega:
   ```
   https://lagrangianitos.streamlit.app
   http://localhost:8501
   ```
5. En **Authorized redirect URIs** agrega (**exactamente esto, con tu Project ID de Supabase**):
   ```
   https://<TU-PROJECT-ID>.supabase.co/auth/v1/callback
   ```
   Por ejemplo: `https://hueeucoqvbnivaepbvgi.supabase.co/auth/v1/callback`
6. Guarda y copia el **Client ID** y **Client Secret** → pégalos en Supabase (paso 1.2).

---

## 3. 🚀 Streamlit Cloud

### 3.1 Conectar el repositorio

1. Ve a [share.streamlit.io](https://share.streamlit.io).
2. Conecta tu cuenta de GitHub y selecciona el repositorio `johnbij/lagrangianitos`.
3. Archivo principal: `app.py`.
4. Branch: `main`.

### 3.2 Agregar los Secrets (¡obligatorio!)

1. En tu app desplegada, haz clic en **⋮ (menú) → Settings → Secrets**.
2. Pega el siguiente contenido, completando con tus valores reales:

```toml
[supabase]
url          = "https://<TU-PROJECT-ID>.supabase.co"
key          = "<TU-ANON-KEY>"
redirect_url = "https://lagrangianitos.streamlit.app"
```

- `url`: la URL del proyecto de Supabase (*Settings → API → Project URL*).
- `key`: la **anon/public key** de Supabase (*Settings → API → anon public*).
- `redirect_url`: la URL exacta de tu app en Streamlit Cloud (sin barra final).

> ⚠️ Si estos secrets no están configurados, la app se ejecutará sin autenticación (modo demo).

### 3.3 Verificar la configuración

Después de guardar los secrets y reiniciar la app, verifica que:

- [ ] La pantalla de login aparece al entrar.
- [ ] El botón "Continuar con Google" redirige a Google sin error 403.
- [ ] Se puede iniciar sesión con correo y contraseña.
- [ ] Después de iniciar sesión, se muestra el email del usuario en el sidebar.

---

## 4. 🖥️ Desarrollo local

Para correr la app en tu máquina:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Crear el archivo de secrets (NO lo subas a GitHub)
mkdir -p .streamlit
cat > .streamlit/secrets.toml << 'EOF'
[supabase]
url          = "https://<TU-PROJECT-ID>.supabase.co"
key          = "<TU-ANON-KEY>"
redirect_url = "http://localhost:8501"
EOF

# 3. Correr la app
python -m streamlit run app.py
```

> El archivo `.streamlit/secrets.toml` ya está en `.gitignore` — nunca se subirá al repositorio.

---

## 5. 📋 Checklist de configuración completa

| Paso | Servicio | Descripción | Estado |
|------|----------|-------------|--------|
| 1 | Supabase | Proyecto creado | ☐ |
| 2 | Supabase | Google OAuth activado con credenciales de Google | ☐ |
| 3 | Supabase | Redirect URLs configuradas | ☐ |
| 4 | Supabase | Tablas `progress` y `quiz_results` creadas con RLS | ☐ |
| 5 | Google Cloud | Pantalla de consentimiento en modo **Production** | ☐ |
| 6 | Google Cloud | Authorized redirect URI: `https://<id>.supabase.co/auth/v1/callback` | ☐ |
| 7 | Streamlit Cloud | App conectada al repositorio | ☐ |
| 8 | Streamlit Cloud | Secrets `[supabase]` configurados | ☐ |

---

## 6. 🔧 Solución de problemas comunes

| Error | Causa probable | Solución |
|-------|---------------|----------|
| Google retorna **403** | App OAuth en modo Testing o redirect URI incorrecto | Poner en Production (paso 2.2) y verificar redirect URI (paso 2.3) |
| `StreamlitSecretNotFoundError` | No hay secrets configurados | Agregar secrets en Streamlit Cloud (paso 3.2) |
| `Invalid redirect URL` en Supabase | La `redirect_url` no está en la lista de permitidas | Agregarla en Supabase → Authentication → URL Configuration |
| Login correcto pero vuelve a login | El token no se está guardando en session_state | Verificar que `_handle_oauth_callback()` funciona — revisar consola del navegador |
| La app en GitHub Pages no tiene login | Normal — stlite no tiene secrets, funciona en modo demo sin auth | Solo la app de Streamlit Cloud tiene autenticación |
