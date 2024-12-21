import mysql.connector as mycon

# Establish a connection to the MySQL database
mydb = mycon.connect(
    host="localhost",
    user="root",
    password="Rishik@2004",
    database="Practice_connection"  # Ensure this database name exists in MySQL
)

# Create a cursor object
dbcursor = mydb.cursor()

# Correct the SQL INSERT query syntax
insert_query = "INSERT INTO emp (roll, name) VALUES (%s, %s)"

# Values to be inserted
insert_values = [
    (1, "Rahul"),
    (2, "Ravi"),
    (3, "Rishik"),
    (4, "Ram")
]

# Execute the query with multiple values
dbcursor.executemany(insert_query, insert_values)

# Commit the changes to the database
mydb.commit()

# Print the number of rows inserted
print(dbcursor.rowcount, "Records inserted")

# Close the cursor and connection
dbcursor.close()
mydb.close()
