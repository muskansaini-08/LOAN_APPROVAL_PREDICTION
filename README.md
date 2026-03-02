# 🏦 Loan Approval Prediction System

> An end-to-end Machine Learning system that predicts whether a loan application will be **Approved ✅ or Rejected ❌** using applicant financial and demographic data.

🚀 **Live App:**  
👉 https://muskan-loan-approval-ml.streamlit.app/

---

## 📌 Project Overview

| 📘 Notebook | 🌐 Live App | 🏆 Best Model | 🤖 Models Compared |
|------------|------------|---------------|-------------------|
| `LOAN_PREDICTION_PROJECT.ipynb` | Streamlit Web App | Random Forest Classifier | 7 Classification Algorithms |

---

## 🎯 Objective

To build a reliable classification model that assists in predicting loan approval decisions based on applicant information.

This project demonstrates a complete ML workflow including:

- Data preprocessing  
- Feature engineering  
- Model comparison  
- Performance evaluation  
- Final model deployment using **Streamlit**

---

## 🌐 Live Deployment

The model has been successfully deployed using **Streamlit Cloud**.

🔗 **Access the application here:**  
https://muskan-loan-approval-ml.streamlit.app/

### ✨ Web App Features

- Clean and interactive loan application form  
- Real-time loan approval prediction  
- Modern fintech-style UI  
- Responsive layout  
- Instant result display (Approved ✅ / Rejected ❌)  
- Deployed using Streamlit  

---

## 🧠 Machine Learning Pipeline

- 📊 Exploratory Data Analysis (EDA)  
- 🧹 Data Cleaning  
- 🔄 Feature Engineering & Encoding  
- 🔀 Train–Test Split  
- 🤖 Training Multiple Classification Models  
- 📈 Model Evaluation (Accuracy, Confusion Matrix, ROC Curve)  
- 🏆 Best Model Selection  
- 🚀 Model Deployment with Streamlit  

---

## 📊 Dataset Information

**Dataset:** `loan.csv`

It contains applicant financial and demographic information used to determine loan approval status.

### 📋 Features Included

| Feature | Description |
|----------|-------------|
| Loan_ID | Unique loan identifier |
| Gender | Applicant gender |
| Married | Marital status |
| Dependents | Number of dependents |
| Education | Graduate / Not Graduate |
| Self_Employed | Employment type |
| ApplicantIncome | Monthly applicant income |
| CoapplicantIncome | Monthly co-applicant income |
| LoanAmount | Requested loan amount |
| Loan_Amount_Term | Loan duration |
| Credit_History | 1 = Good, 0 = Bad |
| Property_Area | Urban / Semiurban / Rural |
| Loan_Status | Target Variable (Approved / Rejected) |

---

## 🤖 Models Implemented

The following classification algorithms were trained and evaluated:

- Logistic Regression  
- Naive Bayes  
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Random Forest  
- Gradient Boosting  
- Decision Tree  

🏆 **Final Selected Model:** Random Forest Classifier

---

## 📂 Repository Structure

```
LOAN_APPROVAL_PREDICTION/
│
├── LOAN_PREDICTION_PROJECT.ipynb   # Complete ML pipeline
├── app.py                          # Streamlit web app
├── loan.csv                        # Dataset
├── requirements.txt                # Dependencies
└── README.md                       # Documentation
```

---

## ⚙️ Installation & Setup (Run Locally)

Clone the repository:

```bash
git clone https://github.com/your-username/LOAN_APPROVAL_PREDICTION.git
cd LOAN_APPROVAL_PREDICTION
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🛠️ Technology Stack

- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Streamlit  

---

## 🚀 Future Enhancements

- Hyperparameter tuning  
- Feature importance visualization  
- Probability score display  
- REST API integration  
- Docker containerization  
- Cloud deployment (AWS / Azure / GCP)

---

## 👩‍💻 Author

**Muskan Saini**  
GitHub: https://github.com/muskansaini-08  

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
