# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    vim

# pipを使ってpoetryをインストール
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install numpy
RUN pip install poetry
RUN pip install paramiko
RUN pip install pyserial
RUN pip install buildhat
RUN pip install control
RUN pip install matplotlib
RUN pip install scipy

# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]