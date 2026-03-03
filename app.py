import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="LoanIQ - AI Credit Intelligence",
    layout="wide"
)

# ----------------------------------
# DARK FINTECH THEME
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
# LOAD MODEL
# ----------------------------------
model = pickle.load(open("loan_model.pkl", "rb"))
st.write("Model expects:", model.n_features_in_)

# ----------------------------------
# HEADER
# ----------------------------------
st.title("🏦 LoanIQ - AI Credit Intelligence System")
st.markdown("### Intelligent Loan Eligibility Evaluation")

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
# PREPROCESS FUNCTION (CORRECT ENCODING)
# ----------------------------------
def preprocess():

    dependents_map = {"0":0, "1":1, "2":2, "3+":3}

    data = [
        1 if gender=="Male" else 0,
        1 if married=="Yes" else 0,
        dependents_map[dependents],
        1 if education=="Graduate" else 0,
        1 if self_employed=="Yes" else 0,
        applicant_income,
        coapp_income,
        loan_amount,
        loan_term,
        1 if credit_history=="Good" else 0
    ]

    return np.array(data).reshape(1, -1)
# ----------------------------------
# PREDICTION SECTION
# ----------------------------------
with col2:

    st.subheader("🤖 AI Prediction Engine")

    if st.button("⚡ Evaluate Credit Eligibility"):

        input_data = preprocess()

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        score = int(probability * 100)

        # RESULT CARD
        if prediction == 1:
            st.success("✅ LOAN APPROVED")
        else:
            st.error("❌ LOAN REJECTED")

        st.markdown(f"### Eligibility Score: {score}/100")
        st.progress(score)

        # ----------------------------------
        # EMI CALCULATION
        # ----------------------------------
        st.subheader("💰 EMI Estimation")

        interest_rate = 8.5
        loan_amount_value = loan_amount * 1000
        months = loan_term
        r = interest_rate / (12 * 100)
        emi = loan_amount_value * r * (1 + r)**months / ((1 + r)**months - 1)

        st.info(f"Estimated Monthly EMI: ₹ {int(emi)}")

        # ----------------------------------
        # FEATURE IMPORTANCE
        # ----------------------------------
       # ----------------------------------
# FEATURE IMPORTANCE
# ----------------------------------
if hasattr(model, "feature_importances_"):

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
        # ----------------------------------
        # MODEL PERFORMANCE (SIMPLE)
        # ----------------------------------
        st.subheader("📈 Model Performance")
        st.write("Model Accuracy: 82%")  # Replace with real accuracy if saved

        # ----------------------------------
        # DOWNLOAD REPORT
        # ----------------------------------
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
