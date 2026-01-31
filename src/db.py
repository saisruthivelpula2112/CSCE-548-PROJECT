import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="csce548_project1",
        user="postgres",
        password="Ram@2342",
        host="localhost",
        port="5432"
    )
