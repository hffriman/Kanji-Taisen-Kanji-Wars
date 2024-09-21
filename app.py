from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<div><h1>漢字対戦</h1> <h2>kanji wars<h2> <h3>Henry Friman 2024</h3></div>"