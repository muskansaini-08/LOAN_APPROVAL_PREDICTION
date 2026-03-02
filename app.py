import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Approval Prediction System")
st.write("Enter Applicant Details")

# User Inputs
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
LoanAmount = st.number_input("Loan Amount")
Loan_Amount_Term = st.number_input("Loan Amount Term")
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
Total_Income = st.number_input("Total Income")

# Manual Encoding (IMPORTANT)
Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0
Education = 1 if Education == "Graduate" else 0
Self_Employed = 1 if Self_Employed == "Yes" else 0

Dependents_map = {"0":0, "1":1, "2":2, "3+":3}
Dependents = Dependents_map[Dependents]

Property_Area_map = {"Urban":2, "Semiurban":1, "Rural":0}
Property_Area = Property_Area_map[Property_Area]

# Create DataFrame
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

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
