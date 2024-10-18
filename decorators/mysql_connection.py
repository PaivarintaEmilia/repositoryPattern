import mysql.connector


class MysqlConnection:

    def __init__(self):
        from decorators.db_connection import DbBaseDecoration
        self.db_decoration = DbBaseDecoration()

    def get_mysql_connection(self):
        connection = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='localhost',  # tai vastaava osoite
            database='your_dbname'
        )
        return connection
