from services.fetch_data import fetch_data
from services.save_data import save_data
from services.get_last_date import get_last_date
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
        save_data(bitcoin_data, spark, config)

    spark.stop()

if __name__ == "__main__":
    main() 