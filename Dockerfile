# ベースイメージを指定
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN pip install --upgrade pip

# 依存関係をインストール
COPY ./src/flask_postgresql_sample/app.py /app/app.py
COPY requirements.lock requirements.lock
COPY pyproject.toml pyproject.toml
COPY README.md README.md

RUN pip install -r requirements.lock

# コマンドを実行
CMD ["python", "app.py"]
