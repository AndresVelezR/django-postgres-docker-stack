# ============================================
# ETAPA 1: Imagen base
# ============================================
FROM python:3.11-slim

# Metadata
LABEL maintainer="avelezr8@eafit.edu.co"
LABEL description="Django application with PostgreSQL"

# ============================================
# ETAPA 2: Variables de entorno
# ============================================
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# ============================================
# ETAPA 3: Instalar dependencias del sistema
# ============================================
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# ============================================
# ETAPA 4: Directorio de trabajo
# ============================================
WORKDIR /app

# ============================================
# ETAPA 5: Copiar e instalar dependencias
# ============================================
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ============================================
# ETAPA 6: Copiar código de la aplicación
# ============================================
COPY . .

# ============================================
# ETAPA 7: Crear script de entrada
# ============================================
RUN echo '#!/bin/bash\n\
set -e\n\
echo "Esperando a PostgreSQL..."\n\
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do\n\
  sleep 0.1\n\
done\n\
echo "PostgreSQL iniciado"\n\
echo "Aplicando migraciones..."\n\
python manage.py makemigrations --noinput\n\
python manage.py migrate --noinput\n\
echo "Recolectando archivos estáticos..."\n\
python manage.py collectstatic --noinput\n\
echo "Iniciando servidor Django..."\n\
exec python manage.py runserver 0.0.0.0:8000\n\
' > /entrypoint.sh && chmod +x /entrypoint.sh

# ============================================
# ETAPA 8: Exponer puerto
# ============================================
EXPOSE 8000

# ============================================
# ETAPA 9: Comando de inicio
# ============================================
ENTRYPOINT ["/entrypoint.sh"]
