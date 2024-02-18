import os
import json 
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__) # creates an instance of this Flask class
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/") # we use the route decorator to tell Flask what URL should trigger the function that follows # "/" is the root directory when we try to browse it Flask triggers the index function
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company = data) #company is a new variable that will be sent through to the HTML template which is equal to the list of data it's loading


@app.route("/about/<member_name>") # the angle brackets will pass in data from the URL path, into our view below adn the URL path is <a href="/about/{{ member.url }}"> so the value from member.url is passed into the member_name variable
def about_member(member_name):  # this takes member_name from above as an argument
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj # this is the member obj from line 24
    return render_template("member.html", member=member)
# the first member is the variable name being passed through into our html file and thats why we can do member.name in the member.html file and the second member is the member object we created above


@app.route("/contact" , methods=["GET", "POST"]) #this has to be called methods
def contact():
    if request.method == "POST":
        # print(request.form.get("name")) # if there isnt a value that the user has input it will return none
        # print(request.form["email"]) # if there isnt a value that the user has input it will raise an exception
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
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