from pyspark.sql import SparkSession
from utils.config import Config
from datetime import datetime
import os  # Importando os para verificar a existência do arquivo
import logging

def get_last_date(spark, config):

    try:
        df = spark.read.parquet(config.bronze_path_bitcoin_data)
    except Exception as e:
        logging.error(f"Erro ao ler o arquivo Parquet: {e}")
        return None

    if df.isEmpty():
        logging.warning("O DataFrame lido está vazio. Retornando None.")
        return None

    last_date_row = df.agg({"timestamp": "max"}).collect()[0][0]

    if last_date_row is not None:
        last_date = last_date_row / 1000  
        return int(last_date) 
    else:
        last_date = None
