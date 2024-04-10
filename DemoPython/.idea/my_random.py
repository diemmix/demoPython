from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Assuming you have your dataset stored in X and y variables
# Replace this with your actual dataset
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 0, 1, 1]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the random forest model
model_rf = RandomForestClassifier()

# Train the model on the training set
model_rf.fit(X_train, y_train)

# Predict the results on the test set
y_pred_rf = model_rf.predict(X_test)

# Evaluate the model's performance
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print("Accuracy Random Forest:", accuracy_rf)
print(classification_report(y_test, y_pred_rf))