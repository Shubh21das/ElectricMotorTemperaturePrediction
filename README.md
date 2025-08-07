# Description

# Electric Motor Temperature Prediction using Machine Learning and Flask
This project predicts the Permanent Magnet (PM) temperature of an electric motor based on sensor inputs such as voltage, current, motor speed, and ambient conditions. A regression model is trained using a real-world dataset, and the prediction interface is built using Flask and HTML.

# Features
Predicts PM temperature based on 7 key input parameters.

Interactive web interface built using Flask.

Pre-trained ML model integrated using joblib.

Lightweight, clean, and easy to deploy.

# Input Features
Voltage Uq

Coolant Temperature

Voltage Ud

Motor Speed

Current Id

Current Iq

Ambient Temperature

# Tech Stack
Python

Scikit-learn

Flask

HTML/CSS

# Model
A regression model trained on the Electric Motor Temperature Dataset from Kaggle to predict motor PM temperature.

# How to Run
Clone this repository.

# Install dependencies:

pip install -r requirements.txt

# Run the Flask app:

python app.py

Open your browser at http://127.0.0.1:5000/
