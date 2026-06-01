import pandas as pd
import numpy as np

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt
import seaborn as sns


def evaluate_model(model_name, y_test, y_pred):

    print("\n" + "="*50)
    print(model_name)
    print("="*50)

    print("\nAccuracy Score:\n")

    accuracy = accuracy_score(y_test, y_pred)

    print(accuracy)

    print("\nClassification Report:\n")

    print(
        classification_report(
            y_test,
            y_pred,
            zero_division=0
        )
    )

    print("\nConfusion Matrix:\n")

    cm = confusion_matrix(y_test, y_pred)

    print(cm)

    plt.figure(figsize=(8,6))

    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues'
    )

    plt.title(f"{model_name} Confusion Matrix")

    plt.xlabel("Predicted")

    plt.ylabel("Actual")

    plt.show()


def extract_datetime_features(df, column_name):

    df[column_name] = pd.to_datetime(df[column_name])

    df[f"{column_name}_Year"] = df[column_name].dt.year

    df[f"{column_name}_Month"] = df[column_name].dt.month

    df[f"{column_name}_Day"] = df[column_name].dt.day

    df[f"{column_name}_Hour"] = df[column_name].dt.hour

    df[f"{column_name}_Weekday"] = df[column_name].dt.weekday

    return df


def missing_value_summary(df):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    return missing.sort_values(ascending=False)


def model_accuracy(model, X_test, y_test):

    score = model.score(X_test, y_test)

    return round(score * 100, 2)