# swagger_client.SearchApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_search**](SearchApi.md#get_characters_character_id_search) | **GET** /v3/characters/{character_id}/search/ | Search on a string
[**get_search**](SearchApi.md#get_search) | **GET** /v2/search/ | Search on a string


# **get_characters_character_id_search**
> object get_characters_character_id_search(categories, character_id, search, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, strict=strict, token=token)

Search on a string

Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: evesso
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
categories = ['categories_example'] # list[str] | Type of entities to search for
character_id = 56 # int | An EVE character ID
search = 'search_example' # str | The string to search on
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)
strict = false # bool | Whether the search should be a strict match (optional) (default to false)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Search on a string
    api_response = api_instance.get_characters_character_id_search(categories, character_id, search, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, strict=strict, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_characters_character_id_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categories** | [**list[str]**](str.md)| Type of entities to search for | 
 **character_id** | **int**| An EVE character ID | 
 **search** | **str**| The string to search on | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]
 **strict** | **bool**| Whether the search should be a strict match | [optional] [default to false]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**object**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search**
> object get_search(categories, search, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, strict=strict)

Search on a string

Search for entities that match a given sub-string.  ---  This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
categories = ['categories_example'] # list[str] | Type of entities to search for
search = 'search_example' # str | The string to search on
accept_language = 'en' # str | Language to use in the response (optional) (default to en)
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
language = 'en' # str | Language to use in the response, takes precedence over Accept-Language (optional) (default to en)
strict = false # bool | Whether the search should be a strict match (optional) (default to false)

try:
    # Search on a string
    api_response = api_instance.get_search(categories, search, accept_language=accept_language, datasource=datasource, if_none_match=if_none_match, language=language, strict=strict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categories** | [**list[str]**](str.md)| Type of entities to search for | 
 **search** | **str**| The string to search on | 
 **accept_language** | **str**| Language to use in the response | [optional] [default to en]
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **language** | **str**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en]
 **strict** | **bool**| Whether the search should be a strict match | [optional] [default to false]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

