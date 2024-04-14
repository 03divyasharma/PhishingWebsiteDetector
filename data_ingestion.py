import pandas as pd
from sklearn.model_selection import train_test_split
import mysql.connector

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql_root_password",
        database="projects"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM projects.dataset_full")
        data = cursor.fetchall()
        columns = [i[0] for i in cursor.description]
        dframe= pd.DataFrame(data, columns=columns)
except mysql.connector.Error as e:
    print("MySQL Error:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        
print(dframe['qty_slash_domain'])

columns_to_drop = []
for column in dframe.columns:
    if dframe[column].nunique() == 1:
        columns_to_drop.append(column)
print(columns_to_drop)

dframe = dframe.drop(columns=columns_to_drop, axis=1)
print(dframe)