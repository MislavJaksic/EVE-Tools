from datetime import datetime


class ChatChannelMessage:
    def __init__(self, timestamp: datetime, character: str, text: str):
        self.timestamp = timestamp
        self.character = character
        self.text = text

    def __eq__(self, other):
        if self.timestamp == other.timestamp:
            if self.character == other.character:
                if self.text == other.text:
                    return True
        return False

    def __str__(self):
        return "[ {} ] {} > {}".format(str(self.timestamp), self.character, self.text)

    def __repr__(self):
        return self.__str__()
