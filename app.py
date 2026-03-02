import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="AI Loan Approval System",
    page_icon="🏦",
    layout="wide"
)

# 🔥 PREMIUM DARK THEME
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

.big-title {
    font-size: 48px;
    font-weight: bold;
    color: #00d4ff;
}

.subtitle {
    font-size: 20px;
    color: #cfd8dc;
    margin-bottom: 30px;
}

.section-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #00e5ff;
}

.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-size: 18px;
    border-radius: 15px;
    padding: 10px 30px;
    border: none;
}

.stSelectbox, .stNumberInput {
    background-color: #1e2a38 !important;
    color: white !important;
    border-radius: 10px;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load Model
model = pickle.load(open("loan_model.pkl", "rb"))

# Header
st.markdown('<div class="big-title">🏦 AI Loan Approval System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Loan Eligibility Prediction using Machine Learning</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">👤 Applicant Information</div>', unsafe_allow_html=True)
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    st.markdown('<div class="section-title">💰 Financial Details</div>', unsafe_allow_html=True)
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

if st.button("🚀 Predict Loan Status"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown("## 📊 Prediction Result")

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.info(f"📈 Approval Probability: {probability:.2f}%")
    st.progress(int(probability))

st.markdown("""
<div style="text-align:center; margin-top:40px; color:#90a4ae;">
Built with ❤️ using Machine Learning & Streamlit
</div>
""", unsafe_allow_html=True)
