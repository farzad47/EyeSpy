import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="database-eyespy.cyvbyvilxbbf.us-east-2.rds.amazonaws.com",
  user="admin",
  password="Master123",
  database="sys"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a simple query to test the connection
mycursor.execute("SELECT * FROM authorized_customer_mapping LIMIT 10")

# Fetch the results and print them
results = mycursor.fetchall()
for row in results:
    print(row)

# Close the connection
mydb.close()
