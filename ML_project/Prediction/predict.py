import joblib
import numpy as np

def load_model(model_path):
    """
    Load the trained model from a pickle file.
    """
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def make_prediction(model, input_data):
    """
    Make a prediction using the loaded model.
    
    Args:
        model: Loaded model object.
        input_data: List or numpy array of input features.
    
    Returns:
        The prediction result.
    """
    try:
        input_data = np.array(input_data).reshape(1, -1)  # Reshape for single prediction
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None

if __name__ == "__main__":
    # Path to the model file
    model_path = "xgboost_model.pkl"

    # Example input data (replace with your actual feature values)
    input_data = [5.1, 3.5, 1.4, 0.2]  # Example for Iris dataset; adjust accordingly

    # Load the model
    model = load_model(model_path)

    if model:
        # Make a prediction
        prediction = make_prediction(model, input_data)
        if prediction is not None:
            print(f"Prediction: {prediction}")
        else:
            print("Prediction failed.")
