import mysql.connector as mycon
mydb=mycon.connect(host="localhost",
                   user="root",
                   password="Rishik@2004",
                   database="Practice_connection")
dbcursor=mydb.cursor()
delete_record="delete from emp where roll=%s"
value=('4',)
dbcursor.execute(delete_record,value)
mydb.commit()