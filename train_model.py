#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from category_encoders import TargetEncoder
from xgboost import XGBClassifier
import pickle

data = pd.read_csv('LoanTap_Data_Streamlit.csv')

data = data.dropna()

loan_label= {'Fully Paid':0, 'Charged Off':1}
data['loan_status'] = data['loan_status'].replace(loan_label)
data['zip_code'] = data['address'].astype(str).str[-5:]

X = data[data.columns.drop(['loan_status','address'])]
y = data['loan_status']

cat_cols = ['grade','zip_code','application_type','purpose']

te = TargetEncoder(cols=cat_cols)
X[cat_cols] = te.fit_transform(X[cat_cols], y)

xgb_model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=10,
    eval_metric='logloss',
    random_state=42
)

# Fit model
xgb_model.fit(X, y)

# Save model and encoder
with open("target_encoder.pkl", "wb") as f:
    pickle.dump(te, f)

with open("xgb_loan_pred_model.pkl", "wb") as f:
    pickle.dump(xgb_model, f)