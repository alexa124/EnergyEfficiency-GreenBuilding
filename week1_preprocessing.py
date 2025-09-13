"""
Energy Efficiency of Buildings (Green Building Analysis)
Author: Aman Pandey
"""

# ==============================
# 1. Define the Problem
# ==============================
# Goal: Predict Heating Load (Y1) and Cooling Load (Y2) of buildings 
# using architectural features (Wall Area, Roof Area, Orientation, etc.)

# ==============================
# 2. Data Collection & Understanding
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (ENB2012)
data = pd.read_excel("ENB2012_data.xlsx")
print("Data Shape:", data.shape)
print(data.head())

# ==============================
# 3. Data Preprocessing
# ==============================
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Rename columns for clarity
data.columns = [
    "Relative_Compactness", "Surface_Area", "Wall_Area", "Roof_Area", 
    "Overall_Height", "Orientation", "Glazing_Area", "Glazing_Area_Distribution", 
    "Heating_Load", "Cooling_Load"
]

# Features (X) & Targets (Y1, Y2)
X = data.drop(["Heating_Load", "Cooling_Load"], axis=1)
y1 = data["Heating_Load"]
y2 = data["Cooling_Load"]

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==============================
# 4. Data Splitting
# ==============================
X_train, X_test, y1_train, y1_test, y2_train, y2_test = train_test_split(
    X_scaled, y1, y2, test_size=0.2, random_state=42
)

# ==============================
# 5. Algorithm Selection
# ==============================
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42)
}

# ==============================
# 6. Model Training
# ==============================
trained_models = {}
for name, model in models.items():
    model.fit(X_train, y1_train)
    trained_models[name + "_Heating"] = model
    
    model.fit(X_train, y2_train)
    trained_models[name + "_Cooling"] = model

# ==============================
# 7. Model Evaluation
# ==============================
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    return mae, rmse, r2

results = {}
for name, model in trained_models.items():
    if "Heating" in name:
        mae, rmse, r2 = evaluate(model, X_test, y1_test)
    else:
        mae, rmse, r2 = evaluate(model, X_test, y2_test)
    results[name] = {"MAE": mae, "RMSE": rmse, "R2": r2}

results_df = pd.DataFrame(results).T
print("\nModel Evaluation Results:\n", results_df)

# ==============================
# 8. Model Optimization (Hyperparameter Tuning)
# ==============================
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [5, 10, None]
}

grid = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid,
    cv=3,
    scoring="neg_mean_squared_error",
    n_jobs=-1
)

grid.fit(X_train, y1_train)
best_heating_model = grid.best_estimator_

grid.fit(X_train, y2_train)
best_cooling_model = grid.best_estimator_

print("\nBest Params (Heating):", best_heating_model)
print("\nBest Params (Cooling):", best_cooling_model)

# ==============================
# 9. Final Model Evaluation on Test Data
# ==============================
heating_mae, heating_rmse, heating_r2 = evaluate(best_heating_model, X_test, y1_test)
cooling_mae, cooling_rmse, cooling_r2 = evaluate(best_cooling_model, X_test, y2_test)

print("\nFinal Heating Model Performance:")
print("MAE:", heating_mae, "RMSE:", heating_rmse, "R2:", heating_r2)

print("\nFinal Cooling Model Performance:")
print("MAE:", cooling_mae, "RMSE:", cooling_rmse, "R2:", cooling_r2)
