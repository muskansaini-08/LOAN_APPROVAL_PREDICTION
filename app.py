import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="AI Loan Approval System",
    page_icon="🏦",
    layout="wide"
)

# ------------------- STYLING -------------------
st.markdown("""
<style>

/* Main Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Hide default header/footer */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Title */
.main-title {
    font-size: 48px;
    font-weight: 700;
    color: #f8fafc;
}

.subtitle {
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

/* Card Style */
.card {
    background: #ffffff;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.4);
}

/* Section Titles */
.section-title {
    font-size: 22px;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 20px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #facc15, #f59e0b);
    color: #0f172a;
    font-size: 18px;
    font-weight: 600;
    border-radius: 10px;
    padding: 12px 30px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #f59e0b, #facc15);
    transform: scale(1.05);
}

/* Prediction Box */
.result-box {
    background: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ------------------- LOAD MODEL -------------------
model = pickle.load(open("loan_model.pkl", "rb"))

# ------------------- HEADER -------------------
st.markdown('<div class="main-title">🏦 AI Loan Approval System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Premium Smart Loan Eligibility Engine</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------- FORM -------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Applicant Information</div>', unsafe_allow_html=True)

    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Financial Details</div>', unsafe_allow_html=True)

    LoanAmount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("Loan Term (Days)")
    Credit_History = st.selectbox("Credit History", [1.0, 0.0])
    Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    Total_Income = st.number_input("Total Income")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------------- ENCODING -------------------
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

# ------------------- PREDICT -------------------
if st.button("Check Loan Eligibility"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    if prediction[0] == 1:
        st.markdown("## ✅ Loan Approved")
    else:
        st.markdown("## ❌ Loan Rejected")

    st.markdown(f"### Approval Probability: {probability:.2f}%")
    st.progress(int(probability))

    st.markdown('</div>', unsafe_allow_html=True)
