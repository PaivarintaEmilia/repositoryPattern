from dotenv import load_dotenv
from flask import Flask

from controllers import users_controller

app = Flask(__name__)



@app.route('/api/users/<db_type>', methods=['GET'])
def get_users(db_type):
    return users_controller.get_all_users(db_type)



if __name__ == '__main__':
    load_dotenv()
    app.run()