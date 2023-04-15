#pip install mysql
#pip instal mysqlclient
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'raito'
)

#prepare cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute('CREATE DATABASE crm_webapp')

print('All Done!')