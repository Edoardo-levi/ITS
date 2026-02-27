import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
"""
Categorical Features:

protocol_type → (tcp, udp, icmp)
service → (http, ftp, smtp, dns, ssh, etc.)
flag → (SF, S0, REJ, etc.)
Numerical Features:

duration → Connection duration
src_bytes → Bytes sent from source
dst_bytes → Bytes received
wrong_fragment, count, srv_count → Traffic metrics
same_srv_rate, diff_srv_rate, dst_host_same_srv_rate → Traffic behavior
Target:

label → "normal" or "attack"
"""
df = pd.read_csv("nsl_kdd_train.csv")  # Use nsl_kdd_test.csv for testing

# Identify categorical features
categorical_features = ['protocol_type', 'service', 'flag']

# Encode categorical variables
label_encoders = {}
for feature in categorical_features:
    le = LabelEncoder()
    df[feature] = le.fit_transform(df[feature])
    label_encoders[feature] = le  # Save encoders for later use

# Convert target labels (binary: normal=0, attack=1)
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

# Split features and labels
X = df.drop(columns=['label'])
y = df['label']

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("Data preprocessing complete. Ready for training.")


# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy * 100:.2f}%")


# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Normal", "Attack"], yticklabels=["Normal", "Attack"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Print classification report
print(classification_report(y_test, y_pred))


import time

def simulate_realtime_detection(samples=5):
    print("\n🔴 Real-time Network Intrusion Detection 🔴")
    
    for i in range(samples):
        # Pick a random test sample
        index = np.random.randint(0, len(X_test))
        sample = X_test[index].reshape(1, -1)
        actual = "Attack" if y_test.iloc[index] == 1 else "Normal"

        # Predict
        prediction = model.predict(sample)[0]
        predicted_label = "Attack" if prediction == 1 else "Normal"

        # Output result
        print(f"[Packet {i+1}] Actual: {actual} | Predicted: {predicted_label}")
        time.sleep(1)

simulate_realtime_detection()


import joblib

# Save model
joblib.dump(model, "ids_random_forest.pkl")
print("Model saved as 'ids_random_forest.pkl'")

# Load model
loaded_model = joblib.load("ids_random_forest.pkl")


