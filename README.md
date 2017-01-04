# Kobinハンズオン

Kobinのハンズオン資料です。

## 環境構築

#### 用意していただくもの

- MacもしくはLinuxが動く環境
- エディタ(こだわりがない場合はPyCharmがお薦めです)
- Python 3.6


**virtualenvの作成**

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

**必要なライブラリのインストール**

```console
(venv)$ pip install -r requirements.txt
```


## 開催実績

- [神戸Pythonの会 Webアプリ開発 #1](https://kobe-python.connpass.com/event/48080/)

