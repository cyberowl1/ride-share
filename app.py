from cs50 import SQL
from flask import Flask, render_template,request

app = Flask(__name__)
db=SQL("sqlite:///ride.db")



@app.route ("/")
def index():
    return render_template("index.html")

@app.route("/createride")
def ridecreate():
    return render_template("cride.html")

@app.route("/submit", methods=["POST"])
def submit():
     fname= request.form.get("fname")
     phone= request.form.get("phone")
     sourceid= request.form.get("sourceid")
     destid= request.form.get("destid")
     seats= request.form.get("seats")
     if not fname or not phone or not sourceid or not destid or not seats:
         return render_template("error.html",msg="you are missing something")
     db.execute("INSERT INTO rideshare (name,source,dest,seats,phone) VALUES(?,?,?,?,?)", fname,sourceid,destid,seats,phone )
     return render_template("submit.html",fname=fname,sourceid=sourceid,destid=destid,seats=seats)

@app.route("/searchride")
def ridesearch():
    rows=db.execute("select * from rideshare")
    return render_template("sride.html",rows=rows)