# Imagen base compatible con Raspberry Pi (ARM)
FROM python:3.11-slim

# Evita buffers y .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (si usas GPIO u otras libs nativas)
RUN apt-get update && apt-get install -y \
    gcc \
    libgpiod-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero (mejor cache)
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar SOLO los archivos necesarios
COPY gpio-meal-manager.py .
COPY config.py .
COPY run.sh .
COPY web ./web

# Comando por defecto
# CMD ["bash", "run.sh"]
