from flask import *

app = Flask("__main__")

@app.route("/")
def index():
    return render_template("index.html",flask_token="italo")

@app.route("/entrada1", methods = ["GET", "POST"])
def entradas():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        print(f"{email} com a senha {senha}")
        return redirect("/")
    else:
        return render_template("entrada1.html")
    
@app.route("/entrada2/<testeGet>", methods = ["GET", "POST"])
def entrada2(testeGet):
    if request.method == "GET":
        email = testeGet
        print(f"email{email}")
        return redirect("/")
    else:
        return render_template("entrada2.html")

app.run()