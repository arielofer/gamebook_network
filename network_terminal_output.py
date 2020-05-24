from gamebook.output import Output
import json


class NetworkTerminalOutput(Output):
    def __init__(self, client):
        self.client = client

    def output(self, content="", message_type="output"):
        message = {"type": message_type, "data": content}
        message_string = json.dumps(message)
        self.client.send(bytes(message_string, 'utf-8'))

    def exit(self, exit_reason):
        self.output(exit_reason)
        self.client.close()
