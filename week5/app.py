from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load your trained model (make sure the path is correct)
with open('/home/bench/Documents/projects/ML-zoomcamp-Homework/week5/model1.bin', 'rb') as model_file:
    model = pickle.load(model_file)

# Initialize LabelEncoders for categorical features
job_encoder = LabelEncoder()
poutcome_encoder = LabelEncoder()

# Fit the encoders with the categories you used in training
# Replace these with the actual categories used during training
job_encoder.fit(['student', 'employed', 'unemployed'])  # example categories
poutcome_encoder.fit(['failure', 'success'])            # example categories

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Ensure that the input data is in the correct format
        job = data['job']
        duration = data['duration']
        poutcome = data['poutcome']

        # Preprocess input data: encode categorical variables
        job_encoded = job_encoder.transform([job])[0]
        poutcome_encoded = poutcome_encoder.transform([poutcome])[0]

        # Create input array
        input_data = np.array([[job_encoded, duration, poutcome_encoded]])

        # Make the prediction
        prediction = model.predict_proba(input_data)

        # Return the probability for the positive class (assuming binary classification)
        return jsonify({'probability': prediction[0][1]})  # Adjust index if needed

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
