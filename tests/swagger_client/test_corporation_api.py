# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 1.7.15

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import pytest

from eve_tools.swagger_client.api.corporation_api import CorporationApi


@pytest.fixture(scope="module")
def api():
    api = CorporationApi()
    yield api


class TestCorporationApi:
    """CorporationApi unit test stubs"""

    def test_get_corporations_corporation_id(self, api):
        """Test case for get_corporations_corporation_id

        Get corporation information
        """
        pass

    def test_get_corporations_corporation_id_alliancehistory(self, api):
        """Test case for get_corporations_corporation_id_alliancehistory

        Get alliance history
        """
        pass

    def test_get_corporations_corporation_id_blueprints(self, api):
        """Test case for get_corporations_corporation_id_blueprints

        Get corporation blueprints
        """
        pass

    def test_get_corporations_corporation_id_containers_logs(self, api):
        """Test case for get_corporations_corporation_id_containers_logs

        Get all corporation ALSC logs
        """
        pass

    def test_get_corporations_corporation_id_divisions(self, api):
        """Test case for get_corporations_corporation_id_divisions

        Get corporation divisions
        """
        pass

    def test_get_corporations_corporation_id_facilities(self, api):
        """Test case for get_corporations_corporation_id_facilities

        Get corporation facilities
        """
        pass

    def test_get_corporations_corporation_id_icons(self, api):
        """Test case for get_corporations_corporation_id_icons

        Get corporation icon
        """
        pass

    def test_get_corporations_corporation_id_medals(self, api):
        """Test case for get_corporations_corporation_id_medals

        Get corporation medals
        """
        pass

    def test_get_corporations_corporation_id_medals_issued(self, api):
        """Test case for get_corporations_corporation_id_medals_issued

        Get corporation issued medals
        """
        pass

    def test_get_corporations_corporation_id_members(self, api):
        """Test case for get_corporations_corporation_id_members

        Get corporation members
        """
        pass

    def test_get_corporations_corporation_id_members_limit(self, api):
        """Test case for get_corporations_corporation_id_members_limit

        Get corporation member limit
        """
        pass

    def test_get_corporations_corporation_id_members_titles(self, api):
        """Test case for get_corporations_corporation_id_members_titles

        Get corporation's members' titles
        """
        pass

    def test_get_corporations_corporation_id_membertracking(self, api):
        """Test case for get_corporations_corporation_id_membertracking

        Track corporation members
        """
        pass

    def test_get_corporations_corporation_id_roles(self, api):
        """Test case for get_corporations_corporation_id_roles

        Get corporation member roles
        """
        pass

    def test_get_corporations_corporation_id_roles_history(self, api):
        """Test case for get_corporations_corporation_id_roles_history

        Get corporation member roles history
        """
        pass

    def test_get_corporations_corporation_id_shareholders(self, api):
        """Test case for get_corporations_corporation_id_shareholders

        Get corporation shareholders
        """
        pass

    def test_get_corporations_corporation_id_standings(self, api):
        """Test case for get_corporations_corporation_id_standings

        Get corporation standings
        """
        pass

    def test_get_corporations_corporation_id_starbases(self, api):
        """Test case for get_corporations_corporation_id_starbases

        Get corporation starbases (POSes)
        """
        pass

    def test_get_corporations_corporation_id_starbases_starbase_id(self, api):
        """Test case for get_corporations_corporation_id_starbases_starbase_id

        Get starbase (POS) detail
        """
        pass

    def test_get_corporations_corporation_id_structures(self, api):
        """Test case for get_corporations_corporation_id_structures

        Get corporation structures
        """
        pass

    def test_get_corporations_corporation_id_titles(self, api):
        """Test case for get_corporations_corporation_id_titles

        Get corporation titles
        """
        pass

    def test_get_corporations_npccorps(self, api):
        """Test case for get_corporations_npccorps

        Get npc corporations
        """
        pass
