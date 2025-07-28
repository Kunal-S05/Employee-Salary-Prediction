import streamlit as st
import pandas as pd
import joblib

# Load model and column names
model = joblib.load("salary_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Set page config
st.set_page_config(page_title="Employee Salary Predictor", layout="centered", page_icon="💼")

# Header
st.markdown("<h1 style='text-align: center;'>Employee Salary Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Fill in the employee details below to predict whether their salary is above or below ₹50K.</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout in 2 columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("👤 Age", min_value=18, max_value=90, value=30)
    workclass = st.selectbox("🏢 Workclass", ['Private', 'Local-government', 'State-government', 'Federal-government'])
    education = st.selectbox("🎓 Education", ['Post Graduation', 'Bachelors', 'Masters', 'High School', 'Phd'])

with col2:
    occupation = st.selectbox("💼 Occupation", ['Tech-support', 'Dev-Ops', 'HR Manager', 'Exec-Manager', 'Sales'])
    hours_per_week = st.slider("🕒 Hours Per Week", min_value=1, max_value=100, value=40)
    gender = st.radio("🚻 Gender", ['Male', 'Female'], horizontal=True)
    native_country = st.selectbox("🌍 Native Country", ['United-States', 'India', 'Mexico', 'Philippines', 'Germany'])

# Prediction button
st.markdown("### 🔍 Predict Salary Range")
if st.button("📊 Predict"):
    input_dict = {
        'age': age,
        'workclass': workclass,
        'education': education,
        'occupation': occupation,
        'hours-per-week': hours_per_week,
        'sex': gender,
        'native-country': native_country
    }

    # Convert input to dataframe and one-hot encode it
    input_df = pd.DataFrame([input_dict])
    input_encoded = pd.get_dummies(input_df)

    # Align input with training columns
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_encoded)[0]

    st.markdown("---")
    if prediction == 1:
        st.success(" The employee is likely to earn **more than ₹50K**.")
    else:
        st.warning(" The employee is likely to earn **less than ₹50K**.") 