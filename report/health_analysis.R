# Health Status Prediction
# Statistical Analysis using R

cat("====================================\n")
cat(" HEALTH STATUS PREDICTION ANALYSIS\n")
cat("====================================\n")

# Read the health dataset
data <- read.csv(
  "data/diabetes_binary_5050split_health_indicators_BRFSS2015.csv"
)

# Dataset overview
cat("\n1. DATASET OVERVIEW\n")
cat("Total records:", nrow(data), "\n")
cat("Total columns:", ncol(data), "\n")

# Check missing values
cat("\n2. MISSING VALUES\n")
cat("Total missing values:", sum(is.na(data)), "\n")

# Diabetes status counts
cat("\n3. DIABETES STATUS COUNTS\n")
print(table(data$Diabetes_binary))

# Diabetes status percentages
cat("\n4. DIABETES STATUS PERCENTAGES\n")
print(round(prop.table(table(data$Diabetes_binary)) * 100, 2))

# BMI statistics
cat("\n5. BMI STATISTICS\n")
print(summary(data$BMI))

# Age category statistics
cat("\n6. AGE CATEGORY DISTRIBUTION\n")
print(table(data$Age))

# General health distribution
cat("\n7. GENERAL HEALTH DISTRIBUTION\n")
print(table(data$GenHlth))

cat("\nR statistical analysis completed successfully.\n")
