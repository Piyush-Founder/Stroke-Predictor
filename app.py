from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('stroke_model.pkl')
model_columns = joblib.load('model_columns.pkl')


class StrokeInput(BaseModel):
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    avg_glucose_level: float
    work_type: str
    Residence_type: str
    smoking_status: str


app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
def home():
    return FileResponse('static/index.html')


@app.post('/predict')
def predict(data: StrokeInput):
    input_df = pd.DataFrame([{
        'gender': data.gender,
        'age': data.age,
        'hypertension': data.hypertension,
        'heart_disease': data.heart_disease,
        'ever_married': data.ever_married,
        'Residence_type': data.Residence_type,
        'work_type': data.work_type,
        'smoking_status': data.smoking_status,
        'avg_glucose_level': data.avg_glucose_level,
    }])

    input_df = pd.get_dummies(input_df, drop_first=True)
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)[0]
    return {'prediction': int(prediction)}
