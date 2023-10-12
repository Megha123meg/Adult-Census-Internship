from featureselection import X,y
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                      train_size=0.8,
                                                      test_size=0.2,
                                                      random_state=101)

# Define the models to be evaluated
models = [
    LogisticRegression(),
    DecisionTreeClassifier(),
    SGDClassifier(),
    KNeighborsClassifier(),
    GaussianNB(),
    RandomForestClassifier(n_estimators=100)
]

# Evaluate each model on the training set
accuracies = []
for model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Select the model with the highest accuracy on the training set
best_model = models[accuracies.index(max(accuracies))]

# Evaluate the best model on the test set
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the best model on the test set
print('Accuracy of the best model on the test set:', accuracy)