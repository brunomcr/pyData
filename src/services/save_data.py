from pyspark.sql.functions import from_unixtime, year, month, dayofmonth  # Importando funções para manipulação de data
from utils.logging_config import setup_logging  # Importando a configuração de logging

setup_logging()  # Configurando o logging
import logging  # Importando o módulo de logging

def save_data(data, spark, config):  # Atualizado para aceitar spark e config como parâmetros
    # Verifica se os dados estão presentes
    if not data:
        logging.error("Dados retornados estão vazios.")
        return

    # Se todas as listas estiverem presentes, use-as
    prices = data['prices']
    market_caps = data['market_caps']
    total_volumes = data['total_volumes']

    # Criar um DataFrame do Spark a partir das listas
    df_prices = spark.createDataFrame(prices, schema=['timestamp', 'price'])
    df_market_caps = spark.createDataFrame(market_caps, schema=['timestamp', 'market_cap'])
    df_total_volumes = spark.createDataFrame(total_volumes, schema=['timestamp', 'total_volume'])

    # Unir os DataFrames com base no timestamp
    df = df_prices.join(df_market_caps, on='timestamp', how='outer') \
                    .join(df_total_volumes, on='timestamp', how='outer')

    # Adicionar colunas para ano, mês e dia a partir do timestamp
    df = df.withColumn("year", year(from_unixtime(df["timestamp"] / 1000)))  # Convertendo timestamp para datetime e extraindo o ano
    df = df.withColumn("month", month(from_unixtime(df["timestamp"] / 1000)))  # Extraindo o mês
    df = df.withColumn("day", dayofmonth(from_unixtime(df["timestamp"] / 1000)))  # Extraindo o dia

    logging.info("Salvando dados em formato Parquet...")

    # Salvar os dados particionados por ano, mês e dia
    df.write.partitionBy("year", "month", "day").parquet(config.bronze_path_bitcoin_data, mode='overwrite')  # Usando a variável de path
    logging.info("Dados salvos com sucesso.") 