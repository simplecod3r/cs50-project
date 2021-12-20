import requests
from flask import Flask, render_template


from helpers_ import gameList

app = Flask(__name__)

@app.route("/", )
def index():
    #games = gameList()
    #print(games)
    return render_template("index.html")
        
@app.route("/steam")
def steam():
    return render_template("steam.html")