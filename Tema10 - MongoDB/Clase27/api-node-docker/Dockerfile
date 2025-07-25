# Imagen base
FROM node:18

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar las dependencias
RUN npm install

# Exponer puerto
EXPOSE 3000

# Comando por defecto
CMD ["npm","run","dev"]