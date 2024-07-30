# API de Gerenciamento de Usuários

Esta é uma API simples desenvolvida com FastAPI para gerenciar usuários. A API permite criar, ler, atualizar e excluir usuários.

## Tecnologias Utilizadas

- Python
- FastAPI
- Pydantic

## Endpoints

### 1. Hello World

- **Método:** GET
- **Endpoint:** `/`
- **Descrição:** Retorna uma mensagem de saudação.

### 2. Listar Usuários

- **Método:** GET
- **Endpoint:** `/api/v1/users`
- **Descrição:** Retorna uma lista de todos os usuários.

### 3. Registrar Usuário

- **Método:** POST
- **Endpoint:** `/api/v1/users`
- **Descrição:** Adiciona um novo usuário à lista.
- **Corpo da Requisição:**
```json
{
    "first_name": "Vinicius",
    "last_name": "Silva",
    "middle_name": "Leonel",
    "gender": "male",
    "roles": ["admin"]
}
```

### 4. Deletar Usuário

- **Método:** DELETE
- **Endpoint:** `/api/v1/users/{user_id}`
- **Descrição:** Remove um usuário da lista com base no ID fornecido.

### 5. Atualizar Usuário

- **Método:** PUT
- **Endpoint:** `/api/v1/users/{user_id}`
- **Descrição:** Atualiza as informações de um usuário existente.
- **Corpo da Requisição:**
```json
{
    "first_name": "Lucas",
    "last_name": "Leonel",
    "middle_name": "Zeidan",
    "roles": ["user"]
}
```

## Estrutura do Projeto

- `main.py`: Contém a definição da API e os endpoints.
- `db.py`: Simula um banco de dados em memória com uma lista de usuários.
- `models.py`: Define os modelos de dados utilizados na API.

## Como Executar

1. Clone o repositório em https://github.com/viniciusleonel/python-fastapi.
2. Instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```
3. Execute a aplicação:
   ```bash
   uvicorn main:app --reload
   ```
4. Acesse a API em `http://localhost:8000`.

### Documentação FastAPI

- **Documentação Swagger:** http://localhost:8000/docs
- **Documentação Redoc:** http://localhost:8000/redoc

### Criado por **Vinicius Leonel**
- **GitHub:** https://github.com/viniciusleonel
- **LinkedIn:** https://www.linkedin.com/in/viniciuslps/

