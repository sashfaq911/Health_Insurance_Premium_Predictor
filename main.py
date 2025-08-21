
import streamlit as st
from prediction_helper import predict

# Page setup
st.set_page_config(page_title="💸 Premium Predictor", page_icon="🧑‍⚕️", layout="centered")

st.title("Health Insurance Premium Predictor ⚡")
st.markdown("✨ Let's find out how much your insurance might cost. Fill in the details below and see the magic happen!")

# Sidebar fun fact section
with st.sidebar:
    st.header("💡About")
    st.markdown("This app predicts **health insurance premiums** based on your lifestyle and medical history.")

    st.header("🩺 Quick Health Tip")
    st.info("🚭 Quitting smoking can cut your insurance cost significantly and improve your long-term health!")


# Categories
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Married', 'Unmarried'],
    'BMI Category': ['Normal', 'Overweight', 'Obesity', 'Underweight'],
    'Smoking Status': ['Non-Smoker', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid',
        'Heart disease', 'High BP & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Split form into sections
with st.expander("👤 Basic Information", expanded=True):
    age = st.number_input("🎂 Age", 18, 100, 18)
    gender = st.radio("⚧ Gender", categorical_options['Gender'])
    marital_status = st.radio("💍 Marital Status", categorical_options['Marital Status'])
    number_of_dependants = st.number_input("👨‍👩‍👧 Dependants", 0, 20, 0)


with st.expander("📍 Region & Work"):
    region = st.selectbox("🌍 Region", categorical_options['Region'])
    employment_status = st.selectbox("💼 Employment Status", categorical_options['Employment Status'])
    income_lakhs = st.number_input("💰 Yearly Income (Lakhs)", 0, 200, 0)

with st.expander("💪 Health & Habits"):
    genetical_risk = st.number_input("🧬 Genetic Risk (0=Low, 5=High)", 0, 5, 0)
    bmi_category = st.radio("⚖️ BMI Category", categorical_options['BMI Category'])
    smoking_status = st.radio("🚬 Smoking Status", categorical_options['Smoking Status'])
    medical_history = st.selectbox("🧾 Medical History", categorical_options['Medical History'])

with st.expander("🧬 Premiuim Category"):
    insurance_plan = st.radio("📑 Insurance Plan", categorical_options['Insurance Plan'])

# Collect inputs
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction
if st.button("🎯 Predict My Premium"):
    with st.spinner("Crunching numbers... 🔄"):
        prediction = predict(input_dict)
    st.success(f"🎉 Estimated Health Insurance Premium: **₹ {prediction:,}**")
    st.balloons()

