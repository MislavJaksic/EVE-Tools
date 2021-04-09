# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from eve_tools import swagger_client
from eve_tools.swagger_client.api.incursions_api import IncursionsApi  # noqa: E501
from eve_tools.swagger_client.rest import ApiException


class TestIncursionsApi(unittest.TestCase):
    """IncursionsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.incursions_api.IncursionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_incursions(self):
        """Test case for get_incursions

        List incursions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
