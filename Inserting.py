import mysql.connector as mycon
mydb=mycon.connect(host="localhost",
                   user="root",
                   password="Rishik@2004",
                   database="Practice_connection")
dbcursor=mydb.cursor()
insert_query="insert into emp(roll,name) values(%s,%s)"
insert_values=[(5,"Harshith"),(6,"Abhiram")]
dbcursor.execute(insert_query,insert_values) # used to insert manyvalues
dbcursor.ececute(insert_query,insert_values)  #used to insert only 1 value 
mydb.commit()
print(dbcursor.rowcount,"Records inserted")