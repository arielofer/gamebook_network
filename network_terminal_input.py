from gamebook.game_input import Input
from network_terminal_output import NetworkTerminalOutput
import json


class NetworkTerminalInput(Input):
    def __init__(self, client):
        self.client = client
        self.output_instance = NetworkTerminalOutput(client)

    def input(self, prompt):
        self.output_instance.output("input", prompt)
        answer_string = self.client.recv(1024)
        answer = json.loads(answer_string)
        if answer["type"] == "input-answer":
            return answer["data"]
