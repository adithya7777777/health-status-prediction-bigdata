from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder \
    .appName("HealthPredictionFeaturePreparation") \
    .master("local[*]") \
    .getOrCreate()

print("Spark started successfully")

# Read dataset from HDFS
df = spark.read.csv(
    "hdfs://localhost:9000/health_prediction_bigdata_v2/input/diabetes_binary_5050split_health_indicators_BRFSS2015.csv",
    header=True,
    inferSchema=True
)

# Rename target column
df = df.withColumnRenamed("Diabetes_binary", "label")

# Select feature columns
feature_columns = [column for column in df.columns if column != "label"]

# Combine all features into one vector
assembler = VectorAssembler(
    inputCols=feature_columns,
    outputCol="features"
)

data = assembler.transform(df)

print("\nFeature columns:")
print(feature_columns)

print("\nPrepared data:")
data.select("label", "features").show(5, truncate=False)

spark.stop()
