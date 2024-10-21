from flask import jsonify, request
from decorators.db_connection import DbBaseDecoration
from models import User, Product
from repositories.repository_products import ProductsRepository


# Luodaan funktio, jolla hoidetaan databasen yhteys ja repo-instanssin luominen, jotta näitä ei tarvitse joka kerralla tehdä uudestaan
def get_repository(db_type):
    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.
    connection = DbBaseDecoration.get_connection(db_type)
    # Palautetaan Repositoryn instanssi
    return ProductsRepository(connection)


def get_all_products(db_type):
    repo = get_repository(db_type)

    # Kutsutaan repo instanssin get_all_products-metodia ja haetaan kaikki käyttäjät
    users = repo.get_all_products()
    products_json = []
    for product in users:
        products_json.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
        })
    return jsonify(products_json)


# Haetaan product id:llä
def get_product_by_id(db_type, product_id):
    repo = get_repository(db_type)

    # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
    # ONKO TARPEELLISTA TALLENTAA ARRAYHYN?
    product = repo.get_product_by_id(product_id)

    product_to_json = product.to_json()

    print("User/to_json test/controller ", product_to_json)

    if product_to_json:
        return jsonify(product_to_json)
    else:
        return jsonify({'error productById/controller/': 'Product not found'}), 404


# Luodaan uusi tuote
def create_product(db_type):
    repo = get_repository(db_type)

    # Haetaan data api requestin bodyssa
    new_data = request.get_json()

    print("Controller new_data  ", new_data)
    print("Controller new_data ", type(new_data))

    # Luodaan Product-classin instanssi dictionaryn new_data tiedoista. Tämä data lähtee eteenpäin repolle
    product = Product(new_data['name'], new_data['description'])

    print("Controller / product ", product)
    print("Controller / product ", type(product))  # Luokan instanssi

    # Kutsutaan repo instanssin metodia
    new_product = repo.create_product(product)

    print("Controller new_user ", new_product)

    return jsonify(new_product.to_json()), 201


# Poistetaan käyttäjä
def delete_product_by_id(db_type, product_id):
    repo = get_repository(db_type)

    # Kutsutaan repo instanssin get_user_by_id-metodia ja haetaan kaikki käyttäjät
    # ONKO TARPEELLISTA TALLENTAA ARRAYHYN?
    deleted_product = repo.delete_product_by_id(product_id)

    print("Deleted deleted_product/controller: ", deleted_product)
    print("Deleted deleted_product/controller: ", type(deleted_product))

    if deleted_product:
        return jsonify(deleted_product)
    else:
        return jsonify({'error productDelete/controller/': 'Product not found'}), 404


# Päivitetään käyttäjä
def update_product(db_type, product_id):

    # Repon instanssi
    repo = get_repository(db_type)

    # Kyselyssä saatu data
    update_data = request.get_json()

    print("Controller new_data ", update_data)
    print("Controller new_data ", type(update_data))

    # Luodaan User-classin instanssi dictionaryn new_data tiedoista. Tämä data lähtee eteenpäin repolle
    updated_product_data = User(update_data['username'], update_data['firstname'], update_data['lastname'])

    print("Controller / user ", updated_product_data)
    print("Controller / user ", type(updated_product_data))  # Luokan instanssi

    # Kutsutaan repo instanssin metodia
    updated_product = repo.update_product(updated_product_data, product_id)

    print("Controller updated_product ", updated_product)

    return jsonify(updated_product.to_json()), 201

