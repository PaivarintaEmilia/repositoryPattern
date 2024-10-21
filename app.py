from flask import Flask
from flask.cli import load_dotenv

from controllers import users_controller, products_controller

app = Flask(__name__)

#USERS
# Hae kaikki käyttäjät
@app.route('/api/users/<db_type>', methods=['GET'])
def get_users(db_type):
    return users_controller.get_all_users(db_type)


# Hea käyttäjä id:llä
@app.route('/api/users/<db_type>/<user_id>', methods=['GET'])
def get_user_by_id(db_type, user_id):
    return users_controller.get_user_by_id(db_type, user_id)

# Käyttäjän lisääminen
@app.route('/api/users/<db_type>', methods=['POST'])
def create_user(db_type):
    return users_controller.create_user(db_type)

# Käyttäjän poistaminen
@app.route('/api/users/<db_type>/<user_id>', methods=['DELETE'])
def delete_user_by_id(db_type, user_id):
    return users_controller.delete_user(db_type, user_id)

# Käyttäjän muokkaaminen
@app.route('/api/users/<db_type>/<user_id>', methods=['PATCH'])
def update_user_by_id(db_type, user_id):
    return users_controller.update_user(db_type, user_id)


#PRODUCTS
# Hae kaikki tuotteet
@app.route('/api/products/<db_type>', methods=['GET'])
def get_all_products(db_type):
    return products_controller.get_all_products(db_type)


# Hea käyttäjä id:llä
@app.route('/api/products/<db_type>/<product_id>', methods=['GET'])
def get_product_by_id(db_type, product_id):
    return products_controller.get_product_by_id(db_type, product_id)

# Käyttäjän lisääminen
@app.route('/api/products/<db_type>', methods=['POST'])
def create_product(db_type):
    return products_controller.create_product(db_type)

# Käyttäjän poistaminen
@app.route('/api/products/<db_type>/<product_id>', methods=['DELETE'])
def delete_product_by_id(db_type, product_id):
    return products_controller.delete_product_by_id(db_type, product_id)

# Käyttäjän muokkaaminen
@app.route('/api/products/<db_type>/<product_id>', methods=['PATCH'])
def update_product(db_type, product_id):
    return products_controller.update_product(db_type, product_id)


if __name__ == '__main__':
    load_dotenv()
    app.run()
