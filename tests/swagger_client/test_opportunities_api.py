# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 1.7.15

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import pytest

from eve_tools.swagger_client.api.opportunities_api import OpportunitiesApi


@pytest.fixture(scope="module")
def api():
    api = OpportunitiesApi()
    yield api


class TestOpportunitiesApi:
    """OpportunitiesApi unit test stubs"""

    def test_get_characters_character_id_opportunities(self, api):
        """Test case for get_characters_character_id_opportunities

        Get a character's completed tasks
        """
        pass

    def test_get_opportunities_groups(self, api):
        """Test case for get_opportunities_groups

        Get opportunities groups
        """
        pass

    def test_get_opportunities_groups_group_id(self, api):
        """Test case for get_opportunities_groups_group_id

        Get opportunities group
        """
        pass

    def test_get_opportunities_tasks(self, api):
        """Test case for get_opportunities_tasks

        Get opportunities tasks
        """
        pass

    def test_get_opportunities_tasks_task_id(self, api):
        """Test case for get_opportunities_tasks_task_id

        Get opportunities task
        """
        pass
