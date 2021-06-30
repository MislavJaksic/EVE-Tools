import codecs
import re
from datetime import datetime
from typing import List

from loguru import logger

from eve_tools.chat.message import ChatChannelMessage
from eve_tools.chat.metadata import ChatChannelMetadata

log_message = "what={}, why={}, how={}"


class ChatChannelParser:
    def construct_metadata(self, chat_log_path: str) -> ChatChannelMetadata:
        with codecs.open(chat_log_path, "r", encoding="utf-16") as file:
            head = [next(file) for _ in range(12)]
        return self.head_to_metadata(head)

    def head_to_metadata(self, head: List[str]) -> ChatChannelMetadata:
        logger.info(log_message, head, "Finding channel id, name, listener and session start", "Regex")

        channel_id = re.search(":(.*)", head[6]).group(1).strip()
        channel_name = re.search(":(.*)", head[7]).group(1).strip()
        listener = re.search(":(.*)", head[8]).group(1).strip()
        session_started = self.string_to_date(
            re.search(":(.*)", head[9]).group(1).strip()
        )

        return ChatChannelMetadata(channel_id, channel_name, listener, session_started)

    def construct_messages(self, chat_log_path: str) -> List[ChatChannelMessage]:
        with codecs.open(chat_log_path, "r", encoding="utf-16") as file:
            [next(file) for _ in range(12)]
            return [self.line_to_message(line) for line in file]

    def line_to_message(self, line: str) -> ChatChannelMessage:
        logger.info(log_message, line, "Finding timestamp, character and text", "Regex")

        match = re.search("\[ ([0-9\.:\s]*) \] ([^>]*) >(.*)", line.strip())
        timestamp = self.string_to_date(match.group(1).strip())
        character = match.group(2).strip()
        text = match.group(3).strip()

        return ChatChannelMessage(timestamp, character, text)

    def string_to_date(self, string_time: str) -> datetime:
        logger.info(log_message, string_time, "Inspection", "Parsing")

        return datetime.strptime(string_time, "%Y.%m.%d %H:%M:%S")