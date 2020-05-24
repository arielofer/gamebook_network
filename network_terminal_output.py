from gamebook.output import Output
import json


class NetworkTerminalOutput(Output):
    def __init__(self, client):
        self.client = client

    def output(self, message_type, content):
        message = {"type": message_type, "data": content}
        message_string = json.dumps(message)
        self.client.send(bytes(message_string, 'utf-8'))
