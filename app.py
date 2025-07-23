# app.py
import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('xgboost_model.pkl')

st.set_page_config(page_title="SmartPremium", page_icon="💰")
st.title("💰 SmartPremium: Insurance Premium Predictor")

st.markdown("Please enter customer details below:")

# ---------------------- Input Fields ---------------------- #

id = st.number_input("Customer ID", value=1001)

age = st.slider("Age", 18, 100, 35)
gender = st.selectbox("Gender", ['Male', 'Female'])  # 0/1
income = st.number_input("Annual Income", min_value=0, value=500000)
marital = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])  # 0/1/2
dependents = st.slider("Number of Dependents", 0, 10, 2)
education = st.selectbox("Education Level", ['High School', "Bachelor's", "Master's", "PhD"])  # 0–3
occupation = st.selectbox("Occupation", ['Employed', 'Self-Employed', 'Unemployed'])  # 0–2
health = st.slider("Health Score", 0, 100, 70)
location = st.selectbox("Location", ['Urban', 'Suburban', 'Rural'])  # 0–2
policy_type = st.selectbox("Policy Type", ['Basic', 'Comprehensive', 'Premium'])  # 0–2
claims = st.number_input("Previous Claims", 0, 100, 1)
vehicle_age = st.number_input("Vehicle Age", 0.0, 30.0, 5.0, step=0.5)
credit = st.slider("Credit Score", 300, 850, 650)
duration = st.slider("Insurance Duration (Years)", 1, 30, 5)
smoking = st.selectbox("Smoking Status", ['No', 'Yes'])  # 0/1
exercise = st.selectbox("Exercise Frequency", ['Daily', 'Weekly', 'Monthly', 'Rarely'])  # 0–3
property_type = st.selectbox("Property Type", ['House', 'Apartment', 'Condo'])  # 0–2

# ---------------------- Encoding Categorical Fields ---------------------- #

gender_map = {'Male': 0, 'Female': 1}
marital_map = {'Single': 0, 'Married': 1, 'Divorced': 2}
education_map = {'High School': 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
occupation_map = {'Employed': 0, 'Self-Employed': 1, 'Unemployed': 2}
location_map = {'Urban': 0, 'Suburban': 1, 'Rural': 2}
policy_map = {'Basic': 0, 'Comprehensive': 1, 'Premium': 2}
smoking_map = {'No': 0, 'Yes': 1}
exercise_map = {'Daily': 0, 'Weekly': 1, 'Monthly': 2, 'Rarely': 3}
property_map = {'House': 0, 'Apartment': 1, 'Condo': 2}

# Apply mapping
input_data = np.array([[id,
                        age,
                        gender_map[gender],
                        income,
                        marital_map[marital],
                        dependents,
                        education_map[education],
                        occupation_map[occupation],
                        health,
                        location_map[location],
                        policy_map[policy_type],
                        claims,
                        vehicle_age,
                        credit,
                        duration,
                        smoking_map[smoking],
                        exercise_map[exercise],
                        property_map[property_type]
                        ]])

# ---------------------- Prediction ---------------------- #

if st.button("Predict Premium Amount"):
    prediction = model.predict(input_data)
    st.success(f"💵 Predicted Insurance Premium: ₹ {prediction[0]:,.2f}")
