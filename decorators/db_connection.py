from decorators.postgres_connections import get_postgres_connection
from decorators.mysql_connection import get_mysql_connection

def get_connection(db_type):
    if db_type == 'postgres':
        return get_postgres_connection()
    elif db_type == 'mysql':
        return get_mysql_connection()
    else:
        raise ValueError("Invalid database type. Choose 'postgres' or 'mysql'.")
