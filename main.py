from clint.textui import puts, indent
from app.Calendar import Calendar
from pyfiglet import Figlet
from models.event import Event
import datetime
import sys
from util.util import bcolors


class Main(object):

    def __init__(self):
        self.calender = Calendar()

    def print_usage(self):
        puts(bcolors.OKGREEN)
        f = Figlet(font='slant')
        puts(f.renderText('Calender App'))
        puts(bcolors.ENDC)

    def print_event_item(self, event):
        with indent(8):
            puts(event.event_name)
            with indent(4):
                puts("=> " + event.event_description)
            puts("-" * 60)

    def print_day_events(self, events):
        with indent(4):
            puts("Date: " + events[0].event_date)

            for event in events:
                self.print_event_item(event)

    def parse_date(self):
        event_date = None
        while True:
            puts(bcolors.BOLD)
            event_date = raw_input("Date [YYYY-MM-DD]: ").strip()
            if event_date == "":
                puts(bcolors.UNDERLINE + bcolors.WARNING +
                     "The Date is empty" +
                     bcolors.ENDC)
                continue
            try:
                datetime.datetime.strptime(event_date, '%Y-%m-%d')
                break
            except ValueError:
                puts(bcolors.UNDERLINE + bcolors.WARNING +
                     "Incorrect date format, should be YYYY-MM-DD" +
                     bcolors.ENDC)
                continue
        puts(bcolors.ENDC)

        return event_date

    def create_event(self):
        print ('Add New Calendar Item')
        with indent(4):
            event_date = self.parse_date()

            event_name = None
            while True:

                event_name = raw_input("Event Title: ")
                if event_name == "":
                    continue
                else:
                    break

            event_description = None
            while True:
                event_description = raw_input("Event Description: ")
                if event_description == "":
                    continue
                else:
                    break
            event = Event(event_date, event_name, event_description)

        return event

    def run_app(self):
        self.print_usage()

        while True:
            with indent(4):
                puts(bcolors.BOLD)
                puts("MENU")
                puts(bcolors.ENDC)

                with indent(4):
                    puts('1. Add new Event to calender')
                    puts('2. List Events by date')
                    puts('3. Get Latest Event')
                    puts('4. Exit')
                    puts("\n")

                    action = None

                    while True:
                        try:
                            puts(bcolors.BOLD)
                            action = raw_input("select action to continue: ")
                            action = int(action.strip())
                            puts(bcolors.ENDC)
                            if action in [1, 2, 3, 4]:
                                break
                        except ValueError:
                            print (bcolors.UNDERLINE + bcolors.WARNING +
                                   "Error: Invalid Menu item" +
                                   bcolors.ENDC)

                    puts("=" * 80)
                    if action == 1:
                        event = self.create_event()
                        self.calender.add_new_event(event)
                    elif action == 2:
                            date = self.parse_date()
                            data = self.calender.search_event(date)
                            if data is not None:
                                self.print_day_events(data)
                            else:
                                with indent(4):
                                    puts("Date: " + date)
                                    puts("No items scheduled for Date")
                    elif action == 3:
                            latest_event = self.calender.get_last_item()
                            self.print_day_events([latest_event])
                    elif action == 4:
                        with indent(4):
                            puts('Good Bye')
                            sys.exit(0)

                    print ("=" * 80)


main = Main()
main.run_app()
