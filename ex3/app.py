from .request import Request
from .response import Response


def request_response_application(function):
    def app(environ, start_response):
        request = Request(environ)
        response = Response(request)
        start_response(response.status, response.headers.items())
        return iter(response)
    return app


@request_response_application
def app(request):
    name = request.args.get('name', 'World')
    return Response([
        '<doctype html>',
        '<html>'
        f'<head><title>Hello, {name}!</title></head>'
        f'<body><h1>Hello, {name}!</h1></body>'
        '</html>'
    ])
