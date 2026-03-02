import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Loan Data Dashboard",
    page_icon="🏦",
    layout="wide"
)

# -------------------- LOAD DATA --------------------
df = pd.read_csv("loan.csv")

# Convert Loan_Status to numeric
if "Loan_Status" in df.columns:
    df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

# Basic cleaning
df["LoanAmount"] = pd.to_numeric(df["LoanAmount"], errors="coerce")
df = df.dropna(subset=["LoanAmount", "Loan_Status"])

# -------------------- CALCULATIONS --------------------
total_applications = len(df)
approval_rate = df["Loan_Status"].mean() * 100
avg_loan = df["LoanAmount"].mean()

# -------------------- STYLING --------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f4f7fb;
}
.stat-card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}
.stat-number {
    font-size: 28px;
    font-weight: bold;
    color: #0a3d62;
}
.stat-label {
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.title("🏦 Loan Dataset Analytics Dashboard")
st.write("Real-time statistics calculated from uploaded dataset")

st.markdown("---")

# -------------------- KPI CARDS --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{total_applications:,}</div>
        <div class="stat-label">Total Applications</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{approval_rate:.2f}%</div>
        <div class="stat-label">Approval Rate</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">₹{avg_loan:.0f}</div>
        <div class="stat-label">Average Loan Amount</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------- DATA PREVIEW --------------------
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# -------------------- BASIC INSIGHTS --------------------
st.subheader("📊 Quick Insights")

approved = df[df["Loan_Status"] == 1]
rejected = df[df["Loan_Status"] == 0]

st.write(f"✅ Approved Applications: {len(approved)}")
st.write(f"❌ Rejected Applications: {len(rejected)}")
