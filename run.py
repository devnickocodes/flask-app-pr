import os
import json 
from flask import Flask, render_template


app = Flask(__name__) # creates an instance of this Flask class


@app.route("/") # we use the route decorator to tell Flask what URL should trigger the function that follows # "/" is the root directory when we try to browse it Flask triggers the index function
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company = data) #company is a new variable that will be sent through to the HTML template which is equal to the list of data it's loading


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return "<h1>" + member["name"]+ "</h1>"


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # when submitting change it to FALSE
    ) 