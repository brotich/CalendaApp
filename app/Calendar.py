
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

    def search_event(self, event_date):
        """

        """
        
        if event_date in self.calendar.keys():
            return self.calendar[event_date]
        else:
            return None

    def get_last_item(self):
        latest_date = sorted(self.calendar.keys()).pop()

        return self.calendar[latest_date].pop()

