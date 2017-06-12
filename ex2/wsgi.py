# Use gunicorn to serve this with: `gunicorn ex2.wsgi:app`
from cgi import parse_qs


def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]
    start_response(status, headers)

    query_strings = parse_qs(environ['QUERY_STRING'])
    name = query_strings.get('name', 'World')[0]
    return [(f'<h1>Hello {name}!</h1>').encode('utf-8')]
