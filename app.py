import streamlit as st
import numpy as np
import xgboost as xgb

# Load JSON model safely
import xgboost as xgb

booster = xgb.Booster()
booster.load_model("model.json")


st.set_page_config(page_title="Calorie Burn Prediction", page_icon="🔥")

st.title("🔥 Calorie Burn Prediction App")
st.write("Enter the details below to predict how many calories you burned.")

# ---- Input Fields ----
gender = st.radio("Gender", ("Male", "Female"))
age = st.number_input("Age", 1, 100, 25)
height = st.number_input("Height (cm)", 50, 250, 170)
weight = st.number_input("Weight (kg)", 20, 200, 65)
duration = st.number_input("Exercise Duration (minutes)", 1, 300, 30)
heart_rate = st.number_input("Heart Rate", 40, 220, 100)
body_temp = st.number_input("Body Temperature (°C)", 30.0, 45.0, 40.0)

# Convert gender to numeric
gender_val = 0 if gender == "Male" else 1

# ---- Prediction Button ----
if st.button("Predict Calories Burned"):
    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])
    dtest = xgb.DMatrix(input_data)
    prediction = booster.predict(dtest)[0]


    # CARD UI
    st.markdown(
        f"""
        <div style="
            padding: 20px;
            border-radius: 12px;
            background-color: #0E1117;
            border: 1px solid #30363D;
            margin-top: 20px;
        ">
            <h3 style="color:white; text-align:center;">
                🔥 Calories Burned
            </h3>
            <p style="font-size: 32px; font-weight: bold; text-align:center; color:#4CAF50;">
                {prediction:.2f} kcal
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.write("---")
st.caption("Gaurav Chauhan @ 2025")
