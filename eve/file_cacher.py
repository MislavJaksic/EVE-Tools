import os.path
import requests
import pathlib
import json
import datetime

relative_cache_path = "data/"


class FileCacher(object):
    def is_file_exists(self, filename):
        path = pathlib.Path(relative_cache_path + filename)
        if path.is_file():
            return True
        else:
            return False

    def get_uri_to_file_if_stale(self, uri, filename, stale_after):
        if not self.is_file_exists(filename) or not self.is_fresh(
            filename, stale_after
        ):
            try:
                response = requests.get(uri)
                json = response.json()
                self.save_json_to_file(json, filename)
            except:
                print("Response that caused an error:" + str(response))

        return self.load_json_from_file(filename)

    def is_fresh(self, filename, duration):
        if duration:
            creation_time = self.get_file_creation_time(relative_cache_path + filename)
            if datetime.date.today() > (creation_time + duration):
                return False

        return True

    def get_file_creation_time(self, path):
        return datetime.date.fromtimestamp(os.path.getctime(path))

    def save_json_to_file(self, json_data, filename):
        with open(relative_cache_path + filename, "w") as file:
            file.write(json.dumps(json_data))

    def load_json_from_file(self, filename):
        json_data = ""
        with open(relative_cache_path + filename, "r") as file:
            json_data = json.loads(file.read())

        return json_data
