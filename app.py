import streamlit as st
import time

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Loan Approval System",
    layout="centered"
)

# -------------------------------
# Custom CSS (Clean Light Card UI)
# -------------------------------
st.markdown("""
<style>

/* Whole page background */
[data-testid="stAppViewContainer"] {
    background-color: #f4f6fb;
}

/* Center Card */
.main-card {
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}

/* Title */
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: #5b4bdb;
    margin-bottom: 30px;
}

/* Section Title */
.section-title {
    font-size: 20px;
    font-weight: 600;
    color: #5b4bdb;
    margin-bottom: 20px;
}

/* Input fields */
.stSelectbox div[data-baseweb="select"],
.stNumberInput input {
    background-color: #f1f3f9 !important;
    border-radius: 10px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #5b4bdb, #7b6df0);
    color: white;
    font-weight: 600;
    border-radius: 10px;
    height: 45px;
    width: 220px;
    border: none;
}

/* Result Box */
.result-box {
    margin-top: 30px;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
}

.approved {
    background-color: #d4f3e8;
    color: #0f5132;
}

.rejected {
    background-color: #f8d7da;
    color: #842029;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Card Container Start
# -------------------------------
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="main-title">🏦 Loan Approval System</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Enter Applicant Details</div>', unsafe_allow_html=True)

# -------------------------------
# Two Column Layout
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    app_income = st.number_input("Applicant Income", min_value=0, value=40000)
    co_income = st.number_input("Coapplicant Income", min_value=0, value=20000)
    loan_amount = st.number_input("Loan Amount", min_value=0, value=10000)
    loan_term = st.number_input("Loan Term (days)", min_value=0, value=360)
    credit_history = st.selectbox("Credit History", ["1", "0"])

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------
# Button
# -------------------------------
if st.button("Check Loan Eligibility"):

    with st.spinner("Checking eligibility..."):
        time.sleep(1)

    total_income = app_income + co_income

    if credit_history == "1" and total_income > 20000:
        result = "APPROVED"
    else:
        result = "REJECTED"

    if result == "APPROVED":
        st.markdown(
            '<div class="result-box approved">✅ Loan Approved</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-box rejected">❌ Loan Rejected</div>',
            unsafe_allow_html=True
        )

# Close card div
st.markdown('</div>', unsafe_allow_html=True)
