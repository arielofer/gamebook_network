import socket


HOST = '127.0.0.1'
PORT = 6543

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()

    client, address = socket.accept()
    with client:
        print(f"connection made from {address}")
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)

