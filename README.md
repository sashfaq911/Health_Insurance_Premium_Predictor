# 💸 Health Insurance Premium Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://premium-predictor-app.streamlit.app/)

An interactive **Streamlit web app** that predicts health insurance premiums based on your age, lifestyle, medical history, and coverage plan.  
Built with **machine learning models** trained on real-world health insurance data.

---

## 🚀 Installation  
### Prerequisites:  
- Python 3.10+

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sashfaq911/health-insurance-premium-predictor.git
   cd health-insurance-premium-predictor
   ```
2. **Install dependencies**:   
   ```commandline
    pip install -r requirements.txt
   ```
5. **Run the Streamlit app**:   
   ```commandline
    streamlit run main.py
   ```
   
---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) for the web app UI  
- [scikit-learn](https://scikit-learn.org/) for ML modeling  
- [Pandas](https://pandas.pydata.org/) for data preprocessing  
- [Joblib](https://joblib.readthedocs.io/) for model serialization  

---

## 📦 Project Structure

```bash
health-insurance-premium-predictor/
|
├── main.py                 # Streamlit app entry point
├── prediction_helper.py    # Preprocessing & prediction logic
├── artifacts/
│   ├── model_young.joblib  # Linear Regression Model for users <= 25 years
│   ├── model_rest.joblib   # XGBoost Model for users > 25 years
│   ├── scaler_young.joblib # StandardScaler for younger group
│   └── scaler_rest.joblib  # StandardScaler for older group
|
├── README.md               # Project documentation
├── LICENSE                 # Apache License File
└──requirements.txt         # Python dependencies
```

---

## 🚀 Features

- 🧑‍⚕️ Predicts **personalized premium costs** in seconds.  
- 📊 Considers multiple factors:
  - Age, gender, marital status, number of dependants  
  - Income level and employment type  
  - Region of residence  
  - Genetic risk, BMI category, smoking status  
  - Medical history (diabetes, hypertension, thyroid, heart disease, etc.)  
  - Insurance plan type (Bronze, Silver, Gold)  
- ⚡ Switch between different scenarios instantly to compare outcomes.  
- 🎉 Fun and user-friendly interface powered by **Streamlit**.

---

## App Overview

---

## 📖 Usage

The app is divided into **4 expandable sections** for user inputs:

1. **👤 Basic Information**  
   - Age  
   - Gender  
   - Marital Status  
   - Number of Dependants  

2. **📍 Region & Work**  
   - Region  
   - Employment Status  
   - Income (in Lakhs)  

3. **💪 Health & Habits**  
   - Genetic Risk (0–5 scale)  
   - BMI Category  
   - Smoking Status  
   - Medical History  

4. **🧬 Premium Category**  
   - Insurance Plan (Bronze, Silver, Gold)  

Once inputs are provided, the app processes them and selects the correct **model + scaler** based on your age:  

- **Age ≤ 25** → Uses `scaler_young.joblib` and `model_young.joblib` (**Linear Regression**)  
- **Age > 25** → Uses `scaler_rest.joblib` and `model_rest.joblib` (**XGBoost Regressor**)  

This segmentation ensures that younger applicants and older applicants are modeled differently, improving prediction accuracy.

---

## 📊 Example Prediction

**Inputs:**
- Age: 35  
- Gender: Male  
- Marital Status: Married  
- Dependants: 2  
- Region: Southeast  
- Employment: Salaried  
- Income: ₹ 12 Lakhs  
- Genetic Risk: 2  
- BMI: Overweight  
- Smoking: Regular  
- Medical History: Diabetes & High Blood Pressure  
- Insurance Plan: Gold  

**Result:**  
🎉 Estimated Health Insurance Premium: **₹ 18,450** (example)  

> 💡 Notice how risk factors (smoking + medical history + Gold plan) significantly increase the premium compared to a baseline healthy profile.

---

## Live Demo 🌐

👉 Try the app here: **[Health Insurance Premium Predictor](https://premium-predictor-app.streamlit.app/)**

---

## Acknowledgements 🙏 <a name="acknowledgements"></a>

A special thanks to [Dhaval Patel](https://www.linkedin.com/in/dhavalsays/) and [Hemanand Vadivel](https://www.linkedin.com/in/hemvad/) for their guidance through the [CodeBasics Data Analysis BootCamp 3.0](https://codebasics.io/bootcamps/data-analytics-bootcamp-with-practical-job-assistance). This project has been an invaluable learning experience and a key milestone in my data science journey!

---

## License 📄

This project is licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for details.

---

## Support ❤️ <a name="support"></a>

Contributions, issues, and suggestions are welcome!

Give a ⭐️ if you like this project!
