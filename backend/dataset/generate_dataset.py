import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

age = np.random.randint(21, 55, n)
experience = np.random.randint(0, 25, n)
education = np.random.choice(
    ["Bachelor", "Master", "PhD"], n
)
job_role = np.random.choice(
    ["Developer", "Data Analyst", "Manager", "Designer", "Tester"], n
)
location = np.random.choice(
    ["Pune", "Mumbai", "Bangalore", "Delhi", "Hyderabad"], n
)
previous_salary = np.random.randint(20000, 120000, n)

salary = (
    15000
    + experience * 5000
    + age * 500
    + previous_salary * 0.4
    + np.where(education == "Master", 15000, 0)
    + np.where(education == "PhD", 30000, 0)
    + np.where(job_role == "Manager", 25000, 0)
    + np.where(job_role == "Developer", 15000, 0)
    + np.random.normal(0, 10000, n)
)

salary = np.maximum(salary, 15000)

df = pd.DataFrame({
    "Age": age,
    "Years_of_Experience": experience,
    "Education": education,
    "Job_Role": job_role,
    "Location": location,
    "Previous_Salary": previous_salary,
    "Salary": salary.round(0)
})

file_path = "backend/dataset/salary_data.csv"

df.to_csv(file_path, index=False)

print("Dataset created successfully!")
print("Number of records:", len(df))
print("File saved at:", file_path)
print(df.head())