# Use gunicorn to serve this with: `gunicorn -w 4 ex1.example_wsgi:app`
# start response is a callable which takes:
#   status:     a string with the status code and readable description
#   headers:    a list of two tuples containing http headers
# wsgi applications return iterables that yield bytes


def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]
    start_response(status, headers)
    return [b'<h1>Hello World</h1>']
