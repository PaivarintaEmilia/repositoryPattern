from flask import jsonify, request

from decorators.db_connection import DbBaseDecoration
from models import User
from repositories.repository import Repository


# Luodaan funktio, jolla hoidetaan databasen yhteys ja repo-instanssin luominen, jotta näitä ei tarvitse joka kerralla tehdä uudestaan
def get_repository(db_type):
    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.
    connection = DbBaseDecoration.get_connection(db_type)
    # Palautetaan Repositoryn instanssi
    return Repository(connection)


def get_all_users(db_type):
    repo = get_repository(db_type)

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


# Haetaan käyttäjä id:llä
def get_user_by_id(db_type, user_id):
    repo = get_repository(db_type)

    # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
    # ONKO TARPEELLISTA TALLENTAA ARRAYHYN?
    user = repo.get_user_by_id(user_id)

    test = user.to_json()

    print("User/to_json test/controller ", test)

    if test:
        return jsonify(test)
    else:
        return jsonify({'error userById/controller/': 'User not found'}), 404


# Luodaan uusi käyttäjä
def create_user(db_type):
    repo = get_repository(db_type)

    new_data = request.get_json()

    print("Controller new_data (new_data.username) ", new_data)
    print("Controller new_data (new_data.username) ", type(new_data))

    # Luodaan User-classin instanssi dictionaryn new_data tiedoista. Tämä data lähtee eteenpäin repolle
    user = User(new_data['username'], new_data['firstname'], new_data['lastname'])

    print("Controller / user ", user)
    print("Controller / user ", type(user))  # Luokan instanssi

    # Kutsutaan repo instanssin metodia
    new_user = repo.create_user(user)

    print("Controller new_user ", new_user)

    return jsonify(new_user.to_json()), 201


# Poistetaan käyttäjä
def delete_user(db_type, user_id):
    repo = get_repository(db_type)

    # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
    # ONKO TARPEELLISTA TALLENTAA ARRAYHYN?
    deleted_user = repo.delete_user_by_id(user_id)

    print("Deleted user/controller: ", deleted_user)
    print("Deleted user/controller: ", type(deleted_user))

    if deleted_user:
        return jsonify(deleted_user)
    else:
        return jsonify({'error userDelete/controller/': 'User not found'}), 404


# Päivitetään käyttäjä
def update_user(db_type, user_id):

    # Repon instanssi
    repo = get_repository(db_type)

    # Kyselyssä saatu data
    update_data = request.get_json()

    print("Controller new_data (new_data.username) ", update_data)
    print("Controller new_data (new_data.username) ", type(update_data))

    # Luodaan User-classin instanssi dictionaryn new_data tiedoista. Tämä data lähtee eteenpäin repolle
    updated_user_data = User(update_data['username'], update_data['firstname'], update_data['lastname'])

    print("Controller / user ", updated_user_data)
    print("Controller / user ", type(updated_user_data))  # Luokan instanssi

    # Kutsutaan repo instanssin metodia
    updated_user = repo.update_user(updated_user_data, user_id)

    print("Controller new_user ", updated_user)

    return jsonify(updated_user.to_json()), 201

