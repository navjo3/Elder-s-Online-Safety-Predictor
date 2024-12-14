import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('logistic_tree_model.pkl')

# Define the app
st.title("Online Safety Predictor for Elderly Individuals")
st.write("This tool predicts how safe an elder is online based on their information.")

# User inputs
age = st.number_input("Age (years)", min_value=60, max_value=100, value=70, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
education_level = st.selectbox("Education Level", ["High School", "College", "Graduate", "Postgraduate", "Other"])
tech_savvy = st.slider("Tech Savvy Level (1-10)", min_value=1, max_value=10, value=5)
hours_online = st.number_input("Hours Spent Online Daily", min_value=0.0, max_value=24.0, value=2.0, step=0.1)
primary_device = st.selectbox("Primary Device Used", ["Mobile", "Laptop", "Tablet", "Desktop", "Other"])
social_media = st.selectbox("Social Media Usage", ["Yes", "No"])
email_awareness = st.slider("Email Awareness (1-10)", min_value=1, max_value=10, value=5)
password_strength = st.slider("Password Strength (1-10)", min_value=1, max_value=10, value=5)
two_factor_auth = st.selectbox("Two-Factor Authentication Usage", ["Yes", "No"])
scam_history = st.selectbox("Scam History", ["Yes", "No"])
scam_type = st.selectbox("Scam Type", ["Phishing", "Fake Support", "Fake Products", "Investment Fraud", "Other", "Unknown"])
cyber_awareness = st.selectbox("Cybersecurity Awareness", ["Yes", "No"])
confidence = st.slider("Confidence Level (1-10)", min_value=1, max_value=10, value=5)
recent_scams = st.number_input("Recent Scam Attempts", min_value=0, max_value=50, value=2, step=1)

# Preprocessing user inputs
# Example encoding for categorical features
gender_mapping = {"Male": 0, "Female": 1, "Other": 2}
education_mapping = {"High School": 1, "College": 2, "Graduate": 3, "Postgraduate": 4, "Other": 5}
device_mapping = {"Mobile": 1, "Laptop": 2, "Tablet": 3, "Desktop": 4, "Other": 5}
binary_mapping = {"Yes": 1, "No": 0}
scam_type_mapping = {
    "Phishing": 1,
    "Fake Support": 2,
    "Fake Products": 3,
    "Investment Fraud": 4,
    "Other": 5,
    "Unknown": 6,
}

# Encode the inputs
gender_encoded = gender_mapping[gender]
education_encoded = education_mapping[education_level]
primary_device_encoded = device_mapping[primary_device]
social_media_encoded = binary_mapping[social_media]
two_factor_encoded = binary_mapping[two_factor_auth]
scam_history_encoded = binary_mapping[scam_history]
scam_type_encoded = scam_type_mapping[scam_type]
cyber_awareness_encoded = binary_mapping[cyber_awareness]

# Create feature array
user_data = np.array([[age, gender_encoded, education_encoded, tech_savvy, hours_online,
                       primary_device_encoded, social_media_encoded, email_awareness,
                       password_strength, two_factor_encoded, scam_history_encoded,
                       scam_type_encoded, cyber_awareness_encoded, confidence,
                       recent_scams]])

# Make a prediction
# ... existing code ...

# ... existing code ...

if st.button("Predict"):
    prediction = model.predict(user_data)
    prediction_proba = model.predict_proba(user_data)
    
    # Simplified mapping since we know we're getting string predictions
    safety_status = {
        "Safe": "Safe",
        "Moderately Safe": "Moderately Safe",
        "Not Safe": "Not Safe"
    }
    
    # Display the prediction
    predicted_status = safety_status.get(prediction[0], prediction[0])
    st.write(f"### Prediction: {predicted_status}")
    st.write(f"### Confidence: {prediction_proba.max() * 100:.2f}%")

# ... rest of the code ...

# ... rest of the code ...
# Additional info
st.write("The model uses machine learning to predict safety based on online behavior and demographics.")
