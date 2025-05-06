import requests
import os
from datetime import datetime, timezone, timedelta


def fetch_coingecko_data():
    # Variáveis de Ambiente chave de API COINGECKO
    api_key = os.environ.get('COINGECKO_API_KEY')

    # Calcule as datas necessárias
    data_fim = datetime.now(timezone.utc) - timedelta(days=1)
    data_inicio = data_fim - timedelta(days=364)

    # Passara para timestamp UNIX
    timestamp_inicio = int(data_inicio.timestamp())
    timestamp_ontem = int(data_fim.timestamp())

    # URL e parâmetros para solicitação da API
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": str(timestamp_inicio),
        "to": str(timestamp_ontem)
    }
    headers = {'Authorization': f'Bearer {api_key}'}

    # Solicitação GET
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro na solicitação da API:", response.status_code, response.text)
        return None
