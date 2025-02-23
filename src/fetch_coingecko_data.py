import requests  # Importing the requests library
import logging  # Importing the logging module

# Configuring the logging
logging.basicConfig(level=logging.INFO)

def fetch_coingecko_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    logging.info("Making request to CoinGecko API...")
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info("Request successful. Data received.")
        data = response.json()  # Armazena a resposta JSON
        logging.info(f"Primeiras linhas da resposta: {data}")  # Log das primeiras linhas da resposta
        return data  # Return the JSON response if the request was successful
    else:
        logging.error(f"Request error: {response.status_code}")
        return None  # Return None if the request failed 