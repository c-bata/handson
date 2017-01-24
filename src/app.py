from kobin import Kobin, TemplateResponse

app = Kobin()


@app.route('/')
def index() -> TemplateResponse:
    return TemplateResponse('index.html')
