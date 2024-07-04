import psycopg

# データベースとのコネクションを確立し、コネクションオブジェクトを取得する
connection = psycopg.connect("host=localhost dbname=memo user=postgres password=postgres")

# カーソルをオープンする
cursor = connection.cursor()

with psycopg.connect("host=localhost dbname=memo user=postgres password=postgres") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM memo")
        cur.fetchone()

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)
