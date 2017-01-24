name: inverse
layout: true
class: center, middle, inverse
---
# Kobinハンズオン

※ スライド資料はまだ作成途中です。

Masashi Shibata (@c\_bata\_)

.footnote[Go directly to [Github](https://github.com/kobinpy/handson-ja)]

---
layout: false
.left-column[
## Profile
.center[.profileicon[]]
]

.right-column[
こんにちは！

- 芝田 将 (Masashi Shibata)
- twitter: @c\_bata\_
- 明石高専 専攻科
- Kobin Framework開発者
- PyCon JP, Taiwan, Korea参加・登壇
    - http://gihyo.jp/news/report/01/pycon-apac-2015
    - http://gihyo.jp/news/report/01/pycon-apac2016
- PyCon JP 2016では、Webフレームワークの作り方
]

---
## Agenda

1. Kobin
2. Hello World
3. Template Engine
4. Routing
5. Database (SQLite3)

???

ただHTMLを表示するだけだと、静的なHTMLを置くだけでPythonのサーバ使う意味が無いので、
時間は少し短いですが、SQLite3に保存してある情報を取り出して表示するところまでいけたらなと思います。

---
template: inverse

## Kobin

---
## Kobin

- 作者: c-bata
- Simple (考え方を簡潔に) vs Easy (作ることが簡単に)
- 実装は500行程度

???

Kobinは、Easyなフレームワークではありません。

- Django Adminのように少し記述するだけで管理画面はありません。
- Django REST Frameworkのように少し記述するだけでRESTfulなJSON APIサーバはありません。
- Flaskのような強力な周辺ライブラリやエコシステムはありません。
- 他の多くの人気があるWebフレームワークのように書籍やドキュメントなど充実した資料はありません。

Kobinは、Simpleなフレームワークです。

- 500行程度で実装されたKobinに関して覚えることはそもそもそんなにありません。

refs:

- http://eed3si9n.com/ja/simplicity-matters
- http://t-wada.hatenablog.jp/

---
template: inverse

## Tutorial

---
.left-column[
## Tutorial
### Hello World
]
.right-column[
まずは、恒例のHello World.

```python
from kobin import Kobin, Response

app = Kobin()

@app.route('^/$', 'GET')
def hello(request):
    return Response('Hello World')
```

`app.py` という名前で保存して、

```console
$ wsgicli run app.py app
```

http://127.0.0.1:8000/ に行ってみよう。
]

---
template: inverse

# Template Engine

Templates

---
.left-column[
## Tutorial
### Hello World
### Template Engine
]
.right-column[

```python
from kobin import TemplateResponse

@app.route('/')
def index() -> TemplateResponse:
    return TemplateResponse('index.html')
```

`templates/index.html` を用意してKobinから読み込む。

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>Kobin Handson</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.3.1/css/bulma.min.css" />
</head>
<body>
    <section class="section">
        <div class="container">
            <h1 class="title">Hello Kobin</h1>
            <p class="subtitle">HTMLテンプレートを使った例です。</p>
        </div>
    </section>
</body>
</html>
```
]

---
template: inverse

# Routing

---
template: inverse

# Database

---
.left-column[
## Tutorial
### Goal
### Template Engine
### Routing
### Database
]
.right-column[

SQLite3を使ってみる.

```sql
$ sqlite3 db.sqlite3
sqlite> .header on
sqlite> .mode column
sqlite> create table tasks (
   ...>   id integer primary key,
   ...>   name text
   ...> );
sqlite> select * from tasks;
sqlite> insert into tasks(name) values('Run kobin application.');
sqlite> insert into tasks(name) values('Use sqlite3 from python');
sqlite> select * from tasks;
id          name                  
----------  ----------------------
1           Run kobin application.
2           Use sqlite3 from pytho
sqlite> .quit
```
]

---
template: inverse

## Q&A

