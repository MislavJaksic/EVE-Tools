# swagger_client.WarsApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wars**](WarsApi.md#get_wars) | **GET** /v1/wars/ | List wars
[**get_wars_war_id**](WarsApi.md#get_wars_war_id) | **GET** /v1/wars/{war_id}/ | Get war information
[**get_wars_war_id_killmails**](WarsApi.md#get_wars_war_id_killmails) | **GET** /v1/wars/{war_id}/killmails/ | List kills for a war


# **get_wars**
> list[int] get_wars(datasource=datasource, if_none_match=if_none_match, max_war_id=max_war_id)

List wars

Return a list of wars  ---  This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WarsApi()
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
max_war_id = 56 # int | Only return wars with ID smaller than this (optional)

try:
    # List wars
    api_response = api_instance.get_wars(datasource=datasource, if_none_match=if_none_match, max_war_id=max_war_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarsApi->get_wars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **max_war_id** | **int**| Only return wars with ID smaller than this | [optional] 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wars_war_id**
> object get_wars_war_id(war_id, datasource=datasource, if_none_match=if_none_match)

Get war information

Return details about a war  ---  This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WarsApi()
war_id = 56 # int | ID for a war
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get war information
    api_response = api_instance.get_wars_war_id(war_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarsApi->get_wars_war_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **war_id** | **int**| ID for a war | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wars_war_id_killmails**
> list[object] get_wars_war_id_killmails(war_id, datasource=datasource, if_none_match=if_none_match, page=page)

List kills for a war

Return a list of kills related to a war  ---  This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WarsApi()
war_id = 56 # int | A valid war ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)

try:
    # List kills for a war
    api_response = api_instance.get_wars_war_id_killmails(war_id, datasource=datasource, if_none_match=if_none_match, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarsApi->get_wars_war_id_killmails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **war_id** | **int**| A valid war ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

