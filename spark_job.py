from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RealTimeETL") \
    .getOrCreate()

print("Spark Job Started")
