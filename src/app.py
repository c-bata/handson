from kobin import Kobin, Response, TemplateResponse

app = Kobin()


@app.route('/')
def index() -> TemplateResponse:
    return TemplateResponse('index.html')


@app.route('/tasks/{task_id}')
def task_detail(task_id: int) -> Response:
    return Response(f'Task {task_id}')
