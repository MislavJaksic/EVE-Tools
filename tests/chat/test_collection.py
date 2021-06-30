from datetime import datetime
from pathlib import Path

import pytest

from eve_tools.chat.channel import ChatChannel
from eve_tools.chat.collection import ChatChannelCollection
from eve_tools.chat.message import ChatChannelMessage
from eve_tools.chat.metadata import ChatChannelMetadata
from eve_tools.chat.parser import ChatChannelParser


@pytest.fixture(scope="function")
def chat_log_dir():
    chat_file = Path.cwd() / "tests/chat/logs"
    yield chat_file.as_posix()


@pytest.fixture(scope="function")
def collection(chat_log_dir):
    path = Path.cwd() / "tests/chat/logs/chatlog.txt"
    metadata = ChatChannelMetadata("corp", "Corp", "EVE Pilot", datetime(2021, 2, 27, 13, 52, 46))
    messages = [ChatChannelMessage(datetime(2021, 2, 27, 15, 2, 59), "Cader Audier", "thank you!"),
                ChatChannelMessage(datetime(2021, 2, 27, 15, 3, 5), "Azrayel1994", "yw"),
                ChatChannelMessage(datetime(2021, 2, 27, 15, 21, 19), "Axure", "Mining Upgrades (130,000)"),
                ChatChannelMessage(datetime(2021, 2, 27, 15, 22, 11), "RLoagan", "Axure on it")]
    channels = [ChatChannel(path.as_posix(), metadata, messages)]
    yield ChatChannelCollection(ChatChannelParser(), chat_log_dir, channels)


class TestConstructChannels:
    def test_construct_channels(self, collection):
        path = Path.cwd() / "tests/chat/logs/chatlog.txt"
        assert collection.construct_channels() == [path]

# class TestGetFilePaths:
#     def test_get_file_paths(self, collection):
#         assert collection.get_file_paths() == None
#
# class TestFilterByChannelName:
#     def test_filter_by_channel_name(self, collection):
#         name = None
#         assert collection.filter_by_channel_name(name) == None
