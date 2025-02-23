from pyspark.sql import SparkSession  # Importando o SparkSession
import logging  # Importando o módulo de logging

# Configurando o logging
logging.basicConfig(level=logging.INFO)

def save_data_to_parquet(data):
    # Verifica se a chave 'market_data' está presente nos dados
    if 'market_data' not in data:
        logging.error("Dados retornados não contêm a chave 'market_data'")
        return

    # Extraindo as features desejadas
    market_data = data['market_data']
    features = {
        'current_price': market_data['current_price']['usd'],
        'market_cap': market_data['market_cap']['usd'],
        'total_volume': market_data['total_volume']['usd'],
        'price_change_percentage_24h': market_data['price_change_percentage_24h'],
        'high_24h': market_data['high_24h']['usd'],
        'low_24h': market_data['low_24h']['usd'],
        'ath': market_data['ath']['usd'],
        'ath_change_percentage': market_data['ath_change_percentage']['usd'],
        'last_updated': market_data['last_updated'],
    }

    # Criar uma sessão do Spark
    spark = SparkSession.builder \
        .appName("Save Data to Parquet") \
        .getOrCreate()

    # Criar um DataFrame do Spark a partir das features
    df = spark.createDataFrame([features])  # Usando uma lista para criar um DataFrame com uma linha
    logging.info("Salvando dados em formato Parquet...")
    df.write.parquet('data/bitcoin_data.parquet', mode='overwrite')  # Salvar sem particionamento
    logging.info("Dados salvos com sucesso.")

    # Parar a sessão do Spark
    spark.stop() 