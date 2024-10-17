
## Model

`model.py`

- sisältää tietokannan mallit (user ja product 2. teht.)
- id tulee olla optional, koska add ja update -metodeissa id saadaan vasta tietokannan kyselyn suorittamisen jälkeen 

```
class User:  
    def __init__(self, username, firstname, lastname, _id=None):  
        self.id = _id  
        self.username = username  
        self.firstname = firstname  
        self.lastname = lastname  
  
  
class Product:  
    def __init__(self, name, description, _id=None):  
        self.id = _id  
        self.name = name  
        self.description = description
```


## Repository

`repositories-package/repository.py`

- hoitaa tietokantaoperaatiot, eli sisältää metodit datan hakemiseen ja käsittelyyn tietokannassa
- Sisältää luokan, jota kautta tehdään yhdsitäminen tietokantaan
- Sisältää CRUD-metodit

```
from decorators.postgres_connection import get_postgres_connection  
from decorators.mysql_connection import get_mysql_connection  
import models  
  
class Repository:  
    def __init__(self, db_type):  
        self.db_type = db_type  
        self.connection = self.get_connection()  
  
    def get_connection(self):  
        if self.db_type == 'postgres':  
            return get_postgres_connection()  
        elif self.db_type == 'mysql':  
            return get_mysql_connection()  
        else:  
            raise ValueError("Invalid database type. Choose 'postgres' or 'mysql'.")  
  
  
    def get_all(self):  
        with self.con.cursor() as cur:  
            cur.execute('SELECT * FROM users')  
            result = cur.fetchall()  
            users = []  
            for user in result:  
                users.append(models.User(user[0], user[1], user[2], user[3]))  
  
            return users
```


## Controllers


- Controlleri käsittelee vain ja ainoastaan req & res


```
from flask import jsonify  
from repositories.repository import Repository  
  
def get_all_users(db_type):  
  
    # Valitaanko tässä kumpaa tietokantaa käytetään?  
    # db_type = 'postgres'  # tai 'mysql' tarpeen mukaan  
    # Repositoryn instanssi    repo = Repository(db_type)  
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
```


## App.py

- rakennetaan routet

```
from dotenv import load_dotenv  
from flask import Flask  
  
from controllers import users  
  
app = Flask(__name__)  
  
  
@app.route('/api/users/<db_type>', methods=['GET'])  
def get_users(db_type):  
    return users.get_all_users(db_type)  

  
if __name__ == '__main__':  
    load_dotenv()  
    app.run()
```



## Tiedostos databasen yhdistämistä varten

- decoration package `decorations`

`mysql_connection.py`

```
import mysql.connector  
  
def get_mysql_connection():  
    connection = mysql.connector.connect(  
        user='your_username',  
        password='your_password',  
        host='localhost',  # tai vastaava osoite  
        database='your_dbname'  
    )  
    return connection
```


``postgres_connection.py`

```
import psycopg2  
import os  
from dotenv import load_dotenv  
  
# Lataa ympäristömuuttujat .env-tiedostosta  
load_dotenv()  
  
  
def get_postgres_connection():  
    connection = psycopg2.connect(  
        dbname=os.getenv('POSTGRES_DATABASE'),  
        user=os.getenv('POSTGRES_USER'),  
        password=os.getenv('POSTGRES_PASSWORD'),  
        host=os.getenv('POSTGRES_HOST'),  # tai vastaava osoite  
        port=os.getenv('POSTGRES_PORT')  # Oletusportti PostgreSQL:lle  
    )  
    return connection
```


## Tiedon kulku ohjelmassa


- **Initialization**: When the application starts, it sets up the Flask framework and loads environment variables.
    
- **Routing**: The application has a single route for fetching users, which accepts a database type as a URL parameter.
    
- **Controller Logic**: The controller creates a `Repository` instance with the specified database type and calls the `get_all` method to retrieve users.
    
- **Database Interaction**: The repository manages database connections, executes queries, and transforms the results into `User` model instances.
    
- **Response**: The controller formats the user data into JSON and returns it to the client.