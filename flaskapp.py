from flask import Flask, render_template, request
from gingerit.gingerit import GingerIt

parser = GingerIt()

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("index.html")


@app.route('/send', methods=['POST'])
def send():
    if(request.method == 'POST'):
        userText = request.form['usertext']

        grammerCorrections = {}

        for i in parser.parse(userText)["corrections"]:
            grammerCorrections[i["text"]] = i["correct"]

        return(render_template('index.html', grammerCorrections=grammerCorrections))
