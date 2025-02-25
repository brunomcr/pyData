from services.fetch_data import fetch_data
from services.save_data import save_data_bronze, save_data_silver
from services.get_last_date import get_last_date
from services.data_processing import clean_data, transform_data
from utils.spark_session import get_spark_session
from utils.config import Config
from utils.create_directories import create_directories
import logging


def main():
    config = Config()

    logging.info("Creating directories...")
    create_directories(config)

    logging.info("Getting Spark session...")
    spark = get_spark_session("Save Data to Parquet")

    logging.info("Getting last date...")
    last_date = get_last_date(spark, config)

    logging.info("Fetching data...")
    if last_date is None:
        logging.info("No last date found. Fetching data for the last 90 days.")
        bitcoin_data = fetch_data()
    else:
        logging.info(f"Last date found. Fetching data 90 days ago from last date: {last_date}.")
        bitcoin_data = fetch_data(last_date)

    logging.info("Saving data to bronze...")
    if bitcoin_data:
        save_data_bronze(bitcoin_data, spark, config.bronze_path_bitcoin_data)       
    
    if save_data_bronze:
        logging.info("Cleaning and transforming data...")
        df_cleaned = clean_data(config.bronze_path_bitcoin_data, config.silver_path_bitcoin_data, spark)

        logging.info("Transforming data...")
        df_transformed = transform_data(df_cleaned)

        logging.info("Saving data to silver...")
        save_data_silver(df_transformed, spark, config.silver_path_bitcoin_data)

    logging.info("Stopping Spark session...")
    spark.stop()

if __name__ == "__main__":
    main() 