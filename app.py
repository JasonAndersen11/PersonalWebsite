from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
    
@app.route("/projects")
def projects():
    return render_template("projects.html")
    
@app.route("/javajam")
def java():
    return render_template("javajam.css")