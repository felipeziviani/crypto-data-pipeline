import pandas as pd
from datetime import datetime


def transform_data(data):

    if data is None:
        return None

    registros = []

    for moeda, valores in data.items():
        registros.append({
            "moeda": moeda,
            "preco_usd": valores["usd"],
            "data_coleta": datetime.now().replace(second=0, microsecond=0)
        })

    df = pd.DataFrame(registros)

    return df
