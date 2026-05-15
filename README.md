# GeekStore - Testes Automatizados

Este projeto foi desenvolvido como atividade prática da disciplina de Automação de Testes de Software.

A aplicação consiste em um pequeno e-commerce chamado **GeekStore**, desenvolvido com **FastAPI**, contendo funcionalidades de listagem de produtos e compra online, além de uma suíte completa de testes automatizados.

---

# Tecnologias Utilizadas

## Backend

* Python 3
* FastAPI
* SQLite
* Uvicorn

## Testes Automatizados

* Pytest
* Pytest-Cov
* Pytest-BDD
* Tavern
* Selenium
* WebDriver Manager


---

# Como configurar o ambiente local

## 1. Criar o ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

# Como executar a aplicação

A aplicação utiliza o FastAPI como backend.

Execute o comando:

```bash
uvicorn main:app --reload
```

Após iniciar o servidor:

* Frontend:

```text
http://localhost:8000
```

* Documentação Swagger:

```text
http://localhost:8000/docs
```

---

# Como executar os testes

Com o servidor FastAPI executando, abra um novo terminal e execute os testes.

## Executar todos os testes

```bash
pytest
```

---

## Executar testes com cobertura

```bash
pytest --cov=.
```

---

## Validar cobertura mínima obrigatória

```bash
pytest --cov=. --cov-fail-under=90
```

---

# Cobertura de Testes

O projeto atingiu:

```text
97% de cobertura total
```

---

# Tipos de Testes Implementados

## Testes Unitários

Validação das regras de negócio:

* cálculo de desconto
* processamento de pedidos
* gateway de pagamento

---

## Testes de API

Validação dos endpoints FastAPI:

* listagem de produtos
* compra com sucesso
* produto inexistente
* produto sem estoque

---

## Testes BDD

Implementados com:

* pytest-bdd
* Gherkin

Cenários escritos em linguagem natural.

---

## Testes Tavern

Validação do contrato da API REST.

---

## Testes End-to-End (E2E)

Automação do fluxo completo da aplicação utilizando:

* Selenium
* ChromeDriver

Simulando ações reais do usuário no navegador.

---

# Banco de Dados

A aplicação utiliza SQLite.

O banco é criado automaticamente na primeira execução.

Arquivo:

```text
geekstore.db
```

---

# Funcionalidades da Aplicação

* Listagem de produtos
* Compra de produtos
* Aplicação de cupom de desconto
* Controle de estoque
* Integração simulada com gateway de pagamento

---

# Autor

Arthur Matos Rocha

Projeto desenvolvido para fins acadêmicos na disciplina de Automação de Testes de Software.
