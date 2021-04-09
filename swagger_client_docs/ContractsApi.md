# swagger_client.ContractsApi

All URIs are relative to *https://esi.evetech.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_characters_character_id_contracts**](ContractsApi.md#get_characters_character_id_contracts) | **GET** /v1/characters/{character_id}/contracts/ | Get contracts
[**get_characters_character_id_contracts_contract_id_bids**](ContractsApi.md#get_characters_character_id_contracts_contract_id_bids) | **GET** /v1/characters/{character_id}/contracts/{contract_id}/bids/ | Get contract bids
[**get_characters_character_id_contracts_contract_id_items**](ContractsApi.md#get_characters_character_id_contracts_contract_id_items) | **GET** /v1/characters/{character_id}/contracts/{contract_id}/items/ | Get contract items
[**get_contracts_public_bids_contract_id**](ContractsApi.md#get_contracts_public_bids_contract_id) | **GET** /v1/contracts/public/bids/{contract_id}/ | Get public contract bids
[**get_contracts_public_items_contract_id**](ContractsApi.md#get_contracts_public_items_contract_id) | **GET** /v1/contracts/public/items/{contract_id}/ | Get public contract items
[**get_contracts_public_region_id**](ContractsApi.md#get_contracts_public_region_id) | **GET** /v1/contracts/public/{region_id}/ | Get public contracts
[**get_corporations_corporation_id_contracts**](ContractsApi.md#get_corporations_corporation_id_contracts) | **GET** /v1/corporations/{corporation_id}/contracts/ | Get corporation contracts
[**get_corporations_corporation_id_contracts_contract_id_bids**](ContractsApi.md#get_corporations_corporation_id_contracts_contract_id_bids) | **GET** /v1/corporations/{corporation_id}/contracts/{contract_id}/bids/ | Get corporation contract bids
[**get_corporations_corporation_id_contracts_contract_id_items**](ContractsApi.md#get_corporations_corporation_id_contracts_contract_id_items) | **GET** /v1/corporations/{corporation_id}/contracts/{contract_id}/items/ | Get corporation contract items


# **get_characters_character_id_contracts**
> list[object] get_characters_character_id_contracts(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get contracts

Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \"in_progress\".  ---  This route is cached for up to 300 seconds

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get contracts
    api_response = api_instance.get_characters_character_id_contracts(character_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_characters_character_id_contracts: %s\n" % e)
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

# **get_characters_character_id_contracts_contract_id_bids**
> list[object] get_characters_character_id_contracts_contract_id_bids(character_id, contract_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get contract bids

Lists bids on a particular auction contract  ---  This route is cached for up to 300 seconds

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
contract_id = 56 # int | ID of a contract
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get contract bids
    api_response = api_instance.get_characters_character_id_contracts_contract_id_bids(character_id, contract_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_characters_character_id_contracts_contract_id_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **contract_id** | **int**| ID of a contract | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**list[object]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_character_id_contracts_contract_id_items**
> list[object] get_characters_character_id_contracts_contract_id_items(character_id, contract_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get contract items

Lists items of a particular contract  ---  This route is cached for up to 3600 seconds

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
character_id = 56 # int | An EVE character ID
contract_id = 56 # int | ID of a contract
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get contract items
    api_response = api_instance.get_characters_character_id_contracts_contract_id_items(character_id, contract_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_characters_character_id_contracts_contract_id_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **character_id** | **int**| An EVE character ID | 
 **contract_id** | **int**| ID of a contract | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**list[object]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts_public_bids_contract_id**
> list[object] get_contracts_public_bids_contract_id(contract_id, datasource=datasource, if_none_match=if_none_match, page=page)

Get public contract bids

Lists bids on a public auction contract  ---  This route is cached for up to 300 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
contract_id = 56 # int | ID of a contract
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)

try:
    # Get public contract bids
    api_response = api_instance.get_contracts_public_bids_contract_id(contract_id, datasource=datasource, if_none_match=if_none_match, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contracts_public_bids_contract_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of a contract | 
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

# **get_contracts_public_items_contract_id**
> list[object] get_contracts_public_items_contract_id(contract_id, datasource=datasource, if_none_match=if_none_match, page=page)

Get public contract items

Lists items of a public contract  ---  This route is cached for up to 3600 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
contract_id = 56 # int | ID of a contract
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)

try:
    # Get public contract items
    api_response = api_instance.get_contracts_public_items_contract_id(contract_id, datasource=datasource, if_none_match=if_none_match, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contracts_public_items_contract_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of a contract | 
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

# **get_contracts_public_region_id**
> list[object] get_contracts_public_region_id(region_id, datasource=datasource, if_none_match=if_none_match, page=page)

Get public contracts

Returns a paginated list of all public contracts in the given region  ---  This route is cached for up to 1800 seconds

### Example
```python
from __future__ import print_function
import time
from eve_tools import swagger_client
from eve_tools.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
region_id = 56 # int | An EVE region id
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)

try:
    # Get public contracts
    api_response = api_instance.get_contracts_public_region_id(region_id, datasource=datasource, if_none_match=if_none_match, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contracts_public_region_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **int**| An EVE region id | 
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

# **get_corporations_corporation_id_contracts**
> list[object] get_corporations_corporation_id_contracts(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation contracts

Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \"in_progress\".  ---  This route is cached for up to 300 seconds

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation contracts
    api_response = api_instance.get_corporations_corporation_id_contracts(corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_corporations_corporation_id_contracts: %s\n" % e)
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

# **get_corporations_corporation_id_contracts_contract_id_bids**
> list[object] get_corporations_corporation_id_contracts_contract_id_bids(contract_id, corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)

Get corporation contract bids

Lists bids on a particular auction contract  ---  This route is cached for up to 3600 seconds

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
contract_id = 56 # int | ID of a contract
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
page = 1 # int | Which page of results to return (optional) (default to 1)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation contract bids
    api_response = api_instance.get_corporations_corporation_id_contracts_contract_id_bids(contract_id, corporation_id, datasource=datasource, if_none_match=if_none_match, page=page, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_corporations_corporation_id_contracts_contract_id_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of a contract | 
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

# **get_corporations_corporation_id_contracts_contract_id_items**
> list[object] get_corporations_corporation_id_contracts_contract_id_items(contract_id, corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)

Get corporation contract items

Lists items of a particular contract  ---  This route is cached for up to 3600 seconds

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
contract_id = 56 # int | ID of a contract
corporation_id = 56 # int | An EVE corporation ID
datasource = 'tranquility' # str | The server name you would like data from (optional) (default to tranquility)
if_none_match = 'if_none_match_example' # str | ETag from a previous request. A 304 will be returned if this matches the current ETag (optional)
token = 'token_example' # str | Access token to use if unable to set a header (optional)

try:
    # Get corporation contract items
    api_response = api_instance.get_corporations_corporation_id_contracts_contract_id_items(contract_id, corporation_id, datasource=datasource, if_none_match=if_none_match, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_corporations_corporation_id_contracts_contract_id_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of a contract | 
 **corporation_id** | **int**| An EVE corporation ID | 
 **datasource** | **str**| The server name you would like data from | [optional] [default to tranquility]
 **if_none_match** | **str**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **str**| Access token to use if unable to set a header | [optional] 

### Return type

**list[object]**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

