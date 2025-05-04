

from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

# question 4 section a
data = np.array([[100, 0.001],
                 [8, 0.05],
                 [50, 0.005],
                 [88, 0.07]])


scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)


print("Standardized Data:\n", standardized_data)


# question 4 section c
iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


mlp = MLPClassifier(max_iter=1000)
mlp.fit(X_train, y_train)
y_pred_mlp = mlp.predict(X_test)


svm = SVC()
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)


# question 4 section d

print("MLP Classifier Report:")
print(classification_report(y_test, y_pred_mlp))


print("SVM Classifier Report:")
print(classification_report(y_test, y_pred_svm))

# question 4 section f



# Accuracy
acc_mlp = cross_val_score(mlp, X, y, cv=5, scoring='accuracy').mean()
acc_svm = cross_val_score(svm, X, y, cv=5, scoring='accuracy').mean()


# Precision
prec_mlp = cross_val_score(mlp, X, y, cv=5, scoring='precision_macro').mean()
prec_svm = cross_val_score(svm, X, y, cv=5, scoring='precision_macro').mean()


# Recall
rec_mlp = cross_val_score(mlp, X, y, cv=5, scoring='recall_macro').mean()
rec_svm = cross_val_score(svm, X, y, cv=5, scoring='recall_macro').mean()
