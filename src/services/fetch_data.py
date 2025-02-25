import requests  
from utils.logging_config import setup_logging  
import time  
from datetime import datetime

setup_logging()  
import logging  

def fetch_data(from_timestamp=None, to_timestamp=None):
    to_timestamp = int(time.time())
    logging.info(f"Timestamp atual: {datetime.fromtimestamp(to_timestamp)}")
    
    if from_timestamp is None:
        from_timestamp = to_timestamp - (90 * 24 * 60 * 60)        

    logging.info(f"Timestamp de 90 dias atrás: {datetime.fromtimestamp(from_timestamp)}")

    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={from_timestamp}&to={to_timestamp}"  # Endpoint atualizado
    logging.info("Making request to CoinGecko API...")
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info("Request successful. Data received.")
        data = response.json() 
        return data 
    else:
        logging.error(f"Request error: {response.status_code}")
        return None 