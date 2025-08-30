# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar todos os arquivos do projeto para o container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para rodar a aplicação Flask usando Gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
