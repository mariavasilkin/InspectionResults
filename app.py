from flask import Flask,render_template


app = Flask(__name__)

@app.route("/Zip")
def Zip():
    return render_template("Zip.html")

@app.route("/Cuisine")
def Cuisine():
    return render_template("Cuisine.html")
