import requests
from flask import Flask, render_template


from helpers_ import gameList

app = Flask(__name__)

@app.route("/", )
def index():
    #games = gameList()
    #print(games)
    return render_template("index.html")
    
@app.route("/ps4")
def ps4():
    return render_template("ps4.html")
    
@app.route("/xbox")
def xbox():
    return render_template("xbox.html")
    
@app.route("/switch")
def switch():
    return render_template("switch.html")
    
@app.route("/steam")
def steam():
    return render_template("steam.html")