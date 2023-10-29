from flask import Flask, render_template, request
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='devops',
    user='root',
    password=''
)

cursor = connection.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        module = request.form['module']

        cursor.execute("INSERT INTO student (name, email, age, module) VALUES (%s, %s, %s, %s)", (name, email, age, module))
        connection.commit()

    return render_template("index.html")

@app.route("/DevOps", methods=['GET', 'POST'])
def DevOps():
    cursor.execute("SELECT * FROM student WHERE module = 'DevOps'")
    data = cursor.fetchall()
    return render_template("registration.html", data=data, module='DevOps')

@app.route("/BigData", methods=['GET', 'POST'])
def BigData():
    cursor.execute("SELECT * FROM student WHERE module = 'BigData'")
    data = cursor.fetchall()
    return render_template("registration.html", data=data, module='BigData')

@app.route("/DataMining", methods=['GET', 'POST'])
def DataMining():
    cursor.execute("SELECT * FROM student WHERE module = 'DataMining'")
    data = cursor.fetchall()
    return render_template("registration.html", data=data, module='DataMining')

if __name__ == "__main__":
    app.run(debug=True)
