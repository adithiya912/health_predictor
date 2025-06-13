import sys
import json
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

def prepare_input(input_data):
    """Prepare input data in the correct format for prediction"""
    # Create a DataFrame with the same structure as training data
    input_df = pd.DataFrame([{
        'age': input_data['age'],
        'sex': input_data['sex'],
        'cp': input_data['cp'],
        'trestbps': input_data['trestbps'],
        'chol': input_data['chol'],
        'fbs': input_data['fbs'],
        'restecg': input_data['restecg'],
        'thalch': input_data['thalch'],
        'exang': input_data['exang'],
        'oldpeak': input_data['oldpeak'],
        'slope': input_data['slope'],
        'ca': input_data['ca'],
        'thal': input_data['thal']
    }])
    
    return input_df

def predict(input_data):
    try:
        # Prepare input
        input_df = prepare_input(input_data)
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0][1] * 100
        
        # Generate recommendation
        if prediction == 1:
            if proba >= 80:
                recommendation = "High risk of heart disease. Please consult a cardiologist immediately."
            elif proba >= 60:
                recommendation = "Moderate to high risk of heart disease. Consider consulting a doctor soon."
            else:
                recommendation = "Some risk factors detected. Consider lifestyle changes and monitoring."
        else:
            if proba <= 20:
                recommendation = "Low risk of heart disease. Maintain healthy habits."
            else:
                recommendation = "No heart disease detected, but some risk factors present. Consider preventive measures."
        
        return {
            "prediction": bool(prediction),
            "risk_percentage": round(float(proba), 1),
            "recommendation": recommendation
        }
    
    except Exception as e:
        return {
            "error": str(e),
            "prediction": None,
            "risk_percentage": 0.0,
            "recommendation": "Prediction failed"
        }

if __name__ == "__main__":
    # Read input from stdin
    input_str = sys.stdin.read()
    
    try:
        input_data = json.loads(input_str)
        result = predict(input_data)
        print(json.dumps(result))
    except json.JSONDecodeError:
        print(json.dumps({
            "error": "Invalid JSON input",
            "prediction": None,
            "risk_percentage": 0.0,
            "recommendation": "Invalid input format"
        }))