from gamebook.output import Output


class NetworkTerminalOutput(Output):
    def __init__(self, client):
        self.client = client

    def output(self, content):
        if content == "":
            self.client.send(bytes("no content recieved", 'utf-8'))
        else:
            self.client.send(content)
