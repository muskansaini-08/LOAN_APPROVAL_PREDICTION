# ----------------------------------
# IMPORT LIBRARIES (ALWAYS FIRST)
# ----------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# ----------------------------------
# PAGE CONFIG (MUST BE AFTER IMPORTS)
# ----------------------------------
st.set_page_config(
    page_title="LoanIQ - AI Credit Intelligence",
    layout="wide"
)

# ----------------------------------
# DARK THEME STYLING
# ----------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color: white;
}
label {
    color: white !important;
    font-weight: 600;
}
div.stButton > button {
    background: linear-gradient(90deg,#00c853,#1de9b6);
    color: white;
    height: 55px;
    width: 100%;
    font-size: 18px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
}
div.stButton > button:hover {
    background: linear-gradient(90deg,#00b248,#00e5ff);
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# LOAD MODEL (for feature importance)
# ----------------------------------
try:
    model = pickle.load(open("loan_model.pkl", "rb"))
except:
    model = None

# ----------------------------------
# TITLE
# ----------------------------------
st.title("🏦 LoanIQ - AI Credit Intelligence System")
st.markdown("### Smart Loan Approval Based on Income & Credit Score")

col1, col2 = st.columns(2)

# ----------------------------------
# INPUT SECTION
# ----------------------------------
with col1:

    st.subheader("📋 Applicant Details")

    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

    applicant_income = st.number_input("Applicant Income", value=40000)
    coapp_income = st.number_input("Coapplicant Income", value=0)

    loan_amount = st.number_input("Loan Amount (in thousands)", value=150)
    loan_term = st.selectbox("Loan Term (Months)", [360, 180, 120, 60])

    credit_history = st.selectbox("Credit History", ["Good", "Bad"])

# ----------------------------------
# PREDICTION SECTION
# ----------------------------------
with col2:

    st.subheader("🤖 Loan Decision Engine")

    if st.button("⚡ Evaluate Loan Eligibility"):

        total_income = applicant_income + coapp_income
        score = 0

        # -----------------------------
        # RULE-BASED SCORING SYSTEM
        # -----------------------------

        # Credit Score Weight
        if credit_history == "Good":
            score += 50
        else:
            score += 10

        # Income Weight
        if total_income >= 30000:
            score += 30
        elif total_income >= 15000:
            score += 20
        else:
            score += 5

        # Loan Amount Risk
        if loan_amount <= 200:
            score += 20
        else:
            score += 5

        # -----------------------------
        # FINAL DECISION
        # -----------------------------
        if score >= 70:
            prediction = "Approved"
            st.success("✅ LOAN APPROVED")
        else:
            prediction = "Rejected"
            st.error("❌ LOAN REJECTED")

        st.markdown(f"### Eligibility Score: {score}/100")
        st.progress(score)

        # -----------------------------
        # EMI CALCULATION
        # -----------------------------
        st.subheader("💰 EMI Estimation")

        interest_rate = 8.5
        loan_amount_value = loan_amount * 1000
        months = loan_term
        r = interest_rate / (12 * 100)

        emi = loan_amount_value * r * (1 + r)**months / ((1 + r)**months - 1)

        st.info(f"Estimated Monthly EMI: ₹ {int(emi)}")

        # -----------------------------
        # FEATURE IMPORTANCE CHART
        # -----------------------------
        if model is not None and hasattr(model, "feature_importances_"):

            st.subheader("📊 Feature Importance")

            feature_names = [
                "Gender",
                "Married",
                "Dependents",
                "Education",
                "SelfEmployed",
                "ApplicantIncome",
                "CoappIncome",
                "LoanAmount",
                "LoanTerm",
                "CreditHistory"
            ]

            fig, ax = plt.subplots()
            ax.barh(feature_names, model.feature_importances_)
            ax.set_title("Feature Impact on Loan Decision")
            st.pyplot(fig)

        # -----------------------------
        # DOWNLOAD REPORT
        # -----------------------------
        report = pd.DataFrame({
            "Prediction": [prediction],
            "Eligibility Score": [score],
            "Total Income": [total_income],
            "Loan Amount (Thousands)": [loan_amount],
            "Loan Term (Months)": [loan_term],
            "Credit History": [credit_history]
        })

        st.download_button(
            "📄 Download Loan Report",
            report.to_csv(index=False),
            file_name="loan_report.csv",
            mime="text/csv"
        )
