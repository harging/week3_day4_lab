from flask import render_template, request, redirect
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('rules.html', title='ROCK PAPER SCISSORS')

@app.route('/<choice1>/<choice2>')
def play(choice1, choice2):
    player1 = Player("Player one", choice1)
    player2 = Player("Player two", choice2)
    game = Game()

    winner = game.play_game(player1, player2)
    
    return render_template('play.html', title='ROCK PAPER SCISSORS', player1=player1, player2=player2, winner=winner)