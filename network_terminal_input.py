from gamebook.game_input import Input
from network_terminal_output import NetworkTerminalOutput


class NetworkTerminalInput(Input):
    def __init__(self, client):
        self.client = client
        self.output_instance = NetworkTerminalOutput(client)

    def input(self, prompt):
        self.output_instance.output(bytes(prompt, 'utf-8'))
        return self.client.recv(1024)
