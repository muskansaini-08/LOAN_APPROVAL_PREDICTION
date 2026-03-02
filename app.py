import streamlit as st
import pickle
import numpy as np

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Loan Approval System", page_icon="🏦", layout="wide")

# -------- PROFESSIONAL CSS --------
st.markdown("""
<style>

/* Main background */
body {
    background-color: #f5f7fa;
}

/* Header */
.header {
    background-color: #0a1f44;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

.header h1 {
    color: white;
    margin-bottom: 5px;
}

.header p {
    color: #d1d9e6;
    font-size: 16px;
}

/* Form Card */
.card {
    background-color: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
}

/* Labels */
label {
    font-weight: 600 !important;
    color: #1f2937 !important;
}

/* Button */
.stButton>button {
    background-color: #0a1f44;
    color: white;
    font-size: 16px;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 30px;
    border: none;
}

.stButton>button:hover {
    background-color: #163c7a;
    color: white;
}

/* Success box */
.success-box {
    background-color: #e6f4ea;
    color: #1e7e34;
    padding: 15px;
    border-radius: 8px;
    font-weight: 600;
}

/* Error box */
.error-box {
    background-color: #fdecea;
    color: #b02a37;
    padding: 15px;
    border-radius: 8px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# -------- LOAD MODEL --------
model = pickle.load(open("loan_model.pkl", "rb"))

# -------- HEADER --------
st.markdown("""
<div class="header">
    <h1>🏦 Secure Loan Approval System</h1>
    <p>AI-Based Eligibility Prediction</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------- FORM CARD --------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("Applicant Information")

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
    loan_term = st.number_input("Loan Term (in days)", min_value=0)
    credit_history = st.selectbox("Credit History", [1, 0])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

st.markdown("<br>", unsafe_allow_html=True)

# -------- ENCODING --------
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

# -------- PREDICTION --------
if st.button("Check Loan Eligibility"):
    prediction = model.predict(input_data)

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction[0] == 1:
        st.markdown("<div class='success-box'>✅ Loan Approved</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='error-box'>❌ Loan Rejected</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
