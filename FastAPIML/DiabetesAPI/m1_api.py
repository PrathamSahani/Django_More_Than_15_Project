from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int  # Fixed the type annotation

# Load the saved model
with open('diabetes_model.sav', 'rb') as model_file:
    diabetes_model = pickle.load(model_file)

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: ModelInput):
    # Don't convert the Pydantic model to JSON and back to a dictionary; you can access the attributes directly.
    preg = input_parameters.Pregnancies
    glu = input_parameters.Glucose
    bp = input_parameters.BloodPressure
    skin = input_parameters.SkinThickness
    insulin = input_parameters.Insulin
    bmi = input_parameters.BMI
    dpf = input_parameters.DiabetesPedigreeFunction
    age = input_parameters.Age
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The Person is not Diabetic'
    else:
        return 'The person is Diabetic'
