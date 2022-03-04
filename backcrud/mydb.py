import psycopg2.pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'
db_username = 'postgres'
db_password = '123456'
dbpool2 = psycopg2.pool.ThreadedConnectionPool(5,20, host=db_host,port=db_port,dbname=db_name,user=db_username,password=db_password)

@contextmanager
def db_cursor():
    conn = dbpool2.getconn()
    conn.set_client_encoding('UTF8')
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            yield cur
            conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        dbpool2.putconn(conn)