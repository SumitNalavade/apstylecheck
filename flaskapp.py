from flask import Flask, render_template, request
from gingerit.gingerit import GingerIt

parser = GingerIt()

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/documentation")
def docs_page():
    return render_template("documentation.html")
