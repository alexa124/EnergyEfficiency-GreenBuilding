import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# --------------------------
# Step 1: Define the Problem
# --------------------------
''' We want to predict Heating Load (Y1) and Cooling Load (Y2) of buildings 
 based on design parameters like Relative Compactness, Surface Area, Wall Area, Roof Area, etc.
 This helps in understanding energy efficiency in green buildings.'''

# --------------------------
# Step 2: Load Dataset
# --------------------------
data = pd.read_excel("ENB2012_data.xlsx")

# Rename columns for clarity
data.columns = [
    "Relative_Compactness", "Surface_Area", "Wall_Area", "Roof_Area",
    "Overall_Height", "Orientation", "Glazing_Area", "Glazing_Area_Distribution",
    "Heating_Load", "Cooling_Load"
]

print("Dataset Loaded. Shape:", data.shape)

# --------------------------
# Step 3: Split Data
# --------------------------
X = data.iloc[:, :-2]   # Features
y1 = data["Heating_Load"]   # Target 1
y2 = data["Cooling_Load"]   # Target 2

X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=42)
X_train, X_test, y2_train, y2_test = train_test_split(X, y2, test_size=0.2, random_state=42)

print("Training and testing sets created successfully.")

# --------------------------
# Step 4: Algorithm Selection
# --------------------------
# We start with a simple model: Linear Regression
model_y1 = LinearRegression()
model_y2 = LinearRegression()

# --------------------------
# Step 5: Model Training
# --------------------------
model_y1.fit(X_train, y1_train)
model_y2.fit(X_train, y2_train)

print("\nModels trained successfully.")

# --------------------------
# Step 6: Model Evaluation
# --------------------------
# Predictions
y1_pred = model_y1.predict(X_test)
y2_pred = model_y2.predict(X_test)

# Evaluation Metrics
mse_y1 = mean_squared_error(y1_test, y1_pred)
rmse_y1 = np.sqrt(mse_y1)
r2_y1 = r2_score(y1_test, y1_pred)

mse_y2 = mean_squared_error(y2_test, y2_pred)
rmse_y2 = np.sqrt(mse_y2)
r2_y2 = r2_score(y2_test, y2_pred)

print("\n--- Heating Load Model Performance ---")
print("MSE:", mse_y1)
print("RMSE:", rmse_y1)
print("R2 Score:", r2_y1)

print("\n--- Cooling Load Model Performance ---")
print("MSE:", mse_y2)
print("RMSE:", rmse_y2)
print("R2 Score:", r2_y2)

# Scatter plot: Actual vs Predicted (Heating Load)
plt.figure(figsize=(6,4))
plt.scatter(y1_test, y1_pred, alpha=0.7, color="blue")
plt.xlabel("Actual Heating Load")
plt.ylabel("Predicted Heating Load")
plt.title("Actual vs Predicted Heating Load")
plt.show()

# Scatter plot: Actual vs Predicted (Cooling Load)
plt.figure(figsize=(6,4))
plt.scatter(y2_test, y2_pred, alpha=0.7, color="green")
plt.xlabel("Actual Cooling Load")
plt.ylabel("Predicted Cooling Load")
plt.title("Actual vs Predicted Cooling Load")
plt.show()
