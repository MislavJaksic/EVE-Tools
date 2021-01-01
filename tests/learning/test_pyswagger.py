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
def getInventory_op(app):
    operation_id = "getInventory"
    yield app.op[operation_id]


@pytest.fixture(scope="module")
def getUserByName_op(app):
    operation_id = "getUserByName"
    yield app.op[operation_id]


@pytest.fixture(scope="module")
def response_200(client, getInventory_op):
    yield client.request(getInventory_op())


@pytest.fixture(scope="module")
def response_404(client, getUserByName_op):
    username = "Alice"
    yield client.request(getUserByName_op(username=username))


class TestResponse200:
    def test_status(self, response_200):
        assert response_200.status == 200

    def test_header(self, response_200):
        assert response_200.header["Content-Type"][0] == "application/json"

    # def test_data(self, response_200):  # flakey!
    #     assert response_200.data["sold"] == 1

    # def test_raw(self, response_200):  # flakey!
    #     assert response_200.raw == b'{"sold":1,"string":724,"available":249}'


class TestResponse404:
    def test_status(self, response_404):
        assert response_404.status == 404

    def test_header(self, response_404):
        assert response_404.header["Content-Type"][0] == "application/json"

    def test_data(self, response_404):
        assert response_404.data == None

    def test_raw(self, response_404):
        assert (
            response_404.raw == b'{"code":1,"type":"error","message":"User not found"}'
        )
