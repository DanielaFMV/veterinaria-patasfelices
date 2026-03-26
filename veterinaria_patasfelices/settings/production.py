import dj_database_url
from .base import *
from decouple import config

# ─── MODO DEPURACIÓN ────────────────────────────────────────

# OBLIGATORIO: False en producción
DEBUG = False

# ─── HOSTS PERMITIDOS ───────────────────────────────────────

# Lee desde variable de entorno en Render, separados por coma
# Ejemplo: ALLOWED_HOSTS = veterinaria.onrender.com
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

# ─── BASE DE DATOS ──────────────────────────────────────────

# Lee la URL de Supabase desde la variable de entorno DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# ─── SEGURIDAD HTTPS ────────────────────────────────────────

# Render usa HTTPS, estas opciones protegen las cookies y sesiones
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
