FROM python:3.11

# Definir o diretório de trabalho na imagem
WORKDIR /src

# Copiar o arquivo de requisitos para a imagem
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação para a imagem
COPY src .
COPY .env .

# migrations
RUN alembic upgrade head

# Comando padrão para executar os testes (pode ser ajustado conforme necessário)

CMD ["uvicorn", "application:app"]