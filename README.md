# Crypto Data Pipeline

Pipeline de dados em Python para coleta e armazenamento de preços de criptomoedas utilizando API, Pandas e PostgreSQL.

Este projeto implementa um **pipeline de dados em Python** para coletar informações de preços de criptomoedas através de uma API, realizar o tratamento desses dados e armazená-los em um **banco de dados PostgreSQL**.
O projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de **engenharia de dados**, incluindo extração, transformação e carga de dados (ETL), manipulação de dados com Python e integração com banco de dados.

---

# Tecnologias utilizadas

- Python
- Pandas
- Requests
- PostgreSQL
- python-dotenv
- Logging

---

# Estrutura do projeto

```
projeto-pipeline-cripto/
│
├── src/
│   ├── extract.py          # Extração dos dados da API
│   ├── transform.py        # Tratamento e transformação dos dados
│   ├── load.py             # Inserção dos dados no PostgreSQL
│   └── pipeline.py         # Orquestração do pipeline
│
├── data/                   # Arquivos CSV gerados pelo pipeline
│
├── logs/
│   └── pipeline.log        # Logs de execução
│
├── logger_config.py        # Configuração de logs
├── scheduler.py            # Agendamento do pipeline
├── main.py                 # Arquivo principal para executar o projeto
│
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd projeto-pipeline-cripto
```

---

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 3. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as credenciais do banco de dados.

Exemplo:

```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=criptomoedas
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
```

---

## 4. Executar o pipeline

```bash
python main.py
```

O pipeline irá:

1. Coletar dados de preços de criptomoedas através de uma API  
2. Transformar os dados utilizando **Pandas**  
3. Salvar os dados no **PostgreSQL**  
4. Registrar logs da execução

---

# Logs

Os logs de execução são registrados no arquivo:

```
logs/pipeline.log
```

---

# Agendamento

O projeto possui um arquivo `scheduler.py` que permite executar o pipeline automaticamente em horários definidos.

---

# Possíveis melhorias

Algumas melhorias que podem ser adicionadas futuramente:

- containerização com Docker
- orquestração com Airflow
- integração com um Data Warehouse
- criação de dashboards para visualização dos dados