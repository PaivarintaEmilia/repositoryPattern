from flask import jsonify
from repositories.repository import Repository


def get_all_users(db_type):

    # Valitaanko tässä kumpaa tietokantaa käytetään?
    # db_type = 'postgres'  # tai 'mysql' tarpeen mukaan

    # Repositoryn instanssi
    repo = Repository(db_type)
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