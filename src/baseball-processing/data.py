__all__ = ["get_connection"]

def get_connection():
    conn = psycopg2.connect(
        dbname="statcast",
        user="postgres",
        password="jamin",
        host="localhost",
        port="5432"
    )
    return conn