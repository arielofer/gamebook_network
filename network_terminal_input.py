from gamebook.game_input import Input
from network_terminal_output import NetworkTerminalOutput
import json


class NetworkTerminalInput(Input):
    def __init__(self, client):
        self.client = client
        self.output_instance = NetworkTerminalOutput(client)

    def input(self, prompt):
        self.output_instance.output(prompt, "input")
        answer_string = self.client.recv(1024)
        answer = json.loads(answer_string)
        if answer["type"] == "input-answer":
            return answer["data"]
        return "no answer"

    def ask_for_user_inputs(self, options):
        user_input_string = ""
        for option in options:
            user_input_string += (f"to {option.show_title()} enter one of the"
                                  f" following {option.show_user_inputs()}\n")
        return self.input(user_input_string + "your choice: ")
