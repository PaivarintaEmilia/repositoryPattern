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