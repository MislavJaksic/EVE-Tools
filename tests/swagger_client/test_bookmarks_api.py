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
from eve_tools.swagger_client.api.bookmarks_api import BookmarksApi
from eve_tools.swagger_client.rest import ApiException


@pytest.fixture(scope="module")
def api():
    api = BookmarksApi()
    yield api


class TestBookmarksApi:
    """BookmarksApi unit test stubs"""

    def test_get_characters_character_id_bookmarks(self, api):
        """Test case for get_characters_character_id_bookmarks

        List bookmarks
        """
        pass

    def test_get_characters_character_id_bookmarks_folders(self, api):
        """Test case for get_characters_character_id_bookmarks_folders

        List bookmark folders
        """
        pass

    def test_get_corporations_corporation_id_bookmarks(self, api):
        """Test case for get_corporations_corporation_id_bookmarks

        List corporation bookmarks
        """
        pass

    def test_get_corporations_corporation_id_bookmarks_folders(self, api):
        """Test case for get_corporations_corporation_id_bookmarks_folders

        List corporation bookmark folders
        """
        pass
