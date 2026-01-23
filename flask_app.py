from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load model once at startup
with open("xgb_loan_pred_model.pkl", "rb") as f:
    xgb_model = pickle.load(f)

with open("target_encoder.pkl", "rb") as f:
    te = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    # Create a dataframe from input JSON
    input_df = pd.DataFrame([{
        'loan_amnt': data["loan_amnt"],
        'installment': data["installment"],
        'grade': data["grade"],
        'annual_inc': data["annual_inc"],
        'purpose': data["purpose"],
        'dti': data["dti"],
        'revol_util': data["revol_util"],
        'application_type': data["application_type"],
        'zip_code': data["zip_code"]
    }])

    # One-hot encoding
    # Encode categorical variables
    cat_cols = ['grade', 'zip_code', 'application_type', 'purpose']
    input_df[cat_cols] = te.transform(input_df[cat_cols])

    prediction = xgb_model.predict(input_df)[0]
    probability = xgb_model.predict_proba(input_df)[0][1]

    if prediction == 1:
        res = (f"⚠️ High Risk of Default (Probability: {probability:.2%})")
    else:
        res = (f"✅ Low Risk (Probability: {probability:.2%})")
        
    return jsonify({"message": res })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Type python flask_app.py to run the app