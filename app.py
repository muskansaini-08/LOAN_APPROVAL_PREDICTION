import streamlit as st
import pickle
import numpy as np

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}
.main {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    padding: 2rem;
    border-radius: 20px;
}
.card {
    background-color: white;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
}
.stButton>button {
    background-color: #1f4037;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 24px;
}
.stButton>button:hover {
    background-color: #14532d;
}
</style>
""", unsafe_allow_html=True)

# ---- LOAD MODEL ----
model = pickle.load(open("loan_model.pkl", "rb"))

# ---- HEADER ----
st.markdown("<h1 style='text-align: center; color: white;'>🏦 Smart Loan Approval System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>AI-powered Loan Eligibility Prediction</p>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Enter Applicant Details")

# ---- FORM LAYOUT ----
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Term (in days)", min_value=0)
    credit_history = st.selectbox("Credit History", [1, 0])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

st.markdown("<br>", unsafe_allow_html=True)

# ---- ENCODING ----
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
property_area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]

input_data = np.array([[gender, married, dependents, education,
                        self_employed, applicant_income,
                        coapplicant_income, loan_amount,
                        loan_term, credit_history, property_area]])

# ---- PREDICTION ----
if st.button("🚀 Predict Loan Status"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Congratulations! Loan Approved")
        st.balloons()
    else:
        st.error("❌ Sorry! Loan Rejected")

st.markdown("</div>", unsafe_allow_html=True)
