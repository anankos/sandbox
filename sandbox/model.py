import datetime

class Item():

    def __init__(self, title, description = None, created = datetime.datetime.now()):
        self.title = title
        self.description = description
        self.created = created
        self.planned = None
        self.due = None
        self.closed = None
        self.parent = None
        self.items = []

class Goal():

    def __init__(self, title, description = None, motivation = None, created = datetime.datetime.now()):
        self.title = title
        self.description = description
        self.motivation = motivation
        self.created = created
        self.closed = None

        self.items = []
