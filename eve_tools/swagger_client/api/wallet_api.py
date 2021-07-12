# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from eve_tools.swagger_client.api_client import ApiClient


class WalletApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_wallet(self, character_id, **kwargs):
        """Get a character's wallet balance

        Returns a character's wallet balance  ---  This route is cached for up to 120 seconds  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/wallet/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_wallet(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: float
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_characters_character_id_wallet_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_wallet_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_wallet_with_http_info(self, character_id, **kwargs):
        """Get a character's wallet balance

        Returns a character's wallet balance  ---  This route is cached for up to 120 seconds  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/wallet/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_wallet_with_http_info(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: float
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'if_none_match', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_wallet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError(
                "Missing the required parameter `character_id` when calling `get_characters_character_id_wallet`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `character_id` when calling `get_characters_character_id_wallet`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v1/characters/{character_id}/wallet/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='float',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_characters_character_id_wallet_journal(self, character_id, **kwargs):
        """Get character wallet journal

        Retrieve the given character's wallet journal going 30 days back  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_wallet_journal(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_characters_character_id_wallet_journal_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_wallet_journal_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_wallet_journal_with_http_info(self, character_id, **kwargs):
        """Get character wallet journal

        Retrieve the given character's wallet journal going 30 days back  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_wallet_journal_with_http_info(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'if_none_match', 'page', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_wallet_journal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError(
                "Missing the required parameter `character_id` when calling `get_characters_character_id_wallet_journal`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `character_id` when calling `get_characters_character_id_wallet_journal`, must be a value greater than or equal to `1`")
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):
            raise ValueError(
                "Invalid value for parameter `page` when calling `get_characters_character_id_wallet_journal`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v6/characters/{character_id}/wallet/journal/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_characters_character_id_wallet_transactions(self, character_id, **kwargs):
        """Get wallet transactions

        Get wallet transactions of a character  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_wallet_transactions(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show transactions happened before the one referenced by this id
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_characters_character_id_wallet_transactions_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_wallet_transactions_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_wallet_transactions_with_http_info(self, character_id, **kwargs):
        """Get wallet transactions

        Get wallet transactions of a character  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_wallet_transactions_with_http_info(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show transactions happened before the one referenced by this id
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'from_id', 'if_none_match', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_wallet_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError(
                "Missing the required parameter `character_id` when calling `get_characters_character_id_wallet_transactions`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `character_id` when calling `get_characters_character_id_wallet_transactions`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'from_id' in params:
            query_params.append(('from_id', params['from_id']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v1/characters/{character_id}/wallet/transactions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_corporations_corporation_id_wallets(self, corporation_id, **kwargs):
        """Returns a corporation's wallet balance

        Get a corporation's wallets  ---  This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_wallets(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_corporations_corporation_id_wallets_with_http_info(corporation_id, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_wallets_with_http_info(corporation_id, **kwargs)
            return data

    def get_corporations_corporation_id_wallets_with_http_info(self, corporation_id, **kwargs):
        """Returns a corporation's wallet balance

        Get a corporation's wallets  ---  This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_wallets_with_http_info(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'datasource', 'if_none_match', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_wallets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if self.api_client.client_side_validation and ('corporation_id' not in params or
                                                       params['corporation_id'] is None):
            raise ValueError(
                "Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_wallets`")

        if self.api_client.client_side_validation and ('corporation_id' in params and params['corporation_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `corporation_id` when calling `get_corporations_corporation_id_wallets`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v1/corporations/{corporation_id}/wallets/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_corporations_corporation_id_wallets_division_journal(self, corporation_id, division, **kwargs):
        """Get corporation wallet journal

        Retrieve the given corporation's wallet journal for the given division going 30 days back  ---  This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_journal(corporation_id, division, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_corporations_corporation_id_wallets_division_journal_with_http_info(corporation_id,
                                                                                                division, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_wallets_division_journal_with_http_info(corporation_id,
                                                                                                  division, **kwargs)
            return data

    def get_corporations_corporation_id_wallets_division_journal_with_http_info(self, corporation_id, division,
                                                                                **kwargs):
        """Get corporation wallet journal

        Retrieve the given corporation's wallet journal for the given division going 30 days back  ---  This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_journal_with_http_info(corporation_id, division, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'division', 'datasource', 'if_none_match', 'page', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_wallets_division_journal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if self.api_client.client_side_validation and ('corporation_id' not in params or
                                                       params['corporation_id'] is None):
            raise ValueError(
                "Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_wallets_division_journal`")
        # verify the required parameter 'division' is set
        if self.api_client.client_side_validation and ('division' not in params or
                                                       params['division'] is None):
            raise ValueError(
                "Missing the required parameter `division` when calling `get_corporations_corporation_id_wallets_division_journal`")

        if self.api_client.client_side_validation and ('corporation_id' in params and params['corporation_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `corporation_id` when calling `get_corporations_corporation_id_wallets_division_journal`, must be a value greater than or equal to `1`")
        if self.api_client.client_side_validation and ('division' in params and params['division'] > 7):
            raise ValueError(
                "Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_journal`, must be a value less than or equal to `7`")
        if self.api_client.client_side_validation and ('division' in params and params['division'] < 1):
            raise ValueError(
                "Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_journal`, must be a value greater than or equal to `1`")
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):
            raise ValueError(
                "Invalid value for parameter `page` when calling `get_corporations_corporation_id_wallets_division_journal`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']
        if 'division' in params:
            path_params['division'] = params['division']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v4/corporations/{corporation_id}/wallets/{division}/journal/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_corporations_corporation_id_wallets_division_transactions(self, corporation_id, division, **kwargs):
        """Get corporation wallet transactions

        Get wallet transactions of a corporation  ---  This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_transactions(corporation_id, division, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_corporations_corporation_id_wallets_division_transactions_with_http_info(corporation_id,
                                                                                                     division, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_wallets_division_transactions_with_http_info(corporation_id,
                                                                                                       division,
                                                                                                       **kwargs)
            return data

    def get_corporations_corporation_id_wallets_division_transactions_with_http_info(self, corporation_id, division,
                                                                                     **kwargs):
        """Get corporation wallet transactions

        Get wallet transactions of a corporation  ---  This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_wallets_division_transactions_with_http_info(corporation_id, division, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param int division: Wallet key of the division to fetch journals from (required)
        :param str datasource: The server name you would like data from
        :param int from_id: Only show journal entries happened before the transaction referenced by this id
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'division', 'datasource', 'from_id', 'if_none_match', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_wallets_division_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if self.api_client.client_side_validation and ('corporation_id' not in params or
                                                       params['corporation_id'] is None):
            raise ValueError(
                "Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_wallets_division_transactions`")
        # verify the required parameter 'division' is set
        if self.api_client.client_side_validation and ('division' not in params or
                                                       params['division'] is None):
            raise ValueError(
                "Missing the required parameter `division` when calling `get_corporations_corporation_id_wallets_division_transactions`")

        if self.api_client.client_side_validation and ('corporation_id' in params and params['corporation_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `corporation_id` when calling `get_corporations_corporation_id_wallets_division_transactions`, must be a value greater than or equal to `1`")
        if self.api_client.client_side_validation and ('division' in params and params['division'] > 7):
            raise ValueError(
                "Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_transactions`, must be a value less than or equal to `7`")
        if self.api_client.client_side_validation and ('division' in params and params['division'] < 1):
            raise ValueError(
                "Invalid value for parameter `division` when calling `get_corporations_corporation_id_wallets_division_transactions`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']
        if 'division' in params:
            path_params['division'] = params['division']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'from_id' in params:
            query_params.append(('from_id', params['from_id']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v1/corporations/{corporation_id}/wallets/{division}/transactions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
