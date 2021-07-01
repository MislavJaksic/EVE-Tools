from datetime import datetime


class ChatChannelMetadata:
    def __init__(self, channel_id: str, channel_name: str, listener: str, session_started: datetime):
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.listener = listener
        self.session_started = session_started

    def __eq__(self, other):
        if self.channel_id == other.channel_id:
            if self.channel_name == other.channel_name:
                if self.listener == other.listener:
                    if self.session_started == other.session_started:
                        return True
        return False

    def __str__(self):
        return "Channel ID: {}\nChannel Name: {} \nListener:{} \nSession started: {}".format(self.channel_id,
                                                                                                self.channel_name,
                                                                                                self.listener, str(
                self.session_started))
