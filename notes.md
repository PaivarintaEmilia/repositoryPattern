# Selitys tiedonkulusta ohjelmassa ja eri osien tarkoitukset


1. Käyttäjä kirjoittaa insomniaan tai postmaniin seuraavan GET-requestin, jonka tarkoituksena on saada kaikki data users-taulusta

- postgres määrittää mitä tietokantaa käyttäjä haluaa käyttää, kun vaihtoehtoina ovat postgres ja mysql

```
http://127.0.0.1:5000/api/users/postgres
```


2. App.py

- Täällä on määritetty route ja get_users-metodilla tehty yhdistys controllerin get_all_users-metodiin 
- Parametrinä on db_type parametri mikä on määritetty routessa (postgres)


```
from flask.cli import load_dotenv  
from controllers import users_controller  
  
app = Flask(__name__)  
  
@app.route('/api/users/<db_type>', methods=['GET'])  
def get_users(db_type):  
    return users_controller.get_all_users(db_type)  
  
  
if __name__ == '__main__':  
    load_dotenv()  
    app.run()
```


3. Controller

- controlleri on vain tietojen välittämiseen
- täällä haetaan myös tietokantaan yhdistämiseen liittyvä data decorator-kansiosta db_connection.py-tiedostosta
	- db_connection.py tiedostossa periytymisen avulla saadaan haluttu data joko mysql yhdistämistä tai postgres yhdistämistä varten
- Täällä tehdään myös repositorysta instanssi, jotta saadaan tietokannasta haluttu data
	- kutsutaan repo-instanssin get_all-metodia ja muutetaan data haluttuun json muotoon, jotta se voidaan lähettää takaisin käyttäjälle 


```
from flask import jsonify  
from decorators import db_connection  
from repositories.repository import Repository  
  
  
def get_all_users(db_type):  
  
    # Haetaan yhteys oikeaan tietokantaan. Tarvitaan vain tähän tarkoitukseen niin ei tehdä instanssia.  
    connection = db_connection.get_connection(db_type)  
  
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
```



3.1. Databasen yhdistäminen decoration-kansiosta


DbBaseDecoration-class

```
from decorators.mysql_connection import MysqlConnection  
from decorators.postgres_connections import PostgresConnection  
  
  
class DbBaseDecoration:  
  
    def get_connection(self, db_type):  
        if db_type == 'mysql':  
            return MysqlConnection().get_mysql_connection()  
        elif db_type == 'postgres':  
            return PostgresConnection().get_postgres_connection()  
        else:  
            raise ValueError("Väärä valittu tietokantatyyppi. Valitse joko postgres tai mysql.")
```


mysql_connection-class

```
import mysql.connector  
from decorators.db_connection import DbBaseDecoration  
  
  
class MysqlConnection(DbBaseDecoration):  
    def get_mysql_connection(self):  
        connection = mysql.connector.connect(  
            user='your_username',  
            password='your_password',  
            host='localhost',  # tai vastaava osoite  
            database='your_dbname'  
        )  
        return connection
```


postgres_connection-class:

```
import psycopg2  
import os  
from flask.cli import load_dotenv  
from decorators.db_connection import DbBaseDecoration  
  
# Lataa ympäristömuuttujat .env-tiedostosta  
load_dotenv()  
  
class PostgresConnection(DbBaseDecoration):  
    def get_postgres_connection(self):  
        connection = psycopg2.connect(  
            dbname=os.getenv('POSTGRES_DATABASE'),  
            user=os.getenv('POSTGRES_USER'),  
            password=os.getenv('POSTGRES_PASSWORD'),  
            host=os.getenv('POSTGRES_HOST'),  
            port=os.getenv('POSTGRES_PORT')  
        )  
        return connection
```


3.2.  Repository

- Täällä tehdään vain databasesta tiedon haku 


```
import models  
  
class Repository:  
  
    def __init__(self, connection):  
        self.connection = connection  
  
    def get_all(self):  
        users = []  
        with self.connection.cursor() as cursor:  
            cursor.execute('SELECT * FROM users')  
            result = cursor.fetchall()  
            for user in result:  
                users.append(models.User(user[0], user[1], user[2], user[3]))  
  
            return users
```


3.2.1. Modeli

- Repository saa tiedon minkälaisessa muodossa datan kuuluu olla

```
class User:  
    def __init__(self, username, firstname, lastname, _id=None):  
        self.id = _id  
        self.username = username  
        self.firstname = firstname  
        self.lastname = lastname
```