from flask import render_template, request
from app import app
from app.generate import generate_tiles
import pickle

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
    tiles = generate_tiles()

    with open("boards.bog", "rb") as board_file:
        boards = pickle.load(board_file)

    boards[name] = tiles

    with open("boards.bog", "wb") as board_file:
        pickle.dump(boards, board_file)

    return render_template("game.html", tiles=tiles)

@app.route("/join")
def join():
    with open("boards.bog", "rb") as board_file:
        tiles = pickle.load(boards)[request.form['name']]
    return render_template("game.html", tiles=tiles)
