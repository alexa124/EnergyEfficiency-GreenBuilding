# Energy Efficiency of Buildings (Green Building Analysis)

This project is part of my **Edunet X Shell Internship** (4 weeks), where I am analyzing the energy efficiency of buildings using AI and Machine Learning.  

The objective is to understand how building design parameters influence **heating and cooling loads**, and to develop models that can guide sustainable and energy-efficient building designs.  

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

## Week 3
- Implemented advanced algorithms:  
  - **Decision Trees**  
  - **Random Forests**  
  - **Gradient Boosting (XGBoost/LightGBM)**  
- Compared performances with baseline  
- Tuned **hyperparameters** (GridSearchCV/RandomizedSearchCV)  
- Achieved improved accuracy & reduced error  

---

## Week 4
- Selected **best-performing model** on test set  
- Conducted **final evaluation** with unseen data  
- Built an interactive **Streamlit app**:  
  - User inputs building features  
  - Model predicts **Heating & Cooling Loads**  
- Deployed locally using **Streamlit**  

---

## Why this matters
Heating and cooling are the largest contributors to building energy consumption.  

By identifying how features like **compactness, surface area, wall area, and glazing ratio** affect these loads, we can design buildings that consume less energy while maintaining comfort.  

The visualizations and models confirm important patterns, such as **compact buildings needing less heating energy**, which supports sustainable architectural choices.