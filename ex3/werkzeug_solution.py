from werkzeug.wrappers import Request, Response


@Request.application
def application(request):
    name = request.args.get('name', 'World')
    return Response(f'''
    <html>
    <head><title>Hello, {name}!</title></head>
    <body><h1>Hello, {name}!</h1></body>
    </html>
    ''', content_type='text/html')
