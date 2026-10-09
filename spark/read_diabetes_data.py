from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

spark = SparkSession.builder \
    .appName("HealthPredictionBigData") \
    .master("local[*]") \
    .getOrCreate()

print("Spark started successfully")

df = spark.read.csv(
    "hdfs://localhost:9000/health_prediction_bigdata_v2/input/diabetes_binary_5050split_health_indicators_BRFSS2015.csv",
    header=True,
    inferSchema=True
)

print("Total records:", df.count())

print("\nMissing values:")
df.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in df.columns
]).show()

spark.stop()
