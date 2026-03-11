import logging
from src.load import load_data
from src.transform import transform_data
from src.extract import extract_data

def pipeline():

    logging.info("Iniciando pipeline...") 
    dados = extract_data()

    logging.info("Transformando dados...")
    df = transform_data(dados)

    logging.info("Carregando dados no banco...")
    load_data(df)
    
if __name__ == "__main__":
    pipeline()
