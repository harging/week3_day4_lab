import datetime
from models.event import *

event1 = Event(datetime.date(2021, 12, 3), "Lady Gaga", 10000, "Edinburgh", "Lady Gaga concert", False)
event2 = Event(datetime.date(2021, 12, 4), "Suede", 1000, "Edinburgh", "Suede concert", False)
event3 = Event(datetime.date(2021, 12, 22), "Elton John", 100000, "Glasgow", "Elton John charity concert", True)

event_list = [event1, event2, event3]

def add_new_event(event):
    event_list.append(event)

# def delete_event(event):
#     event_list.remove(event)