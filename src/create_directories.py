import os
from utils.config import Config

def create_directories():
    """Verifica se as pastas necessárias existem e as cria se não existirem."""
    config = Config()
    
    # Cria as pastas necessárias
    os.makedirs(config.bronze_path, exist_ok=True)
    os.makedirs(config.silver_path, exist_ok=True)
    os.makedirs(config.gold_path, exist_ok=True)
    os.makedirs(config.bronze_path_bitcoin_data, exist_ok=True)
    os.makedirs(config.silver_path_bitcoin_data, exist_ok=True)
    os.makedirs(config.gold_path_bitcoin_data, exist_ok=True)
    
    print("Pastas necessárias criadas com sucesso.")

if __name__ == "__main__":
    create_directories() 