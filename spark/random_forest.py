from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("HealthPredictionRandomForestEvaluation") \
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

# Feature columns
feature_columns = [column for column in df.columns if column != "label"]

# Create feature vector
assembler = VectorAssembler(
    inputCols=feature_columns,
    outputCol="features"
)

data = assembler.transform(df).select("label", "features")

# Split data
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

print("Training records:", train_data.count())
print("Testing records:", test_data.count())

# Random Forest
rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="features",
    numTrees=100,
    seed=42
)

print("\nTraining Random Forest...")
model = rf.fit(train_data)

print("Random Forest training completed")

# Predictions
predictions = model.transform(test_data)

# Accuracy
accuracy_evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = accuracy_evaluator.evaluate(predictions)

# Weighted Precision
precision_evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedPrecision"
)

precision = precision_evaluator.evaluate(predictions)

# Weighted Recall
recall_evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedRecall"
)

recall = recall_evaluator.evaluate(predictions)

# F1 Score
f1_evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="f1"
)

f1 = f1_evaluator.evaluate(predictions)

print("\n========== MODEL EVALUATION ==========")

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

print("\n========== PERCENTAGE ==========")

print("Accuracy :", accuracy * 100)
print("Precision:", precision * 100)
print("Recall   :", recall * 100)
print("F1 Score :", f1 * 100)

spark.stop()
