#  SmartPremium: Predicting Insurance Premiums with Machine Learning

**SmartPremium** is an end-to-end machine learning project that predicts insurance premium costs based on customer and policy features. It includes data preprocessing, model comparison, XGBoost training, and a Streamlit web app for real-time prediction.

---

##  Live App

 **[Try the App on Streamlit Cloud](https://smartpremiumapp-daziur43ekfg7zquj6qypx.streamlit.app/)**  
_(Deployed directly from this GitHub repo)_

---

##  Folder Structure

```text
SmartPremium_App/
├── app.py # Streamlit app source code
├── xgboost_model.pkl # Trained model used in the app
├── requirements.txt # Required libraries for deployment
├── SmartPremium_Project_CLEANED.ipynb # Jupyter Notebook (EDA + training)
├── README.md # Project description
├── train.csv # Training dataset
├── test.csv # Testing dataset
└── sample_submission.csv # Sample output format
```


---

##  Objective

To predict the **Premium Amount** a customer needs to pay for an insurance policy using machine learning based on the following features:

- Age, Gender, Marital Status
- Annual Income, Dependents, Occupation
- Health Score, Previous Claims
- Credit Score, Vehicle Age, and more

---

##  Models Trained & Evaluated

| Model              | RMSE   | MAE    | R² Score |
|--------------------|--------|--------|----------|
| Linear Regression  | 863.34 | 667.33 | 0.0026   |
| Random Forest      | 858.13 | 662.51 | 0.0146   |
| **XGBoost (Best)** | **847.99** | **648.14** | **0.0377**  |

---

##  Tech Stack

- Python, Pandas, NumPy
- Scikit-learn, XGBoost
- Streamlit (for app)
- Joblib (for model saving)
- Git & GitHub (for version control & deployment)

---

##  How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Jaisrinivaspk/SmartPremium_App.git
```
   cd SmartPremium_App
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```

---
##  How the App Works


 - User selects input values via dropdowns and sliders.

 - Inputs are preprocessed to match training structure.

 - Trained xgboost_model.pkl is loaded and used for prediction.

 - Prediction output (expected Premium Amount) is displayed instantly.
---
##  Deployment
 
 
 - The app is hosted live using [Streamlit Cloud](https://Jaisrinivaspk-smartpremium-app.streamlit.app)

 - Model is pre-trained and stored in the repo as xgboost_model.pkl for fast loading.

---
##  Contact
 
 - **Jaisrinivas P K**
 - **[GitHub Profile](https://github.com/Jaisrinivaspk)**

---
##  Acknowledgements


- This project was developed as a capstone for hands-on machine learning practice.
- Thanks to GUVI & community support for the dataset and guidance!


