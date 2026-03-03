import streamlit as st
import time

st.set_page_config(page_title="LoanIQ - Loan Approval", layout="centered")

# Title
st.title("🏦 LoanIQ - Loan Approval Prediction")
st.write("Fill applicant details and click predict to see result instantly.")

st.markdown("---")

# =========================
# Applicant Form
# =========================

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

# =========================
# Prediction Button
# =========================

if st.button("⚡ Predict Loan Approval"):

    # Fake loading effect
    with st.spinner("Processing..."):
        time.sleep(1)

    # Simple Manual Logic (You can replace with ML model)
    if credit_history == "Good" and app_income + co_income > 20000:
        result = "APPROVED"
        color = "green"
    else:
        result = "REJECTED"
        color = "red"

    st.markdown("---")

    # =========================
    # Result Section (Below Button)
    # =========================

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:10px;
            background-color:#111;
            text-align:center;
            border: 2px solid {color};
        ">
            <h2 style="color:{color};">Loan {result}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
