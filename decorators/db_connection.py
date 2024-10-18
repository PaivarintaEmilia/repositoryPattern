from decorators.mysql_connection import MysqlConnection
from decorators.postgres_connections import PostgresConnection


class DbBaseDecoration:

    @staticmethod
    def get_connection(db_type):
        if db_type == 'mysql':
            return MysqlConnection().get_mysql_connection()
        elif db_type == 'postgres':
            return PostgresConnection().get_postgres_connection()
        else:
            raise ValueError("Väärä valittu tietokantatyyppi. Valitse joko postgres tai mysql.")
