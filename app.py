import streamlit as st
import pickle
import pandas as pd
import time

st.set_page_config(
    page_title="AI Loan Approval System",
    page_icon="🏦",
    layout="wide"
)

# --------------------- STYLING ---------------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #f4f7fb;
}

header {visibility: hidden;}
footer {visibility: hidden;}

/* Top Header */
.top-bar {
    background-color: #0a3d62;
    padding: 25px 40px;
    border-radius: 12px;
    color: white;
    margin-bottom: 35px;
}

.title {
    font-size: 34px;
    font-weight: 700;
}

.subtitle {
    font-size: 15px;
    opacity: 0.85;
}

/* Stats Cards */
.stat-card {
    background: white;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s;
}

.stat-card:hover {
    transform: translateY(-6px);
}

.stat-number {
    font-size: 30px;
    font-weight: 700;
    color: #0a3d62;
}

.stat-label {
    font-size: 14px;
    color: gray;
}

/* Form Cards */
.section-box {
    background-color: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
}

/* Button */
.stButton>button {
    background-color: #0a3d62;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    padding: 10px 30px;
    border: none;
}

.stButton>button:hover {
    background-color: #145da0;
}

</style>
""", unsafe_allow_html=True)

# --------------------- LOAD MODEL ---------------------
model = pickle.load(open("loan_model.pkl", "rb"))

# --------------------- HEADER ---------------------
st.markdown("""
<div class="top-bar">
    <div class="title">🏦 AI Loan Approval System</div>
    <div class="subtitle">Secure & Intelligent Loan Eligibility Dashboard</div>
</div>
""", unsafe_allow_html=True)

# --------------------- STATS SECTION ---------------------
st.markdown("### 📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">1,248</div>
        <div class="stat-label">Total Applications</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">78%</div>
        <div class="stat-label">Approval Rate</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">₹4.6L</div>
        <div class="stat-label">Avg Loan Amount</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">89%</div>
        <div class="stat-label">Model Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------- FORM SECTION ---------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("Applicant Information")

    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("Financial Details")

    LoanAmount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("Loan Term (Days)")
    Credit_History = st.selectbox("Credit History", [1.0, 0.0])
    Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    Total_Income = st.number_input("Total Income")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------- ENCODING ---------------------
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

# --------------------- PREDICTION ---------------------
if st.button("Check Loan Eligibility"):
    with st.spinner("Analyzing application..."):
        time.sleep(1.5)

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown("### 🏦 Loan Decision")

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")

    st.progress(int(probability))
    st.info(f"Approval Probability: {probability:.2f}%")
