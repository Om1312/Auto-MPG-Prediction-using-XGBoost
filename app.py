import streamlit as st
import pickle
import pandas as pd

# Load model
with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🚗 MPG Prediction App (XGBoost Model)")

st.write("Enter car details below to predict its fuel efficiency (MPG).")

# Input fields
cylinders = st.number_input("Cylinders", min_value=3, max_value=12, value=4)
displacement = st.number_input("Displacement", min_value=50, max_value=500, value=140)
horsepower = st.number_input("Horsepower", min_value=40, max_value=300, value=90)
weight = st.number_input("Weight (lbs)", min_value=1000, max_value=6000, value=2500)
acceleration = st.number_input("Acceleration (0-60 time)", min_value=5.0, max_value=30.0, value=15.0)
model_year = st.number_input("Model Year", min_value=60, max_value=100, value=80)
origin = st.selectbox("Origin (1 = USA, 2 = Europe, 3 = Japan)", [1, 2, 3])

# Predict button
if st.button("Predict MPG"):
    data_df = pd.DataFrame({
        'cylinders': [cylinders],
        'displacement': [displacement],
        'horsepower': [horsepower],
        'weight': [weight],
        'acceleration': [acceleration],
        'model year': [model_year],
        'origin': [origin]
    })

    prediction = model.predict(data_df)[0]
    st.success(f"Estimated MPG: **{prediction:.2f}**")
