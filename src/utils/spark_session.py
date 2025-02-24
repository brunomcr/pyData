from pyspark.sql import SparkSession

def get_spark_session(app_name="Spark Application"):
    """Cria e retorna uma sessão do Spark."""
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    return spark

def stop_spark_session(spark):
    """Para a sessão do Spark."""
    if spark:
        spark.stop() 