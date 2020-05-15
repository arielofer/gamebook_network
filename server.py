import socket
from network_terminal_output import NetworkTerminalOutput
from gamebook.terminal_output import TerminalOutput


HOST = '0.0.0.0'
PORT = 6543

server_output = TerminalOutput()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()
    while True:
        client, address = socket.accept()
        client_output = NetworkTerminalOutput(client)
        with client:
            server_output.output(f"connection made from {address}")
            client.settimeout(15)
            while True:
                data = client.recv(1024)
                server_output.output(f"recieved {data.decode('utf-8')}")
                if data.decode('utf-8') == "quit":
                    server_output.output(f"closing connection with {address}")
                    client.close()
                    break
                else:
                    client_output.output(data)
