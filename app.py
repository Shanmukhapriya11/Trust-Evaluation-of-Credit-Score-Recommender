# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# -------------------------------
# Load the saved model and preprocessing objects
# -------------------------------
model = load_model("german_credit_model.keras")
scaler = joblib.load("minmax_scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# -------------------------------
# Define your feature names and descriptions
# -------------------------------
feature_names = [
    "Status_of_existing_checking_account",
    "Duration_in_month",
    "Credit_history",
    "Purpose",
    "Credit_amount",
    "Savings_account_bonds",
    "Present_employment_since",
    "Installment_rate",
    "Personal_status_and_sex",
    "Other_debtors_guarantors",
    "Present_residence_since",
    "Age_in_years",
    "Other_installment_plans",
    "Housing",
    "Number_of_existing_credits",
    "Job",
    "Number_of_people_liable"
]

feature_descriptions = {
    "Status_of_existing_checking_account": "Select your checking account status.",
    "Duration_in_month": "Enter the duration of the credit in months (e.g., 24).",
    "Credit_history": "Select your credit history.",
    "Purpose": "Select the purpose of the credit.",
    "Credit_amount": "Enter the credit amount (in whole units).",
    "Savings_account_bonds": "Select your savings account/bonds status.",
    "Present_employment_since": "Select your employment duration status.",
    "Installment_rate": "Enter the installment rate (as an integer).",
    "Personal_status_and_sex": "Select your personal status and sex.",
    "Other_debtors_guarantors": "Enter other debtors/guarantors information (as an integer).",
    "Present_residence_since": "Enter the number of years at your current residence (integer).",
    "Age_in_years": "Enter your age in whole years.",
    "Other_installment_plans": "Select if you have other installment plans.",
    "Housing": "Select your housing type.",
    "Number_of_existing_credits": "Enter the number of existing credits (integer).",
    "Job": "Select your job category.",
    "Number_of_people_liable": "Enter the number of people liable for this credit (integer)."
}

st.title("German Credit Risk Prediction")
st.markdown("""
This application predicts the credit risk based on the input features.
Please enter the required information below. For categorical features, select an option from the dropdown.
For numerical features, enter the value in its natural format (for example, for Duration_in_month, enter 24 instead of a decimal).
The app will then convert these values to the scaled/encoded format that the model expects.
""")

# -------------------------------
# Specify which numerical features should accept only integers.
# -------------------------------
int_features = {
    "Duration_in_month",
    "Credit_amount",
    "Installment_rate",
    "Other_debtors_guarantors",  # Now treated as integer input
    "Present_residence_since",
    "Age_in_years",
    "Number_of_existing_credits",
    "Number_of_people_liable"
}

# -------------------------------
# Build the input form
# -------------------------------
inputs = {}
for feature in feature_names:
    st.subheader(feature)
    st.caption(feature_descriptions.get(feature, ""))
    
    # If the feature is categorical (i.e., exists in label_encoders), use a selectbox
    if feature in label_encoders:
        le = label_encoders[feature]
        # Display the original classes as options
        options = list(le.classes_)
        selected_option = st.selectbox(f"Select {feature}", options)
        # Convert the selection into the encoded value
        encoded_val = le.transform([selected_option])[0]
        inputs[feature] = encoded_val
    else:
        # For numerical features, decide if the input should be an integer or a float.
        if feature in int_features:
            # For integer features, set step=1 and use an integer display format.
            inputs[feature] = st.number_input(f"Enter {feature}", value=0, step=1, format="%d")
        else:
            # For other numerical features, allow decimals.
            inputs[feature] = st.number_input(f"Enter {feature}", value=0.0)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    # Convert the inputs into a DataFrame with one row
    input_df = pd.DataFrame([inputs], columns=feature_names)
    
    # Identify numerical features that need scaling.
    # Here we assume that features not in label_encoders are numerical.
    numerical_features = [feat for feat in feature_names if feat not in label_encoders]
    
    # IMPORTANT: Apply the scaler (as was done in training) to convert raw inputs 
    # into their scaled versions.
    if numerical_features:
        try:
            input_df[numerical_features] = scaler.transform(input_df[numerical_features])
        except Exception as e:
            st.error(f"Error in scaling input values: {e}")
    
    # Reshape the input to match the model's expected shape: (samples, time steps, features)
    X_input = input_df.values.reshape((input_df.shape[0], 1, input_df.shape[1]))
    
    # Make prediction
    prediction_prob = model.predict(X_input)[0][0]
    # For a binary classification model with sigmoid activation, use a threshold (e.g., 0.5)
    prediction = "High Risk" if prediction_prob < 0.5 else "Low Risk"
    
    st.markdown("### Prediction Results")
    st.write(f"**Predicted Risk:** {prediction}")
    st.write(f"**Prediction Probability:** {prediction_prob:.4f}")
