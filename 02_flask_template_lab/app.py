from flask import Flask
import flask

app = flask(__name__)

from controllers import controller

if __name__ == "__main__":
    app.run(debug=True)