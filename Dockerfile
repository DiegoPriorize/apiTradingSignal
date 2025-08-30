
# Usar uma imagem base do Python
FROM python:3.9-slim

# Setar o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expôr a porta do Flask
EXPOSE 5000

# Comando para iniciar o servidor
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
