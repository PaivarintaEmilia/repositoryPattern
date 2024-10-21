class User:
    def __init__(self, username, firstname, lastname, _id=None):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    # Data to json. Ymmärtääkseni tämä kuuluu tänne.
    def to_json(self):
        return {'id': self.id, 'username': self.username, 'firstname': self.firstname, 'lastname': self.lastname}