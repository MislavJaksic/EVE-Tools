from tests import context

import pytest
from pyswagger import App
from pyswagger.contrib.client.requests import Client

# Learner's tests


@pytest.fixture(scope="module")
def app():
    uri = "https://petstore.swagger.io/v2/swagger.json"
    yield App.create(uri)


@pytest.fixture(scope="module")
def client():
    yield Client()


@pytest.fixture(scope="module")
def op(app):
    operation_id = "getUserByName"
    yield app.op[operation_id]


@pytest.fixture(scope="module")
def response(client, op):
    username = "Alice"
    yield client.request(op(username=username))


class TestResponse:
    def test_status(self, response):
        assert response.status == 404

    def test_data(self, response):
        assert response.data == None

    def test_header(self, response):
        assert response.header["Content-Type"][0] == "application/json"

    def test_raw(self, response):
        assert response.raw == b'{"code":1,"type":"error","message":"User not found"}'
