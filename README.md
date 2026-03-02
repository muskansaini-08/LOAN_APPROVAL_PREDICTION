🏦 Loan Approval Prediction System

A complete end-to-end Machine Learning project that predicts whether a loan application will be Approved ✅ or Rejected ❌ using applicant financial and demographic details.

This project demonstrates the full ML lifecycle — from data exploration to final model selection — combined with a clean, standalone web interface.

📦 Project Overview
📘 Notebook	🌐 Web Interface	🏆 Final Model	🤖 Models Trained
LOAN_PREDICTION_PROJECT.ipynb	loan_approval_app.html	Random Forest Classifier	7 Classification Algorithms
📂 Project Structure
LOAN_APPROVAL_PREDICTION/
│
├── LOAN_PREDICTION_PROJECT.ipynb   # Complete ML pipeline
├── loan_approval_app.html          # Standalone web interface
├── loan.csv                        # Dataset
├── requirements.txt                # Dependencies
└── README.md                       # Documentation
🧠 Machine Learning Pipeline

The project follows a structured workflow:

1️⃣ Data Loading
2️⃣ Exploratory Data Analysis
3️⃣ Data Cleaning
4️⃣ Feature Engineering & Encoding
5️⃣ Train–Test Split
6️⃣ Model Training (Multiple Algorithms)
7️⃣ Model Evaluation (Accuracy, Confusion Matrix, ROC)
8️⃣ Best Model Selection

📊 Dataset Overview

The dataset contains applicant information used to determine loan approval status.

Feature	Description
Gender	Applicant gender
Married	Marital status
Dependents	Number of dependents
Education	Graduate / Not Graduate
Self_Employed	Employment type
ApplicantIncome	Monthly income
CoapplicantIncome	Co-applicant income
LoanAmount	Loan amount requested
Loan_Amount_Term	Loan duration
Credit_History	1 = Good, 0 = Bad
Property_Area	Urban / Semiurban / Rural
Loan_Status	Target Variable
🤖 Models Implemented

The following classification algorithms were trained and evaluated:

Logistic Regression

Naive Bayes

K-Nearest Neighbors

Support Vector Machine

Random Forest

Gradient Boosting

Decision Tree

After comparing performance metrics and validation results, Random Forest Classifier was selected as the final model.

📈 Model Evaluation

Models were evaluated using:

Accuracy Score

Confusion Matrix

ROC Curve

Cross Validation

These metrics ensured reliable model comparison and robust selection.

🌐 Web Application

A lightweight standalone frontend interface is included.

✨ Features

Clean loan application form

Instant approval/rejection display

Responsive design

Built with HTML, CSS & JavaScript

No backend required

▶️ To Run

Simply open:

loan_approval_app.html

in your browser.

⚙️ Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/LOAN_APPROVAL_PREDICTION.git
cd LOAN_APPROVAL_PREDICTION
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Notebook
jupyter notebook

Open:

LOAN_PREDICTION_PROJECT.ipynb
🛠️ Tech Stack
Layer	Technology
Programming	Python 3.x
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-learn
Development	Jupyter Notebook
Frontend	HTML5, CSS3, JavaScript
🚀 Future Improvements

Hyperparameter tuning

Feature importance visualization

Model deployment using Streamlit/Flask

Cloud hosting

REST API integration

👩‍💻 Author

Muskan Saini
GitHub: https://github.com/muskansaini-08

⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
