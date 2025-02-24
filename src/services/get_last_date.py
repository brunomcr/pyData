from pyspark.sql import SparkSession
from utils.config import Config
from datetime import datetime

def get_last_date(spark, config):

    # Ler os dados do Parquet
    df = spark.read.parquet(config.bronze_path_bitcoin_data)

    # Obter a última data
    last_date_row = df.agg({"timestamp": "max"}).collect()[0][0]

    # Converter o timestamp para datetime
    if last_date_row is not None:
        last_date = datetime.fromtimestamp(last_date_row / 1000)  # Convertendo de milissegundos para segundos
    else:
        last_date = None

    return last_date 