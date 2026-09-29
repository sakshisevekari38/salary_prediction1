import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load dataset
data = pd.read_csv("backend/dataset/salary_data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)


# 2. Separate features and target
X = data.drop("Salary", axis=1)
y = data["Salary"]


# 3. Define columns
numeric_features = [
    "Age",
    "Years_of_Experience",
    "Previous_Salary"
]

categorical_features = [
    "Education",
    "Job_Role",
    "Location"
]


# 4. Preprocessing
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])


# 5. Create model pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])


# 6. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# 7. Train model
model.fit(X_train, y_train)

print("Model trained successfully!")


# 8. Make predictions
y_pred = model.predict(X_test)


# 9. Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))


# 10. Save model
joblib.dump(model, "backend/model/salary_model.pkl")

# Save evaluation results
with open("backend/model/evaluation_results.txt", "w") as file:
    file.write(f"MAE: {mae:.2f}\n")
    file.write(f"MSE: {mse:.2f}\n")
    file.write(f"RMSE: {rmse:.2f}\n")
    file.write(f"R2 Score: {r2:.4f}\n")


print("\nModel saved successfully!")
print("Location: backend/model/salary_model.pkl")