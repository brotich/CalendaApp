from clint.textui import puts, indent
from app.Calendar import Calendar
from pyfiglet import Figlet
from models.event import Event
import datetime

class Main(object):

    def create_event(self):
        event_date = None
        while True:
            event_date = raw_input("Please Enter the Date the Event YYYY-MM-DD: ")
            if event_date == "":
                continue

            try:
                datetime.datetime.strptime(event_date, '%Y-%m-%d')
                break
            except ValueError:
                print ("Incorrect data format, should be YYYY-MM-DD")
                continue

        event_name = None
        while True:
            event_name = raw_input("Enter the Name of the Event:")
            if event_name == "":
                continue
            else:
                break

        event_description = None
        while True:
            event_description = raw_input("Please Describe the event: ")
            if event_description == "":
                continue
            else:
                break

    def print_usage(self):
        f = Figlet(font='slant')
        puts(f.renderText('Calender App'))

    def run_app(self):
        self.print_usage()
        with indent(4):
            puts('Menu')
            with indent(4):
                puts('1. Add new Event to calender')
                puts('2. List Events by date')

    def print_event_item(self, event):
        with indent(4):
            puts(event.event_name)
            with indent(4):
                puts("desc: " +event.event_description)

    def print_day_events(self, events):
        with indent(4):
            puts("Date: "+events[0].event_date)

            for event in events:
                self.print_event_item(event)
        
d = Main()
d.run_app()

t = Event("04-15-2015", "file github", "works")

d.print_day_events([t])