import mysql.connector as mycon
mydb=mycon.connect(host="localhost",
                   user="root",
                   password="Rishik@2004",
                   database="Practice_connection")
dbcursor=mydb.cursor()
dbcursor.execute("select* from emp")
for dbdata in dbcursor.fetchall():
    print(dbdata)