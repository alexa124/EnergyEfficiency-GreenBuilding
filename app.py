import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -------------------------
# Load dataset
# -------------------------
data = pd.read_excel("ENB2012_data.xlsx")

# Rename input + target columns
data.rename(columns={
    "X1": "Relative_Compactness",
    "X2": "Surface_Area",
    "X3": "Wall_Area",
    "X4": "Roof_Area",
    "X5": "Overall_Height",
    "X6": "Orientation",
    "X7": "Glazing_Area",
    "X8": "Glazing_Area_Distribution",
    "Y1": "Heating_Load",
    "Y2": "Cooling_Load"
}, inplace=True)

# Features
X = data.drop(["Heating_Load", "Cooling_Load"], axis=1)

# -------------------------
# Streamlit UI
# -------------------------
st.markdown(
    """
    <div style="text-align:center; padding:15px; background-color:#e8f5e9; border-radius:10px;">
        <h1 style="color:#2e7d32;">🌿 Energy Efficiency of Green Buildings</h1>
        <h4 style="color:#1b5e20;">Predicting Heating & Cooling Loads for Sustainable Design</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# Credit section
st.info("👨‍💻 Made by **Aman Pandey** during 4-week internship at **Edunet x Shell**")

st.write("This app predicts the **Heating Load** or **Cooling Load** of a building based on its design features — contributing to the analysis of **Energy Efficiency in Green Buildings**.")

# -------------------------
# Sidebar Info
# -------------------------
st.sidebar.title("📘 Project Info")
st.sidebar.markdown(
    """
    **Energy Efficiency of Green Buildings**  
    - Dataset: *Energy Efficiency Dataset (ENB2012)*  
    - Features: Building geometry & design  
    - Targets: Heating & Cooling Load  
    - Goal: Promote **sustainable, low-energy architecture**
    """
)
st.sidebar.markdown("---")
st.sidebar.success("Internship Project • Edunet x Shell")

# -------------------------
# Target selection
# -------------------------
target_choice = st.radio(
    "Select which load to predict:",
    ("Heating_Load", "Cooling_Load")
)

y = data[target_choice]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------
# User Input Section
# -------------------------
st.subheader("🏗️ Enter Building Features")

features = {}
for col in X.columns:
    features[col] = st.number_input(
        col.replace("_", " "),  # prettier label
        float(data[col].min()),
        float(data[col].max()),
        float(data[col].mean())
    )

input_df = pd.DataFrame([features])

if st.button(f"Predict {target_choice}"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Predicted {target_choice}: {prediction:.2f}")

    # -------------------------
    # Actual vs Predicted Graph
    # -------------------------
    y_pred = model.predict(X_test)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(y_test, y_pred, color="blue", alpha=0.6, label="Predictions")
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linewidth=2, label="Ideal Fit")
    ax.set_xlabel("Actual Values")
    ax.set_ylabel("Predicted Values")
    ax.set_title(f"Actual vs Predicted ({target_choice})")
    ax.legend()
    st.pyplot(fig)

# -------------------------
# Footer
# -------------------------
st.markdown(
    """
    <hr>
    <div style="text-align:center; color:gray; font-size:14px;">
        © 2025 | Energy Efficiency of Green Buildings | Developed by Aman Pandey
    </div>
    """,
    unsafe_allow_html=True
)
