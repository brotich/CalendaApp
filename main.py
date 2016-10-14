from clint.textui import puts, indent
from app.Calendar import Calendar
from pyfiglet import Figlet
from models.event import Event

class Main(object):

    def print_usage(self):
        f = Figlet(font='slant')
        puts(f.renderText('Calender App'))

    def run_app(self):
        self.print_usage()

        while True:
            with indent(4):
                puts('Menu')
                with indent(4):
                    puts('1. Add new Event to calender')
                    puts('2. List Events by date')
                    puts('3. Exit')
                    puts("\n")

                    

                    while True:
                        i = raw_input("select action: ")
                        if i in [1, 2]:
                            break;


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