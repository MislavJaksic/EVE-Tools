from os import listdir
from os.path import isfile, join
from typing import List

from eve_tools.chat.channel import ChatChannel
from eve_tools.chat.parser import ChatChannelParser


class ChatChannelCollection:
    def __init__(self, parser: ChatChannelParser, chat_log_dir: str, channels: List[ChatChannel]):
        self.parser = parser
        self.chat_log_dir = chat_log_dir
        if channels:
            self.channels = channels
        else:
            self.channels = self.construct_channels()

    def construct_channels(self) -> List[ChatChannel]:
        return [ChatChannel(path, self.parser.construct_metadata(path), self.parser.construct_messages(path)) for path in self.get_file_paths()]

    def get_file_paths(self) -> List[str]:
        return [x for x in listdir(self.chat_log_dir) if isfile(join(self.chat_log_dir, x))]

    def filter_by_channel_name(self, name: str):
        self.channels = [x for x in self.channels if name in x.metadata.channel_name]

# for file_path in file_paths:
#     with  as file:
#         channel = ChatChannel(file)
#
#         channel_name = "Fleet"
#         start_time = "2020.10.23 00:00:00"
#         end_time = "2020.10.25 00:00:00"
#
#         filter = ChatFilter(channel)
#         filter.filter_channel_name(channel_name)
#         filter.filter_start_datetime(start_time)
#         filter.filter_end_datetime(end_time)
#
#         filter.print_channel()
#         messages = filter.get_messages()
#
#         for message in messages:
#             match = re.search("^(\d*) - ([^-]*) - ([^-]*)", message.text.strip())
#             if match:
#                 level = match.group(1).strip()
#                 type = match.group(2).strip()
#                 corp = match.group(3).strip()
#
#                 output = ""
#                 output = output + str(message.timestamp) + "|"
#                 output = output + str(message.character) + "|"
#                 output = output + str(level) + "|"
#                 output = output + str(type) + "|"
#                 output = output + str(corp) + "|"
#                 print(output)