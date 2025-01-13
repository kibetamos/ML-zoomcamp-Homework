from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model
model = joblib.load('xgboost_model.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define request body schema
class Features(BaseModel):
    features: list

@app.post("/predict/")
def predict(data: Features):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
