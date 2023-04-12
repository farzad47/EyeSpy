import json
import mysql.connector
import flask
from flask import Flask
app = Flask(_name_)


@app.route("/")
def hello():
    return "Hello, World!"



@app.route('/users', methods=["GET"])
def getLoginDetails():
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
 mycursor.execute("SELECT * FROM login_details")

# Fetch the results and print them
 results = mycursor.fetchall()
 data = results
        
 return flask.jsonify(data)

# Close the connection
 mydb.close()



if _name_ == "_main_":
    app.run("localhost", 6969)