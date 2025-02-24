from services.fetch_data import fetch_data
from services.save_data import save_data_bronze, save_data_silver
from services.get_last_date import get_last_date
from services.data_processing import clean_data, transform_data
from utils.spark_session import get_spark_session
from utils.config import Config

def main():
    config = Config()

    spark = get_spark_session("Save Data to Parquet")

    # Obter a última data antes de coletar os dados
    last_date = get_last_date(spark, config)

    # Coletar os dados, passando a última data
    bitcoin_data = fetch_data(last_date)

    if bitcoin_data:
        save_data_bronze(bitcoin_data, spark, config.bronze_path_bitcoin_data)       

    # Limpar e transformar os dados da camada bronze
    df_cleaned = clean_data(config.bronze_path_bitcoin_data, config.silver_path_bitcoin_data, spark)
    df_transformed = transform_data(df_cleaned)

    # Salvar os dados transformados na camada silver
    save_data_silver(df_transformed, spark, config.silver_path_bitcoin_data)

    spark.stop()

if __name__ == "__main__":
    main() 