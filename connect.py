import mysql.connector as myconn
mydb=myconn.connect(host="localhost",
                    user="root",
                    password="Rishik@2004")
                    #database="databse_name"
print(mydb,"Connected Successfully!")