from pyswagger import App
from pyswagger.contrib.client.requests import Client


class Swaggerer:
    def __init__(self, swagger_uri):
        self.app = App.create(swagger_uri)
        self.client = Client()

    def do(self, operation_id, **parameters):
        op = self.app.op[operation_id]
        response = self.client.request(op(**parameters))
        return response
