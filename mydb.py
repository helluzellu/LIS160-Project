import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'lis160'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE gidb")

print("Done.")