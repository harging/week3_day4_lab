import datetime
from models.event import *

event1 = Event(datetime.date(2021, 12, 3), "Lady Gaga", 10000, "Edinburgh", "Lady Gaga concert")
event2 = Event(datetime.date(2021, 12, 4), "Suede", 1000, "Edinburgh", "Suede concert")
event3 = Event(datetime.date(2021, 12, 22), "Elton John", 100000, "Glasgow", "Elton John charity concert")

event_list = [event1, event2, event3]

def add_new_event(event):
    tasks.append(event)