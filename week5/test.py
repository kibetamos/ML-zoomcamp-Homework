import requests

url = "http://127.0.0.1:5000/predict"  # Update with your actual URL if different
client = {"job": "student", "duration": 280, "poutcome": "failure"}

response = requests.post(url, json=client)

try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print(f"Error: {response.status_code}, Response: {response.text}")
