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
from eve_tools.swagger_client.api.calendar_api import CalendarApi
from eve_tools.swagger_client.rest import ApiException


@pytest.fixture(scope="module")
def api():
    api = CalendarApi()
    yield api


class TestCalendarApi:
    """CalendarApi unit test stubs"""

    def test_get_characters_character_id_calendar(self, api):
        """Test case for get_characters_character_id_calendar

        List calendar event summaries
        """
        pass

    def test_get_characters_character_id_calendar_event_id(self, api):
        """Test case for get_characters_character_id_calendar_event_id

        Get an event
        """
        pass

    def test_get_characters_character_id_calendar_event_id_attendees(self, api):
        """Test case for get_characters_character_id_calendar_event_id_attendees

        Get attendees
        """
        pass

    def test_put_characters_character_id_calendar_event_id(self, api):
        """Test case for put_characters_character_id_calendar_event_id

        Respond to an event
        """
        pass
