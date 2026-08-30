# WS Backend Fábrica de Software 26.2

API desenvolvida em Python utilizando Django e Django REST Framework para gerenciamento de produtos.

##  Sobre o projeto

Este projeto foi desenvolvido para a disciplina Fábrica de Software 26.2.

A aplicação consiste em uma API REST para cadastro e gerenciamento de produtos, permitindo realizar um CRUD completo:

- Criar produtos
- Listar produtos
- Consultar um produto específico
- Atualizar produtos
- Excluir produtos

##  Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Git
- GitHub
- Visual Studio Code

## 📁 Estrutura do projeto

    WSBackendFabricaDeSoftware26.2/
    │
    ├── api/
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   └── ...
    │
    ├── config/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── manage.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

# Como executar o projeto

## 1. Pré-requisitos

É necessário ter instalado:

- Python 3
- Git
- Visual Studio Code

Para verificar o Python:

    python --version

Para verificar o Git:

    git --version

## 2. Clonar o projeto

No terminal:

    git clone URL_DO_REPOSITORIO

Depois entre na pasta:

    cd WSBackendFabricaDeSoftware26.2

## 3. Abrir o projeto no VS Code

Dentro da pasta do projeto:

    code .

Também é possível abrir a pasta manualmente pelo Visual Studio Code.

## 4. Criar o ambiente virtual

Execute:

    python -m venv venv

Isso criará a pasta `venv`, responsável pelo ambiente virtual do projeto.

## 5. Ativar o ambiente virtual

No Windows PowerShell:

    .\venv\Scripts\Activate.ps1

No Windows CMD:

    venv\Scripts\activate

Quando estiver ativado, aparecerá `(venv)` no início do terminal.

Exemplo:

    (venv) PS C:\Users\usuario\WSBackendFabricaDeSoftware26.2>

## 6. Instalar as dependências

Com o ambiente virtual ativado:

    pip install -r requirements.txt

Caso seja necessário instalar manualmente:

    pip install django djangorestframework

## 7. Criar as migrações

Execute:

    python manage.py makemigrations

Depois:

    python manage.py migrate

As migrações são responsáveis por preparar e atualizar as estruturas do banco de dados.

## 8. Iniciar o servidor

Execute:

    python manage.py runserver

Se estiver tudo correto, aparecerá algo semelhante a:

    Starting development server at http://127.0.0.1:8000/

## 9. Acessar a API

Com o servidor funcionando, abra o navegador e acesse:

    http://127.0.0.1:8000/api/produtos/

Essa é a rota principal da API de produtos.

Para acessar um produto específico:

    http://127.0.0.1:8000/api/produtos/1/

O número `1` representa o ID do produto.

# 🔄 Operações da API

## GET - Listar produtos

Método:

    GET

URL:

    http://127.0.0.1:8000/api/produtos/

Retorna todos os produtos cadastrados.

## GET - Consultar um produto

Método:

    GET

URL:

    http://127.0.0.1:8000/api/produtos/1/

Retorna o produto que possui ID 1.

## POST - Criar produto

Método:

    POST

URL:

    http://127.0.0.1:8000/api/produtos/

Exemplo de dados:

    {
        "nome": "tênis",
        "preco": "300.90",
        "descricao": "tênis esportivo"
    }

## PUT - Atualizar produto

Método:

    PUT

URL:

    http://127.0.0.1:8000/api/produtos/1/

Exemplo:

    {
        "nome": "tênis",
        "preco": "350.90",
        "descricao": "tênis esportivo de alta qualidade"
    }

## PATCH - Atualizar parcialmente

Método:

    PATCH

URL:

    http://127.0.0.1:8000/api/produtos/1/

Exemplo:

    {
        "preco": "350.90"
    }

O PATCH permite alterar somente um campo ou alguns campos do produto.

## DELETE - Excluir produto

Método:

    DELETE

URL:

    http://127.0.0.1:8000/api/produtos/1/

Exclui o produto que possui ID 1.

#  Como testar a API

Com o servidor ligado, acesse:

    http://127.0.0.1:8000/api/produtos/

O Django REST Framework disponibiliza uma interface no navegador para testar os endpoints.

É possível testar:

- GET
- POST
- PUT
- PATCH
- DELETE

Também podem ser utilizadas ferramentas como Postman ou Insomnia.

#  Fluxo completo do CRUD

## 1. Criar um produto

Utilize:

    POST /api/produtos/

Exemplo:

    {
        "nome": "tênis",
        "preco": "300.90",
        "descricao": "tênis esportivo"
    }

## 2. Listar os produtos

Utilize:

    GET /api/produtos/

## 3. Consultar um produto

Utilize:

    GET /api/produtos/1/

## 4. Atualizar um produto

Utilize PUT:

    PUT /api/produtos/1/

Ou PATCH:

    PATCH /api/produtos/1/

## 5. Excluir um produto

Utilize:

    DELETE /api/produtos/1/

#  Como parar o servidor

Para parar o servidor Django:

    CTRL + C

#  Como executar novamente depois

Quando voltar ao projeto em outro momento:

## 1. Entrar na pasta

    cd WSBackendFabricaDeSoftware26.2

## 2. Ativar o ambiente virtual

No Windows PowerShell:

    .\venv\Scripts\Activate.ps1

## 3. Iniciar o servidor

    python manage.py runserver

## 4. Acessar a API

    http://127.0.0.1:8000/api/produtos/

Não é necessário criar o ambiente virtual novamente se a pasta `venv` já existir.


#  Desenvolvimento

Projeto desenvolvido para a disciplina Fábrica de Software 26.2.

##  Licença

Projeto acadêmico desenvolvido para fins de estudo e aprendizado.