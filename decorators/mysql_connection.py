import mysql.connector

def get_mysql_connection():
    connection = mysql.connector.connect(
        user='your_username',
        password='your_password',
        host='localhost',  # tai vastaava osoite
        database='your_dbname'
    )
    return connection
