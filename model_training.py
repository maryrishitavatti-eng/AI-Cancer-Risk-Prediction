import pandas as pd

# Load dataset
df = pd.read_csv("data/breast_cancer_risk.csv")

print(df.head())
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:")
print(df.isnull().sum())
print("Risk label counts:")
print(df["risk_label"].value_counts())

# Separate input features (X) and target (y)
X = df.drop(["patient_id", "risk_label"], axis=1)
y = df["risk_label"]

print("\nInput features:")
print(X.columns.tolist())

print("\nTarget:")
print(y.name)

# Convert Yes/No values into 0/1
binary_columns = [
    "family_history",
    "breast_lump",
    "breast_pain",
    "nipple_discharge",
    "skin_changes",
    "previous_breast_disease"
]

for col in binary_columns:
    X[col] = X[col].map({"No": 0, "Yes": 1})

print("\nEncoded input data:")
print(X.head())

# Convert risk labels into numbers
y = y.map({
    "Low": 0,
    "Moderate": 1,
    "High": 2
})

print("\nEncoded target:")
print(y.head())

# Split data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# Create and train the Random Forest model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully!")

# Make predictions on test data
y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred[:10])

# Calculate model accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("Model Accuracy (%):", accuracy * 100)

# Detailed model evaluation
from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Low", "Moderate", "High"]
))

# Confusion Matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Low", "Moderate", "High"],
    yticklabels=["Low", "Moderate", "High"]
)

plt.xlabel("Predicted Risk")
plt.ylabel("Actual Risk")
plt.title("Confusion Matrix")
plt.show()

# Feature Importance
import pandas as pd
import matplotlib.pyplot as plt

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance)

plt.figure(figsize=(8, 5))
plt.barh(importance["Feature"], importance["Importance"])
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importance - Random Forest")
plt.gca().invert_yaxis()
plt.show()

# Save the trained model
import joblib

joblib.dump(model, "cancer_risk_model.pkl")

print("\nModel saved successfully!")