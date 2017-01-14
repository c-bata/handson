# Kobinハンズオン

Kobinのハンズオン資料です。

## 環境構築

#### 用意していただくもの

- MacもしくはLinuxが動く環境
- エディタ(こだわりがない場合はPyCharmがお薦めです)
- Python 3.6
- SQLite3


#### virtualenvの作成

ハンズオンをしていくにあたって、virtualenvの使用を推奨しています。
Python3では、 `venv` モジュールが含まれていますのでこちらを使用して作成してください。

```console
$ python3.6 -m venv venv
$ source ./venv/activate
(venv)$ which python
/<path to pwd>/venv/bin/python
(venv)$ which pip
/<path to pwd>/venv/bin/pip
```


#### 必要なライブラリのインストール

```console
(venv)$ pip install -U pip
(venv)$ pip install -c constraints.txt -r requirements.txt
```

#### Hello World

余裕のある方は，無事に動くかどうか確認してみましょう。
Hello Worldは次のようになります。

```python
from kobin import Kobin, Response

app = Kobin()

@app.route('/')
def index() -> Response:
    return Response('Hello World')
```

`app.py` という名前で保存した場合、次のコマンドでサーバを起動します。

```console
$ wsgicli run app.py app -p 8000
Start: 127.0.0.1:8000
```

http://127.0.0.1:8000 にアクセスしてください。
「Hello World」と表示されれば、準備完了です。

ハンズオンに進んでみましょう。
ここまでで躓いたことやわからないことがあれば、[@c_bata_](https://twitter.com/c_bata_) に気軽に相談してください。


## 開催実績

- 神戸Pythonの会 Webアプリ開発 #1
    - [connpass](https://kobe-python.connpass.com/event/48080/)
    - [doorkeeper](https://f0697a62045dae763ed7b3c489.doorkeeper.jp/events/55869)

