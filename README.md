# Calorie Burn Prediction

This project predicts the number of calories burned during physical exercise using a machine learning model built with XGBoost. The app provides an intuitive Streamlit-based UI, and is fully containerized using Docker for easy deployment.

## Features
🔹 Machine Learning

Trained XGBoost regression model

Inputs:

Gender

Age

Height

Weight

Exercise Duration

Heart Rate

Body Temperature

Predicts calories burned in real-time

🔹 Web Interface (Streamlit)

Clean, simple UI

Interactive input form

Card-style results

Mobile-friendly interface

🔹 Docker Support

Fully dockerized app

Build and run using a single command

Works on any system with Docker installed

## How the Model Works

The model is trained on a dataset containing exercise physiological parameters and corresponding calorie burn values.
It uses:

XGBoost Regression

Train/Test Split

Performance metrics like MAE, RMSE, R² Score

Saved using .json to ensure compatibility across XGBoost versions

## Technologies Used

Python

XGBoost

NumPy

Pandas

Scikit-Learn

Streamlit

Docker

▶️ How to Run (Local Machine)
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit App
streamlit run app.py


App will open at:
= http://localhost:8501

## Run with Docker
Build Image
docker build -t calorie-app .

Run Container
docker run -p 8501:8501 calorie-app


Open browser:
👉 http://localhost:8501
