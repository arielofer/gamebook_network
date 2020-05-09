import socket
from network_terminal_output import NetworkTerminalOutput


HOST = '127.0.0.1'
PORT = 6543

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()

    client, address = socket.accept()
    output_instance = NetworkTerminalOutput(client)
    with client:
        print(f"connection made from {address}")
        while True:
            data = client.recv(1024)
            output_instance.output(data)

