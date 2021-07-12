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


class WarsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_wars(self, **kwargs):
        """List wars

        Return a list of wars  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wars(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int max_war_id: Only return wars with ID smaller than this
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_wars_with_http_info(**kwargs)
        else:
            (data) = self.get_wars_with_http_info(**kwargs)
            return data

    def get_wars_with_http_info(self, **kwargs):
        """List wars

        Return a list of wars  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wars_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int max_war_id: Only return wars with ID smaller than this
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'if_none_match', 'max_war_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wars" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'max_war_id' in params:
            query_params.append(('max_war_id', params['max_war_id']))

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
        auth_settings = []

        return self.api_client.call_api(
            '/v1/wars/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wars_war_id(self, war_id, **kwargs):
        """Get war information

        Return details about a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wars_war_id(war_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int war_id: ID for a war (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_wars_war_id_with_http_info(war_id, **kwargs)
        else:
            (data) = self.get_wars_war_id_with_http_info(war_id, **kwargs)
            return data

    def get_wars_war_id_with_http_info(self, war_id, **kwargs):
        """Get war information

        Return details about a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wars_war_id_with_http_info(war_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int war_id: ID for a war (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['war_id', 'datasource', 'if_none_match']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wars_war_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'war_id' is set
        if self.api_client.client_side_validation and ('war_id' not in params or
                                                       params['war_id'] is None):
            raise ValueError("Missing the required parameter `war_id` when calling `get_wars_war_id`")

        if self.api_client.client_side_validation and ('war_id' in params and params['war_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `war_id` when calling `get_wars_war_id`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'war_id' in params:
            path_params['war_id'] = params['war_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))

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
        auth_settings = []

        return self.api_client.call_api(
            '/v1/wars/{war_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wars_war_id_killmails(self, war_id, **kwargs):
        """List kills for a war

        Return a list of kills related to a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wars_war_id_killmails(war_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int war_id: A valid war ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async_req'):
            return self.get_wars_war_id_killmails_with_http_info(war_id, **kwargs)
        else:
            (data) = self.get_wars_war_id_killmails_with_http_info(war_id, **kwargs)
            return data

    def get_wars_war_id_killmails_with_http_info(self, war_id, **kwargs):
        """List kills for a war

        Return a list of kills related to a war  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wars_war_id_killmails_with_http_info(war_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int war_id: A valid war ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param int page: Which page of results to return
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['war_id', 'datasource', 'if_none_match', 'page']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wars_war_id_killmails" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'war_id' is set
        if self.api_client.client_side_validation and ('war_id' not in params or
                                                       params['war_id'] is None):
            raise ValueError("Missing the required parameter `war_id` when calling `get_wars_war_id_killmails`")

        if self.api_client.client_side_validation and ('war_id' in params and params['war_id'] < 1):
            raise ValueError(
                "Invalid value for parameter `war_id` when calling `get_wars_war_id_killmails`, must be a value greater than or equal to `1`")
        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):
            raise ValueError(
                "Invalid value for parameter `page` when calling `get_wars_war_id_killmails`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'war_id' in params:
            path_params['war_id'] = params['war_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'page' in params:
            query_params.append(('page', params['page']))

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
        auth_settings = []

        return self.api_client.call_api(
            '/v1/wars/{war_id}/killmails/', 'GET',
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
