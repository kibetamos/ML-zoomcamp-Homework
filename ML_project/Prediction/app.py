from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('xgboost_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)  # Make sure data is in proper shape

    # Make prediction
    prediction = model.predict(features)

    # Return prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
