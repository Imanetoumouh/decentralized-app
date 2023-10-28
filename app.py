from flask import Flask, render_template

import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',
                                     database = 'devops',
                                     user = 'root',
                                     password = '')
cursor = connection.cursor()

# Create an app instance
app = Flask(__name__)

# Special python decorator which flask provides
# This decorator will assign urls to the associated functions (here index) that is intented to perform that specific task

#@app.route("/")
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/DevOps")
def DevOps():
    # return some other message registration
    cursor.execute("select * from student where module='DevOps'")
    value = cursor.fetchall()
    return render_template("registration.html", data=value, module='DevOps')

@app.route("/BigData")
def BigData():
    # return some other message registration
    cursor.execute("select * from student where module='Big Data'")
    value = cursor.fetchall()
    return render_template("registration.html", data=value, module='Big Data')

@app.route("/DataMining")
def DataMining():
    # return some other message registration
    cursor.execute("select * from student where module='Data Mining'")
    value = cursor.fetchall()
    return render_template("registration.html", data=value, module='Data Mining')

# To run the application
# Port of Flask : 5000
if __name__ == "__main__":
    # to activate the automatic reloader
    # All changes will be updated in the output
    app.run(debug=True)
