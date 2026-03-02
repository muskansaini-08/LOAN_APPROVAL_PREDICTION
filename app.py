import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Loan Approval AI System",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}
.big-title {
    font-size: 42px;
    font-weight: bold;
    color: #1f4e79;
}
.subtitle {
    font-size: 18px;
    color: gray;
    margin-bottom: 30px;
}
.footer {
    margin-top: 50px;
    text-align: center;
    font-size: 14px;
    color: gray;
}
.stButton>button {
    background-color: #1f77b4;
    color: white;
    font-size: 18px;
    border-radius: 12px;
    padding: 10px 30px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("loan_model.pkl", "rb"))

# Header
st.markdown('<div class="big-title">🏦 AI Loan Approval System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Loan Eligibility Prediction using Machine Learning</div>', unsafe_allow_html=True)

st.markdown("---")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Applicant Information")
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    st.subheader("💰 Financial Details")
    LoanAmount = st.number_input("Loan Amount", min_value=0.0)
    Loan_Amount_Term = st.number_input("Loan Term (Days)", min_value=0.0)
    Credit_History = st.selectbox("Credit History", [1.0, 0.0])
    Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    Total_Income = st.number_input("Total Income", min_value=0.0)

st.markdown("---")

# Encoding
Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0
Education = 1 if Education == "Graduate" else 0
Self_Employed = 1 if Self_Employed == "Yes" else 0
Dependents = {"0":0, "1":1, "2":2, "3+":3}[Dependents]
Property_Area = {"Urban":2, "Semiurban":1, "Rural":0}[Property_Area]

input_data = pd.DataFrame({
    'Gender': [Gender],
    'Married': [Married],
    'Dependents': [Dependents],
    'Education': [Education],
    'Self_Employed': [Self_Employed],
    'LoanAmount': [LoanAmount],
    'Loan_Amount_Term': [Loan_Amount_Term],
    'Credit_History': [Credit_History],
    'Property_Area': [Property_Area],
    'Total_Income': [Total_Income]
})

# Prediction
if st.button("🚀 Predict Loan Status"):

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown("## 📊 Prediction Result")

    if prediction[0] == 1:
        st.success(f"✅ Loan Approved")
    else:
        st.error(f"❌ Loan Rejected")

    st.info(f"📈 Approval Probability: {probability:.2f}%")

    # Risk meter
    st.progress(int(probability))

st.markdown("""
<div class="footer">
Built with ❤️ using Streamlit | Machine Learning Portfolio Project
</div>
""", unsafe_allow_html=True)
