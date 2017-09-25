# File for MySQL

import MySQLdb

host = "localhost"
user = "test"
password = "password"
database = "example"

#Connect to MySQL
db = MySQLdb.connect(host + user + password + database)

# Cursor object to execute queries
cursor = db.cursor()

# Show table if already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table 
sql = """CREATE TABLE EMPLOYEE (
			FIRST_NAME CHAR(20) NOT NULL,
			LAST_NAME CHAR(20),
			AGE INT,
			SEX CHAR(1),
			INCOME FLOAT )"""

cursor.execute(sql)

# Disconnect from mysql server
db.close()