from flask import render_template, request, redirect
from app import app
from models.event_list import event_list, add_new_event
from models.event import Event
import datetime

@app.route('/events')
def index():
    return render_template('index.html', title='Events', event_list=event_list)


@app.route('/events', methods=['POST'])
def add_event():
    print(request.form)
    event_title = request.form['name']
    event_date = request.form['date']
    split_date = event_date.split('-')
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    event_capacity = request.form['attendance']
    event_location = request.form['city']
    event_description = request.form['description']
    event_rec = False
    if request.form['recurring'] == "yes":
        event_rec = True
    new_event = Event(date, event_title, event_capacity, event_location, event_description, event_rec)
    add_new_event(new_event)
    return redirect('/events')

@app.route('/events/<index>')
def event(index):
    return render_template("event.html", title="Event", event=event_list[int(index)])

# @app.route('/events/delete/<index>', methods=['POST'])
# def del_event():
    