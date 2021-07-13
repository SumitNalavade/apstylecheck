from flask import Flask, render_template, request
from gingerit.gingerit import GingerIt

parser = GingerIt()

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/docs")
def docs_page():
    return render_template("docs.html")