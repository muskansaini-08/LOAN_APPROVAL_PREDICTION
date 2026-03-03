import streamlit as st
import time

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="LoanIQ - Loan Approval",
    layout="centered"
)

# -------------------------------
# Custom CSS (Dark Futuristic UI)
# -------------------------------
st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #00F5A0;
}

.sub-text {
    text-align: center;
    font-size: 18px;
    color: #AAAAAA;
    margin-bottom: 30px;
}

.stButton>button {
    background: linear-gradient(90deg, #00F5A0, #00C9FF);
    color: black;
    font-size: 18px;
    font-weight: 600;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    border: none;
}

.stButton>button:hover {
    opacity: 0.85;
}

.result-box {
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    margin-top: 20px;
}

.approved {
    background-color: #0f5132;
    color: #00ff88;
    border: 2px solid #00ff88;
}

.rejected {
    background-color: #5a1a1a;
    color: #ff4d4d;
    border: 2px solid #ff4d4d;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown('<div class="main-title">🏦 LoanIQ</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Fill applicant details and click predict to see result instantly.</div>', unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# Applicant Form
# -------------------------------

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Marital Status", ["Married", "Single"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
credit_history = st.selectbox("Credit History", ["Good", "Poor"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

app_income = st.number_input("Applicant Income (Monthly)", min_value=0)
co_income = st.number_input("Co-Applicant Income (Monthly)", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (Months)", min_value=0)

st.markdown("")

# -------------------------------
# Predict Button
# -------------------------------

if st.button("⚡ Predict Loan Approval"):

    with st.spinner("Processing..."):
        time.sleep(1)

    # Simple Approval Logic (Replace with ML model if needed)
    total_income = app_income + co_income

    if credit_history == "Good" and total_income > 20000:
        result = "APPROVED"
    else:
        result = "REJECTED"

    # -------------------------------
    # Result Section (Below Button)
    # -------------------------------

    if result == "APPROVED":
        st.markdown(
            '<div class="result-box approved">✅ LOAN APPROVED</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-box rejected">❌ LOAN REJECTED</div>',
            unsafe_allow_html=True
        )
