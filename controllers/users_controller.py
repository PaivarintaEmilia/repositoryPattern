from flask import jsonify

from decorators import db_connection
from repositories.repository import Repository


def get_all_users(db_type):

    # täällä avataan yhteys db:seen
    db_connection.get_connection(db_type)

    # Repositoryn instanssi
    repo = Repository()
    # Kutsutaan repo instanssin get_all-metodia
    users = repo.get_all()
    users_json = []
    for user in users:
        users_json.append({
            'id': user.id,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
        })
    return jsonify(users_json)