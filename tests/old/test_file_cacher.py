from tests import context

import pytest
import datetime
import json

from eve_tools.old import file_cacher


@pytest.fixture(scope="function")
def cache():
    cache = file_cacher.JsonFileCacher()
    yield cache


@pytest.fixture(scope="function")
def dir_path(tmp_path):
    dir_path = tmp_path / "sub_dir"
    dir_path.mkdir()
    yield dir_path


@pytest.fixture(scope="function")
def json_data():
    yield {"hello": "world"}


@pytest.fixture(scope="function")
def bad_path():
    yield "bad/file/path"


@pytest.fixture(scope="function")
def file_path(dir_path, json_data):
    file_path = dir_path / "file_path.json"
    file_path.write_text(json.dumps(json_data))
    yield file_path


# class TestGetUriToFileIfStale(object):
#     def test_get_uri_to_file_if_stale(self):
#         assert 0


class TestIsFileExists:
    def test_true(self, cache, file_path):
        assert cache.is_file_exists(file_path) == True

    def test_false(self, cache, bad_path):
        assert cache.is_file_exists(bad_path) == False


class TestIsFresh:
    def test_true(self, cache, file_path):
        max_age_days = datetime.timedelta(days=1)
        assert cache.is_file_fresh(file_path, max_age_days) == True

    def test_false(self, cache, file_path):
        max_age_days = datetime.timedelta(days=0)
        assert cache.is_file_fresh(file_path, max_age_days) == False

    def test_bad(self, cache, bad_path):
        max_age_days = datetime.timedelta(days=0)
        with pytest.raises(FileNotFoundError):
            cache.is_file_fresh(bad_path, max_age_days)


class TestGetFileCreationDate:
    def test_good(self, cache, file_path):
        assert cache.get_file_creation_date(file_path) == datetime.date.today()

    def test_bad(self, cache, bad_path):
        with pytest.raises(FileNotFoundError):
            cache.get_file_creation_date(bad_path)


class TestSaveJsonToFile:
    def test_good(self, cache, dir_path, json_data):
        file_path = dir_path / "test.json"
        cache.save_json_file_path(json_data, file_path)
        with open(file_path, "r") as file:
            assert json.loads(file.read()) == json_data


class TestLoadJsonFromFile:
    def test_good(self, cache, file_path, json_data):
        json_data_file = cache.load_json_file_path(file_path)
        assert json_data_file == json_data

    def test_bad(self, cache, bad_path):
        with pytest.raises(FileNotFoundError):
            cache.load_json_file_path(bad_path)
