
import models

class Repository:

    def get_all(self):
        users = []
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            result = cursor.fetchall()
            for user in result:
                users.append(models.User(user[0], user[1], user[2], user[3]))

            return users
