import requests

def extract_data():
    
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum,solana,cardano",
        "vs_currencies": "usd"
    }  

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as erro:
        print(f'Erro ao acessar API: {erro}')
    return None