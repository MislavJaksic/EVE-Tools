from eve_tools.helper.file_cache import FileCache
from eve_tools.helper.swaggerer import Swaggerer


class SwaggerApi:
    def __init__(self, swagger_uri, cache_path):
        self.swagger_uri = swagger_uri
        self.cache = FileCache(cache_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getattr__(self, attribute):
        if attribute == "swaggerer":
            value = Swaggerer(self.swagger_uri)
            setattr(self, attribute, value)
            return value
        else:
            raise AttributeError

    def get_json_from(self, get_operation_id, **parameters):
        key = self.create_key(get_operation_id, parameters)
        if self.cache.exists(key):
            response = self.cache.get(key)
        else:
            response = self.swaggerer.do(get_operation_id, **parameters)
            if response.status == 200:
                self.cache.set(key, response)
            else:
                raise Exception(response)
        return response.json

    def create_key(self, get_operation_id, parameters):
        return (get_operation_id, parameters)

    def close(self):
        self.cache.close()
