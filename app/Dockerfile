# Dockerfile

# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos (requirements.txt) al contenedor
COPY requirements.txt .

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente al contenedor
COPY . .

# Expone el puerto 5000 para que Flask esté accesible desde fuera del contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]

