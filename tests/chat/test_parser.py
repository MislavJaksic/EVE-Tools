from datetime import datetime

import pytest

from eve_tools.chat.message import ChatChannelMessage
from eve_tools.chat.metadata import ChatChannelMetadata


class TestConstructMetadata:
    def test_construct_metadata(self, parser, chat_log_path):
        assert parser.construct_metadata(chat_log_path) == ChatChannelMetadata("corp", "Corp", "EVE Pilot",
                                                                               datetime(2021, 2, 27, 13, 52, 46))


class TestHeadToMetadata:
    def test_head_to_metadata(self, parser):
        head = ["",
                "",
                "",
                "",
                "        ---------------------------------------------------------------",
                "",
                "          Channel ID:      corp",
                "          Channel Name:    Corp",
                "          Listener:        EVE Pilot",
                "          Session started: 2021.02.27 13:52:46",
                "        ---------------------------------------------------------------",
                "",
                ]
        assert parser.head_to_metadata(head) == ChatChannelMetadata("corp", "Corp", "EVE Pilot",
                                                                    datetime(2021, 2, 27, 13, 52, 46))

    def test_index_exception(self, parser):
        head = [""]
        with pytest.raises(IndexError):
            parser.head_to_metadata(head)

    def test_parse_exception(self, parser):
        head = ["", "", "", "", "", "", "", "", "", "", "", ""]
        with pytest.raises(AttributeError):
            parser.head_to_metadata(head)


class TestConstructMessages:
    def test_construct_messages(self, parser, chat_log_path, messages):
        assert parser.construct_messages(chat_log_path) == messages


class TestLineToMessage:
    def test_parse_utf_16(self, parser):
        line = "﻿[ 2021.02.27 15:22:11 ] RLoagan > Axure on it"
        assert parser.line_to_message(line) == ChatChannelMessage(datetime(2021, 2, 27, 15, 22, 11), "RLoagan",
                                                                  "Axure on it")

    def test_exception(self, parser):
        line = "bla bla"
        with pytest.raises(AttributeError):
            parser.line_to_message(line)


class TestStringToDate:
    def test_success(self, parser):
        string_time = "2021.02.27 13:52:48"
        assert parser.string_to_date(string_time) == datetime(2021, 2, 27, 13, 52, 48)

    def test_bad_format(self, parser):
        string_time = "13:52"
        with pytest.raises(ValueError):
            parser.string_to_date(string_time)
