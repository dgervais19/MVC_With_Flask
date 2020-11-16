# This lesson covers MVC with Flask in Python

## MVC - Model, View, Controller
### Display data on the browser using HTML, CSS, JS and Bootstrap

* HTML - Hyper Text Markup Language
* CSS - Cascading Style Sheet
* JS - Java Script
* Bootstrap

**Building our API**
- Display data from python flask to specific API call/URL/end point/

### Why Flask?
* Flask is a web app framework
* Very Powerful to interact with DB and user interface/browsers etc
* Flask can be used to create an API
* It allows us to integrate with HTML, CSS, JS etc
* It allows us to map HTTP requests to python functions - URL, HTTP GET
* It allows us to set the API path as URL to view in the browser

**Lets install Flask:**

* ```pip install flask```

**Ensure Flask is installed**

**How to run the flask app**
* ```flask run```

**Import all the correct packages**
```
from flask import Flask, jsonify, redirect, url_for
```

**Create a home page on the localhost:**
```
# decorator - to create our api/url for user to access our data in the browser.
@app.route("/") # localhost:5000 is default port for Flask
def home():
    return "<h1>This is a dream team of DevOps consultants!!</h1> "
```

**Create a welcome page using our ow customised API/URL**
```
@app.route("/Welcome/")
def greet_user():
    return "Welcome To DevOps"
# This function runs when the URL/API is accessed
```

**Get data from the script and display it on the webpage**
```
# creating our own API to display data on the specific route URL/End point/API
@app.route("/api/v1/student/data/", methods = ["GET"])
# This will add this API/URL to http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students) # Extract Transform Load (ETL), transforms data into Json
```
**Redirect if page is not found**
```
# Find out the module to redirect the user back to specific page (Welcome Page)
# If page is not found (status code 404) redirect the user to welcome page
@app.route("/login/")
def login():
    return redirect(url_for("greet_user")) # you put the function that has the page you want it to redirect to
```

**How to pass an argument into the decorator (<username>)**
```
@app.route("/<username>/") # how we pass the user argument in the decorator
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps {username}</h1>"
if __name__ == "__main__":
    app.run(debug=True)
```

**interacting with HTML**
* Naming conventions are essential
* We need to create templates folder in our dir
* Flasks looks for templates folder and anything inside the folder
* We will create index.html inside our templates folder


**Use bootsrap to design our page with HTML, CSS etc**
