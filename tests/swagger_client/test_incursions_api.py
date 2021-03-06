# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 1.7.15

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import pytest

from eve_tools.swagger_client.api.incursions_api import IncursionsApi


@pytest.fixture(scope="module")
def api():
    api = IncursionsApi()
    yield api


class TestIncursionsApi:
    """IncursionsApi unit test stubs"""

    def test_get_incursions(self, api):
        """Test case for get_incursions

        List incursions
        """
        pass
