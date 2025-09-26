# Ludox Backend

Backend API desenvolvido com FastAPI para o aplicativo Ludox


## 🚀 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido para Python
- **MongoDB** - Banco de dados NoSQL
- **PyMongo** - Driver oficial do MongoDB para Python
- **Pydantic** - Validação de dados e serialização
- **Passlib** - Biblioteca para hash de senhas com Argon2
- **Poetry** - Gerenciamento de dependências e ambientes virtuais


## 🔧 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd Ludox_backend/Backend
```

### 2. Instale o Poetry (se não tiver instalado)
```bash
pip install -r requirements.txt
```

### 3. Instale as dependências
```bash
poetry install
```

### 4. Ative o ambiente virtual
```bash
poetry shell
```

### 5. Configure as variáveis de ambiente (opcional)
Crie um arquivo `.env` na raiz do projeto para configurações personalizadas:
```env
DB_NAME=name_mongodb
DB_PASSWORD=sua_senha
```

## 🚀 Como Executar

```bash
# Ative o ambiente virtual
poetry shell

# Execute o servidor de desenvolvimento
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após executar o servidor, acesse:
- **Swagger UI**: `http://localhost:8000/docs`


## 👨‍💻 Autor

**Eduardo** - [duduclobo00@gmail.com](mailto:duduclobo00@gmail.com)
