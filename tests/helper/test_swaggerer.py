from tests import context

import pytest

from eve_tools.helper.swaggerer import Swaggerer
from eve_tools.helper.swaggerer import JsonResponse


@pytest.fixture(scope="module")
def swaggerer():
    uri = "https://petstore.swagger.io/v2/swagger.json"
    yield Swaggerer(uri)


@pytest.fixture(scope="module")
def operation_id():
    operation_id = "getUserByName"
    yield operation_id


@pytest.fixture(scope="module")
def username():
    username = "Alice"
    yield username


@pytest.fixture(scope="module")
def response(swaggerer, operation_id, username):
    response = swaggerer.do(operation_id, username=username)
    yield response


class TestCreateOperation:
    def test_check_id(self, swaggerer, operation_id):
        assert (
            swaggerer.create_operation(operation_id)._Operation__operationId
            == operation_id
        )


class TestDo404:
    def test_status(self, response):
        assert response.status == 404

    def test_header(self, response):
        assert response.header["Content-Type"][0] == "application/json"

    def test_data(self, response):
        assert response.json == {
            "code": 1,
            "type": "error",
            "message": "User not found",
        }
