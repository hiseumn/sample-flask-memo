from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    memo = request.form.get("memo")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
