# Step 4: Define Features (X) and Target (y)

import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv('SONY_ready_file.csv')

# Use the calculated technical indicators as features
X = df[['MACD', 'RSI', 'EMA', 'MA', 'SMA', 'Upper', 'Lower']]

# Predict if the next day's Close price will be higher or lower
df['Price_Change'] = df['Close'].shift(-1) > df['Close']
y = df['Price_Change'].astype(int)  # Convert boolean to 0 (False) or 1 (True)

# Step 5: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 7: Train an SVM Classifier
svm = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)  # RBF kernel with default parameters
svm.fit(X_train_scaled, y_train)

y_pred = svm.predict(X_test_scaled)

# Step 8: Evaluate model performance

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Precision
precision = precision_score(y_test, y_pred)
print(f"Precision: {precision:.2f}")

# Recall
recall = recall_score(y_test, y_pred)
print(f"Recall: {recall:.2f}")


# Step 9: Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix:\n{conf_matrix}")

# Step 10: Visualize the Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Down', 'Up'], yticklabels=['Down', 'Up'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()


# Step 11: Cross-validation and F1 Score

from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score

# Cross-validation
cv_scores = cross_val_score(svm, X, y, cv=5, scoring='accuracy')
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Accuracy: {cv_scores.mean():.2f}")

# F1 Score
f1 = f1_score(y_test, y_pred)
print(f"F1 Score: {f1:.2f}")
