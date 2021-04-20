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
from eve_tools.swagger_client.api.character_api import CharacterApi
from eve_tools.swagger_client.rest import ApiException


@pytest.fixture(scope="module")
def api():
    api = CharacterApi()
    yield api


class TestCharacterApi:
    """CharacterApi unit test stubs"""

    def test_get_characters_character_id(self, api):
        """Test case for get_characters_character_id

        Get character's public information
        """
        pass

    def test_get_characters_character_id_agents_research(self, api):
        """Test case for get_characters_character_id_agents_research

        Get agents research
        """
        pass

    def test_get_characters_character_id_blueprints(self, api):
        """Test case for get_characters_character_id_blueprints

        Get blueprints
        """
        pass

    def test_get_characters_character_id_corporationhistory(self, api):
        """Test case for get_characters_character_id_corporationhistory

        Get corporation history
        """
        pass

    def test_get_characters_character_id_fatigue(self, api):
        """Test case for get_characters_character_id_fatigue

        Get jump fatigue
        """
        pass

    def test_get_characters_character_id_medals(self, api):
        """Test case for get_characters_character_id_medals

        Get medals
        """
        pass

    def test_get_characters_character_id_notifications(self, api):
        """Test case for get_characters_character_id_notifications

        Get character notifications
        """
        pass

    def test_get_characters_character_id_notifications_contacts(self, api):
        """Test case for get_characters_character_id_notifications_contacts

        Get new contact notifications
        """
        pass

    def test_get_characters_character_id_portrait(self, api):
        """Test case for get_characters_character_id_portrait

        Get character portraits
        """
        pass

    def test_get_characters_character_id_roles(self, api):
        """Test case for get_characters_character_id_roles

        Get character corporation roles
        """
        pass

    def test_get_characters_character_id_standings(self, api):
        """Test case for get_characters_character_id_standings

        Get standings
        """
        pass

    def test_get_characters_character_id_titles(self, api):
        """Test case for get_characters_character_id_titles

        Get character corporation titles
        """
        pass

    def test_post_characters_affiliation(self, api):
        """Test case for post_characters_affiliation

        Character affiliation
        """
        pass

    def test_post_characters_character_id_cspa(self, api):
        """Test case for post_characters_character_id_cspa

        Calculate a CSPA charge cost
        """
        pass