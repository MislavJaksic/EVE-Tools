from typing import List

from eve_tools.chat.message import ChatChannelMessage
from eve_tools.chat.metadata import ChatChannelMetadata


class ChatChannel:
    def __init__(self, chat_log_path: str, metadata: ChatChannelMetadata, messages: List[ChatChannelMessage]):
        self.chat_log_path = chat_log_path
        self.metadata = metadata
        self.messages = messages

    def __str__(self):
        return "{} \n Message count: {}\n".format(str(self.metadata), str(len(self.messages)))