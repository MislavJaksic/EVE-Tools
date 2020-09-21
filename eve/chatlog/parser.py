from os import listdir
from os.path import isfile, join
from datetime import datetime
import codecs
import re

directory = "C:/Users/Korisnik/Documents/EVE/logs/Chatlogs"
time_format = "%Y.%m.%d %H:%M:%S"


class ChatFilter(object):
    def __init__(self, chat_channel):
        self.chat_channel = chat_channel

    def print_channel(self):
        if not self._is_channel_name():
            return
        print(self.chat_channel)

    def get_messages(self):
        list = []
        if not self._is_channel_name():
            return list
        for message in self.chat_channel.messages:
            if self._is_message_in_datetime(message):
                list.append(message)
        return list

    def _is_channel_name(self):
        if self.filter_channel_name == self.chat_channel.metadata.channel_name:
            return True
        return False

    def _is_message_in_datetime(self, message):
        if self._is_message_after_start_datetime(message):
            if self._is_message_before_end_datetime(message):
                return True
        return False

    def _is_message_after_start_datetime(self, message):
        if self.filter_start_datetime:
            if message.timestamp >= self.filter_start_datetime:
                return True
            else:
                return False
        return True

    def _is_message_before_end_datetime(self, message):
        if self.filter_end_datetime:
            if message.timestamp <= self.filter_end_datetime:
                return True
            else:
                return False
        return True

    def filter_channel_name(self, channel_name):
        self.filter_channel_name = channel_name

    def filter_start_datetime(self, string_time):
        self.filter_start_datetime = datetime.strptime(string_time, time_format)

    def filter_end_datetime(self, string_time):
        self.filter_end_datetime = datetime.strptime(string_time, time_format)


class ChatChannel(object):
    def __init__(self, file):
        self.metadata = ChatChannelMetadata(file)
        self.messages = []
        for line in file:
            self.messages.append(ChatLogMessage(line))

    def __str__(self):
        output = "--- Metadata ---" + "\n"
        output = output + str(self.metadata) + "\n"
        output = output + "--- Metadata ---" + "\n"
        output = output + "Message count:" + str(len(self.messages)) + "\n"

        return output


class ChatChannelMetadata(object):
    def __init__(self, file):
        head = [next(file) for x in range(12)]
        self.channel_id = re.search(":(.*)", head[6]).group(1).strip()
        self.channel_name = re.search(":(.*)", head[7]).group(1).strip()
        self.listener = re.search(":(.*)", head[8]).group(1).strip()
        self.session_started = self._string_to_date(
            re.search(":(.*)", head[9]).group(1).strip()
        )

    def _string_to_date(self, string_time):
        return datetime.strptime(string_time, "%Y.%m.%d %H:%M:%S")

    def __str__(self):
        output = ""
        output = output + "Channel ID:" + self.channel_id + "\n"
        output = output + "Channel Name:" + self.channel_name + "\n"
        output = output + "Listener:" + self.listener + "\n"
        output = output + "Session started:" + str(self.session_started)
        return output


class ChatLogMessage(object):
    def __init__(self, line):
        match = re.search("\[ ([0-9\.:\s]*) \] ([^>]*) >(.*)", line.strip())
        if match:
            self.timestamp = self._string_to_date(match.group(1).strip())
            self.character = match.group(2).strip()
            self.text = match.group(3).strip()

    def _string_to_date(self, string_time):
        return datetime.strptime(string_time, time_format)

    def __str__(self):
        output = ""
        output = output + "[ " + str(self.timestamp) + " ] "
        output = output + self.character + " > "
        output = output + self.text
        return output


file_paths = [f for f in listdir(directory) if isfile(join(directory, f))]

for file_path in file_paths:
    with codecs.open(directory + "/" + file_path, "r", encoding="utf-16") as file:
        channel = ChatChannel(file)

        channel_name = "Fleet"
        start_time = "2020.09.20 18:55:00"
        end_time = "2020.09.20 22:05:00"

        filter = ChatFilter(channel)
        filter.filter_channel_name(channel_name)
        filter.filter_start_datetime(start_time)
        filter.filter_end_datetime(end_time)

        filter.print_channel()
        messages = filter.get_messages()

        for message in messages:
            match = re.search("^(\d*) - ([^-]*) - ([^-]*)", message.text.strip())
            if match:
                level = match.group(1).strip()
                type = match.group(2).strip()
                corp = match.group(3).strip()

                output = ""
                output = output + str(message.timestamp) + "|"
                output = output + str(message.character) + "|"
                output = output + str(level) + "|"
                output = output + str(type) + "|"
                output = output + str(corp) + "|"
                print(output)
