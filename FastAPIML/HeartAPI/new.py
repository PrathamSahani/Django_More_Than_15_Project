import json
import requests

url = 'http://127.0.0.1:8000/heart_prediction'

input_data_for_model = {
    "Age": 63,
    "Sex": 1,
    "Cp": 3,
    "Trestbps": 145,
    "Chol": 233,
    "Fbs": 1,
    "Restcg": 0,
    "Thalach": 150,
    "Exang": 0,  # Fix typo in attribute name
    "Oldpeak": 2.3,
    "Slope": 0,
    "Ca": 1,
    "Thal": 1,
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)
print(response.text)