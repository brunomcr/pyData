import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def clean_data(bronze_path, silver_path, spark):
    """Limpa os dados recebidos da camada bronze, removendo linhas nulas."""
    # Carregar os dados da camada bronze
    df_bronze = spark.read.parquet(bronze_path)

    # Verifica se os dados estão vazios
    if df_bronze.isEmpty():
        raise ValueError("Dados inválidos ou vazios.")

    # Remove linhas nulas
    df_bronze = df_bronze.na.drop()  # Remove linhas com valores nulos

    return df_bronze  # Retorna o DataFrame limpo

def transform_data(df):
    """Transforma os dados para análise, convertendo features específicas em float."""
    # Converte as colunas 'price', 'market_cap' e 'total_volume' para float
    df = df.withColumn('price', col('price').cast('float'))
    df = df.withColumn('market_cap', col('market_cap').cast('float'))
    df = df.withColumn('total_volume', col('total_volume').cast('float'))

    return df  # Retorna o DataFrame transformado 