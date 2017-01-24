from kobin import Kobin, TemplateResponse
import sqlite3

app = Kobin()

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


@app.route('/tasks/{task_id}')
def task_detail(task_id: int) -> TemplateResponse:
    return TemplateResponse('task-detail.html', task_id=task_id)
