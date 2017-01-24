name: inverse
layout: true
class: center, middle, inverse
---
# Kobinハンズオン

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
3. Routing
4. Template Engine
5. Database (SQLite3)

???

ただHTMLを表示するだけだと、静的なHTMLを置くだけでPythonのサーバ使う意味が無いので、
時間は少し短いですが、SQLite3に保存してある情報を取り出して表示するところまでいけたらなと思います。

---
template: inverse

## Kobin

---
## Kobin

- https://github.com/kobinpy/kobin
- Type Hints friendly WSGI Framework for Python3.
- **Simple** (考え方を簡潔に) vs **Easy** (作ることが簡単に)
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

# Routing

---
.left-column[
## Tutorial
### Hello World
### Routing
]
.right-column[
ルーティングとURL変数

```python
from kobin import Kobin, Response

app = Kobin()


@app.route('/')
def index() -> Response:
    return Response('Hello World')


@app.route('/tasks/<task_id>')
def task_detail(task_id: int) -> Response:
    return Response(f'Task {task_id}')
```

http://127.0.0.1:8000/tasks/1
]

---
template: inverse

# Template Engine

Templates

---
.left-column[
## Tutorial
### Hello World
### Routing
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
<!DOCTYPE html>
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
http://127.0.0.1:8000/ に行ってみよう。
]

---
.left-column[
## Tutorial
### Hello World
### Routing
### Template Engine
]
.right-column[
変数の表示

```python
@app.route('/tasks/{task_id}')
def task_detail(task_id: int) -> TemplateResponse:
    return TemplateResponse('task-detail.html', task_id=task_id)
```

`templates/task-detail.html` を追加

```html
<!DOCTYPE html>
<html>
<head>
    <title>Kobin Handson</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.3.1/css/bulma.min.css" />
</head>
<body>
    <section class="section">
        <div class="container">
            <h1 class="title">This is task{{ task_id }}</h1>
            <p class="subtitle">変数をテンプレートで表示してみましょう。</p>
        </div>
    </section>
</body>
</html>
```
http://127.0.0.1:8000/tasks/1 に行ってみよう。
]

---
.left-column[
## Tutorial
### Hello World
### Routing
### Template Engine
]
.right-column[
テンプレートの継承

`base.html` を用意

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.3.1/css/bulma.min.css" />
</head>
<body>
    <section class="section">
        <div class="container">
            {% block content %}{% endblock %}
        </div>
    </section>
</body>
</html>
```
]

---
.left-column[
## Tutorial
### Hello World
### Routing
### Template Engine
]
.right-column[
テンプレートの継承

`index.html`

```html
{% extends "base.html" %}
{% block title %}Hello Kobin!{% endblock %}

{% block content %}
<h1 class="title">Hello Kobin</h1>
<p class="subtitle">HTMLテンプレートを使った例です。</p>
{% endblock %}
```

`task-detail.html`

```html
{% extends "base.html" %}
{% block title %}Task Detail{% endblock %}

{% block content %}
<h1 class="title">This is task{{ task_id }}</h1>
<p class="subtitle">変数をテンプレートで表示してみましょう。</p>
{% endblock %}
```
]

---
template: inverse

# Database

---
.left-column[
## Tutorial
### Goal
### Routing
### Template Engine
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

See https://sqlite.org/cli.html
]

---
.left-column[
## Tutorial
### Goal
### Routing
### Template Engine
### Database
]
.right-column[
PythonからSQLite3を操作する。

```python
>>> import sqlite3
>>> conn = sqlite3.connect('db.sqlite3')
>>> cur = conn.cursor()
>>> for row in cur.execute("SELECT * from tasks"):
...     print(row)
...
(1, 'Run kobin application.')
(2, 'Use sqlite3 from python')
>>> cur.close()
>>> conn.close()
```

See http://docs.python.jp/3/library/sqlite3.html
]

---
.left-column[
## Tutorial
### Goal
### Routing
### Template Engine
### Database
]
.right-column[
`app.py` に組み込む

```python
SQLITE_PATH = 'db.sqlite3'
_db = None


def get_db():
    global _db
    if _db is None:
        _db = sqlite3.connect(SQLITE_PATH)
    return _db


@app.route('/')
def index() -> TemplateResponse:
    cur = get_db().cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    return TemplateResponse('index.html', tasks=tasks)
```
]

---
.left-column[
## Tutorial
### Goal
### Routing
### Template Engine
### Database
]
.right-column[

`index.html` に追加

```html
<ul>
    {% for task in tasks %}
    <li>{{ task[0] }}. {{ task[1] }}</li>
    {% endfor %}
</ul>
```

http://127.0.0.1:8000/ に行ってみよう。
]

---
template: inverse

## Q&A

