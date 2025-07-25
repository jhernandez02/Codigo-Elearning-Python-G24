# Imagen base
FROM python:3.13-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 5000

# Comandos por defecto
CMD ["python","app.py"]