import mysql.connector as mycon
mydb=mycon.connect( host="localhost",
                   user="root",
                   password="Rishik@2004",
                   
)
dbcursor=mydb.cursor()
dbcursor.execute("create database Practice_connection")
print("Data Base created successfully.....!")