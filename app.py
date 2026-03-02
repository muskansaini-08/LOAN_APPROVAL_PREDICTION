import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="AI Loan Approval System",
    page_icon="🏦",
    layout="wide"
)

# Clean modern styling
st.markdown("""
<style>
/* Background */
[data-testid="stAppViewContainer"] {
    background-color: #eef2f7;
}

/* Hide Streamlit header */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Main title */
.title {
    font-size: 42px;
    font-weight: 700;
    color: #1e293b;
}

.subtitle {
    font-size: 18px;
    color: #64748b;
    margin-bottom: 30px;
}

/* Card */
.card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* Button */
.stButton>button {
    background-color: #2563eb;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    padding: 10px 28px;
    border: none;
}

.stButton>button:hover {
    background-color: #1e40af;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("loan_model.pkl", "rb"))

# Header
st.markdown('<div class="title">🏦 AI Loan Approval System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Loan Eligibility Prediction using Machine Learning</div>', unsafe_allow_html=True)

st.markdown("")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Applicant Information")

    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Financial Details")

    LoanAmount = st.number_input("Loan Amount", min_value=0.0)
    Loan_Amount_Term = st.number_input("Loan Term (Days)", min_value=0.0)
    Credit_History = st.selectbox("Credit History", [1.0, 0.0])
    Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    Total_Income = st.number_input("Total Income", min_value=0.0)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("")

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

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown("### Prediction Result")

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")

    st.info(f"Approval Probability: {probability:.2f}%")
    st.progress(int(probability))
