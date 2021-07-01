class TestConstructChannels:
    def test_construct_channels(self, collection, channels):
        assert collection.construct_channels() == channels


class TestGetFilePaths:
    def test_get_file_paths(self, collection, chat_log_path):
        assert collection.get_file_paths() == [chat_log_path]

# class TestFilterByChannelName:
#     def test_filter_by_channel_name(self, collection):
#         name = None
#         assert collection.filter_by_channel_name(name) == None
