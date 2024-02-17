import os
from flask import Flask

app = Flask(__name__) # creates an instance of this Flask class

@app.route("/") # we use the route decorator to tell Flask what URL should trigger the function that follows # "/" is the root directory when we try to browse it Flask triggers the index function
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True # when submitting change it to FALSE
    )