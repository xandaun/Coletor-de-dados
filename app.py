from flask import Flask, render_template
from scraper import coletar_manchetes_g1

app = Flask(__name__)

@app.route("/")
def index():
    manchetes = coletar_manchetes_g1()
    return render_template("index.html", manchetes=manchetes)

if __name__ == "__main__":
    app.run(debug=True)
