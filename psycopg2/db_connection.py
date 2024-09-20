import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname = 'sql_alchemy_learning',
            user='postgres',
            password = 'pass',
            host='localhost',
            port='5432'
        )
        return conn
    except Exception as e:
        print(e)