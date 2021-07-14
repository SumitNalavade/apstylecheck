from flask import Flask, render_template, request
from gingerit.gingerit import GingerIt

grammarParser = GingerIt()

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/docs")
def docs_page():
    return render_template("docs.html")


@app.route('/send', methods=['POST'])
def send():
    if(request.method == 'POST'):
        usertext = request.form['usertext']

        grammarCorrections = {}

        for i in grammarParser.parse(usertext)["corrections"]:
            grammarCorrections[i["text"]] = i["correct"]

        return render_template("index.html", usertext=usertext, grammarCorrections=grammarCorrections)
