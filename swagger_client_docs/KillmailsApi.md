# swagger_client.KillmailsApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_killmails_recent**](KillmailsApi.md#get_characters_character_id_killmails_recent) | **GET** /v1/characters/{character_id}/killmails/recent/ | Get a character&#39;s recent kills and losses
[**get_corporations_corporation_id_killmails_recent**](KillmailsApi.md#get_corporations_corporation_id_killmails_recent) | **GET** /v1/corporations/{corporation_id}/killmails/recent/ | Get a corporation&#39;s recent kills and losses
[**get_killmails_killmail_id_killmail_hash**](KillmailsApi.md#get_killmails_killmail_id_killmail_hash) | **GET** /v1/killmails/{killmail_id}/{killmail_hash}/ | Get a single killmail


# **get_characters_character_id_killmails_recent**
> list[object] get_characters_character_id_killmails_recent(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get a character's recent kills and losses

Return a list of a character's kills and losses going back 90 days  ---  This route is cached for up to 300 seconds

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
api_instance = swagger_client.KillmailsApi(swagger_client.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get a character's recent kills and losses
    api_response = api_instance.get_characters_character_id_killmails_recent(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KillmailsApi->get_characters_character_id_killmails_recent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**list[object]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporations_corporation_id_killmails_recent**
> list[object] get_corporations_corporation_id_killmails_recent(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get a corporation's recent kills and losses

Get a list of a corporation's kills and losses going back 90 days  ---  This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Director

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
api_instance = swagger_client.KillmailsApi(swagger_client.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get a corporation's recent kills and losses
    api_response = api_instance.get_corporations_corporation_id_killmails_recent(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KillmailsApi->get_corporations_corporation_id_killmails_recent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **page** | **int**| Which page of results to return | [optional] [default to 1]
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**list[object]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_killmails_killmail_id_killmail_hash**
> object get_killmails_killmail_id_killmail_hash(killmail_hash, killmail_id, datasource=datasource, if_none_match=if_none_match)

Get a single killmail

Return a single killmail from its ID and hash  ---  This route is cached for up to 30758400 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KillmailsApi()
killmail_hash = 'killmail_hash_example' # str | The killmail hash for verification
killmail_id = 56 # int | The killmail ID to be queried
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)

try:
    # Get a single killmail
    api_response = api_instance.get_killmails_killmail_id_killmail_hash(killmail_hash, killmail_id, datasource=datasource, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KillmailsApi->get_killmails_killmail_id_killmail_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **killmail_hash** | **str**| The killmail hash for verification | 
 **killmail_id** | **int**| The killmail ID to be queried | 
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

