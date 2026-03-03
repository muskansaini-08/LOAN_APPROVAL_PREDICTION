import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="LoanIQ - Smart Loan Approval",
                   layout="wide")

# ----------------------------
# CUSTOM CSS (PREMIUM UI)
# ----------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color: white;
}
div.stButton > button {
    background: linear-gradient(90deg,#00c853,#1de9b6);
    color: white;
    height: 55px;
    width: 100%;
    font-size: 18px;
    border-radius: 12px;
    border: none;
}
div.stButton > button:hover {
    background: linear-gradient(90deg,#00b248,#00e5ff);
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD MODEL
# ----------------------------
model = pickle.load(open("loan_model.pkl", "rb"))

# ----------------------------
# HEADER
# ----------------------------
st.title("🏦 LoanIQ - AI Credit Intelligence System")
st.markdown("### Predict Loan Approval Instantly Using Machine Learning")

col1, col2 = st.columns(2)

# ----------------------------
# INPUT SECTION
# ----------------------------
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
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# ----------------------------
# ENCODING INPUT
# ----------------------------
def preprocess():
    data = [
        1 if gender=="Male" else 0,
        1 if married=="Yes" else 0,
        0 if dependents=="0" else 1,
        1 if education=="Graduate" else 0,
        1 if self_employed=="Yes" else 0,
        applicant_income,
        coapp_income,
        loan_amount,
        loan_term,
        1 if credit_history=="Good" else 0,
        1 if property_area=="Urban" else 0
    ]
    return np.array(data).reshape(1, -1)

# ----------------------------
# PREDICTION SECTION
# ----------------------------
with col2:

    st.subheader("🤖 AI Prediction Engine")

    if st.button("⚡ Evaluate Credit Eligibility"):

        input_data = preprocess()
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        score = int(probability * 100)

        # RESULT CARD
        if prediction == 1:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg,#00c853,#1de9b6);
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0px 0px 25px rgba(0,255,150,0.6);
            ">
                <h1>✅ LOAN APPROVED</h1>
                <h3>Eligibility Score: {score}/100</h3>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg,#d50000,#ff5252);
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0px 0px 25px rgba(255,0,0,0.6);
            ">
                <h1>❌ LOAN REJECTED</h1>
                <h3>Eligibility Score: {score}/100</h3>
            </div>
            """, unsafe_allow_html=True)

        st.progress(score)

        # EMI CALCULATOR
        st.subheader("💰 EMI Calculation")
        interest_rate = 8.5
        loan_amount_value = loan_amount * 1000
        months = loan_term

        r = interest_rate / (12 * 100)
        emi = loan_amount_value * r * (1 + r)**months / ((1 + r)**months - 1)

        st.success(f"Estimated Monthly EMI: ₹ {int(emi)}")

        # FEATURE IMPORTANCE (if tree-based model)
        if hasattr(model, "feature_importances_"):
            st.subheader("📊 Feature Importance")
            feature_names = [
                "Gender","Married","Dependents","Education","SelfEmployed",
                "ApplicantIncome","CoappIncome","LoanAmount",
                "LoanTerm","CreditHistory","PropertyArea"
            ]
            fig, ax = plt.subplots()
            ax.barh(feature_names, model.feature_importances_)
            st.pyplot(fig)

        # DOWNLOAD REPORT
        report = pd.DataFrame({
            "Prediction": ["Approved" if prediction==1 else "Rejected"],
            "Eligibility Score": [score],
            "Applicant Income": [applicant_income],
            "Loan Amount": [loan_amount]
        })

        st.download_button(
            "📄 Download Report",
            report.to_csv(index=False),
            file_name="loan_prediction_report.csv",
            mime="text/csv"
        )
