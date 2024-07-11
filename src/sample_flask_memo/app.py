from flask import Flask, render_template, request
import psycopg
import csv
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sample_flask_memo.infra.models.memo import Memo

app = Flask(__name__)

engine=create_engine(f"postgresql+psycopg://postgres:postgres@localhost:5432/memo")
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/", methods=["GET"])
def index():

    memo_list=session.query(Memo).all()
    return render_template("index.html", memo_list=memo_list)
    # with psycopg.connect("host=localhost dbname=memo user=postgres password=postgres") as conn:
    #     with conn.cursor() as cur:
    #         cur.execute("SELECT * FROM memo")
    #         memo_list = cur.fetchall()
    # return render_template("index.html", memo_list=memo_list)


@app.route("/add", methods=["POST"])
def add():
    memo = request.form.get("memo")

    with open("test_data.csv","r",encoding="utf-8") as csvfile:
        reader=csv.reader(csvfile)
        next(reader) #csvファイルの1行目(列名)を除く
        for row in reader:
            memo=Memo(id=row[0],memo=row[1])
            session.add(memo)
        session.commit()

    # with psycopg.connect("host=localhost dbname=memo user=postgres password=postgres") as conn:
    #     with conn.cursor() as cur:
    #         cur.execute("INSERT INTO memo (id, memo) VALUES(%(id)s, %(memo)s)",
    #                 {"id": uuid7(), "memo": memo})
    # return index()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
