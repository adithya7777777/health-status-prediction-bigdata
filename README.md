# Health Status Prediction Using Big Data

## Project Overview

This project uses Big Data technologies and Machine Learning to predict diabetes status based on health indicators. It processes the dataset using Hadoop and Apache Spark, evaluates a Random Forest classification model, and uses R for statistical analysis and visualization.

## Objectives

* Process health data using Hadoop HDFS.
* Analyze diabetes records using Hadoop MapReduce.
* Build a prediction model using Apache Spark MLlib.
* Evaluate the model using classification metrics.
* Analyze and visualize health indicators using R.

## Technologies Used

* Hadoop HDFS
* Hadoop MapReduce
* Apache Spark
* PySpark MLlib
* Random Forest
* Python
* R Programming

## Dataset

**Dataset:** Diabetes Health Indicators BRFSS 2015

* Total records: 70,692
* Total columns: 22
* Input features: 21
* Target column: `Diabetes_binary`
* Class 0: No diabetes
* Class 1: Diabetes

The dataset is not included in this repository. Obtain it from a legitimate source and place the CSV file in the `data/` folder before running the programs.

## Project Structure

* `mapreduce/` — Hadoop MapReduce mapper and reducer.
* `spark/` — Data preparation, Random Forest training, and evaluation scripts.
* `report/` — R statistical analysis and visualization scripts.
* `results/` — Model metrics and generated visualization images.

## Model Results

Random Forest model using 100 trees:

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 74.31% |
| Precision | 74.38% |
| Recall    | 74.31% |
| F1 Score  | 74.30% |

## Visualizations

The project generates the following plots:

1. Diabetes class distribution
2. BMI distribution
3. General health distribution

The images are available in the `results/` folder.

## Conclusion

The project demonstrates how Hadoop, Apache Spark, Random Forest, and R can be combined for large-scale health data processing, prediction, statistical analysis, and visualization.

**Disclaimer:** This is an educational project and is not intended for medical diagnosis.
