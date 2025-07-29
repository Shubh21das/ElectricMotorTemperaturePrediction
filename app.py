from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manual')
def manual():
    return render_template('Manual_predict.html')

@app.route('/sensor')
def sensor():
    return render_template('Sensor_predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        input_data = np.array(data).reshape(1, -1)
        scaled_data = scaler.transform(input_data)
        output = model.predict(scaled_data)
        return render_template('result.html', prediction=round(output[0], 4))
    except:
        return "Error: Please check your inputs!"

if __name__ == '__main__':
    app.run(debug=True)
