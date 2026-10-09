from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("HealthPredictionConfusionMatrix") \
    .master("local[*]") \
    .getOrCreate()

# Read dataset from HDFS
df = spark.read.csv(
    "hdfs://localhost:9000/health_prediction_bigdata_v2/input/diabetes_binary_5050split_health_indicators_BRFSS2015.csv",
    header=True,
    inferSchema=True
)

# Rename target column
df = df.withColumnRenamed("Diabetes_binary", "label")

# Prepare features
feature_columns = [c for c in df.columns if c != "label"]

assembler = VectorAssembler(
    inputCols=feature_columns,
    outputCol="features"
)

data = assembler.transform(df).select("label", "features")

# Use the same train-test split as before
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

# Train Random Forest
rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="features",
    numTrees=100,
    seed=42
)

model = rf.fit(train_data)

# Generate predictions
predictions = model.transform(test_data)

# Create confusion matrix
print("\n========== CONFUSION MATRIX ==========")

predictions.groupBy("label", "prediction") \
    .count() \
    .orderBy("label", "prediction") \
    .show()

print("========== CLASSIFICATION REPORT ==========")

evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

print("Accuracy:", evaluator.evaluate(predictions))

spark.stop()
