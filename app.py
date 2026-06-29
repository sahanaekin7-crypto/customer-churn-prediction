import streamlit as st
import pandas as pd
import pickle


model = pickle.load(open("models/churn_model.pkl", "rb"))


st.title("Customer Churn Prediction")


tenure = st.number_input("Tenure", 0)
monthly = st.number_input("Monthly Charges", 0.0)
total = st.number_input("Total Charges", 0.0)


if st.button("Predict"):

    data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total],

        "gender_Female": [1],
        "gender_Male": [0],
        "SeniorCitizen": [0],
        "Partner_No": [0],
        "Partner_Yes": [1],
        "Dependents_No": [0],
        "Dependents_Yes": [1],
        "PhoneService_No": [0],
        "PhoneService_Yes": [1],
        "Contract_Month-to-month": [1],
        "Contract_One year": [0],
        "Contract_Two year": [0]
    })


    # add missing columns automatically
    for col in model.feature_names_in_:
        if col not in data.columns:
            data[col] = 0


    data = data[model.feature_names_in_]


    prediction = model.predict(data)


    if prediction[0] == 1:
        st.error("Customer may churn")
    else:
        st.success("Customer will stay")