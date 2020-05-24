import socket
from network_terminal_output import NetworkTerminalOutput
from network_terminal_input import NetworkTerminalInput
from gamebook.terminal_output import TerminalOutput
from gamebook.game_manager import GameManager
from game_manager_example import scenes_list, intro_scene


HOST = '0.0.0.0'
PORT = 6543

server_output = TerminalOutput()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()
    while True:
        client, address = socket.accept()
        client_output = NetworkTerminalOutput(client)
        client_input = NetworkTerminalInput(client)
        with client:
            gm = GameManager(scenes_list, client_output, client_input)
            server_output.output(f"connection made from {address}")
            # client.settimeout(15)
            while True:
                data = client_input.input("enter a word: ")
                server_output.output(f"recieved {data}")
                if data == "quit":
                    server_output.output(f"closing connection with {address}")
                    client.close()
                    break
                else:
                    client_output.output("output", data)
