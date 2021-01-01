import os.path
import pathlib
import json
import datetime


class JsonFileCacher:
    def get_uri_to_file_if_stale(self, uri, file_path, max_age_days):
        if not self.is_file_exists(file_path):
            if not self.is_file_fresh(file_path, max_age_days):
                try:
                    response = requests.get(uri)
                    json = response.json()
                    self.save_json_file_path(json, file_path)
                except:
                    print("Response that caused an error:" + str(response))

        return self.load_json_file_path(file_path)

    def is_file_exists(self, file_path):
        path = pathlib.Path(file_path)
        if path.is_file():
            return True
        else:
            return False

    def is_file_fresh(self, file_path, max_age_days):
        creation_datetime = self.get_file_creation_date(file_path)
        if datetime.date.today() < (creation_datetime + max_age_days):
            return True
        else:
            return False

    def get_file_creation_date(self, file_path):
        return datetime.date.fromtimestamp(os.path.getctime(file_path))

    def save_json_file_path(self, json_data, file_path):
        with open(file_path, "w") as file:
            file.write(json.dumps(json_data))

    def load_json_file_path(self, file_path):
        with open(file_path, "r") as file:
            return json.loads(file.read())
