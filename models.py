class User:
    def __init__(self, username, firstname, lastname, _id=None):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname