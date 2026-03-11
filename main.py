from src.pipeline import pipeline
from logger_config import setup_logger
import logging
import time

def main():
    setup_logger()

    logging.info("Iniciando execução do pipeline...")
    inicio = time.time()

    try:
        pipeline()
        fim = time.time()
        tempo_execucao = fim - inicio
        logging.info(f"Pipeline finalizado com sucesso em {tempo_execucao:.2f} segundos.")
    except Exception as e:
        logging.error(f"Erro na execução do pipeline: {e}")


if __name__ == "__main__":
    main()