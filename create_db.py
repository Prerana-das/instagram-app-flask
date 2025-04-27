import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='instagram_app'
)

mycursor = conn.cursor()
mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)