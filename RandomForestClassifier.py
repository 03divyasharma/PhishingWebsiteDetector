from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint

model=RandomForestClassifier()
            #HyperparameterTuning
param_dist = {'n_estimators': randint(100,110),      
                          'max_depth':  list(range(10, 100, 10)),  
                          'min_samples_split': randint(2, 20),      
                          'min_samples_leaf': randint(1, 20),
                           'criterion':['gini', 'entropy','log_loss'] }