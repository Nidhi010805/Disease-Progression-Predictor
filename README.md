# Heart Disease Risk Prediction System

##  Overview

The Heart Disease Risk Prediction System is an end-to-end Machine Learning application that predicts the likelihood of heart disease using clinical health parameters.

The system utilizes machine learning algorithms such as Logistic Regression, Random Forest, and XGBoost to analyze patient data and generate real-time risk predictions. An interactive Streamlit web application enables users to obtain instant risk assessments along with probability scores.

The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis, model training, evaluation, and deployment.

The system can assist in early risk identification and support healthcare decision-making.


##  Live Demo

[https://disease-progression-predictor-5vzotkw6atlrgdkuskwkmq.streamlit.app/]


##  Problem Statement

In healthcare, early prediction of disease progression is critical. Manual analysis of patient data is slow and error-prone.

This project builds an AI system that:
- Analyzes patient health data
- Predicts disease risk
- Classifies risk as Low / Medium / High

---

## Solution Approach

- Data collection and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training (Logistic Regression, Random Forest, XGBoost)
- Model evaluation using accuracy, precision, recall, F1-score
- Explainability using feature importance
- Deployment using Streamlit


## Features

- 🏥 Disease progression prediction
- 📈 Real-time ML predictions
- ⚖️ Risk classification:
  - 🟢 Low Risk
  - 🟠 Medium Risk
  - 🔴 High Risk
- 📉 High accuracy (~98–99%)
- 🌐 Interactive Streamlit web app
- 🧾 Explainable AI support (feature importance / SHAP ready)

---

## Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib & Seaborn
- Joblib

## Installation & Setup

### 1️⃣ Clone repository
[https://github.com/yourusername/Heart-Disease-Risk-Prediction.git](https://github.com/Nidhi010805/Disease-Progression-Predictor)


### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run Streamlit app
streamlit run app/app.py

 Model Performance
Model	Accuracy
Logistic Regression	79%
Random Forest	98.5%
XGBoost	98.5%

✔ Best Model: Random Forest / XGBoost

 Input Features
Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol
Fasting Blood Sugar
Rest ECG
Max Heart Rate
Exercise Induced Angina
Oldpeak
Slope
Number of vessels colored (ca)
Thalassemia


 # Output
The system predicts:
Probability of disease progression
Risk Category
🟢 Low Risk
🟠 Medium Risk
🔴 High Risk

 # Key Insights
Random Forest performed best due to non-linear pattern handling
Dataset shows strong feature separability
Explainability improves trust in medical predictions
Model is suitable for early risk detection systems

# Future Improvements
Add SHAP explainability inside Streamlit UI
Deploy on Streamlit Cloud / AWS
Add patient history tracking
Improve dataset size for better generalization
Add authentication system
