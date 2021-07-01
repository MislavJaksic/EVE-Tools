import re
from datetime import datetime
from pathlib import Path
from typing import List

from loguru import logger

from eve_tools.chat.message import ChatChannelMessage
from eve_tools.chat.metadata import ChatChannelMetadata

log_message = "what={}, why={}, how={}"


class ChatChannelParser:
    def construct_metadata(self, chat_log_path: Path) -> ChatChannelMetadata:
        with open(chat_log_path.as_posix(), "r", encoding="utf-16") as file:
            head = [next(file) for _ in range(12)]
        try:
            return self.head_to_metadata(head)
        except AttributeError as error:
            logger.error(log_message, "Path: {}, Head: {}".format(chat_log_path, head),
                         "Failed to find channel id, name, listener and session start", "Regex")
            raise error

    def head_to_metadata(self, head: List[str]) -> ChatChannelMetadata:
        channel_id = re.search(":(.*)", head[6]).group(1).strip()
        channel_name = re.search(":(.*)", head[7]).group(1).strip()
        listener = re.search(":(.*)", head[8]).group(1).strip()
        session_started = self.string_to_date(
            re.search(":(.*)", head[9]).group(1).strip()
        )
        return ChatChannelMetadata(channel_id, channel_name, listener, session_started)

    def construct_messages(self, chat_log_path: Path) -> List[ChatChannelMessage]:
        messages = []
        with open(chat_log_path.as_posix(), "r", encoding="utf-16") as file:
            [next(file) for _ in range(12)]
            for line in file:
                try:
                    messages.append(self.line_to_message(line))
                except AttributeError as error:
                    logger.error(log_message, "Path: {}, Line: {}".format(chat_log_path, line),
                                 "Failed to find timestamp, character and text", "Regex")
                    raise error
        return messages

    def line_to_message(self, line: str) -> ChatChannelMessage:
        match = re.search("\[ ([0-9\.:\s]*) \] ([^>]*) >(.*)", line.strip())
        timestamp = self.string_to_date(match.group(1).strip())
        character = match.group(2).strip()
        text = match.group(3).strip()
        return ChatChannelMessage(timestamp, character, text)

    def string_to_date(self, string_time: str) -> datetime:
        return datetime.strptime(string_time, "%Y.%m.%d %H:%M:%S")
