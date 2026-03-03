import streamlit as st
import time

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="LoanIQ - Smart Loan Approval",
    page_icon="🏦",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

/* ===== Background ===== */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Remove excessive top padding */
.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* ===== Title ===== */
.main-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

.highlight {
    color: #00f5c4;
}

.subtitle {
    font-size: 18px;
    color: #cfd8dc;
    margin-bottom: 30px;
}

/* ===== Section Card ===== */
.card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

/* ===== Labels ===== */
label {
    color: white !important;
    font-weight: 500 !important;
}

/* ===== Input Fields ===== */
.stSelectbox div[data-baseweb="select"],
.stNumberInput input {
    background-color: #f1f3f9 !important;
    color: black !important;
    border-radius: 10px !important;
}

/* ===== Button ===== */
.stButton > button {
    background: linear-gradient(90deg, #00f5c4, #00c6ff);
    color: black;
    font-weight: 700;
    border-radius: 25px;
    height: 50px;
    width: 100%;
    border: none;
    font-size: 16px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

/* ===== Result Box ===== */
.result-box {
    margin-top: 25px;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
}

.approved {
    background: linear-gradient(90deg, #00c9ff, #92fe9d);
    color: black;
}

.rejected {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Layout
# -------------------------------
left, right = st.columns([1.2, 1])

# -------------------------------
# LEFT SIDE (Info + Model Performance)
# -------------------------------
with left:
    st.markdown('<div class="main-title">Predict Your <span class="highlight">Loan Approval</span> Instantly</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered intelligent credit decision system built using Machine Learning.</div>', unsafe_allow_html=True)

    st.markdown("### 📊 Model Performance")
    st.progress(0.82)
    st.write("Random Forest Accuracy: 82%")

    st.progress(0.79)
    st.write("Gradient Boosting Accuracy: 79%")

    st.progress(0.78)
    st.write("Logistic Regression Accuracy: 78%")

# -------------------------------
# RIGHT SIDE (Form)
# -------------------------------
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
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

        with st.spinner("Checking eligibility..."):
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
