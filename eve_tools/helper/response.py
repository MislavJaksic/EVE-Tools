import json


class JsonResponse:
    def __init__(self, py_swagger_response):
        self.status = py_swagger_response.status
        self.header = py_swagger_response.header
        self.json = self.parse_json(py_swagger_response.raw)

    def parse_json(self, raw):
        return json.loads(raw)

    def __str__(self):
        return str({"status": self.status, "header": self.header, "json": self.json})
