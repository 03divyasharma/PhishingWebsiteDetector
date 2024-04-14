
import pandas as pd
from sklearn.model_selection import train_test_split
import data_ingestion
from data_ingestion import dframe

X = data_ingestion.dframe.drop(columns=['phishing']) 
y = data_ingestion.dframe['phishing']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train)
        
print("Data retrieval and splitting successful!")
