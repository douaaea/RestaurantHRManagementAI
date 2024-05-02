import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database='facesmatdb'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM login')
users=mycursor.fetchall()

for user in users:
    print(user)