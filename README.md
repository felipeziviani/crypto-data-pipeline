# Crypto Data Pipeline

Pipeline de dados em Python para coleta e armazenamento de preços de criptomoedas utilizando API, Pandas e PostgreSQL.

Este projeto implementa um **pipeline de dados em Python** para coletar informações de preços de criptomoedas através de uma API, realizar o tratamento desses dados e armazená-los em um **banco de dados PostgreSQL**.
O projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de **engenharia de dados**, incluindo extração, transformação e carga de dados (ETL), manipulação de dados com Python e integração com banco de dados.

---

# Tecnologias utilizadas

* Python
* Pandas
* Requests
* PostgreSQL
* python-dotenv

---

# Estrutura do projeto

```
project/
│
├── src/                      # Código do pipeline
│   ├── extract.py            # Extração de dados da API
│   ├── transform.py          # Tratamento e transformação dos dados
│   ├── load.py               # Inserção dos dados no banco PostgreSQL
│   └── pipeline.py           # Orquestração do pipeline
│
├── .env.example              # Exemplo de variáveis de ambiente
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Funcionamento do pipeline

O pipeline segue o fluxo clássico de **ETL**:

### 1. Extração

O módulo `extract.py` coleta dados de preços de criptomoedas a partir de uma API.

### 2. Transformação

O módulo `transform.py` realiza o tratamento e a organização dos dados utilizando **Pandas**.

### 3. Carga

O módulo `load.py` salva os dados tratados em um **banco de dados PostgreSQL**.

### 4. Orquestração

O arquivo `pipeline.py` executa todas as etapas do pipeline na ordem correta.

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd nome-do-projeto
```

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 3. Criar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com as credenciais do banco de dados.

Exemplo:

```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=criptomoedas
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
```

## 4. Executar o pipeline

```
python src/pipeline.py
```

Após a execução, os dados serão coletados, processados e armazenados no banco de dados configurado.

---

# Objetivo do projeto

Este projeto foi desenvolvido como prática em:

* Construção de pipelines de dados
* Consumo de APIs
* Manipulação de dados com Pandas
* Persistência de dados em banco relacional
* Organização de projetos Python para engenharia de dados

---

# Possíveis melhorias futuras

* Agendamento automático do pipeline
* Containerização com Docker
* Orquestração com Airflow
* Integração com Data Warehouse
* Criação de dashboards para visualização dos dados
