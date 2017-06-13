from cgi import parse_qs


class Request:

    def __init__(self, environ):
        self.environ = environ

    @property
    def args(self):
        q_strings = parse_qs(self.environ['QUERY_STRING'])
        return {k: v[0] for k, v in q_strings.items()}
