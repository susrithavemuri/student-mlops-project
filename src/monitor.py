import pandas as pd
import numpy as np
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("monitoring-experiment")


# Load reference data
reference_data = pd.read_csv("data/student_data.csv")

# Create strong drift
current_data = reference_data.copy()
current_data["study_hours"] = np.random.normal(15, 5, len(reference_data))
current_data["attendance"] = np.random.normal(50, 10, len(reference_data))

# Create report
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference_data,
           current_data=current_data)

report.save_html("drift_report.html")

print("Drift report generated!")
