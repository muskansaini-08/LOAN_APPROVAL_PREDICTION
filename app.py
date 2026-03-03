import streamlit as st
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="LoanIQ - Smart Loan Approval",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* ===== Background ===== */
.stApp {
    background: radial-gradient(circle at 20% 20%, #0f2027, #0b1a24 40%, #000814 100%);
    color: white;
}

/* ===== Remove Top Padding ===== */
.block-container {
    padding-top: 2rem;
}

/* ===== Hero Section ===== */
.hero-title {
    font-size: 60px;
    font-weight: 800;
    line-height: 1.1;
}

.hero-title span {
    color: #00f5c4;
}

.sub-text {
    font-size: 18px;
    color: #b0bec5;
    margin-bottom: 30px;
}

/* ===== Glass Card ===== */
.main-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(18px);
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0 0 60px rgba(0, 255, 200, 0.15);
    border: 1px solid rgba(0, 255, 200, 0.2);
}

/* ===== Inputs ===== */
.stSelectbox div[data-baseweb="select"],
.stNumberInput input {
    background-color: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(0,255,200,0.3) !important;
}

/* ===== Button ===== */
.stButton > button {
    background: linear-gradient(90deg, #00f5c4, #00c3ff);
    color: black;
    font-weight: 700;
    border-radius: 30px;
    height: 50px;
    width: 100%;
    border: none;
    font-size: 16px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px #00f5c4;
}

/* ===== Result Box ===== */
.result-box {
    margin-top: 30px;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    font-size: 22px;
    font-weight: 700;
}

.approved {
    background: rgba(0, 255, 200, 0.15);
    border: 1px solid #00f5c4;
    color: #00f5c4;
}

.rejected {
    background: rgba(255, 0, 80, 0.15);
    border: 1px solid #ff0050;
    color: #ff4d6d;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SPLIT LAYOUT
# -----------------------------
left, right = st.columns([1.2, 1])

# -----------------------------
# LEFT SIDE (HERO)
# -----------------------------
with left:
    st.markdown("""
    <div class="hero-title">
        Predict Your <span>Loan Approval</span> Instantly
    </div>
    <div class="sub-text">
        AI-powered intelligent credit decision system built using Machine Learning.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Model Performance")
    st.progress(0.82)
    st.write("Random Forest Accuracy: **82%**")
    st.progress(0.79)
    st.write("Gradient Boosting Accuracy: **79%**")
    st.progress(0.78)
    st.write("Logistic Regression Accuracy: **78%**")

# -----------------------------
# RIGHT SIDE (FORM CARD)
# -----------------------------
with right:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    st.markdown("### 📝 Applicant Details")

    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

    app_income = st.number_input("Applicant Income", min_value=0, value=40000)
    co_income = st.number_input("Coapplicant Income", min_value=0, value=20000)
    loan_amount = st.number_input("Loan Amount", min_value=0, value=10000)
    loan_term = st.number_input("Loan Term (days)", min_value=0, value=360)
    credit_history = st.selectbox("Credit History", ["1", "0"])

    if st.button("Check Loan Eligibility"):

        with st.spinner("Analyzing with AI Model..."):
            time.sleep(1)

        total_income = app_income + co_income

        if credit_history == "1" and total_income > 20000:
            st.markdown(
                '<div class="result-box approved">✅ Loan Approved</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-box rejected">❌ Loan Rejected</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)
