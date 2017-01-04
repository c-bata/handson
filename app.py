from kobin import Kobin, Response

app = Kobin()

@app.route('/')
def index() -> Response:
    return Response('Hello World')

