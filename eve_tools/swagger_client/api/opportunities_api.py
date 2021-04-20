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


class OpportunitiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_characters_character_id_opportunities(self, character_id, **kwargs):
        """Get a character's completed tasks

        Return a list of tasks finished by a character  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_opportunities(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_characters_character_id_opportunities_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_opportunities_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_opportunities_with_http_info(self, character_id, **kwargs):
        """Get a character's completed tasks

        Return a list of tasks finished by a character  ---  This route is cached for up to 3600 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_opportunities_with_http_info(character_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str token: Access token to use if unable to set a header
        :return: list[object]
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
                    " to method get_characters_character_id_opportunities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_opportunities`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_opportunities`, must be a value greater than or equal to `1`")
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
            '/v1/characters/{character_id}/opportunities/', 'GET',
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

    def get_opportunities_groups(self, **kwargs):
        """Get opportunities groups

        Return a list of opportunities groups  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_opportunities_groups_with_http_info(**kwargs)
        else:
            (data) = self.get_opportunities_groups_with_http_info(**kwargs)
            return data

    def get_opportunities_groups_with_http_info(self, **kwargs):
        """Get opportunities groups

        Return a list of opportunities groups  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'if_none_match']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_opportunities_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/opportunities/groups/', 'GET',
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

    def get_opportunities_groups_group_id(self, group_id, **kwargs):
        """Get opportunities group

        Return information of an opportunities group  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_groups_group_id(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: ID of an opportunities group (required)
        :param str accept_language: Language to use in the response
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str language: Language to use in the response, takes precedence over Accept-Language
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_opportunities_groups_group_id_with_http_info(group_id, **kwargs)
        else:
            (data) = self.get_opportunities_groups_group_id_with_http_info(group_id, **kwargs)
            return data

    def get_opportunities_groups_group_id_with_http_info(self, group_id, **kwargs):
        """Get opportunities group

        Return information of an opportunities group  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_groups_group_id_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int group_id: ID of an opportunities group (required)
        :param str accept_language: Language to use in the response
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :param str language: Language to use in the response, takes precedence over Accept-Language
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'accept_language', 'datasource', 'if_none_match', 'language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_opportunities_groups_group_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in params or
                                                       params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_opportunities_groups_group_id`")

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'language' in params:
            query_params.append(('language', params['language']))

        header_params = {}
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
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
            '/v1/opportunities/groups/{group_id}/', 'GET',
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

    def get_opportunities_tasks(self, **kwargs):
        """Get opportunities tasks

        Return a list of opportunities tasks  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_tasks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_opportunities_tasks_with_http_info(**kwargs)
        else:
            (data) = self.get_opportunities_tasks_with_http_info(**kwargs)
            return data

    def get_opportunities_tasks_with_http_info(self, **kwargs):
        """Get opportunities tasks

        Return a list of opportunities tasks  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_tasks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'if_none_match']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_opportunities_tasks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/opportunities/tasks/', 'GET',
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

    def get_opportunities_tasks_task_id(self, task_id, **kwargs):
        """Get opportunities task

        Return information of an opportunities task  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_tasks_task_id(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int task_id: ID of an opportunities task (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_opportunities_tasks_task_id_with_http_info(task_id, **kwargs)
        else:
            (data) = self.get_opportunities_tasks_task_id_with_http_info(task_id, **kwargs)
            return data

    def get_opportunities_tasks_task_id_with_http_info(self, task_id, **kwargs):
        """Get opportunities task

        Return information of an opportunities task  ---  This route expires daily at 11:05
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_opportunities_tasks_task_id_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int task_id: ID of an opportunities task (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id', 'datasource', 'if_none_match']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_opportunities_tasks_task_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in params or
                                                       params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `get_opportunities_tasks_task_id`")

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task_id'] = params['task_id']

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
            '/v1/opportunities/tasks/{task_id}/', 'GET',
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
