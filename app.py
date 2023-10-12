import socket

host = socket.gethostbyname(socket.gethostname())
print(f"Running on IP address: {host}")

import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
from logger_config import logger
import sklearn
import joblib

app = Flask(__name__)

# Load the model and scaler
regmodel = joblib.load('best_model.pkl')


# Load the model
ss = joblib.load('standard.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    logger.info("Received data for prediction: %s", data)
    new_data = ss.transform([list(data.values())])
    output = regmodel.predict(new_data)
    logger.info("Prediction result: %s", output[0])
    return jsonify({'prediction': int(output[0])})

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data for each feature
    Age = float(request.form.get("Age"))
    Work_Class = request.form.get("Work_Class")
    fnlwgt = float(request.form.get("fnlwgt"))
    Education = request.form.get("Education")
    Education_num = float(request.form.get("Education_num"))
    Martial_Status = request.form.get("Martial_Status")
    Occupation = request.form.get("Occupation")
    Relationship = request.form.get("Relationship")
    Race = request.form.get("Race")
    Sex = request.form.get("Sex")
    Capital_gain = float(request.form.get("Capital_gain"))
    Capital_loss = float(request.form.get("Capital_loss"))
    hours_per_week = float(request.form.get("hours_per_week"))
    native_country = request.form.get("native_country")

    # Create an array with the feature values
    data = np.array([
        [Age, Work_Class, fnlwgt, Education, Education_num, Martial_Status, Occupation, Relationship, Race, Sex, Capital_gain, Capital_loss, hours_per_week, native_country]
    ])

    # Scale the input data
    final_input = ss.transform(data)

    # Make the prediction
    output = regmodel.predict(final_input)[0]
    
    result = '>=50k' if output == 1 else '<=50k'

    return render_template("home.html", prediction_text=f"The Predicted Salary is {result}")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

'''  
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)'''
