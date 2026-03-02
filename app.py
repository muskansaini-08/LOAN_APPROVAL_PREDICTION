import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Approval Prediction System")

st.write("Enter Applicant Details")

# Inputs (you may adjust later)
income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1, 0])

if st.button("Predict"):
    input_data = pd.DataFrame([[income, loan_amount, credit_history]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
