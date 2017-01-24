from kobin import Kobin, Response

app = Kobin()


@app.route('/')
def index() -> Response:
    return Response('Hello World')


@app.route('/tasks/{task_id}')
def task_detail(task_id: int) -> Response:
    return Response(f'Task {task_id}')
