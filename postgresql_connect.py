import psycopg
from uuid6 import uuid7

# データベースとのコネクションを確立し、コネクションオブジェクトを取得する
connection = psycopg.connect("host=localhost dbname=memo user=postgres password=postgres")

# カーソルをオープンする
cursor = connection.cursor()

with psycopg.connect("host=localhost dbname=memo user=postgres password=postgres") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.
        cur.execute("INSERT INTO memo (id, memo) VALUES(%(id)s, %(memo)s)",
                    {"id": uuid7(), "memo": "hello world"})
        conn.commit()
        
    
        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM memo")
        cur.fetchone()

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()

        # for record in cur:
        #     print(record)
