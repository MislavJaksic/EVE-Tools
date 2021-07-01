from pathlib import Path
from typing import List

from eve_tools.chat.message import ChatChannelMessage
from eve_tools.chat.metadata import ChatChannelMetadata


class ChatChannel:
    def __init__(self, chat_log_path: Path, metadata: ChatChannelMetadata, messages: List[ChatChannelMessage]):
        self.chat_log_path = chat_log_path
        self.metadata = metadata
        self.messages = messages

    def filter_by_character(self, name: str):
        return ChatChannel(self.chat_log_path, self.metadata, [x for x in self.messages if name in x.character])

    def is_empty(self) -> bool:
        if self.messages:
            return False
        return True

    def __eq__(self, other):
        if self.chat_log_path == other.chat_log_path:
            if self.metadata == other.metadata:
                if self.messages == other.messages:
                    return True
        return False

    def __str__(self):
        return "Metadata:\n{}\nMessage:\n{}".format(self.metadata, "\n".join([str(x) for x in self.messages]))
