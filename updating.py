import mysql.connector as mycon
mydb=mycon.connect(host="localhost",
                   user="root",
                   password="Rishik@2004",
                   database="Practice_connection")
dbcursor=mydb.cursor()
db_update="update emp set roll=%s where name=%s"
db_setvalue=(7,"Abhiram")
dbcursor.execute(db_update,db_setvalue)
mydb.commit()
print(dbcursor.rowcount,"Data is updated.....!")