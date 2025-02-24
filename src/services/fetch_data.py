import requests  # Importando a biblioteca requests
from utils.logging_config import setup_logging  # Importando a configuração de logging
import time  # Importando o módulo time para calcular timestamps

setup_logging()  # Configurando o logging
import logging  # Importando o módulo de logging

def fetch_data(last_date=None):
    to_timestamp = int(time.time())  # Timestamp atual
    
    if last_date:
        from_timestamp = int(last_date.timestamp())  # Convertendo a última data para timestamp
    else:
        from_timestamp = to_timestamp - (90 * 24 * 60 * 60)  # Timestamp para 90 dias atrás
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={from_timestamp}&to={to_timestamp}"  # Endpoint atualizado
    logging.info("Making request to CoinGecko API...")
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info("Request successful. Data received.")
        data = response.json()  # Armazena a resposta JSON
        return data  # Retorna todos os dados recebidos
    else:
        logging.error(f"Request error: {response.status_code}")
        return None  # Return None if the request failed 