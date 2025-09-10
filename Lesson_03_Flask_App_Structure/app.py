from flask import Flask

app = Flask(__name__)

@app.route("/") # / Front page 
def home():
    return "Home Page!"

@app.route("/about")
def about():
    # return "About Page!"
    return """<h1>Welcome</h1>
                <p> This is my first website </p>
    """

app.run(debug=True)