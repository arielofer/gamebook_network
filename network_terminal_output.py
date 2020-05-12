from gamebook.output import Output


class NetworkTerminalOutput(Output):
    def __init__(self, client):
        self.client = client

    def output(self, content):
        if content == "":
            self.client.send(b"no content recieved")
        else:
            self.client.send(content)
