
from models.event import Event

class Calendar:

    def __init__(self):
        self.calendar = {}


    def add_new_event(self, event):
        """

        """

        if not isinstance(event, Event):
            raise TypeError("Expected parameter event to be Event class")

        event_date = event.event_date

        if event_date in self.calendar.keys():
            self.calendar[event_date].append(event)
        else:
            self.calendar[event_date] = [event]

        print self.calendar

    def search_event(self, event_date):
        """

        """
        
        if event_date in self.__calendar.keys():
            return self.__calendar[event_date]
        else:
            return None
