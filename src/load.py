import psycopg2
import os
import logging
from dotenv import load_dotenv

load_dotenv()


def load_data(df):

    if df is None or df.empty:
        logging.info("Nenhum dado para salvar.")
        return

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cursor = conn.cursor()

    # cria a tabela caso não exista
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cotacoes (
            id SERIAL PRIMARY KEY,
            moeda VARCHAR(50),
            preco_usd NUMERIC,
            data_coleta TIMESTAMP,
            UNIQUE (moeda, data_coleta)
        )
    """)

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO cotacoes (moeda, preco_usd, data_coleta)
            VALUES (%s, %s, %s)
            ON CONFLICT (moeda, data_coleta) DO NOTHING
            """,
            (row["moeda"], row["preco_usd"], row["data_coleta"])
        )

    conn.commit()

    cursor.close()
    conn.close()

    logging.info(f"{len(df)} registros inseridos no PostgreSQL.")
