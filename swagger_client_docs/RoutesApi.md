# swagger_client.RoutesApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_route_origin_destination**](RoutesApi.md#get_route_origin_destination) | **GET** /v1/route/{origin}/{destination}/ | Get route


# **get_route_origin_destination**
> list[int] get_route_origin_destination(destination, origin, avoid=avoid, connections=connections, datasource=datasource, flag=flag, if_none_match=if_none_match)

Get route

Get the systems between origin and destination  ---  This route is cached for up to 86400 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoutesApi()
destination = 56 # int | destination solar system ID
origin = 56 # int | origin solar system ID
avoid = [56] # list[int] | avoid solar system ID(s) (optional)
connections = [swagger_client.list[int]()] # list[list[int]] | connected solar system pairs (optional)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
flag = 'shortest' # str | route security preference (optional) (default to shortest)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get route
    api_response = api_instance.get_route_origin_destination(destination, origin, avoid=avoid, connections=connections, datasource=datasource, flag=flag, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->get_route_origin_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **int**| destination solar system ID | 
 **origin** | **int**| origin solar system ID | 
 **avoid** | [**list[int]**](int.md)| avoid solar system ID(s) | [optional] 
 **connections** | [**list[list[int]]**](list[int].md)| connected solar system pairs | [optional] 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **flag** | **str**| route security preference | [optional] [default to shortest]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

