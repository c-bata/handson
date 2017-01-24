from kobin import Kobin, load_config, TemplateResponse

app = Kobin(
    config=load_config({'DEBUG': True})
)


@app.route('/')
def index() -> TemplateResponse:
    return TemplateResponse('index.html')
