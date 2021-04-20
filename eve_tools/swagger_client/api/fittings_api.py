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


class FittingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_characters_character_id_fittings_fitting_id(self, character_id, fitting_id, **kwargs):
        """Delete fitting

        Delete a fitting from a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_characters_character_id_fittings_fitting_id(character_id, fitting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int fitting_id: ID for a fitting of this character (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_characters_character_id_fittings_fitting_id_with_http_info(character_id, fitting_id, **kwargs)
        else:
            (data) = self.delete_characters_character_id_fittings_fitting_id_with_http_info(character_id, fitting_id, **kwargs)
            return data

    def delete_characters_character_id_fittings_fitting_id_with_http_info(self, character_id, fitting_id, **kwargs):
        """Delete fitting

        Delete a fitting from a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_characters_character_id_fittings_fitting_id_with_http_info(character_id, fitting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param int fitting_id: ID for a fitting of this character (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'fitting_id', 'datasource', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_characters_character_id_fittings_fitting_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `delete_characters_character_id_fittings_fitting_id`")
        # verify the required parameter 'fitting_id' is set
        if self.api_client.client_side_validation and ('fitting_id' not in params or
                                                       params['fitting_id'] is None):
            raise ValueError("Missing the required parameter `fitting_id` when calling `delete_characters_character_id_fittings_fitting_id`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError("Invalid value for parameter `character_id` when calling `delete_characters_character_id_fittings_fitting_id`, must be a value greater than or equal to `1`")
        collection_formats = {}

        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']
        if 'fitting_id' in params:
            path_params['fitting_id'] = params['fitting_id']

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}

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
            '/v1/characters/{character_id}/fittings/{fitting_id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_characters_character_id_fittings(self, character_id, **kwargs):
        """Get fittings

        Return fittings of a character  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_fittings(character_id, async_req=True)
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
            return self.get_characters_character_id_fittings_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_fittings_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_fittings_with_http_info(self, character_id, **kwargs):
        """Get fittings

        Return fittings of a character  ---  This route is cached for up to 300 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_characters_character_id_fittings_with_http_info(character_id, async_req=True)
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
                    " to method get_characters_character_id_fittings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_fittings`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError("Invalid value for parameter `character_id` when calling `get_characters_character_id_fittings`, must be a value greater than or equal to `1`")
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
            '/v2/characters/{character_id}/fittings/', 'GET',
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

    def post_characters_character_id_fittings(self, character_id, fitting, **kwargs):
        """Create fitting

        Save a new fitting for a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_characters_character_id_fittings(character_id, fitting, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param Fitting fitting: Details about the new fitting (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_characters_character_id_fittings_with_http_info(character_id, fitting, **kwargs)
        else:
            (data) = self.post_characters_character_id_fittings_with_http_info(character_id, fitting, **kwargs)
            return data

    def post_characters_character_id_fittings_with_http_info(self, character_id, fitting, **kwargs):
        """Create fitting

        Save a new fitting for a character  --- 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_characters_character_id_fittings_with_http_info(character_id, fitting, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int character_id: An EVE character ID (required)
        :param Fitting fitting: Details about the new fitting (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use if unable to set a header
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'fitting', 'datasource', 'token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_characters_character_id_fittings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if self.api_client.client_side_validation and ('character_id' not in params or
                                                       params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `post_characters_character_id_fittings`")
        # verify the required parameter 'fitting' is set
        if self.api_client.client_side_validation and ('fitting' not in params or
                                                       params['fitting'] is None):
            raise ValueError("Missing the required parameter `fitting` when calling `post_characters_character_id_fittings`")

        if self.api_client.client_side_validation and ('character_id' in params and params['character_id'] < 1):
            raise ValueError("Invalid value for parameter `character_id` when calling `post_characters_character_id_fittings`, must be a value greater than or equal to `1`")
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
        if 'fitting' in params:
            body_params = params['fitting']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(
            '/v2/characters/{character_id}/fittings/', 'POST',
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