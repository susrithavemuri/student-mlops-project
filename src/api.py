from fastapi import FastAPI
import pandas as pd
import mlflow.pyfunc

app = FastAPI()

MODEL_NAME = "student-performance-model"
MODEL_ALIAS = "production"

model = mlflow.pyfunc.load_model(
   "production_model"
)

@app.get("/")
def home():
    return {"message": "Student Performance ML API (Production Model)"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction[0]}
