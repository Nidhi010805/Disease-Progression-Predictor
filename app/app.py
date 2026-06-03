import streamlit as st
import numpy as np
import joblib
import os

# ----------------------------
# SAFE PATH HANDLING
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "notebooks", "models", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "notebooks", "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# ----------------------------
# UI
# ----------------------------
st.title("🫀 Disease Progression Predictor")
st.write("Enter patient details to predict risk level")

# ----------------------------
# INPUT FIELDS (MATCH TRAINING DATA)
# ----------------------------
age = st.number_input("Age")
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.number_input("Chest Pain Type")
bp = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar (0/1)", [0, 1])
restecg = st.number_input("Rest ECG")
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Induced Angina (0/1)", [0, 1])
oldpeak = st.number_input("Oldpeak")
slope = st.number_input("Slope")
ca = st.number_input("Number of vessels colored (ca)")
thal = st.number_input("Thalassemia")

# ----------------------------
# PREDICTION
# ----------------------------
if st.button("Predict Risk"):

    input_data = np.array([[
        age, sex, cp, bp, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope,
        ca, thal
    ]])

    # scale input
    input_scaled = scaler.transform(input_data)

    # prediction probability
    prob = model.predict_proba(input_scaled)[0][1]

    # risk classification
    if prob < 0.3:
        risk = "🟢 Low Risk"
    elif prob < 0.7:
        risk = "🟠 Medium Risk"
    else:
        risk = "🔴 High Risk"

    # output
    st.subheader("Prediction Result")
    st.write("Probability:", round(prob, 3))
    st.write("Risk Level:", risk)