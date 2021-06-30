time_format = "%Y.%m.%d %H:%M:%S"


class ChatFilter:
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
