# FastAPI - API de Acomodações

Esta é uma API simples construída com FastAPI para gerenciar informações sobre acomodações. A API permite listar todas as acomodações, buscar por ID e filtrar por cidade.

## Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes itens instalados:

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)
- PostgreSQL (banco de dados)
- `dotenv` para gerenciar variáveis de ambiente

## Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Crie um ambiente virtual**

   ```bash
   python -m venv venv

3. **Ative o ambiente virtual**

   ```bash
   venv\Scripts\activate - se estiver usando windows
   source venv/bin/activate - se estiver usando macOS/Linux  

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt

## Configuração

1. **Crie um banco de dados no Postgresql**

   ```bash
   Ex: desafio

2. **Configure as variáveis de ambiente em um arquivo .env. Se tiver dúvidas, basta verificar o arquivo .env-example.**

   ```bash 
    USER='seu_user'
    PASSWORD='sua_senha'
    DB='seu_banco
'

## Executando a API

1. **Rode o comando:**

   ```bash
   uvicorn main:app --reload

A API estará disponível em http://127.0.0.1:8000