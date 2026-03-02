# 🏦 Loan Approval Prediction System

> An end-to-end Machine Learning system that predicts whether a loan application will be **Approved ✅ or Rejected ❌** using applicant financial and demographic data.

This project demonstrates a complete ML workflow — including data preprocessing, feature engineering, model comparison, evaluation, and final model selection — along with a lightweight standalone web interface.

---

## 📌 Project Overview

| 📘 Notebook | 🌐 Web App | 🏆 Best Model | 🤖 Models Compared |
|------------|------------|---------------|-------------------|
| `LOAN_PREDICTION_PROJECT.ipynb` | `loan_approval_app.html` | Random Forest Classifier | 7 Classification Algorithms |

---

## 🎯 Objective

To build a reliable classification model that assists in predicting loan approval decisions based on applicant information.

---

## 🧠 Machine Learning Pipeline

The project follows a structured approach:

- 📊 Exploratory Data Analysis (EDA)  
- 🧹 Data Cleaning  
- 🔄 Feature Engineering & Encoding  
- 🔀 Train–Test Split  
- 🤖 Training Multiple Classification Models  
- 📈 Model Evaluation (Accuracy, Confusion Matrix, ROC Curve)  
- 🏆 Best Model Selection  

---

## 📊 Dataset Information

The dataset used in this project is:

**`loan.csv`**

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

After performance comparison and validation, **Random Forest Classifier** was selected as the final model.

---

## 📂 Repository Structure

```
LOAN_APPROVAL_PREDICTION/
│
├── LOAN_PREDICTION_PROJECT.ipynb   # Complete ML pipeline
├── loan_approval_app.html          # Standalone web interface
├── loan.csv                        # Dataset
├── requirements.txt                # Dependencies
└── README.md                       # Documentation
```

---

## 🌐 Web Application

A lightweight standalone frontend interface is included.

### ✨ Features

- Clean and user-friendly loan input form  
- Instant approval/rejection result display  
- Responsive layout  
- Built using HTML, CSS, and JavaScript  
- No backend required  

### ▶️ To Run the Web App

Open:

```
loan_approval_app.html
```

in any modern browser.

---

## ⚙️ Installation & Setup

Clone the repository:

```
git clone https://github.com/your-username/LOAN_APPROVAL_PREDICTION.git
cd LOAN_APPROVAL_PREDICTION
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the notebook:

```
jupyter notebook
```

Then open:

```
LOAN_PREDICTION_PROJECT.ipynb
```

---

## 🛠️ Technology Stack

- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- HTML, CSS, JavaScript  

---

## 🚀 Future Enhancements

- Hyperparameter tuning  
- Feature importance visualization  
- Model deployment using Streamlit or Flask  
- Cloud hosting  
- REST API integration  

---

## 👩‍💻 Author

**Muskan Saini**  
GitHub: https://github.com/muskansaini-08  

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
