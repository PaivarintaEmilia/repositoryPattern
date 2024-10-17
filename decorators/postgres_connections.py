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