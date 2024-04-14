from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
from FeatureEngineering import y_test, y_train
from FeatureSelection import X_train_features, X_test_features
from RandomForestClassifier import model, param_dist

print("Training model")

rscv = RandomizedSearchCV(model, param_dist, n_iter=10, cv=5, scoring='accuracy', n_jobs=-1, random_state=42)
rscv.fit(X_train_features, y_train)

# Update the best parameters to the pipeline
best_model = rscv.best_estimator_
best_params = rscv.best_params_
print("Best Hyperparameters:", best_params)

# Train the model using the best found parameters
best_model.fit(X_train_features, y_train)

# Evaluate the model on training and testing data
y_train_pred = best_model.predict(X_train_features)
y_test_pred = best_model.predict(X_test_features)

train_model_score = accuracy_score(y_train, y_train_pred)
test_model_score = accuracy_score(y_test, y_test_pred)
print("Train Score:", train_model_score)
print("Test Score:", test_model_score)

# Additional evaluation metrics and checks
best_model_score = best_model.score(X_test_features, y_test)
if best_model_score < 0.72:
    print("No best model found")

print("Best found model on both training and testing dataset", best_model)
