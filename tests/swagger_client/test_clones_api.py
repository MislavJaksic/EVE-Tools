# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 1.7.15

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import pytest

from eve_tools.swagger_client.api.clones_api import ClonesApi


@pytest.fixture(scope="module")
def api():
    api = ClonesApi()
    yield api


class TestClonesApi:
    """ClonesApi unit test stubs"""

    def test_get_characters_character_id_clones(self, api):
        """Test case for get_characters_character_id_clones

        Get clones
        """
        pass

    def test_get_characters_character_id_implants(self, api):
        """Test case for get_characters_character_id_implants

        Get active implants
        """
        pass
