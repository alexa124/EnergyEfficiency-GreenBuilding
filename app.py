import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_excel("ENB2012_data.xlsx")

# Rename target columns for clarity
data.rename(columns={"Y1": "Heating_Load", "Y2": "Cooling_Load"}, inplace=True)

# Features & targets
X = data.drop(["Heating_Load", "Cooling_Load"], axis=1)

# Streamlit UI
st.title("🏠 Energy Efficiency Predictor")
st.write("This app predicts the **Heating Load** or **Cooling Load** of a building based on its design features.")

# User chooses target
target_choice = st.radio(
    "Select which load to predict:",
    ("Heating_Load", "Cooling_Load")
)

y = data[target_choice]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# User input
features = {}
for col in X.columns:
    features[col] = st.number_input(
        col, float(data[col].min()), float(data[col].max()), float(data[col].mean())
    )

input_df = pd.DataFrame([features])

if st.button(f"Predict {target_choice}"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Predicted {target_choice}: {prediction:.2f}")

