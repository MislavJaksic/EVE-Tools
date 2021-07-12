from os import listdir
from pathlib import Path
from typing import List

from eve_tools.chat.channel import ChatChannel
from eve_tools.chat.parser import ChatChannelParser


class ChatChannelCollection:
    """
    parser = ChatChannelParser()
    collection = ChatChannelCollection(parser, Path("C:/Users/Korisnik/Documents/EVE/logs/Chatlogs"), [])
    collection = collection.filter_by_character("EVE Pilot")
    for channel in collection.channels:
        print(channel)
    """

    def __init__(self, parser: ChatChannelParser, chat_log_dir: Path, channels: List[ChatChannel]):
        self.parser = parser
        self.chat_log_dir = chat_log_dir
        if channels:
            self.channels = channels
        else:
            self.channels = self.construct_channels()

    def construct_channels(self) -> List[ChatChannel]:
        return [ChatChannel(path, self.parser.construct_metadata(path), self.parser.construct_messages(path)) for path
                in self.get_file_paths()]

    def get_file_paths(self) -> List[Path]:
        return [Path.joinpath(self.chat_log_dir, x) for x in listdir(self.chat_log_dir)]

    def filter_by_channel_name(self, name: str):
        return ChatChannelCollection(self.parser, self.chat_log_dir,
                                     [x for x in self.channels if name in x.metadata.channel_name])

    def filter_by_character(self, name: str):
        filtered_channels = [x.filter_by_character(name) for x in self.channels]
        return ChatChannelCollection(self.parser, self.chat_log_dir, [x for x in filtered_channels if not x.is_empty()])
