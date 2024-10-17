from decorators.postgres_connections import get_postgres_connection
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
        users = []
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            result = cursor.fetchall()
            for user in result:
                users.append(models.User(user[0], user[1], user[2], user[3]))

            return users
