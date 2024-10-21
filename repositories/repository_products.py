
import models

class ProductsRepository:

    def __init__(self, connection):
        self.connection = connection

    # GET
    def get_all_products(self):
        products = []
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM products')
            result = cursor.fetchall()
            for product in result:
                products.append(models.Product(product[0], product[1], product[2]))

            print("Get user luokan instanssi? ", products)

            return products

    # GET BY ID
    def get_product_by_id(self, product_id):
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM products WHERE id = %s', (product_id,))
            result = cursor.fetchone()

            # Luodaan luokan instanssi
            if result:
                print("Get product by id luokan instanssi? ", models.Product(result[0], result[1], result[2]))
                return models.Product(result[0], result[1], result[2])
            else:
                return None


    # CREATE PRODUCT
    def create_product(self, product):
        with self.connection.cursor() as cursor:
            print("repo/product.username", product.name)
            print("repo/product.username", type(product.description))

            cursor.execute('INSERT INTO products (name, description) VALUES (%s, %s) RETURNING id', (product.name, product.description))

            self.connection.commit()


            # Haetaan lisätyn käyttäjän tiedot
            product_id = cursor.fetchone()[0]
            print("repo/product_id", product_id)

            if product_id > 0:
                # Haetaan lisätyn käyttäjän tiedot
                cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
                new_product = cursor.fetchone()

                if new_product:
                    print("Create product repo/instanssi ", models.User(new_product[0], new_product[1], new_product[2], new_product[3]))
                    return models.User(new_product[0], new_product[1], new_product[2], new_product[3])
            else:
                return None


    # PUT
    def update_product(self, product, product_id):
        with self.connection.cursor() as cursor:
            print("repo/product.name", product.name)
            print("repo/product.name", type(product.name))
            print("repo/product.description", product.description)

            cursor.execute('UPDATE products SET name=%s, description=%s WHERE id=%s RETURNING id', (product.name, product.description, product_id))

            self.connection.commit()


            # Haetaan lisätyn käyttäjän tiedot
            # user_id = cursor.fetchone()[0]
            # print("repo/user_id", user_id)


            # Haetaan päivitetyn käyttäjän tiedot
            cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
            updated_product = cursor.fetchone()

            if updated_product:
                print("Update product repo/instanssi ", models.User(updated_product[0], updated_product[1], updated_product[2], updated_product[3]))
                return models.User(updated_product[0], updated_product[1], updated_product[2], updated_product[3])
            else:
                return None



    # DELETE
    def delete_product_by_id(self, selectedId):

        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM products WHERE id = %s', (selectedId,))

            # Kommitoidaan
            self.connection.commit()

            return "Tuote poistettu"






