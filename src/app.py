from kobin import Kobin, TemplateResponse

app = Kobin()


@app.route('/')
def index() -> TemplateResponse:
    return TemplateResponse('index.html')


@app.route('/tasks/{task_id}')
def task_detail(task_id: int) -> TemplateResponse:
    return TemplateResponse('task-detail.html', task_id=task_id)
