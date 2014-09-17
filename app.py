from flask import Flask,render_template


app = Flask(__name__)

@app.route("/Zip")
def Zip():
    return render_template("Zip.html")

@app.route("/Cuisine")
def Cuisine():
    return render_template("Cuisine.html")


def get_file(filename):
    l=[]
    for line in open(filename).readlines():
        l.append(line.strip().split(','))
    return l
    inspectiondata = get_file('Results_Without_violations.csv')
    for list in inspectiondata:
        print list

def print_grades():
    for list in inspectiondata: 
        if list[1]=='QUEENS':
            grade=int(list[8])
            print grade
    
