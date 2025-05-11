# REST-FASTAPI

Este é um projeto de exemplo usando FastAPI com banco de dados SQLite, demonstrando uma API REST simples com suporte aos métodos GET, POST e DELETE. Criado como parte de um desafio técnico da CEOS Jr. em seu Setor de Projetos.

Repositório: [https://github.com/nicolas-wallace/REST-FASTAPI](https://github.com/nicolas-wallace/REST-FASTAPI)

## Tecnologias usadas:

* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite
* Pydantic
* pytest
* Postman (para testes manuais)

Como rodar o projeto:

###  1. Clone o repositório:

git clone [https://github.com/nicolas-wallace/REST-FASTAPI.git](https://github.com/nicolas-wallace/REST-FASTAPI.git)
cd REST-FASTAPI

###  2. (Opcional) Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  (no Windows: venv\Scripts\activate)

### 3. Instale as dependências:

pip install requirements.txt

### 4. Rode a API com o Uvicorn:

uvicorn main\:app --reload

Ou com o FastAPI dev (se instalado):

fastapi dev main\:app

### Documentação automática da API:

* Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoints disponíveis:

GET /items - Lista todos os itens
POST /items - Cria um novo item
DELETE /items/{id} - Deleta um item pelo ID

### Exemplo de JSON para POST:

{
  "nome": "Caneta",
  "descricao": "Caneta preta"
}

### Testes automatizados:

Para executar os testes:

pytest

Isso roda o arquivo test\_main.py e verifica se os endpoints funcionam corretamente.

### Testando com Postman:

Abra o Postman e crie requisições para [http://127.0.0.1:8000/items](http://127.0.0.1:8000/items)
Use GET para listar, POST para criar (com JSON no corpo), DELETE para remover com /items/{id}

### Estrutura do projeto:

REST-FASTAPI/

├── app.db           # Arquivo do banco de dados SQLite

└── README.md        # Este arquivo

/app/

├── main.py          # Inicia a aplicação e importa as rotas

├── routes.py        # Define os endpoints da API

├── models.py        # Modelos de dados (com Pydantic e SQLAlchemy)

├── database.py      # Conexão e inicialização do banco de dados

├── test_main.py     # Testes automatizados com pytest

