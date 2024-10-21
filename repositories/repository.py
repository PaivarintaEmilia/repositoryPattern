
import models

class Repository:

    def __init__(self, connection):
        self.connection = connection

    # GET
    def get_all(self):
        users = []
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            result = cursor.fetchall()
            for user in result:
                users.append(models.User(user[0], user[1], user[2], user[3]))

            print("Get user luokan instanssi? ", users)

            return users

    # GET BY ID
    def get_user_by_id(self, user_id):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            result = cursor.fetchone()

            # Luodaan luokan instanssi
            if result:
                print("Get user by id luokan instanssi? ", models.User(result[0], result[1], result[2], result[3]))
                return models.User(result[0], result[1], result[2], result[3])
            else:
                return None


    # CREATE HUOM TÄSSÄ KYSELY EI OLE SAMA MYSQLILLE, JOTEN PITÄÄ MUOKATA JOKO KYSELY SAMANLAISEKSI TAI SITTEN KEKSI JOTAIN MUUTA
    # vOIDAANKO ESIM ID HAKEMINEN JA KYSELY LAITTAA IF LAUSEKKEESEEN? ONKO JÄRKEÄ VAI MENEEKÖ VAIKEAKSI?
    def create_user(self, user):
        with self.connection.cursor() as cursor:
            print("repo/user.username", user.username)
            print("repo/user.username", type(user.username))
            print("repo/user-firstname", user.firstname)
            print("repo/user.lastname", user.lastname)
            cursor.execute('INSERT INTO users (username, firstname, lastname) VALUES (%s, %s, %s) RETURNING id', (user.username, user.firstname, user.lastname))

            self.connection.commit()


            # Haetaan lisätyn käyttäjän tiedot
            user_id = cursor.fetchone()[0]
            print("repo/user_id", user_id)

            if user_id > 0:
                # Haetaan lisätyn käyttäjän tiedot
                cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))  # Muista että tämä taas tuple!!!!
                new_user = cursor.fetchone()

                if new_user:
                    print("Create user repo/instanssi ", models.User(new_user[0], new_user[1], new_user[2], new_user[3]))
                    return models.User(new_user[0], new_user[1], new_user[2], new_user[3])
            else:
                return None


    # PUT
    def update_user(self, user, user_id):
        with self.connection.cursor() as cursor:
            print("repo/user.username", user.username)
            print("repo/user.username", type(user.username))
            print("repo/user-firstname", user.firstname)
            print("repo/user.lastname", user.lastname)
            cursor.execute('UPDATE users SET username=%s, firstname=%s, lastname=%s WHERE id=%s RETURNING id', (user.username, user.firstname, user.lastname, user_id))

            self.connection.commit()


            # Haetaan lisätyn käyttäjän tiedot
            # user_id = cursor.fetchone()[0]
            # print("repo/user_id", user_id)


            # Haetaan päivitetyn käyttäjän tiedot
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            updated_user = cursor.fetchone()

            if updated_user:
                print("Update user repo/instanssi ", models.User(updated_user[0], updated_user[1], updated_user[2], updated_user[3]))
                return models.User(updated_user[0], updated_user[1], updated_user[2], updated_user[3])
            else:
                return None



    # DELETE
    def delete_user_by_id(self, selectedId):

        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM users WHERE id = %s', (selectedId,))

            # Kommitoidaan
            self.connection.commit()

            return "Käyttäjä poistettu"






