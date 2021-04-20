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
from eve_tools.swagger_client.api.contacts_api import ContactsApi
from eve_tools.swagger_client.rest import ApiException


@pytest.fixture(scope="module")
def api():
    api = ContactsApi()
    yield api


class TestContactsApi:
    """ContactsApi unit test stubs"""

    def test_delete_characters_character_id_contacts(self, api):
        """Test case for delete_characters_character_id_contacts

        Delete contacts
        """
        pass

    def test_get_alliances_alliance_id_contacts(self, api):
        """Test case for get_alliances_alliance_id_contacts

        Get alliance contacts
        """
        pass

    def test_get_alliances_alliance_id_contacts_labels(self, api):
        """Test case for get_alliances_alliance_id_contacts_labels

        Get alliance contact labels
        """
        pass

    def test_get_characters_character_id_contacts(self, api):
        """Test case for get_characters_character_id_contacts

        Get contacts
        """
        pass

    def test_get_characters_character_id_contacts_labels(self, api):
        """Test case for get_characters_character_id_contacts_labels

        Get contact labels
        """
        pass

    def test_get_corporations_corporation_id_contacts(self, api):
        """Test case for get_corporations_corporation_id_contacts

        Get corporation contacts
        """
        pass

    def test_get_corporations_corporation_id_contacts_labels(self, api):
        """Test case for get_corporations_corporation_id_contacts_labels

        Get corporation contact labels
        """
        pass

    def test_post_characters_character_id_contacts(self, api):
        """Test case for post_characters_character_id_contacts

        Add contacts
        """
        pass

    def test_put_characters_character_id_contacts(self, api):
        """Test case for put_characters_character_id_contacts

        Edit contacts
        """
        pass