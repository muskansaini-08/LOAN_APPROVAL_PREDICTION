import streamlit as st
import pickle
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Loan Approval System", page_icon="🏦", layout="wide")

# ---------- LOAD MODEL ----------
model = pickle.load(open("loan_model.pkl", "rb"))

# ---------- PROFESSIONAL HEADER ----------
st.markdown("""
    <h1 style='text-align:center; color:#0a1f44;'>🏦 Loan Approval System</h1>
    <hr>
""", unsafe_allow_html=True)

st.subheader("Enter Applicant Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Term", min_value=0)
    credit_history = st.selectbox("Credit History", [1, 0])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# ---------- ENCODING ----------
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
property_area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]

# Base feature list (10 main Kaggle features)
features = [
    gender,
    married,
    dependents,
    education,
    self_employed,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history
]

# ---------- AUTO FEATURE MATCH FIX ----------
expected_features = model.n_features_in_

if len(features) < expected_features:
    # Add zeros if model expects more features
    features.extend([0] * (expected_features - len(features)))

if len(features) > expected_features:
    # Trim extra features
    features = features[:expected_features]

input_data = np.array([features])

# ---------- PREDICTION ----------
if st.button("Check Loan Eligibility"):

    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

    except Exception as e:
        st.error("⚠ Model feature mismatch or encoding issue.")
        st.write("Model expects:", expected_features, "features")
        st.write("App is sending:", len(features), "features")
