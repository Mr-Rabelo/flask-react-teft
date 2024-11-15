from flask import *

app = Flask("__main__")

@app.route("/")
def index():
    return render_template("index.html", meuNome="Teste")

app.run()