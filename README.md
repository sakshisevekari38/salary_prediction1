# SalaryPredict AI – Employee Salary Prediction System

## Project Overview

SalaryPredict AI is a Machine Learning based web application that predicts an employee's expected salary based on personal and professional details.

## Features

- Employee salary prediction
- Machine Learning based prediction
- FastAPI backend
- HTML, CSS and JavaScript frontend
- Data preprocessing
- Model evaluation
- Saved ML model
- User-friendly interface

## Input Features

- Age
- Years of Experience
- Education Level
- Job Role
- Location
- Previous Salary

## Output

Predicted Salary in Indian Rupees.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- FastAPI
- HTML
- CSS
- JavaScript
- Streamlit

## Machine Learning Model

The project uses Linear Regression for salary prediction.

## Dataset

The dataset contains 500 employee records.

Dataset file:

backend/dataset/salary_data.csv

## How to Run

### Install required libraries

pip install -r requirements.txt

### Start FastAPI backend

uvicorn backend.main:app --reload

### Start frontend

cd frontend

python -m http.server 5500

## API Documentation

http://127.0.0.1:8000/docs

## Project Workflow

Data Collection → Data Preprocessing → Model Training → Model Evaluation → Model Saving → FastAPI Backend → Web Frontend → Salary Prediction

## Future Scope

- Add more employee records
- Improve model accuracy
- Add more job roles and locations
- Deploy the application online
- Add user authentication

## Conclusion

SalaryPredict AI demonstrates how Machine Learning can be integrated with a web application to predict employee salaries.
