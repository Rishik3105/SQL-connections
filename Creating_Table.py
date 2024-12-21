import mysql.connector as mycon
mydb=mycon.connect(host="localhost",
                   user="root",
                   password="Rishik@2004",
                   database="Practice_connection")
dbcursor=mydb.cursor()
dbcursor.execute("create table emp(roll int , name varchar(20))")
print("Table created........!")