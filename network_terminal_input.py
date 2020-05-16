from gamebook.game_input import Input


class NetworkTerminalInput(Input):
    def __init__(self, client):
        self.client = client

    def input(self, prompt):
        self.client.send(bytes(prompt, 'utf-8'))
        return self.client.recv(1024)
