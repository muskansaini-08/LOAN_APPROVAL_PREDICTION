import streamlit as st
import numpy as np

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Loan Approval System",
    page_icon="🏦",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F4F6FB;
}

/* Title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #4F46E5, #7C3AED);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Card container */
.card {
    background-color: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.05);
}

/* Section headers */
.section-title {
    font-size: 22px;
    font-weight: 600;
    color: #4F46E5;
    margin-bottom: 15px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #4F46E5, #7C3AED);
    color: white;
    border-radius: 10px;
    padding: 0.7rem 1.5rem;
    border: none;
    font-weight: 600;
    font-size: 16px;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #4338CA, #6D28D9);
}

/* Input fields */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("<h1 class='main-title'>🏦 Loan Approval System</h1>", unsafe_allow_html=True)
st.write("")

# ---------------- CARD START ---------------- #
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>Enter Applicant Details</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    applicant_income = st.number_input("Applicant Income", min_value=0, value=40000)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0, value=20000)
    loan_amount = st.number_input("Loan Amount", min_value=0, value=10000)
    loan_term = st.number_input("Loan Term (days)", min_value=0, value=360)
    credit_history = st.selectbox("Credit History", [1, 0])

st.write("")
predict_btn = st.button("Check Loan Eligibility")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SIMPLE DUMMY PREDICTION ---------------- #
def simple_prediction(applicant_income, loan_amount, credit_history):
    if credit_history == 1 and applicant_income > loan_amount * 2:
        return 1
    else:
        return 0

# ---------------- RESULT SECTION ---------------- #
if predict_btn:
    result = simple_prediction(applicant_income, loan_amount, credit_history)

    st.write("")

    if result == 1:
        st.markdown("""
        <div style='background-color:#ECFDF5;
                    padding:25px;
                    border-radius:15px;
                    color:#065F46;
                    font-weight:700;
                    font-size:20px;
                    text-align:center;
                    box-shadow:0 4px 12px rgba(16,185,129,0.2);'>
        ✅ Loan Approved
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='background-color:#FEF2F2;
                    padding:25px;
                    border-radius:15px;
                    color:#7F1D1D;
                    font-weight:700;
                    font-size:20px;
                    text-align:center;
                    box-shadow:0 4px 12px rgba(239,68,68,0.2);'>
        ❌ Loan Rejected
        </div>
        """, unsafe_allow_html=True)
