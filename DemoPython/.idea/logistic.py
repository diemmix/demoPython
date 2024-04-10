from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, classification_report

#*** Example dataset
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 0, 1, 1]
#*** Define your feature matrix X and target vector y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#*** Build the logistic regression model 
model_lr = LogisticRegression()

#*** Train the model on the training set 
model_lr.fit(X_train, y_train)

#*** Predict the results on the test set 
y_pred_lr = model_lr.predict(X_test)

#*** Evaluate the model's performance 
accuracy_lr = accuracy_score(y_test, y_pred_lr) 
print("Accuracy Logistic Regression:", accuracy_lr) 
print(classification_report(y_test, y_pred_lr, zero_division=1))