# Health Status Prediction
# Data Visualization using R

# Read dataset
data <- read.csv(
  "data/diabetes_binary_5050split_health_indicators_BRFSS2015.csv"
)

# Save graphs in results folder
png("results/diabetes_distribution.png",
    width = 900, height = 600)

diabetes_counts <- table(data$Diabetes_binary)

barplot(
  diabetes_counts,
  names.arg = c("No Diabetes", "Diabetes"),
  col = c("skyblue", "tomato"),
  main = "Diabetes Status Distribution",
  xlab = "Health Status",
  ylab = "Number of Records"
)

dev.off()


# BMI Distribution
png("results/bmi_distribution.png",
    width = 900, height = 600)

hist(
  data$BMI,
  col = "lightgreen",
  main = "BMI Distribution",
  xlab = "BMI",
  ylab = "Frequency",
  breaks = 30
)

dev.off()


# General Health Distribution
png("results/general_health_distribution.png",
    width = 900, height = 600)

health_counts <- table(data$GenHlth)

barplot(
  health_counts,
  names.arg = c(
    "Excellent", "Very Good", "Good", "Fair", "Poor"
  ),
  col = "orange",
  main = "General Health Distribution",
  xlab = "General Health",
  ylab = "Number of Records"
)

dev.off()

cat("All visualizations created successfully.\n")
