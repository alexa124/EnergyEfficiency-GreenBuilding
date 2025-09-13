"""
Energy Efficiency of Buildings (Green Building Analysis)
Author: Aman Pandey
"""

# week6_energy_efficiency.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------
# Step 1: Define the Problem
# -------------------------
print("Problem: Predict Heating and Cooling Load of buildings based on their design features.")

# -------------------------
# Step 2: Data Collection and Understanding
# -------------------------
data = pd.read_excel("ENB2012_data.xlsx")
print("\nFirst 5 rows of dataset:")
print(data.head())
print("\nDataset Info:")
print(data.info())

# -------------------------
# Step 3: Data Preprocessing
# -------------------------
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

data.columns = [
    "Relative_Compactness", "Surface_Area", "Wall_Area", "Roof_Area",
    "Overall_Height", "Orientation", "Glazing_Area", "Glazing_Area_Distribution",
    "Heating_Load", "Cooling_Load"
]

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# -------------------------
# Step 4: Data Splitting
# -------------------------
X = data.drop(["Heating_Load", "Cooling_Load"], axis=1)
y_heating = data["Heating_Load"]
y_cooling = data["Cooling_Load"]

X_train, X_test, y_train_heat, y_test_heat = train_test_split(X, y_heating, test_size=0.2, random_state=42)
_, _, y_train_cool, y_test_cool = train_test_split(X, y_cooling, test_size=0.2, random_state=42)

# -------------------------
# Step 5: Algorithm Selection
# -------------------------
print("\nSelected Algorithms: Linear Regression, Ridge, Lasso")

# -------------------------
# Step 6: Model Training
# -------------------------
lin_model = LinearRegression()
lin_model.fit(X_train, y_train_heat)

ridge = Ridge()
lasso = Lasso()

# -------------------------
# Step 7: Model Evaluation
# -------------------------
y_pred_heat = lin_model.predict(X_test)
print("\nHeating Load - Linear Regression")
print("MSE:", mean_squared_error(y_test_heat, y_pred_heat))
print("R² Score:", r2_score(y_test_heat, y_pred_heat))

plt.figure(figsize=(6, 6))
plt.scatter(y_test_heat, y_pred_heat, alpha=0.7, color="blue")
plt.xlabel("Actual Heating Load")
plt.ylabel("Predicted Heating Load")
plt.title("Heating Load: Actual vs Predicted")
plt.plot([y_test_heat.min(), y_test_heat.max()],
         [y_test_heat.min(), y_test_heat.max()], "r--")
plt.show()

# -------------------------
# Step 8: Model Optimization (Hyperparameter Tuning)
# -------------------------
param_grid = {"alpha": [0.01, 0.1, 1, 10, 100]}

ridge_cv = GridSearchCV(ridge, param_grid, cv=5, scoring="r2")
ridge_cv.fit(X_train, y_train_heat)

lasso_cv = GridSearchCV(lasso, param_grid, cv=5, scoring="r2")
lasso_cv.fit(X_train, y_train_heat)

print("\nBest Ridge Alpha:", ridge_cv.best_params_)
print("Best Ridge Score:", ridge_cv.best_score_)

print("Best Lasso Alpha:", lasso_cv.best_params_)
print("Best Lasso Score:", lasso_cv.best_score_)

# -------------------------
# Step 9: Final Model Evaluation on Test Data
# -------------------------
ridge_best = Ridge(alpha=ridge_cv.best_params_["alpha"])
ridge_best.fit(X_train, y_train_heat)
y_pred_ridge = ridge_best.predict(X_test)

lasso_best = Lasso(alpha=lasso_cv.best_params_["alpha"])
lasso_best.fit(X_train, y_train_heat)
y_pred_lasso = lasso_best.predict(X_test)

print("\nFinal Evaluation (Heating Load):")
print("Linear Regression R²:", r2_score(y_test_heat, y_pred_heat))
print("Ridge Regression R²:", r2_score(y_test_heat, y_pred_ridge))
print("Lasso Regression R²:", r2_score(y_test_heat, y_pred_lasso))

# Plot comparison
models = ["Linear", "Ridge", "Lasso"]
scores = [
    r2_score(y_test_heat, y_pred_heat),
    r2_score(y_test_heat, y_pred_ridge),
    r2_score(y_test_heat, y_pred_lasso)
]

plt.figure(figsize=(6, 4))
sns.barplot(x=models, y=scores, palette="viridis")
plt.title("Model Comparison (Heating Load)")
plt.ylabel("R² Score")
plt.show()
