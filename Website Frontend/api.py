import json
from flask_cors import CORS
import mysql.connector
from flask import Flask, request


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route("/")
def hello():
    return "Hello, World!"



@app.route('/getUserLogin', methods=["POST"])
def users():
 mydb = mysql.connector.connect(
  host="database-eyespy.cyvbyvilxbbf.us-east-2.rds.amazonaws.com",
  user="admin",
  password="Master123",
  database="sys"
  )
 
 data = json.loads(request.data)
# Create a cursor object
 mycursor = mydb.cursor()

# # Execute a simple query to test the connection
 email = data['user_email']
 mycursor.execute("SELECT * FROM login_details WHERE EMAIL = '"+ email +"';")
 print("SELECT * FROM login_details WHERE EMAIL = '"+ email +"';")

 results = mycursor.fetchall()
 return results
# Close the connection
 mydb.close()


@app.route('/getHistory', methods=["POST"])
def us():
 mydb = mysql.connector.connect(
  host="database-eyespy.cyvbyvilxbbf.us-east-2.rds.amazonaws.com",
  user="admin",
  password="Master123",
  database="sys"
  )
 
 data = json.loads(request.data)
# Create a cursor object
 mycursor = mydb.cursor()

# # Execute a simple query to test the connection
 custId = data['cust_id']
 mycursor.execute("SELECT srNo, personName, AlertSent, created_date_Time, method_of_Alert, authorized_status FROM sys.history_all WHERE cust_id = '"+ custId +"';")

 results = mycursor.fetchall()
 return results
# Close the connection
 mydb.close()

@app.route('/submitDemoDetails', methods=["POST"])
def sub():
  mydb = mysql.connector.connect(
  host="database-eyespy.cyvbyvilxbbf.us-east-2.rds.amazonaws.com",
  user="admin",
  password="Master123",
  database="sys"
  )
 
  data = json.loads(request.data)
# Create a cursor object
  mycursor = mydb.cursor()

# # Execute a simple query to test the connection
  name = data['user_name']
  email= data['email_id']
  phone= data['phone_no']
  photos= data['photos_link']
  carrier=data['carrier']
  address = data['address']
  mycursor.execute("Insert into person_detail(PERSON_NAME,EMAIL_ID,PHONE_NUMBER,ADDRESS,carrier_detail) values('"+ name +"','"+ email +"','"+ phone +"','"+ address +"','"+ carrier +"');")
  mydb.commit()
  results = mycursor.rowcount
  return results
# Close the connection
  mydb.close()

if __name__ == "__main__":
    app.run("localhost", 8888)