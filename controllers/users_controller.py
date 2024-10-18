from flask import jsonify

from decorators.db_connection import DbBaseDecoration
from repositories.repository import Repository


def get_all_users(db_type):

    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.
    connection = DbBaseDecoration.get_connection(db_type)

    # Luodaan repositoryn intanssi
    repo = Repository(connection)

    # Kutsutaan repo instanssin get_all-metodia ja haetaan kaikki käyttäjät
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