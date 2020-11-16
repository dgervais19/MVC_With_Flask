from flask import Flask, jsonify, redirect, url_for, render_template

# Create an instance of our app

app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Donovan", "last_name": "Gervais", "course": "DevOps"}
]

# decorator - to create our api/url for user to access our data in the browser.
@app.route("/") # localhost:5000 is default port for Flask
def home():
    return "<h1>This is a dream team of DevOps consultants!!</h1> "

@app.route("/Welcome/") # http://127.0.0.1:5000/welcome/
def greet_user():
    return redirect(url_for('welcome.html'))
# This function runs when the URL/API is accessed

# creating our own API to display data on the specific route URL/End point/API
@app.route("/api/v1/student/data/", methods = ["GET"])
# This will add this API/URL to http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students) # Extract Transform Load (ETL), transforms data into Json

# Find out the module to redirect the user back to specific page (Welcome Page)
# If page is not found (status code 404) redirect the user to welcome page
@app.route("/login/")
def login():
    return render_template("login.html") # you put the function that has the page you want it to redirect to

@app.route("/<username>/") # how we pass the user argument in the decorator
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps {username}</h1>"

@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/base/")
def base():
    return render_template(("base.html"))

if __name__ == "__main__":
    app.run(debug=True)