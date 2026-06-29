import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle


# Load dataset
df = pd.read_csv("Telco-Customer-Churn.csv")


# Cleaning
df.drop("customerID", axis=1, inplace=True)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df.dropna(inplace=True)


# Convert target column
df["Churn"] = LabelEncoder().fit_transform(df["Churn"])


# Convert all remaining text columns
df = pd.get_dummies(df)


# Split data
X = df.drop("Churn", axis=1)
y = df["Churn"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# Test
prediction = model.predict(X_test)


print("Accuracy:")
print(accuracy_score(y_test, prediction))


print("\nClassification Report:")
print(classification_report(y_test, prediction))


# Save model
with open("models/churn_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model saved successfully")