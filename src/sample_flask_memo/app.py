from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sample_flask_memo.infra.models.memo import Memo
from uuid6 import uuid7


app = Flask(__name__)

engine=create_engine(f"postgresql+psycopg://postgres:postgres@localhost:5432/memo")
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/", methods=["GET"])
def index():
    memo_list=session.query(Memo).order_by('memo').all()
    print(memo_list)
    return render_template("index.html", memo_list=memo_list)


@app.route("/add", methods=["POST"])
def add():
    memo = request.form.get("memo")

    memo=Memo(id=uuid7(), memo=memo)
    session.add(memo)
    session.commit()
    return index()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
