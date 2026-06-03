# 🫀 Disease Progression Predictor (AI + ML Project)

## 📌 Overview

The **Disease Progression Predictor** is an end-to-end Machine Learning system that predicts the risk level of disease progression in patients based on clinical health parameters.

It uses ML models like **Random Forest / XGBoost** and provides a **Streamlit web app** for real-time predictions with risk classification.

The system helps in early disease detection and supports medical decision-making.

---

## 🚀 Live Demo

[https://disease-progression-predictor-5vzotkw6atlrgdkuskwkmq.streamlit.app/]

---

## 🎯 Problem Statement

In healthcare, early prediction of disease progression is critical. Manual analysis of patient data is slow and error-prone.

This project builds an AI system that:
- Analyzes patient health data
- Predicts disease risk
- Classifies risk as Low / Medium / High

---

## 🧠 Solution Approach

- Data collection and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training (Logistic Regression, Random Forest, XGBoost)
- Model evaluation using accuracy, precision, recall, F1-score
- Explainability using feature importance
- Deployment using Streamlit

---

## 📊 Features

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

## 🛠️ Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib & Seaborn
- Joblib

---

## 📁 Project Structure
Disease-Progression-Predictor/
│
├── app/
│ └── app.py # Streamlit web app
│
├── notebooks/
│ ├── model.pkl # Trained ML model
│ ├── scaler.pkl # Feature scaler
│ ├── EDA_training.ipynb # Data analysis & training
│
├── requirements.txt
├── README.md
├── .gitignore


---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository
```bash
git clone https://github.com/yourusername/Disease-Progression-Predictor.git
cd Disease-Progression-Predictor

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run Streamlit app
streamlit run app/app.py

🧪 Model Performance
Model	Accuracy
Logistic Regression	79%
Random Forest	98.5%
XGBoost	98.5%

✔ Best Model: Random Forest / XGBoost

📌 Input Features
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


📊 Output

The system predicts:

Probability of disease progression
Risk Level:
🟢 Low Risk
🟠 Medium Risk
🔴 High Risk

🧠 Key Insights
Random Forest performed best due to non-linear pattern handling
Dataset shows strong feature separability
Explainability improves trust in medical predictions
Model is suitable for early risk detection systems

📸 Screenshots (Add Later)
Streamlit UI
Prediction results

Feature importance graph
SHAP explanation plots
🚀 Future Improvements
Add SHAP explainability inside Streamlit UI
Deploy on Streamlit Cloud / AWS
Add patient history tracking
Improve dataset size for better generalization
Add authentication system
