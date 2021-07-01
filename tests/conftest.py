from datetime import datetime
from pathlib import Path

import pytest

from eve_tools.chat.channel import ChatChannel
from eve_tools.chat.collection import ChatChannelCollection
from eve_tools.chat.message import ChatChannelMessage
from eve_tools.chat.metadata import ChatChannelMetadata
from eve_tools.chat.parser import ChatChannelParser


@pytest.fixture(scope="package")
def parser():
    yield ChatChannelParser()


@pytest.fixture(scope="package")
def chat_log_dir():
    yield Path.cwd() / "tests/chat/logs"


@pytest.fixture(scope="package")
def chat_log_path():
    yield Path.cwd() / "tests/chat/logs/chatlog.txt"


@pytest.fixture(scope="package")
def metadata():
    yield ChatChannelMetadata("corp", "Corp", "EVE Pilot", datetime(2021, 2, 27, 13, 52, 46))


@pytest.fixture(scope="package")
def messages():
    yield [ChatChannelMessage(datetime(2021, 2, 27, 15, 2, 59), "Cader Audier", "thank you!"),
           ChatChannelMessage(datetime(2021, 2, 27, 15, 3, 5), "Azrayel1994", "yw"),
           ChatChannelMessage(datetime(2021, 2, 27, 15, 21, 19), "Axure", "Mining Upgrades (130,000)"),
           ChatChannelMessage(datetime(2021, 2, 27, 15, 22, 11), "RLoagan", "Axure on it")]


@pytest.fixture(scope="package")
def channels(chat_log_path, metadata, messages):
    yield [ChatChannel(chat_log_path, metadata, messages)]


@pytest.fixture(scope="package")
def collection(parser, chat_log_dir, channels):
    yield ChatChannelCollection(ChatChannelParser(), chat_log_dir, channels)
