import psycopg2
from db_connection import get_connection

conn = get_connection()
if conn is not None:
    try:
        cur = conn.cursor()
        table_sql = '''
                    CREATE TABLE psycopg2_test(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    age INT)
                    '''
        cur.execute(table_sql)
        conn.commit()
        print('table created')



    except Exception as error:
        print(error)
    finally:
        cur.close()
        conn.close()