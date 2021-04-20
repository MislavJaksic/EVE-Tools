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


class AssetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_assets(self, character_id, **kwargs):
        """Get character assets

        Return a list of the characters assets  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_assets(character_id, async_req=True)
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
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_assets_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_assets_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_assets_with_http_info(self, character_id, **kwargs):
        """Get character assets

        Return a list of the characters assets  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_assets_with_http_info(character_id, async_req=True)
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
                    " to method get_characters_character_id_assets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_assets`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_assets`, must be a value greater than or equal to `1`")
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):
            raise ValueError("Invalid value for parameter `page` when calling `get_characters_character_id_assets`, must be a value greater than or equal to `1`")
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
            '/v5/characters/{character_id}/assets/', 'GET',
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

    def get_corporations_corporation_id_assets(self, corporation_id, **kwargs):
        """Get corporation assets

        Return a list of the corporation assets  ---  This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_assets(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_corporations_corporation_id_assets_with_http_info(corporation_id, **kwargs)
        else:
            (data) = self.get_corporations_corporation_id_assets_with_http_info(corporation_id, **kwargs)
            return data

    def get_corporations_corporation_id_assets_with_http_info(self, corporation_id, **kwargs):
        """Get corporation assets

        Return a list of the corporation assets  ---  This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_corporations_corporation_id_assets_with_http_info(corporation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'datasource', 'if_none_match', 'page', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_corporations_corporation_id_assets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if self.api_client.client_side_validation and ('corporation_id' not in params or
                                                       params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `get_corporations_corporation_id_assets`")

        if self.api_client.client_side_validation and ('corporation_id' in params and params['corporation_id'] < 1):
            raise ValueError("Invalid value for parameter `corporation_id` when calling `get_corporations_corporation_id_assets`, must be a value greater than or equal to `1`")
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):
            raise ValueError("Invalid value for parameter `page` when calling `get_corporations_corporation_id_assets`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'corporation_id' in params:
            path_params['corporation_id'] = params['corporation_id']

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
            '/v5/corporations/{corporation_id}/assets/', 'GET',
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

    def post_characters_character_id_assets_locations(self, character_id, item_ids, **kwargs):
        """Get character asset locations

        Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_characters_character_id_assets_locations(character_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_characters_character_id_assets_locations_with_http_info(character_id, item_ids, **kwargs)
        else:
            (data) = self.post_characters_character_id_assets_locations_with_http_info(character_id, item_ids, **kwargs)
            return data

    def post_characters_character_id_assets_locations_with_http_info(self, character_id, item_ids, **kwargs):
        """Get character asset locations

        Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_characters_character_id_assets_locations_with_http_info(character_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'item_ids', 'datasource', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_characters_character_id_assets_locations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `post_characters_character_id_assets_locations`")
        # verify the required parameter 'item_ids' is set
        if self.api_client.client_side_validation and ('item_ids' not in params or
                                                       params['item_ids'] is None):
            raise ValueError("Missing the required parameter `item_ids` when calling `post_characters_character_id_assets_locations`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError("Invalid value for parameter `character_id` when calling `post_characters_character_id_assets_locations`, must be a value greater than or equal to `1`")
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

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item_ids' in params:
            body_params = params['item_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v2/characters/{character_id}/assets/locations/', 'POST',
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

    def post_characters_character_id_assets_names(self, character_id, item_ids, **kwargs):
        """Get character asset names

        Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_characters_character_id_assets_names(character_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_characters_character_id_assets_names_with_http_info(character_id, item_ids, **kwargs)
        else:
            (data) = self.post_characters_character_id_assets_names_with_http_info(character_id, item_ids, **kwargs)
            return data

    def post_characters_character_id_assets_names_with_http_info(self, character_id, item_ids, **kwargs):
        """Get character asset names

        Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_characters_character_id_assets_names_with_http_info(character_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'item_ids', 'datasource', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_characters_character_id_assets_names" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `post_characters_character_id_assets_names`")
        # verify the required parameter 'item_ids' is set
        if self.api_client.client_side_validation and ('item_ids' not in params or
                                                       params['item_ids'] is None):
            raise ValueError("Missing the required parameter `item_ids` when calling `post_characters_character_id_assets_names`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError("Invalid value for parameter `character_id` when calling `post_characters_character_id_assets_names`, must be a value greater than or equal to `1`")
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

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item_ids' in params:
            body_params = params['item_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v1/characters/{character_id}/assets/names/', 'POST',
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

    def post_corporations_corporation_id_assets_locations(self, corporation_id, item_ids, **kwargs):
        """Get corporation asset locations

        Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  ---  Requires one of the following EVE corporation role(s): Director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_corporations_corporation_id_assets_locations(corporation_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_corporations_corporation_id_assets_locations_with_http_info(corporation_id, item_ids, **kwargs)
        else:
            (data) = self.post_corporations_corporation_id_assets_locations_with_http_info(corporation_id, item_ids, **kwargs)
            return data

    def post_corporations_corporation_id_assets_locations_with_http_info(self, corporation_id, item_ids, **kwargs):
        """Get corporation asset locations

        Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  ---  Requires one of the following EVE corporation role(s): Director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_corporations_corporation_id_assets_locations_with_http_info(corporation_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'item_ids', 'datasource', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_corporations_corporation_id_assets_locations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if self.api_client.client_side_validation and ('corporation_id' not in params or
                                                       params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `post_corporations_corporation_id_assets_locations`")
        # verify the required parameter 'item_ids' is set
        if self.api_client.client_side_validation and ('item_ids' not in params or
                                                       params['item_ids'] is None):
            raise ValueError("Missing the required parameter `item_ids` when calling `post_corporations_corporation_id_assets_locations`")

        if self.api_client.client_side_validation and ('corporation_id' in params and params['corporation_id'] < 1):
            raise ValueError("Invalid value for parameter `corporation_id` when calling `post_corporations_corporation_id_assets_locations`, must be a value greater than or equal to `1`")
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

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item_ids' in params:
            body_params = params['item_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v2/corporations/{corporation_id}/assets/locations/', 'POST',
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

    def post_corporations_corporation_id_assets_names(self, corporation_id, item_ids, **kwargs):
        """Get corporation asset names

        Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships  ---  Requires one of the following EVE corporation role(s): Director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_corporations_corporation_id_assets_names(corporation_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_corporations_corporation_id_assets_names_with_http_info(corporation_id, item_ids, **kwargs)
        else:
            (data) = self.post_corporations_corporation_id_assets_names_with_http_info(corporation_id, item_ids, **kwargs)
            return data

    def post_corporations_corporation_id_assets_names_with_http_info(self, corporation_id, item_ids, **kwargs):
        """Get corporation asset names

        Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships  ---  Requires one of the following EVE corporation role(s): Director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_corporations_corporation_id_assets_names_with_http_info(corporation_id, item_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int corporation_id: An EVE corporation ID (required)
        :param list[int] item_ids: A list of item ids (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['corporation_id', 'item_ids', 'datasource', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_corporations_corporation_id_assets_names" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'corporation_id' is set
        if self.api_client.client_side_validation and ('corporation_id' not in params or
                                                       params['corporation_id'] is None):
            raise ValueError("Missing the required parameter `corporation_id` when calling `post_corporations_corporation_id_assets_names`")
        # verify the required parameter 'item_ids' is set
        if self.api_client.client_side_validation and ('item_ids' not in params or
                                                       params['item_ids'] is None):
            raise ValueError("Missing the required parameter `item_ids` when calling `post_corporations_corporation_id_assets_names`")

        if self.api_client.client_side_validation and ('corporation_id' in params and params['corporation_id'] < 1):
            raise ValueError("Invalid value for parameter `corporation_id` when calling `post_corporations_corporation_id_assets_names`, must be a value greater than or equal to `1`")
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

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item_ids' in params:
            body_params = params['item_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v1/corporations/{corporation_id}/assets/names/', 'POST',
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