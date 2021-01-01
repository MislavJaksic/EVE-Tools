from pyswagger import App
from pyswagger.contrib.client.requests import Client
from eve_tools.helper.response import JsonResponse


class Swaggerer:
    def __init__(self, swagger_uri):
        self.app = App.create(swagger_uri)
        self.client = Client()

    def do(self, operation_id, **parameters):
        operation = self.create_operation(operation_id)
        response = self.client.request(operation(**parameters))
        return JsonResponse(response)

    def create_operation(self, operation_id):
        return self.app.op[operation_id]
