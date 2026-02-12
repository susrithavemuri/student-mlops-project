import joblib
import pandas as pd

model = joblib.load("models/student_model.pkl")

sample = pd.DataFrame([{
    "study_hours": 6,
    "attendance": 80,
    "sleep_hours": 7,
    "previous_score": 70
}])

prediction = model.predict(sample)

print("Prediction:", prediction[0])
