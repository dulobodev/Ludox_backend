# Ludox Backend

Backend API desenvolvido com FastAPI para o aplicativo Ludox - uma plataforma de e-commerce moderna e eficiente.

## 📋 Sobre o Projeto

O Ludox Backend é uma API REST robusta que fornece funcionalidades essenciais para um aplicativo de e-commerce, incluindo:

- **Autenticação de usuários** - Sistema de registro e login seguro
- **Gerenciamento de produtos** - CRUD completo para produtos com upload de imagens
- **Sistema de slides** - Gerenciamento de imagens para carrosséis e banners
- **Integração com MongoDB** - Banco de dados NoSQL para alta performance

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

## ⚙️ Pré-requisitos

- Python 3.11 ou superior
- Poetry (para gerenciamento de dependências)
- Acesso à internet (para conexão com MongoDB Atlas)

## 🔧 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd Ludox_backend/Backend
```

### 2. Instale o Poetry (se não tiver instalado)
```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Linux/macOS
curl -sSL https://install.python-poetry.org | python3 -
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
MONGODB_URL=sua_string_de_conexao_mongodb
PORT=8000
```

## 🚀 Como Executar

### Desenvolvimento
```bash
# Ative o ambiente virtual
poetry shell

# Execute o servidor de desenvolvimento
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

### Produção
```bash
# Execute sem reload
uvicorn src.app:app --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após executar o servidor, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

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

## 📝 Exemplos de Uso

### Registrar um usuário
```bash
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@exemplo.com",
    "password": "senha123"
  }'
```

### Fazer login
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@exemplo.com",
    "password": "senha123"
  }'
```

### Criar um produto
```bash
curl -X POST "http://localhost:8000/product" \
  -F "title=Produto Exemplo" \
  -F "description=Descrição do produto" \
  -F "feedback=5" \
  -F "value=99.99" \
  -F "parcela=12" \
  -F "file=@caminho/para/imagem.jpg"
```

### Listar produtos
```bash
curl -X GET "http://localhost:8000/products"
```

## 🔒 Segurança

- Senhas são criptografadas usando Argon2
- CORS configurado para permitir requisições de qualquer origem (ajuste conforme necessário)
- Validação de dados com Pydantic

## 🧪 Testes

```bash
# Execute os testes
poetry run pytest

# Execute com cobertura
poetry run pytest --cov=src
```

## 📦 Deploy

### Usando Docker (recomendado)
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Deploy em plataformas cloud
- **Heroku**: Configure o `Procfile`
- **Railway**: Deploy direto do GitHub
- **Render**: Configure o build command

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Eduardo** - [duduclobo00@gmail.com](mailto:duduclobo00@gmail.com)

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique a documentação da API em `/docs`
2. Consulte os logs do servidor
3. Abra uma issue no repositório
4. Entre em contato com o desenvolvedor

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!
