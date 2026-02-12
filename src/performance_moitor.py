from sklearn.metrics import accuracy_score
import pandas as pd
import joblib
import mlflow

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("performance-monitoring")

# Load model
model = joblib.load("models/student_model.pkl")

# Load new data
data = pd.read_csv("data/student_data.csv")

X = data.drop("result", axis=1)
y = data["result"]

preds = model.predict(X)

acc = accuracy_score(y, preds)

with mlflow.start_run():
    mlflow.log_metric("accuracy", acc)

print("Accuracy:", acc)
