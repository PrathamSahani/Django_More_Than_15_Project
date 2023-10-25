#import Necessary Libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import requests

#Create a FastAPI App
app = FastAPI()

#Define a Pydantic Model
class ModelInput(BaseModel):
    Age: int
    Sex: int
    Cp: int
    Trestbps: int
    Chol: int
    Fbs: int
    Restcg: int
    Thalach: int
    Exang: int  
    Oldpeak: float
    Slope: int
    Ca: int
    Thal: int

# Load the saved model
with open('heart_disease_model.sav', 'rb') as model_file:
    heart_model = pickle.load(model_file)

#Define a POST Endpoint for Diabtes Prediction
@app.post('/heart_prediction')
def diabetes_pred(input_parameters: ModelInput):
    age = input_parameters.Age
    sex = input_parameters.Sex
    cp = input_parameters.Cp
    trestbps = input_parameters.Trestbps  # Fix typo in attribute name
    chol = input_parameters.Chol
    fbs = input_parameters.Fbs
    restecg = input_parameters.Restcg
    thalach = input_parameters.Thalach
    exang = input_parameters.Exang  # Fix typo in attribute name
    oldpeak = input_parameters.Oldpeak
    slope = input_parameters.Slope
    ca = input_parameters.Ca
    thal = input_parameters.Thal

    input_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    prediction = heart_model.predict([input_list])

    if prediction[0] == 0:
        return 'The Person have Heart Diseases'
    else:
        return 'The Person Does not have Heart Diseases'
