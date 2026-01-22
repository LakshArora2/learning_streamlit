#!/usr/bin/env python
# coding: utf-8

# In[14]:

import streamlit as st
import pickle
import pandas as pd
import numpy as np

# @pytest.fixture(scope="session") # Everytime i run pytest, this model will be loaded only once

# 'loan_amnt', 'installment', 'annual_inc', 'dti', 'revol_util',
grade = st.selectbox("Grade", ['A','B','C','D','E','F','G'])
zip_code = st.selectbox("ZIP Code",['22690', '05113', '00813', '11650', '30723', '70466', '29597', '48052', '86630', '93700'])
application_type = st.selectbox("Application Type", ['INDIVIDUAL', 'JOINT', 'DIRECT_PAY'])
purpose = st.selectbox("Purpose", ['vacation', 'debt_consolidation', 'credit_card', 'home_improvement', 'small_business', 'major_purchase', 'other',
                                   'medical', 'wedding', 'car', 'moving', 'house', 'educational', 'renewable_energy'])

loan_amnt = st.number_input("Loan Amount", min_value=0)
installment = st.number_input("Installment Amount", min_value=0.0)
annual_inc = st.number_input("Annual Income", min_value=0.0)
dti = st.number_input("Debt to Income", min_value=0.0)
revol_util = st.number_input("Revolving utilization rate", min_value=0.0)

def model():
    with open("xgb_loan_pred_model.pkl", "rb") as f:
        return pickle.load(f)
    
def te():
    with open("target_encoder.pkl", "rb") as f:
        return pickle.load(f)

# Makes any input dataframe ready to be passed to the model for prediction
input_df = pd.DataFrame([{
    'loan_amnt': loan_amnt,
    'installment': installment,
    'grade': grade,
    'annual_inc': annual_inc,
    'purpose': purpose,
    'dti': dti,
    'revol_util': revol_util,
    'application_type': application_type,
    'zip_code': zip_code
}])

# Encode categorical variables
cat_cols = ['grade', 'zip_code', 'application_type', 'purpose']
input_df[cat_cols] = te().transform(input_df[cat_cols])

# Predict
prediction = model.predict(input_df)[0]
probability = model.predict_proba(input_df)[0][1]

# Display Result
if prediction == 1:
    st.error(f"⚠️ High Risk of Default (Probability: {probability:.2%})")
else:
    st.success(f"✅ Low Risk (Probability: {probability:.2%})")

