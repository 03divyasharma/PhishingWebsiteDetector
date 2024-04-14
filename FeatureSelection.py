
from FeatureEngineering import X_train,X_test,y_test,y_train

threshold=0.7
col_corr=set()
corr_matrix=X_train.corr()
for i in range(len(corr_matrix.columns)):
            for j in range(i):
               if abs(corr_matrix.iloc[i,j])>threshold:
                colname=corr_matrix.columns[i]
                col_corr.add(colname)
X_train_features=X_train.drop(col_corr,axis=1)
X_test_features=X_test.drop(col_corr,axis=1)
print(X_train_features)


            

        


