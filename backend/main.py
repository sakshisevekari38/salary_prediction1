from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Salary Prediction API",
    description="ML API for predicting employee salary",
    version="1.0"
)

model = joblib.load("backend/model/salary_model.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class EmployeeDetails(BaseModel):
    Age: int
    Years_of_Experience: int
    Education: str
    Job_Role: str
    Location: str
    Previous_Salary: float


@app.get("/")
def home():
    return {
        "message": "Salary Prediction API is running!"
    }


@app.post("/predict")
def predict_salary(employee: EmployeeDetails):

    data = pd.DataFrame([{
        "Age": employee.Age,
        "Years_of_Experience": employee.Years_of_Experience,
        "Education": employee.Education,
        "Job_Role": employee.Job_Role,
        "Location": employee.Location,
        "Previous_Salary": employee.Previous_Salary
    }])

    prediction = model.predict(data)[0]

    return {
        "predicted_salary": round(float(prediction), 2),
        "currency": "INR",
        "input_summary": employee.model_dump()
    }