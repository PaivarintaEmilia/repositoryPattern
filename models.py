class User:
    def __init__(self, username, firstname, lastname, _id=None):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    # Data to json. Ymmärtääkseni tämä kuuluu tänne.
    def to_json(self):
        return {'id': self.id, 'username': self.username, 'firstname': self.firstname, 'lastname': self.lastname}


class Product:
    def __init__(self, name, description, _id=None):
        self.id = _id
        self.name = name
        self.description = description


    def to_json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}