import os


def create_directories(config):
    """Verifica se as pastas necessárias existem e as cria se não existirem."""
    
    # Cria as pastas necessárias
    os.makedirs(config.bronze_path, exist_ok=True)
    os.makedirs(config.silver_path, exist_ok=True)
    os.makedirs(config.gold_path, exist_ok=True)
    os.makedirs(config.bronze_path_bitcoin_data, exist_ok=True)
    os.makedirs(config.silver_path_bitcoin_data, exist_ok=True)
    os.makedirs(config.gold_path_bitcoin_data, exist_ok=True)
    

