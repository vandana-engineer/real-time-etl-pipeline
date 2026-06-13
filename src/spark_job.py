from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RealTimeETL") \
    .getOrCreate()

data = [("101", 250.75), ("102", 500.00)]

df = spark.createDataFrame(data, ["order_id", "amount"])

df.show()

spark.stop()
