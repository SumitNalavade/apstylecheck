from flask import Flask, render_template, request
from gingerit.gingerit import GingerIt
import apstylecheck

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

        grammarCorrections = apstylecheck.check(usertext)

        try:
            for i in grammarParser.parse(usertext)["corrections"]:
                grammarCorrections[i["text"]] = i["correct"]
        except KeyError:
            sentences = usertext.split(".")

            for i in sentences:
                for j in grammarParser.parse(i)["corrections"]:
                    grammarCorrections[j["text"]] = j["correct"]

        print(grammarCorrections.keys())

        return render_template("index.html", usertext=usertext, grammarCorrections=grammarCorrections)