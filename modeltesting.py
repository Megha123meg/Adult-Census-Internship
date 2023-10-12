import pickle
from modelselection import X_train, X_test, y_train, y_test,best_model
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import joblib

best_model.fit(X_train,y_train)
y_pred=best_model.predict(X_test)

print("Accuracy_score:",accuracy_score(y_test,y_pred))
print("F1-Score:",f1_score(y_test,y_pred))

document = "mypickle.pkl"

joblib.dump(best_model, 'best_model.pkl')