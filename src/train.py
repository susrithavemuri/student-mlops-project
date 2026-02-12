import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import joblib
import os

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("student-performance-experiment")





# tell MLflow where to store runs
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("student-performance-experiment")

# load data
data = pd.read_csv("data/student_data.csv")

X = data.drop("result", axis=1)
y = data["result"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# start MLflow run
with mlflow.start_run():

    # train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # log to MLflow
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", accuracy)

    # log model to MLflow
    mlflow.sklearn.log_model(
    sk_model=model,
    artifact_path="model"
)


    # save model locally
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/student_model.pkl")

    print("Model trained and logged to MLflow")
