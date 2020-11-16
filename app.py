from flask import Flask, jsonify

# Create an instance of our app

app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Donovan", "last_name": "Gervais", "course": "DevOps"}
]

# decorator - to create our api/url for user to access our data in the browser.
@app.route("/") # localhost:5000 is default port for Flask
def home():
    return "<h1>This is a dream team of DevOps consultants!!</h1> "
# This function runs when the URL/API is accessed

# creating our own API to display data on the specific route URL/End point/API
@app.route("/okay cal", methods = ["GET"])
# This will add this API/URL to http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students) # Extract Transform Load (ETL), transforms data into Json

if __name__ == "__main__":
    app.run(debug=True)