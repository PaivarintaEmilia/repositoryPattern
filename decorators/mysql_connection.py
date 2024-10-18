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
