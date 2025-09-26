# Ludox Backend

Backend API desenvolvido com FastAPI para o aplicativo Ludox - uma plataforma de e-commerce moderna e eficiente.

## 🚀 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido para Python
- **MongoDB** - Banco de dados NoSQL
- **PyMongo** - Driver oficial do MongoDB para Python
- **Pydantic** - Validação de dados e serialização
- **Passlib** - Biblioteca para hash de senhas com Argon2
- **Poetry** - Gerenciamento de dependências e ambientes virtuais

## 📁 Estrutura do Projeto

```
Backend/
├── src/
│   ├── app.py              # Aplicação principal FastAPI
│   ├── controllers/        # Controladores/Routers da API
│   │   ├── Auth.py         # Autenticação (login/registro)
│   │   ├── Product.py      # Gerenciamento de produtos
│   │   └── Slide.py        # Upload e gerenciamento de slides
│   ├── models/             # Modelos Pydantic
│   │   ├── Auth.py         # Modelos de autenticação
│   │   ├── Product.py      # Modelos de produtos
│   │   └── Slider.py       # Modelos de slides
│   ├── core/               # Configurações centrais
│   │   └── db.py           # Conexão com MongoDB
│   └── images/             # Diretório para armazenar imagens
├── tests/                  # Testes automatizados
├── pyproject.toml          # Configuração do Poetry
├── poetry.lock             # Lock file das dependências
└── README.md               # Este arquivo
```

## 🔧 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd Ludox_backend/Backend
```

### 2. Instale o Poetry junto de algumas dependecias
```bash
pip install -r requirements.txt
```

### 3. Instale as dependências do Poetry
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
MONGODB_URI = 
```

## 🚀 Como Executar

### Desenvolvimento
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


## 🔗 Endpoints Principais

### Autenticação
- `POST /register` - Registrar novo usuário
- `POST /login` - Fazer login

### Produtos
- `POST /product` - Criar produto (com upload de imagem)
- `GET /products` - Listar todos os produtos

### Slides/Imagens
- `POST /upload` - Upload de imagem para slides
- `POST /get` - Obter imagem de slide

### Saúde da API
- `GET /healtcheck` - Verificar status da API

## 👨‍💻 Autor

**Eduardo** - [duduclobo00@gmail.com](mailto:duduclobo00@gmail.com)
