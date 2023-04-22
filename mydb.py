import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'wojtek',
    passwd = '840310',
)

# Prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE wojciechdb")

print("All done!")