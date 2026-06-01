# ITSM ML Project

## Overview

The ITSM ML Project is an end-to-end Machine Learning system designed to automate and optimize IT Service Management (ITSM) operations.

This project applies Machine Learning, Forecasting, and Predictive Analytics techniques to improve operational efficiency, automate service workflows, and reduce manual incident handling efforts.

The system includes:

- Incident Priority Prediction
- Incident Volume Forecasting
- Auto Ticket Tagging
- RFC Risk Prediction
- Flask API Deployment
- GitHub Version Control

---

# Business Problem

Modern ITSM environments generate large volumes of incidents, change requests, and operational alerts daily.

Manual handling introduces:

- SLA violations
- delayed ticket resolution
- incorrect ticket routing
- operational instability
- poor workload forecasting
- increased downtime risks

This project addresses those challenges using Machine Learning automation.

---

# Project Objectives

The main objectives of this system are:

- Predict incident priority automatically
- Forecast future incident volumes
- Automate ticket categorization/tagging
- Predict operational RFC risks
- Improve IT operational efficiency
- Support proactive service management

---

# Project Architecture

```text
ITSM_ML_Project/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_extraction.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_priority_prediction.ipynb
│   ├── 04_forecasting.ipynb
│   ├── 05_auto_tagging.ipynb
│   └── 06_rfc_failure_prediction.ipynb
│
├── models/
│   ├── priority_model.pkl
│   ├── forecast_model.pkl
│   ├── auto_tagging_model.pkl
│   └── rfc_risk_model.pkl
│
├── app/
│   └── app.py
│
├── utils/
│   └── helper.py
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

# Machine Learning Use Cases

| Use Case | ML Type | Model Used |
|---|---|---|
| Priority Prediction | Classification | XGBoost |
| Incident Forecasting | Time Series Forecasting | Prophet |
| Auto Ticket Tagging | Classification | XGBoost |
| RFC Risk Prediction | Classification | XGBoost |

---

# Technologies Used

## Programming Language
- Python

## Data Processing
- Pandas
- NumPy

## Data Visualization
- Matplotlib
- Seaborn

## Machine Learning
- Scikit-learn
- XGBoost

## Forecasting
- Prophet
- Statsmodels

## Deployment
- Flask

## Model Persistence
- Joblib

## Version Control
- Git
- GitHub

---

# Data Preprocessing

The preprocessing pipeline includes:

- missing value handling
- duplicate removal
- datetime feature extraction
- categorical encoding
- feature engineering
- incident operational metrics generation

Generated features include:

- Open_Year
- Open_Month
- Open_Day
- Open_Hour
- Open_Weekday
- Handle_Time_hrs

---

# Model Performance

## Priority Prediction

| Model | Accuracy |
|---|---|
| Logistic Regression | ~66% |
| Random Forest | ~80% |
| XGBoost | ~82% |

---

## Auto Ticket Tagging

| Model | Accuracy |
|---|---|
| Random Forest | ~99% |
| XGBoost | ~99% |

---

## RFC Risk Prediction

| Model | Cross Validation Accuracy |
|---|---|
| XGBoost | ~93.5% |

---

# Forecasting System

The forecasting module predicts future incident volumes using Prophet.

Forecasting capabilities include:

- incident trend analysis
- operational workload prediction
- proactive staffing support
- incident seasonality analysis

---

# Flask API Deployment

The project includes Flask deployment for real-time prediction serving.

## Available APIs

### Priority Prediction API

```python
/predict_priority
```

### RFC Risk Prediction API

```python
/ predict_rfc_risk
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Jaswanthraj955/ITSM_ML_Project.git
```

---

## Move to Project Directory

```bash
cd ITSM_ML_Project
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Flask Application

```bash
python app/app.py
```

Application runs on:

```text
http://127.0.0.1:5000
```

---

# Future Improvements

Possible future enhancements:

- Streamlit dashboard
- Real-time ticket streaming
- NLP-based ticket summarization
- Cloud deployment
- Docker containerization
- CI/CD pipeline integration

---

# Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow for IT Service Management automation.

The system integrates:

- data engineering
- machine learning
- forecasting
- API deployment
- operational analytics
- version control

to build a scalable and deployment-ready ITSM intelligence platform.

---

# Author

Jaswanth Raj

GitHub:
https://github.com/Jaswanthraj955
