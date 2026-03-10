from extract import extract_data
from load import load_data
from transform import transform_data

def pipeline():

    print("Iniciando pipeline...") 

    dados = extract_data()
    df = transform_data(dados)
    load_data(df)

    print("Pipeline executado com sucesso!")
    
if __name__ == "__main__":
    pipeline()
