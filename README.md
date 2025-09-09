# Energy Efficiency of Buildings (Green Building Analysis)

This project is part of my **Edunet X Shell Internship** (4 weeks), where I am analyzing the energy efficiency of buildings using AI and Machine Learning.  
The objective is to understand how building design parameters influence heating and cooling loads, and to develop models that can guide sustainable and energy-efficient building designs.

---

## Week 1

- Defined the problem statement and project scope  
- Collected and explored the dataset (**ENB2012_data.xlsx**)  
- Preprocessed the data (renamed columns, checked missing values)  
- Created feature distribution plots and a correlation heatmap to study relationships  
- Plotted **Relative Compactness vs Heating Load** to visualize its impact on energy efficiency  
- Split the dataset into **Train and Test sets** for modeling  

---

## Week 2

- Selected **Linear Regression** as the first baseline algorithm  
- Trained two models separately:  
  - **Heating Load Model (Y1)**  
  - **Cooling Load Model (Y2)**  
- Evaluated the models using metrics:  
  - **Mean Squared Error (MSE)**  
  - **Root Mean Squared Error (RMSE)**  
  - **R² Score**  
- Plotted **Actual vs Predicted values** for both Heating and Cooling Loads  
- Observed that Linear Regression gives a decent performance, but there is scope for improvement with advanced models  

---

## Why this matters
Heating and cooling are the largest contributors to building energy consumption.  
By identifying how features like compactness, surface area, wall area, and glazing ratio affect these loads, we can draw insights to design buildings that consume less energy while maintaining comfort.  
The visualizations and baseline models confirm important patterns, such as compact buildings needing less heating energy, which supports sustainable architectural choices.  

---

## Upcoming Weeks

I will continue with:  
- Trying advanced algorithms (Decision Trees, Random Forest, Gradient Boosting, etc.)  
- Optimizing models with hyperparameter tuning  
- Final model evaluation on test data  
- Model deployment with a simple web interface (FastAPI/Streamlit)  
