import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_excel("ENB2012_data.xlsx")

# Features & target
X = data.drop(["Heating_Load", "Cooling_Load"], axis=1)
y = data["Heating_Load"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit UI
st.title("🏠 Energy Efficiency Predictor")
st.write("This app predicts the **Heating Load** of a building based on its design features.")

# User input
features = {}
for col in X.columns:
    features[col] = st.number_input(
        col, float(data[col].min()), float(data[col].max()), float(data[col].mean())
    )

input_df = pd.DataFrame([features])

if st.button("Predict Heating Load"):
    prediction = model.predict(input_df)[0]
    st.success(f"🔥 Predicted Heating Load: {prediction:.2f}")
