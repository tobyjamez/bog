from flask import render_template, request
from app import app
from app.generate import generate_tiles

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    tiles = generate_tiles()
    return render_template("game.html", tiles=tiles)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create")
def create():
    name = request.form['name']
    return render_template("name.html")

@app.route("/join")
def join():
    return render_template("join.html")
