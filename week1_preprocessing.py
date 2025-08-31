import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Step 1: Define the Problem
''' We want to predict Heating Load (Y1) and Cooling Load (Y2) of buildings 
 based on design parameters like Relative Compactness, Surface Area, Wall Area, Roof Area, etc.
 This helps in understanding energy efficiency in green buildings.'''

# Step 2: Load Dataset
data = pd.read_excel("ENB2012_data.xlsx")
print("First 5 rows of dataset:")
print(data.head())

# Step 3: Check for missing values
print("\nMissing values in dataset:")
print(data.isnull().sum())

plt.figure(figsize=(8,5))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Check")
plt.show()

# Step 4: Basic Visualizations
# Histogram of all features
data.hist(figsize=(12, 10), bins=20)
plt.suptitle("Feature Distributions")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Scatter plot example (Relative Compactness vs Heating Load)
plt.figure(figsize=(6,4))
sns.scatterplot(x="X1", y="Y1", data=data)
plt.title("Relative Compactness vs Heating Load")
plt.xlabel("Relative Compactness (X1)")
plt.ylabel("Heating Load (Y1)")
plt.show()

# Step 5: Split Data into Training and Testing Sets
X = data.iloc[:, :-2]  # input features
y1 = data["Y1"]        # Heating Load
y2 = data["Y2"]        # Cooling Load

X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=42)
X_train, X_test, y2_train, y2_test = train_test_split(X, y2, test_size=0.2, random_state=42)

print("\nTraining and Testing data prepared successfully.")
