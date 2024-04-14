from yellowbrick.features import FeatureImportances
from FeatureEngineering import y_test,y_train
from HyperparameterTuning import best_model
from FeatureSelection import X_train_features,X_test_features
import pickle

viz= FeatureImportances(best_model, topn=25)
viz.fit(X_train_features, y_train)
X_train_returned=X_train_features[viz.features_]
X_test_returned=X_test_features[viz.features_]       

best_model.fit(X_train_returned,y_train)

from sklearn.metrics import classification_report
y_pred=best_model.predict(X_test_returned)
class_labels = list(best_model.classes_)
print(classification_report(y_test, y_pred, labels=class_labels))

print("Best model is",best_model)


document = "mymodel.pkl"
    
pickle.dump(best_model,open(document,"wb"))