# Week 1: Energy Efficiency of Buildings (Green Building Analysis)

# Step 1: Problem Definition
"""
This project is about predicting Heating Load and Cooling Load of buildings
using design parameters. By analyzing this, we can suggest more
energy-efficient (green) building designs.
"""

# Step 2: Data Collection and Understanding
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_excel("ENB2012_data.xlsx")  # Make sure this file is inside the project folder

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# Step 3: Data Preprocessing
data.columns = [
    "Relative_Compactness", "Surface_Area", "Wall_Area", "Roof_Area",
    "Overall_Height", "Orientation", "Glazing_Area",
    "Glazing_Area_Distribution", "Heating_Load", "Cooling_Load"
]

print("\nMissing Values Check:")
print(data.isnull().sum())

# Features and Target
X = data.drop(["Heating_Load", "Cooling_Load"], axis=1)
Y = data[["Heating_Load", "Cooling_Load"]]

# Scaling Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nFeatures Shape:", X_scaled.shape)
print("Target Shape:", Y.shape)

# Step 4: Data Splitting
X_train, X_temp, Y_train, Y_temp = train_test_split(X_scaled, Y, test_size=0.3, random_state=1)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=1)

print("\nTraining Set:", X_train.shape, Y_train.shape)
print("Validation Set:", X_val.shape, Y_val.shape)
print("Test Set:", X_test.shape, Y_test.shape)
