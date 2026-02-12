# 🚀 Student Performance MLOps Pipeline
 Production-Grade End-to-End Machine Learning System
# 📌 Overview

This project demonstrates a production-ready MLOps pipeline for student performance prediction, covering the complete ML lifecycle:

Model training and evaluation

Experiment tracking with MLflow (SQLite backend)

Model registry & version control

Production model artifact export

Drift detection & monitoring (Evidently AI)

Automatic retraining trigger

Dockerized inference API (FastAPI)

CI/CD automation via GitHub Actions

The system is designed to reflect real-world ML deployment practices used in industry and research environments.

# 🏗 Architecture
Training Pipeline
        ↓
MLflow Tracking (SQLite DB)
        ↓
Model Registry & Production Approval
        ↓
Production Model Export
        ↓
Dockerized FastAPI Inference Service
        ↓
Monitoring & Drift Detection
        ↓
Auto-Retraining Trigger


This architecture separates:

Training environment

Model management

Inference deployment

Monitoring layer

— following best practices in modern MLOps.

# 🧠 Problem Statement

Predict student performance outcomes based on structured academic features such as:

Study hours

Attendance

Academic metrics

The objective is not only to build a predictive model but to ensure:

Reproducibility

Observability

Model lifecycle management

Deployment robustness

# ⚙️ Tech Stack

| Layer               | Technology              |
| ------------------- | ----------------------- |
| ML Model            | Scikit-learn            |
| Experiment Tracking | MLflow (SQLite backend) |
| Model Registry      | MLflow Model Registry   |
| Monitoring          | Evidently AI            |
| API                 | FastAPI                 |
| Containerization    | Docker                  |
| CI/CD               | GitHub Actions          |
| Language            | Python 3.11             |


# 📊 Key MLOps Features
## ✅ Experiment Tracking

All training runs logged to MLflow

Parameters, metrics, artifacts stored in SQLite DB

## ✅ Model Registry

Versioned model management

Production alias control

## ✅ Production Artifact Export

Clean separation of training and inference

No registry dependency in inference container

## ✅ Data Drift Detection

Statistical comparison between reference and incoming data

Drift detection report generation (HTML)

## ✅ Auto-Retraining Trigger

Drift detection can automatically trigger retraining pipeline

## ✅ Dockerized Deployment

Containerized inference API

Portable and reproducible environment

## ✅ CI/CD Automation

GitHub Actions pipeline:

Install dependencies

Run training

Execute monitoring checks

# ▶️ How to Run Locally

1️⃣ Train Model
python src/train.py

2️⃣ Launch MLflow UI
python -m mlflow ui --backend-store-uri sqlite:///mlflow.db


Open:

http://127.0.0.1:5000

3️⃣ Run API
uvicorn src.api:app --reload


Open:

http://127.0.0.1:8000/docs

4️⃣ Run Drift Monitoring
python src/monitor.py


Generates:

drift_report.html

🐳 Run with Docker

Build image:

docker build -t student-ml-api .


Run container:

docker run -p 8000:8000 student-ml-api


Open:

http://localhost:8000

🔁 CI/CD Workflow

On every push to main:

Install dependencies

Train model

Run monitoring script

Ensures pipeline integrity and reproducibility.

# 🎓 Research & Academic Relevance

This project demonstrates concepts central to modern ML research and production systems:

Reproducibility through environment isolation

Database-backed experiment tracking

Model lifecycle management

Data drift detection in non-stationary environments

Automated retraining workflows

Deployment architecture separation

It reflects applied understanding of:

Reliable ML systems

Observability in production models

End-to-end ML system design

# 📈 Future Improvements

Performance degradation monitoring

Concept drift detection

Cloud deployment (AWS / GCP)

PostgreSQL-backed MLflow

Feature store integration

Canary deployment strategy
