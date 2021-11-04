from flask import render_template, request, redirect
from app import app
from models.event_list import event_list
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Events', event_list=event_list)


@app.route('/events', methods=['POST'])