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
        output_sender = NetworkTerminalOutput(client)
        input_sender = NetworkTerminalInput(client)
        with client:
            gm = GameManager(scenes_list, output_sender, input_sender)
            server_output.output(f"connection made from {address}")
            # client.settimeout(15)
            # while True:
            gm.start(intro_scene)
            """    data = input_sender.input("enter a word: ")
                server_output.output(f"recieved {data}")
                if data == "quit":
                    server_output.output(f"closing connection with {address}")
                    client.close()
                    break
                else:
                    output_sender.output("output", data)
            """
