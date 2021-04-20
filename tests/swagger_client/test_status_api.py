# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 1.7.15

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

from tests import context

import pytest

from eve_tools import swagger_client
from eve_tools.swagger_client.api.status_api import StatusApi
from eve_tools.swagger_client.rest import ApiException


@pytest.fixture(scope="module")
def api():
    api = StatusApi()
    yield api


class TestStatusApi:
    """StatusApi unit test stubs"""

    def test_get_status(self, api):
        """Test case for get_status

        Retrieve the uptime and player counts
        """
        pass