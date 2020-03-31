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

@app.route("/create", methods=["GET", "POST"])
def create():
    name = request.form['name']
    tiles = generate_tiles()

    with open("boards.bog", "rb") as board_file:
        try:
            boards = pickle.load(board_file)
        except(pickle.UnpicklingError):  # First time?
            boards = dict()

    boards[name] = tiles

    with open("boards.bog", "wb") as board_file:
        pickle.dump(boards, board_file)

    return render_template("game.html", tiles=tiles)

@app.route("/join", methods=["GET", "POST"])
def join():
    return render_template("join.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    with open("boards.bog", "rb") as board_file:
        tiles = pickle.load(board_file)[request.form['name']]
    return render_template("game.html", tiles=tiles)
