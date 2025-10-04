# ===============================================
# Pandas and Matplotlib Data Analysis Assignment
# ===============================================

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # Seaborn style for better plots

# --------------------------
# Task 1: Load and Explore Dataset
# --------------------------

try:
    # Load the CSV dataset
    df = pd.read_csv("data/iris.csv")  # Put your CSV in the data/ folder
    
    print("=== First 5 Rows of Dataset ===")
    print(df.head(), "\n")
    
    print("=== Dataset Info ===")
    print(df.info(), "\n")
    
    print("=== Missing Values ===")
    print(df.isnull().sum(), "\n")
    
    # Clean missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

except FileNotFoundError:
    print("Error: File not found. Please check your dataset path.")
except pd.errors.EmptyDataError:
    print("Error: File is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# --------------------------
# Task 2: Basic Data Analysis
# --------------------------

print("=== Summary Statistics ===")
print(df.describe(), "\n")

# Grouping: mean sepal length per species
if 'species' in df.columns and 'sepal_length' in df.columns:
    group_mean = df.groupby('species')['sepal_length'].mean()
    print("=== Average Sepal Length per Species ===")
    print(group_mean, "\n")

# --------------------------
# Task 3: Data Visualization
# --------------------------

# 1. Line Chart: Sepal length trend by index
plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal_length'], marker='o', linestyle='-')
plt.title("Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()

# 2. Bar Chart: Average Petal Length per Species
if 'species' in df.columns and 'petal_length' in df.columns:
    species_mean = df.groupby('species')['petal_length'].mean()
    species_mean.plot(kind='bar', color='skyblue')
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length")
    plt.show()

# 3. Histogram: Distribution of Petal Width
plt.hist(df['petal_width'], bins=10, color='lightgreen', edgecolor='black')
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.scatter(df['sepal_length'], df['petal_length'], c='purple', alpha=0.6)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()
